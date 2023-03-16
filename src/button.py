from abc import ABC, abstractmethod


class Button(ABC):

    @abstractmethod
    def action(self):
        pass
