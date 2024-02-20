from typing import TYPE_CHECKING
from PyQt5.QtWidgets import QMainWindow, QLayout, QWidget
from PyQt5.QtGui import QResizeEvent

from ...widgets import create, LayoutWrap

if TYPE_CHECKING:
    from .mixin import OverflowModalMixin


class OverflowModal:
    def __init__(self, window: 'QMainWindow | OverflowModalMixin') -> None:
        self.__window = window
        self.__shownContext: list[QWidget] = []
        
    @property
    def shown(self):
        return len(self.__shownContext) > 0
    
    def hide(self, *, every: bool = False):
        assert self.shown, "Modal not shown"
        if every:
            for widget in self.__shownContext:
                widget.setParent(None)
                widget.deleteLater()
        else:
            widget: QWidget = self.__shownContext.pop()
            widget.setParent(None)
            widget.deleteLater()

    def show(
        self, content: QLayout | LayoutWrap, *,
        closeManually: bool = True,
        closeEvery: bool = False,
    ):
        if isinstance(content, LayoutWrap):
            content = content._extract()
            
        root: QWidget = self.__window.centralWidget()
        
        overflow = create.scrollArea(
            id="scrollarea",
            parent=root,
            vertical=None,
            resizable=True,
            stylesheet="QScrollArea#scrollarea{ background: transparent; }",
            content=create.widget(
                id="overflow",
                stylesheet="#overflow{ background-color:rgba(0,0,0,0." + 
                    ("1" if len(self.__shownContext) >= 1 else "3") + "); }",
                    
                layout=create.lineLayout(
                    alignment="center", padding=[50, 50, 50, 50],
                    items=[
                        create.widget(
                            id="modal", layout=content,
                            stylesheet="#modal{ background-color: white; border-radius: 10px; }"
                        )
                    ]
                )
            )
        )
        
        if closeManually:
            overflow.mousePressEvent = lambda ev: self.hide(every=closeEvery)
        
        overflow.move(0, 0)
        overflow.resize(root.size())
        
        self.__shownContext.append(overflow)
    
    def _onApplySize(self, ev: QResizeEvent):
        if not self.shown: return
        for widget in self.__shownContext:
            widget.resize(ev.size())
