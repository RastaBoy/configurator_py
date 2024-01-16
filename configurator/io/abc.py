import os
import typing

from abc import ABC, abstractmethod



class InputOutputInterface(ABC):
    '''Интерфейс для работы с файлами'''
    
    def __init__(self):
        ...


    @abstractmethod
    def __parse__(self, data : typing.Any) -> dict:
        ...


    @abstractmethod
    def __serialize__(self, data : dict) -> str:
        ...
    
    
    @abstractmethod
    def read(self) -> dict:
        ...


    @abstractmethod
    def write(self, data : dict) -> None:
        ...