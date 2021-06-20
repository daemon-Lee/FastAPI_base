from fastapi import FastAPI
import os

def create_app(config=None):
    # Define the WSGI application object
    app = app = FastAPI(__name__)

    # load app sepcified configuration
    if config is not None:
        if isinstance(config, dict):
            app.config.update(config)
        elif config.endswith('.py'):
            app.config.from_pyfile(config)
    
    @app.get("/")
    def hello_world():
        return {"message" : "hello world + 1"}

    return app