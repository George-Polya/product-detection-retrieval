<<<<<<< HEAD
from abc import *


class AbstractRetrievalModel(metaclass=ABCMeta):
    def __init__(self, modelName, info):
        self.modelName = modelName
        self.info = info
        
    @abstractmethod
    def fit(self,X,n_epochs, batch_size, callbacks=None):
        pass

    @abstractmethod
    def predict(self,X):
        pass

    @abstractmethod
    def set_arch(self):
        pass
    
    @abstractmethod
    def compile(self, loss, optimizer="adam"):
        pass

    @abstractmethod
    def load_models(self, loss, optimizer="adam"):
        pass

    @abstractmethod
    def save_models(self):
        pass
=======
from abc import *


class AbstractRetrievalModel(metaclass=ABCMeta):
    def __init__(self, modelName, info):
        self.modelName = modelName
        self.info = info
        
    @abstractmethod
    def fit(self,X,n_epochs, batch_size, callbacks=None):
        pass

    @abstractmethod
    def predict(self,X):
        pass

    @abstractmethod
    def set_arch(self):
        pass
    
    @abstractmethod
    def compile(self, loss, optimizer="adam"):
        pass

    @abstractmethod
    def load_models(self, loss, optimizer="adam"):
        pass

    @abstractmethod
    def save_models(self):
        pass
>>>>>>> f72ad1f9408fc1fe4d43d73d29c241a660890638
