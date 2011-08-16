from drinkme.controllers import urls

def app_factory(global_config, **local_conf):
    return urls

