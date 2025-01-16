from property_manager import add_property, add_user, add_lease, add_agent, make_payment


def run_app():
    try:
        add_user("Павел", "pavel@mail.ru")
        add_property("Независимости, 65, кв 25", "Жилая", 500)
        add_agent('Мистер Навар', 0.15)
        add_lease(user_id=1, property_id=1, amount=1000, agent_id=1)

        add_user("Антон", "antony@gmail.com")
        add_property("Нововиленская, 25 пом 1", "Коммерческая", 2000)
        add_agent('Андрей бизнес-аренда', 0.1)
        add_lease(user_id=2, property_id=2, amount=8000.0, agent_id=2)
        make_payment(2, 10000)

        add_user("Сергей", "Seryi@gmail.com")
        add_property("Нововиленская, 25 пом 3", "Коммерческая", 2000)
        add_lease(user_id=3, property_id=3, amount=2000, agent_id=2)
        make_payment(3, 800)

    except ValueError as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    run_app()
