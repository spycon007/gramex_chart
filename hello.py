from gramex.handlers import BaseHandler


def hello_world(handler):
    '''
    Implement data operations here
    '''
    print("hello")
class Hello(BaseHandler):
    def get(self):
        self.write('hello world, this is hello from gramex')
