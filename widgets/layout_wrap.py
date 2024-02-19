from abc import ABC
from PyQt5.QtWidgets import QMainWindow, QLayout


class LayoutWrap(ABC):
    
    def __init__(self, window: QMainWindow) -> None:
        self.window = window
    
    def render(self) -> QLayout:
        pass
