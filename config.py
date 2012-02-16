import web

class Environment:
    home = '/'

class Development(Environment):
    pass

class Production(Environment):
    @property
    def home(self):
        return web.ctx.home.replace('/code.cgi', '')
        
# TODO: choose environment dynamically
environment = 'Production'

config = globals()[environment]()
