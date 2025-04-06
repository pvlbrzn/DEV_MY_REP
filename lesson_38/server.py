from aiohttp import web

# Исходные данные
DATA = {"username": "Pavel", "score": 100}


async def handle_get(request):
    return web.json_response(DATA)


async def handle_post(request):
    json_data = await request.json()
    DATA.update(json_data)
    return web.json_response({"Ответ": "Данные обновлены", "data": DATA})


async def handle_patch(request):
    json_data = await request.json()
    DATA.update(json_data)
    return web.json_response({"Ответ": "Результат обновлен", "data": DATA})


async def handle_delete(request):
    DATA.clear()
    return web.json_response({"Ответ": "Данные удалены"})

app = web.Application()
app.add_routes([
    web.get('/get', handle_get),
    web.post('/post', handle_post),
    web.patch('/patch', handle_patch),
    web.delete('/delete', handle_delete),
])

if __name__ == "__main__":
    web.run_app(app, host='127.0.0.1', port=8080)
