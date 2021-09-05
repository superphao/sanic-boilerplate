from sanic import Sanic
from infrastructure.configs.main import GlobalConfig
from infrastructure.database import init_db

from infrastructure.configs import ServerType
from infrastructure.interceptors.exeption_interceptor import ExceptionInterceptor

async def listener_before_server_start(*args, **kwargs):
    print("before_server_start")
    
async def listener_after_server_start(*args, **kwargs):
    print("after_server_start")
    
async def listener_before_server_stop(*args, **kwargs):
    print("before_server_stop")
    
async def listener_after_server_stop(*args, **kwargs):
    print("after_server_stop")

def init_app(server_type: str, config: GlobalConfig):
    
    app: Sanic = Sanic('face-recognition-service')

    init_db(config.CASSANDRA_DATABASE)

    if server_type == ServerType.uvicorn.value:

        app.error_handler = ExceptionInterceptor()

        app.register_listener(listener_after_server_start, 'after_server_start')
        app.register_listener(listener_before_server_stop, 'before_server_stop')

    elif server_type == ServerType.built_in.value:

        app.register_listener(listener_before_server_start, 'before_server_start')
        app.register_listener(listener_after_server_start, 'after_server_start')
        app.register_listener(listener_before_server_stop, 'before_server_stop')
        app.register_listener(listener_after_server_stop, 'after_server_stop')
    
    return app
