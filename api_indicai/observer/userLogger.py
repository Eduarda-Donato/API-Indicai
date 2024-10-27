from observer.observer import Observer

class UserLogger(Observer):
    def update(self, data):
        print(f"Log: Usuário atualizado - {data}")
