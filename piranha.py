# coding=utf-8
"""Piranha."""
__version__ = '0.1a1'


class App:

    def __init__(self):
        pass

    def get(path: str):
        pass

    async def __call__(self, scope, receive, send):
        if scope["type"] == "lifespan":
            message = await receive()
            if message['type'] == "lifespan.startup":
                await send(dict(type="lifespan.startup.complete"))
            elif message["type"] == "lifespan.shutdown":
                await send(dict(type="lifespan.shutdown.complete"))
        elif scope["type"] == "http":
            message = await receive()
            await send(dict(type="http.response.start", status=200))
            await send(dict(type="http.response.body", body=b"ok"))
        else:
            print(scope)
