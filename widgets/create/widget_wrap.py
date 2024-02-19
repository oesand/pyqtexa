from typing import TypedDict, Unpack
from PyQt5.QtWidgets import QLayout, QWidget


class WidgetKwargs(TypedDict):
    id: str
    parent: QWidget
    layout: QLayout
    stylesheet: str
    visible: bool
    enabled: bool
    fixed_size: tuple[int, int] | int


def widget(*,
    widget: QWidget | None = None,
    **kwargs: Unpack[WidgetKwargs]
):
    if widget is None:
        widget = QWidget()
    
    if "id" in kwargs: widget.setObjectName(kwargs["id"])
    if "parent" in kwargs: widget.setParent(kwargs["parent"])
    if "layout" in kwargs: widget.setLayout(kwargs["layout"])
    if "stylesheet" in kwargs: widget.setStyleSheet(kwargs["stylesheet"])
    if "visible" in kwargs: widget.setVisible(kwargs["visible"])
    if "enabled" in kwargs: widget.setEnabled(kwargs["enabled"])
    
    if "fixed_size" in kwargs:
        size = kwargs["fixed_size"]
        if isinstance(size, int):
            widget.setFixedSize(size, size)
        elif isinstance(size, tuple):
            widget.setFixedSize(size[0], size[1])
    
    return widget
