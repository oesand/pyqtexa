from pathlib import Path
from typing import Generic, Type, TypeVar
import json


TC = TypeVar("TC")
class AppConfig(Generic[TC]):
    
    def __init__(self, target_type: Type[TC]):
        self.__type = target_type
        self.__instance: TC = None

    def load(self, path: Path):
        assert self.__instance is None
        if path.exists():
            with open(path, "r") as f:
                args = json.load(f)
                self.__instance = self.__type(**args)

    def get(self) -> TC:
        assert self.__instance is not None, "Config not loaded, use 'load'"
        return self.__instance
    
    def __call__(self) -> TC:
        return self.get()
    
    @property
    def i(self):
        return self.get()
