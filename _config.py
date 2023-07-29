from pathlib import Path
from threading import Lock
from dataclasses import dataclass
import json, sys

    
BASE_PATH: Path = None
ASSETS_PATH: Path = None

if getattr(sys, 'frozen', False):
    BASE_PATH = Path(sys.executable).absolute().parent
    ASSETS_PATH = Path(sys._MEIPASS, "assets").absolute()
elif __file__:
    BASE_PATH = Path(__file__).absolute().parent.parent
    ASSETS_PATH = BASE_PATH / "assets"

DATA_PATH = BASE_PATH / "_data"
DB_PATH = DATA_PATH / "store.db"
CONFIG_PATH = DATA_PATH / "state.json"


@dataclass
class GlobalState:
    min_delay: int = 2
    max_delay: int = 10
    invite4round: int = 1

class GlobalState(GlobalState):
    _instance = None
    _lock = Lock()
    
    def __init__(self):
        raise Exception("Instance can be only one, use 'get()'")
    
    @classmethod
    def _init(cls, attrs: dict = None):
        obj = super().__new__(cls)
        if attrs: obj.__dict__.update(attrs)
        return obj
    
    @classmethod
    def _load(cls) -> "GlobalState":
        if CONFIG_PATH.exists():
            with open(CONFIG_PATH, "r") as f:
                args = json.load(f)
                return cls._init(args)
        return cls._init()
    
    @classmethod
    def save(cls):
        obj = cls.get()
        with open(CONFIG_PATH, "w") as f:
            json.dump(
                obj, f, 
                default=lambda o: o.__dict__, 
                sort_keys=True, indent=4, ensure_ascii=False
            )
    
    @classmethod
    def get(cls):
        if cls._instance is None: 
            with cls._lock:
                if not cls._instance:
                    cls._instance = cls._load()
        return cls._instance
