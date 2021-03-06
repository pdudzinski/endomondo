from sqlalchemy import engine_from_config

from pyramid.config import Configurator
from pyramid.session import UnencryptedCookieSessionFactoryConfig

from .db import *

def main(global_config, **settings):
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    
    config = Configurator(
        settings=settings,
        session_factory = UnencryptedCookieSessionFactoryConfig('ttxx'))
    
    config.include('pyramid_mako')
    config.add_static_view(
        'static',
        'tracker:static',
        cache_max_age=3600)
    
    config.add_route('home', '/')
    config.add_route('get_workouts', '/get-workouts')
    config.add_route('statistics', '/statistics')
    
    config.scan()
    
    return config.make_wsgi_app()
