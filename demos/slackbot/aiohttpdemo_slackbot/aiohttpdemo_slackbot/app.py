from pathlib import Path

import aiohttp_jinja2
from aiohttp import web
import jinja2

from aiohttpdemo_slackbot.routes import init_routes
from aiohttpdemo_slackbot.utils import init_config


path = Path(__file__).parent


def init_jinja2(app: web.Application) -> None:
    '''
    Initialize jinja2 template for application.
    '''
    aiohttp_jinja2.setup(
        app,
        loader=jinja2.FileSystemLoader(str(path / 'templates'))
    )


def init_app(config: dict = None) -> web.Application:
    app = web.Application()

    init_jinja2(app)
    init_config(app, config=config)
    init_routes(app)

    return app
