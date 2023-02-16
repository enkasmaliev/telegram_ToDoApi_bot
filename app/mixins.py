import json
import requests



class CRUDMixin:
    def create(self, title):
        id_done = False
        model = self.model(title, id_done).dict()
        response = requests.post(self.host + 'todo/create', data=json.dumps(model))
        if response.status_code == 200:
            return 'Успешно создан'
        return 'Ошибка'
    

    def read(self):
        response = requests.get(self.host + 'todo/all')
        if response.status_code == 200:
            return json.loads(response.text)
        raise Exception('Сервер упал')
    
    def retrieve(self, id_):
        response = requests.get(self.host + f'todo/{id_}')
        if response.status_code == 200:
            return json.loads(response.text)
        elif response.status_code == 404:
            raise Exception('id не найден')
        raise Exception('Непредвиденная ошибка')

    def update(self, id_, title):
        id_done = False
        model = self.model(title, id_done).dict()
        response = requests.put(self.host + f'todo/{id_}/update', data=json.dumps(model))
        if response.status_code == 200:
            return "Успешно обновлено"
        return "id не найден"
    
    def delete(self, id_):
        response = requests.delete(self.host + f'todo/{id_}/delete')
        if response.status_code == 200:
            return "Успешно удалено"
        else:
            return "id не найден"

