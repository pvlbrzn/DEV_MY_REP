from sqlalchemy import (create_engine, Column, Integer, String, Float,
                        ForeignKey, Date, Enum, Boolean, CheckConstraint, func)
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
from sqlalchemy.exc import IntegrityError
from datetime import datetime

Base = declarative_base()


# Модель пользователя
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    user_name = Column(String, nullable=False)  # nullable=False запрещает пустое поле
    user_email = Column(String, unique=True, nullable=False)  # unique - уникальное

    # Связь с договором
    leases = relationship("Lease", back_populates="user", cascade="all, delete-orphan")


# Модель объекта недвижимости
class Property(Base):
    __tablename__ = 'properties'

    id = Column(Integer, primary_key=True)
    address = Column(String, nullable=False)
    property_type = Column(Enum('Жилая', 'Коммерческая', name='property_type'), default='Жилая')
    rent_price = Column(Float, nullable=False)

    # Связь с договором
    leases = relationship('Lease', back_populates='property', cascade="all, delete-orphan")


# Модель платежей
class Payment(Base):
    __tablename__ = 'payments'

    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    payment_date = Column(Date, default=datetime.now)
    lease_id = Column(Integer, ForeignKey("leases.id"))

    # Связь с договором
    lease = relationship('Lease', back_populates='payments')


# Модель торгового агента
class Agent(Base):
    __tablename__ = 'agents'

    id = Column(Integer, primary_key=True)
    agent_name = Column(String, nullable=False)
    commission_rate = Column(Float, default=0.1)

    # Связь с договором
    leases = relationship('Lease', back_populates='agent', cascade="all, delete-orphan")


# Модель договора на аренду
class Lease(Base):
    __tablename__ = 'leases'

    id = Column(Integer, primary_key=True)
    start_date = Column(Date, default=datetime.now)
    end_date = Column(Date, nullable=False)
    status_lease = Column(Boolean, default=False, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    property_id = Column(Integer, ForeignKey('properties.id'))
    agent_id = Column(Integer, ForeignKey('agents.id'))

    # Связи с моделями
    user = relationship('User', back_populates='leases')
    property = relationship('Property', back_populates='leases')
    payments = relationship('Payment', back_populates='lease', cascade="all, delete-orphan")
    agent = relationship('Agent', back_populates='leases')

    # Проверка диапазона даты
    __table_args__ = (
        CheckConstraint('end_date > start_date', name='valid_lease_dates'),
    )


engine = create_engine('sqlite:///property_manager.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def add_user(name: str, email: str):
    """
    Добавляет нового пользователя в БД
    :param name: Имя пользователя
    :param email: Электронная почка пользователя
    """
    user = User(user_name=name, user_email=email)
    session.add(user)
    session.commit()
    print(f'В БД добавлен пользователь {name}')


def add_property(addres: str, type: str, rent_price: float):
    """
    Добавляет объект недвижимости в БД
    :param addres: Адрес объекта
    :param type: Тип объекта (жилой/нежилой)
    :param rent_price: Цена аренды объекта
    """
    property = Property(address=addres, property_type=type, rent_price=rent_price)
    session.add(property)
    session.commit()
    print(f'Добавлен новый объект недвижимости: {type}, по адресу {addres}')


def add_agent(name: str, commission_rate: float):
    """
    Добавляет нового агента в БД
    :param name: Имя агента
    :param commission_rate: Комиссионный процент
    """
    agent = Agent(agent_name=name, commission_rate=commission_rate)
    session.add(agent)
    session.commit()
    print(f'В БД добавлен агент {name}')


def add_lease(user_id: int, property_id: int, amount: float, agent_id: int = None):
    """
    Открывает сделку на заключение договора аренды
    :param user_id: Пользователь
    :param property_id: Недвижимость
    :param amount: Стоимость аренды
    :param agent_id: Агент
    """
    try:
        # Проверяем наличие пользователя
        user = session.query(User).get(user_id)
        if not user:
            print("Пользователь не найден.")
            return

        # Проверяем наличие объекта недвижимости
        property = session.query(Property).get(property_id)
        if not property:
            print("Объект недвижимости не найден.")
            return

        # Начинаем транзакцию
        new_lease = Lease(
            start_date=datetime.now(),
            end_date=datetime.now().replace(year=datetime.now().year + 1),
            status_lease=True,
            user_id=user_id,
            property_id=property_id,
            agent_id=agent_id
        )
        session.add(new_lease)
        session.flush()  # Фиксируем временно для получения ID договора

        payment = Payment(amount=amount, lease_id=new_lease.id)
        session.add(payment)

        # Если указан агент, рассчитываем комиссию
        if agent_id:
            agent = session.query(Agent).get(agent_id)
            if agent:
                commission = amount * agent.commission_rate
                print(f'Комиссия агента {agent.agent_name}: {commission:.2f}')
            else:
                print("Агент не найден.")

        # Подтверждаем транзакцию
        session.commit()
        print("Договор аренды успешно добавлен.")
    except IntegrityError as e:
        session.rollback()  # Откат транзакции при ошибке
        print(f"Ошибка: {e}")
    except Exception as e:
        session.rollback()  # Откат транзакции при любой другой ошибке
        print(f"Неизвестная ошибка: {e}")


def make_payment(lease_id: int, amount: float):
    """
    Оплата по сделке
    :param lease_id: номер сделки
    :param amount: сумма к оплате
    """
    lease = session.query(Lease).filter(Lease.id == lease_id, Lease.status_lease == True).first()
    if not lease:
        print("Активный договор аренды не найден.")
        return

    payment = Payment(amount=amount, payment_date=datetime.today(), lease=lease)
    session.add(payment)

    total_payments = sum(p.amount for p in lease.payments) + amount
    if total_payments >= lease.property.rent_price:
        lease.status_lease = False
        print(f"Договор аренды {lease.id} завершён")

    session.commit()


def users_without_pay():
    """
    :return: Пользователи без платежей
    """
    users = session.query(User).outerjoin(Lease).outerjoin(Payment).filter(Payment.id == None)
    return [user.user_name for user in users]


def three_rent():
    """
    :return: объекты недвижимости, которые были арендованы более 3 раз.
    """
    apartments = session.query(Property.address).join(Lease).group_by(Property.address).having(
        func.count(Lease.id) > 3).all()
    return apartments
