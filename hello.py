from gramex.handlers import BaseHandler


class Hello(BaseHandler):
    def get(self):
        self.write('hello world, this is hello from gramex')
