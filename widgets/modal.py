from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QMainWindow, QLayout, QWidget, 
    QScrollArea, QVBoxLayout
)
from PyQt5.QtGui import QMouseEvent, QResizeEvent

from .mini import createLineLayout, createLabel, createButton, createWidget


class OverflowModal:
    def __init__(self, window: QMainWindow) -> None:
        self._window = window
        self._root = self._window.centralWidget()
        self._window.resizeEvent = self._onWindowResize(self._window.resizeEvent)
        
        self._overflow: QWidget
        self._layout: QVBoxLayout
        self._shown = False
        self._allowHide = True
        self._setupWidget()
    
    def _onPress(self, ev: QMouseEvent):
        if self._allowHide:
            self.hide()
        
    def _onWindowResize(self, base):
        def wrapper(ev: QResizeEvent):
            base(ev)
            if self._overflow is None: return
            self._overflow.resize(ev.size())
        return wrapper
    
    def _setupWidget(self):
        self._layout = createLineLayout(None, alignment="center", content_margins=[50, 50, 50, 50])
        
        self._overflow = QScrollArea(self._root)
        self._overflow.setObjectName("scrollarea")
        self._overflow.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self._overflow.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self._overflow.setWidgetResizable(True)
        self._overflow.setWidget(createWidget(
            id="overflow",
            stylesheet="#overflow{ background-color:rgba(0,0,0,0.3); }"
        ))
        self._overflow.setStyleSheet("QScrollArea#scrollarea{ background: transparent; }")
        
        self._overflow.widget().setLayout(self._layout)
        self._overflow.move(0, 0)
        self._overflow.setVisible(False)
        self._overflow.mousePressEvent = self._onPress
        
    def show(
        self, layout: QLayout, *, 
        allowHide: bool = True, 
        append: bool = False
    ):
        if not  append:
            if self._shown: return
            self._shown = True
        self._allowHide = allowHide
        
        self._layout.addWidget(createWidget(
            id="modal", layout=layout,
            stylesheet="#modal{ background-color: white; border-radius: 10px; }"
        ))
        
        self._overflow.resize(self._root.size())
        self._overflow.setVisible(True)
    
    def hide(self):
        if not self._shown: return
        self._shown = False
        self._allowHide = True
        
        self._overflow.resize(0, 0)
        self._overflow.setVisible(False)
        self._layout.clean()
        
    def showText(self, text: str):
        self.show(createLineLayout(alignment="no", items=[
            createLabel(text), createButton(text="OK", handle=self.hide)
        ]))
