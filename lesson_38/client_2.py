import aiohttp
import asyncio


async def send_requests_parallel():
    async with aiohttp.ClientSession() as session:
        tasks = [
            session.get("http://localhost:8080/get"),
            session.post("http://localhost:8080/post", json={"username": "User", "score": 100}),
            session.patch("http://localhost:8080/patch", json={"score": 150}),
            session.delete("http://localhost:8080/delete"),
        ]

        responses = await asyncio.gather(*tasks)

        for response in responses:
            print(await response.json())


if __name__ == "__main__":

    print("\n=== Параллельные запросы ===")
    asyncio.run(send_requests_parallel())