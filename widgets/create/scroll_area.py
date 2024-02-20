from typing import Unpack
from PyQt5.QtWidgets import QWidget, QScrollArea
from PyQt5.QtCore import Qt

from .widget_wrap import WidgetKwargs, widget as wrap_widget


def scrollArea(
    vertical: bool | None = True,
    resizable: bool | None = None,
    content: QWidget | None = None,
    **extra: Unpack[WidgetKwargs]
) -> QScrollArea:
    scroll = QScrollArea()
    
    if vertical is None:
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    if vertical:
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    else:
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        
    if resizable is not None: scroll.setWidgetResizable(resizable)
    if content is not None: scroll.setWidget(content)
    
    extra.setdefault('visible', True)
    if extra: wrap_widget(**extra, widget=scroll)
    return scroll
