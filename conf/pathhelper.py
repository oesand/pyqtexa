from pathlib import Path
import sys, inspect
from .config import Configuration
from ..utils import classproperty


class AppPathHelper:
    __is_executable: bool = getattr(sys, 'frozen', False)
    __base_path: Path = None
    __assets_path: Path = None
    __data_path: Path = None
    __config: Configuration = None
    
    @classmethod
    def init(
        cls, *,
        datapath: bool | str = False,
        _pick_step: int = 0,
    ):
        assert cls.__base_path is None, "Action allowed only once!"
        assert _pick_step in range(0, 5), "Not too more"
        
        if cls.is_executable:
            cls.__base_path = Path(sys.executable).absolute().parent
            cls.__assets_path = Path(sys._MEIPASS, "assets").absolute()
        else:
            stack = inspect.stack()
            cls.__base_path = Path(str(stack[_pick_step+1][1])).absolute().parent
            cls.__assets_path = cls.__base_path / "assets"

        if datapath:
            cls.__data_path = cls.__base_path / (datapath if isinstance(datapath, str) else "_data")
            if not cls.__data_path.exists():
                cls.__data_path.mkdir(parents=True, exist_ok=True)
    
    @classmethod
    def load_config(
        cls, *,
        filename: str = "config.json",
        default: dict | None = None
    ):
        if cls.__base_path is None:
            cls.init(datapath=True)
        
        assert cls.__config is None, "Action allowed only once!"
        cls.__config = Configuration(cls.data_path / filename, default=default)
    
    def __init__(self) -> None:
        raise Exception("Not supported, use 'init'")
    
    @classproperty
    def is_executable(cls):
        return cls.__is_executable
    
    @classproperty
    def config(cls):
        assert cls.__config, "Config is not loaded, use 'load_config'"
        return cls.__config
    
    @classproperty
    def base_path(cls):
        return cls.__base_path
    
    @classproperty
    def assets_path(cls):
        return cls.__assets_path
    
    @classproperty
    def data_path(cls):
        assert cls.__data_path, "Data directory not ininitialized!"
        return cls.__data_path
