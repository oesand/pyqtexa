from pathlib import Path
import json


class Configuration:
    def __init__(
        self, path: str | Path, *, 
        default: dict = None
    ):
        self._path = path if isinstance(path, Path) else Path(path)
        self._data = default or {}
        
        if self._path.exists():
            try:
                with open(str(self._path), 'r') as f:
                    self._data = json.load(f)
            except:
                pass
        else:
            self._path.parent.mkdir(exist_ok=True)        

    def __enter__(self):
        return self.data

    def __exit__(self, *args):
        self.save()

    def __getitem__(self, name: str):
        return self.data[name]

    def __setitem__(self, name: str, value):
        self.data[name] = value

    def get(self, name: str, *, default = None):
        return self.data.get(name, default)
    
    @property
    def data(self):
        return self._data

    def save(self):
        with open(str(self._path), 'w') as f:
            json.dump(self._data, f)
