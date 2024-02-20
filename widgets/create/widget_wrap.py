from typing import TypedDict, Unpack, NotRequired
from PyQt5.QtWidgets import QLayout, QWidget


class WidgetKwargs(TypedDict):
    id: NotRequired[str]
    parent: NotRequired[QWidget]
    layout: NotRequired[QLayout]
    stylesheet: NotRequired[str]
    visible: NotRequired[bool]
    enabled: NotRequired[bool]
    fixedSize: NotRequired[tuple[int, int] | int]


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
    
    if "fixedSize" in kwargs:
        size = kwargs["fixedSize"]
        if isinstance(size, int):
            widget.setFixedSize(size, size)
        elif isinstance(size, tuple):
            widget.setFixedSize(size[0], size[1])
    
    return widget
