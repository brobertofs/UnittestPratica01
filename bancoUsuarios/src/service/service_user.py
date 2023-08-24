from src.models.store import Store
from src.models.user import User


class ServiceUser:
    def __init__(self):
        self.store = Store()

    def search_user(self, name):
        for user in self.store.bd:  # Valida se o "Name" já existe na lista
            if name == user.name:
                return user
        return None

    def add_user(self, name, job):
        if name is not None and job is not None:  # Valida se Name e Job não é vazio
            if isinstance(name, str) and isinstance(job, str):  # Valida se Name e Job são Strings
                if self.search_user(name) is None:
                    user = User(name, job)
                    self.store.bd.append(user)
                    return "SUCCESS: Usuario foi adicionado"
                else:
                    return "ERROR: Esse usuario existe na lista"
            else:
                return "ERROR: Parametro invalido, deveria ser String"
        else:
            return "ERROR: Parametro invalido, nao pode ser None"

    def remove_user(self, name):
        if name is not None:
            if isinstance(name, str):
                user = self.search_user(name)
                if user is not None:
                    self.store.bd.remove(user)
                    return "SUCCESS: Usuario foi removido"
                else:
                    return "ERROR: Esse usuario nao existe na lista"
            else:
                return "ERROR: Parametro invalido, deveria ser String"
        else:
            return "ERROR: Parametro invalido, nao pode ser None"

    def update_user(self, name, new_job): # Dado o nome, quero atualizar os dados do user
        if name is not None:
            if isinstance(name, str):
                user = self.search_user(name)
                if user is not None:
                    user.job = new_job
                    return "SUCCESS: Usuario foi atualizado"
                else:
                    return "ERROR: Esse usuario nao existe na lista"
            else:
                return "ERROR: Parametro invalido, deveria ser String"
        else:
            return "ERROR: Parametro invalido, nao pode ser None"

    def get_user_by_name(self, name): # Dado o nome, quero buscar os dados do user
        if name is not None:
            if isinstance(name, str):
                user = self.search_user(name)
                if user is not None:
                    resultado = "SUCCESS:"+"\n"+"Nome: "+user.name+"\n"+"Trabalho: "+user.job
                    return resultado
                else:
                    return "ERROR: Esse usuario nao existe na lista"
            else:
                return "ERROR: Parametro invalido, deveria ser String"
        else:
            return "ERROR: Parametro invalido, nao pode ser None"
