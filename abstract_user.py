from abc import ABC, abstractmethod

class AbstractUser(ABC):

    def __init__(self, id_user, nama):
        self._id = id_user
        self._nama = nama

    @abstractmethod
    def akses(self):
        pass

class Admin(AbstractUser):

    def akses(self):
        return "Akses penuh"

class Staff(AbstractUser):

    def akses(self):
        return "Akses terbatas"