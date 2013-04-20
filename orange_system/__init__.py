from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models import (
    DBSession,
    Base,
    )


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('search', '/Search')
    config.add_route('customer','/Customers')
    config.add_route('addEmail','/Customers/addEmail')
    config.add_route('addEmailExisting', '/Customers/addEmailExisting')
    config.add_route('addCust','/Customers/addCust')
    config.add_route('addPhone','/Customers/addPhone')
    config.add_route('addPhoneExisting', '/Customers/addPhoneExisting')
    config.add_route('updateCust', '/Customers/updateCustomer')
    config.add_route('deleteCust', '/Customers/deleteCustomer')
    config.add_route('order','/Orders')
    config.add_route('addOrder','/Orders/addOrder')
    config.add_route('updateOrder','/Orders/updateOrder')
    config.add_route('deleteOrder','/Orders/deleteOrder')
    config.add_route('service','/Services')
    config.add_route('addService','/Services/addService')
    config.add_route('updateService','/Services/updateService')
    config.add_route('deleteService','/Services/deleteService')
    config.add_route('part','/Parts')
    config.add_route('addPart','/Parts/addPart')
    config.add_route('updatePart','/Parts/updatePart')
    config.add_route('deletePart','/Parts/deletePart')
    config.add_route('report','/Reports')
    config.add_route('todo','/ToDo')
    config.scan()
    return config.make_wsgi_app()
