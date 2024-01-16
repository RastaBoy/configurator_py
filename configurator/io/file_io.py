import json

from typing import Any
from .abc import InputOutputInterface


class FileInputOutputInterface(InputOutputInterface):
    
    def __init__(
            self,
            filename : str
        ):
        self._filename = filename
        super().__init__()
    

    def read(self) -> dict:
        with open(self._filename, 'r', encoding='utf-8') as file:
            data = file.read()
            file.close()
            
            return self.__parse__(data)
    

    def write(self, data : dict) -> None:
        with open(self._filename, 'w+', encoding='utf-8') as file:
            file.write(self.__serialize__(data))
            file.close()




class JSONFileIO(FileInputOutputInterface):

    def __serialize__(self, data: dict) -> str:
        return json.dumps(data)
    

    def __parse__(self, data: Any) -> dict:
        return json.loads(data)