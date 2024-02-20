from typing import Any
from PyQt5.QtWidgets import QMainWindow, QLayout
from PyQt5.QtGui import QResizeEvent

from ...widgets import create, LayoutWrap
from .layout_wrap import ModalLayoutWrap
from .modal import OverflowModal


class OverflowModalMixin:
    def __init__(self) -> None:
        assert isinstance(self, QMainWindow), "Mixin must be extends from QMainWindow"
        self.overflowModal = OverflowModal(self)
    
    def showModal(
        self, content: QLayout | type[ModalLayoutWrap] | ModalLayoutWrap, *,
        closeManually: bool = True,
        closeEvery: bool = False,
        signal: dict[str, Any] = None
    ):
        if isinstance(content, type(LayoutWrap)):
            content = content(self)
        if isinstance(content, ModalLayoutWrap) and signal:
            content.signal(**signal)
        self.overflowModal.show(
            content=content,
            closeManually=closeManually,
            closeEvery=closeEvery
        )
    
    def hideModal(self, *, every: bool = False):
        self.overflowModal.hide(every=every)
    
    def showTextPopup(self, text: str, *, okayText: str = "OK"):
        self.showModal(
            create.lineLayout(alignment="no", items=[
                create.label(text=text), create.button(text=okayText, handle=self.hideModal)
            ])
        )
    
    @property
    def hasModalShown(self):
        return self.overflowModal.shown
    
    def resizeEvent(self, event: QResizeEvent):
        super(QMainWindow, self).resizeEvent(event)
        if self.overflowModal.shown:
            self.overflowModal._onApplySize(event)
