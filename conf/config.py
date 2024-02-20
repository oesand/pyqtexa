from pathlib import Path
import json


class Configuration:
    def __init__(
        self, path: str | Path, *, 
        default: dict = None
    ):
        self.__path = path if isinstance(path, Path) else Path(path)
        self.__default = default
        self.__data = default or {}
        
        if self.__path.exists():
            try:
                with open(str(self.__path), 'r') as f:
                    self.__data = json.load(f)
            except:
                pass
        else:
            self.__path.parent.mkdir(exist_ok=True)        

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.save()

    def __getitem__(self, name: str):
        try:
            return self.__data[name]
        except KeyError:
            if not self.__default or name not in self.__default:
                raise KeyError(f"Configuration has no '{name}' key.")
            return self.__default[name]

    def __setitem__(self, name: str, value):
        self.__data[name] = value

    def get(self, name: str, *, default = None):
        return self.__data.get(name, default)
    
    def save(self):
        with open(str(self.__path), 'w') as f:
            json.dump(self.__data, f)
