from app.model import ToDo
from app.mixins import CRUDMixin

class Interface(CRUDMixin):
    def __init__(self, host):
        self.host = host
    model = ToDo

api = Interface('http://3.67.196.232/')

# while True:
#     funcs = {
#         'create': api.create,
#         'read': api.read,
#         'retrieve': api.retrieve,
#         'update': api.update,
#         'delete': api.delete
#     }

#     action = input('Введите команду: ')
#     try:
#         funcs[action]()
#     except:
#         print('Неверная команда')


