from collections.abc import Callable
from typing import Unpack
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon

from .widget_wrap import WidgetKwargs, widget


def button(*, 
    text: str | None = None,
    icon: str | tuple[str, int] | None = None,
    handle: Callable | None = None,
    **extra: Unpack[WidgetKwargs]
):
    button = QPushButton(text)
    
    if icon:
        if isinstance(icon, tuple):
            icon_size = icon[1]
            icon = icon[0]
            button.setIconSize(QSize(icon_size, icon_size))
        if isinstance(icon, str):
            button.setIcon(QIcon(icon))
            
    if handle is not None:
        button.pressed.connect(lambda: handle(), Qt.DirectConnection)
    
    if extra: widget(**extra, widget=button)
    return button
