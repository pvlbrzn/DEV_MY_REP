import aiohttp
import asyncio


async def send_requests():
    async with aiohttp.ClientSession() as session:
        # GET-запрос
        async with session.get("http://localhost:8080/get") as response:
            get_data = await response.json()
            print("Получены данные:", get_data)

        # POST-запрос
        post_payload = {"username": "Новый юзер", "score": 100}
        async with session.post("http://localhost:8080/post", json=post_payload) as response:
            post_data = await response.json()
            print("Данные отправлены:", post_data)

        # PATCH-запрос
        patch_payload = {"score": 150}
        async with session.patch("http://localhost:8080/patch", json=patch_payload) as response:
            patch_data = await response.json()
            print("Данные изменены:", patch_data)

        # DELETE-запрос
        async with session.delete("http://localhost:8080/delete") as response:
            delete_data = await response.json()
            print("Удаление данных:", delete_data)


if __name__ == "__main__":
    print("Запуск всех запросов из main")
    asyncio.run(send_requests())

