from threading import Lock
from pathlib import Path
import sys, inspect
from .config import AppConfig


class AppPathHelper:
    __instance = None
    __once = False
    __lock = Lock()
    
    CONFIG_FILENAME = "config.json"
    DB_FILENAME = "store.db"
    
    def __new__(cls):
        if not cls.__instance:
            with cls.__lock:
                if not cls.__instance:
                    cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self) -> None:
        if self.__once: return
        self.__once = True
        self.__is_executable: bool = getattr(sys, 'frozen', False)
        self.__base_path: Path = None
        self.__assets_path: Path = None
        self.__data_path: Path = None
    
    @property
    def is_executable(self):
        return self.__is_executable
    
    def mainfile_init(
        self, *, 
        include_datapath: bool = False,
        load_config: AppConfig = None,
        step: int = 0,
    ):
        assert not self.__base_path, "Action allowed only once!"
        if self.is_executable:
            self.__base_path = Path(sys.executable).absolute().parent
            self.__assets_path = Path(sys._MEIPASS, "assets").absolute()
        else:
            stack = inspect.stack()
            self.__base_path = Path(str(stack[step+1][1])).absolute().parent
            self.__assets_path = Path(sys._MEIPASS, "assets").absolute()

        if load_config: include_datapath = True
        if include_datapath:
            self.__data_path = self.__base_path / "_data"
            if not self.__data_path.exists():
                self.__data_path.mkdir(parents=True, exist_ok=True)
        
        if load_config:
            load_config.load(self.config_path)
    
    @property
    def base_path(self):
        return self.__base_path
    
    @property
    def assets_path(self):
        return self.__assets_path
    
    @property
    def data_path(self):
        return self.__data_path
    
    @property
    def db_path(self):
        assert self.data_path is not None
        return self.__data_path / self.DB_FILENAME
    
    @property
    def config_path(self):
        assert self.data_path is not None
        return self.__data_path / self.CONFIG_FILENAME
