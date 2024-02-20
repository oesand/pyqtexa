from typing import Unpack, Callable
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtGui import QValidator

from .widget_wrap import WidgetKwargs, widget


def inputField(*,
    initial_text: str | None = None,
    placeholder: str | None = None,
    input_mask: str | None = None,
    validator: QValidator | None = None,
    textChanged: Callable[[str], None] | None = None,
    readonly: bool | None = None,
    **extra: Unpack[WidgetKwargs]
):
    input = QLineEdit()
    if initial_text: input.setText(initial_text)
    if placeholder: input.setPlaceholderText(placeholder)
    if input_mask: input.setInputMask(input_mask)
    if validator: input.setValidator(validator)
    if textChanged: input.textChanged.connect(lambda: textChanged(input.text()))
    if readonly is not None: input.setReadOnly(readonly)
    
    if extra: widget(**extra, widget=input)
    return input
