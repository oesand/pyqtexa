from typing import TYPE_CHECKING
from abc import ABC
from PyQt5.QtWidgets import QMainWindow, QLayout, QWidget, QVBoxLayout
if TYPE_CHECKING:
    from ..mixins import OverflowModalMixin
    

class LayoutWrap(ABC):
    
    def __init__(self, window: 'QMainWindow | OverflowModalMixin') -> None:
        self.window = window
        self.__cached: QLayout = None
    
    def _extract(self) -> QLayout:
        if self.__cached is None:
            self.__cached = self.render()
        return self.__cached
    
    def renderLine(self) -> list['QLayout | QWidget | LayoutWrap']:
        pass
    
    def render(self) -> QLayout:
        line = self.renderLine()
        if not line:
            raise ValueError(f"Class '{self.__class__.__name__}' should override 'render' or 'renderLine'")

        layout = QVBoxLayout()
        for item in line:
            if isinstance(item, LayoutWrap):
                item = item._extract()
            if isinstance(item, QLayout):
                layout.addLayout(item)
            elif isinstance(item, QWidget):
                layout.addWidget(item)
                
        return layout
