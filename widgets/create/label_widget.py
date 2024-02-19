from typing import Unpack
from PyQt5.QtWidgets import QLabel

from ..utils import applyAlignment
from .widget_wrap import WidgetKwargs, widget


def label(*,
    text: str | None = None,
    alignment: str | None = None,
    scaled: bool | None = None,
    **extra: Unpack[WidgetKwargs]
) -> QLabel:
    label = QLabel()
    if text: label.setText(text)
    if alignment: applyAlignment(label, alignment)
    if scaled is not None: label.setScaledContents(scaled)
    
    if extra: widget(**extra, widget=label)
    return label
