from PyQt5.QtWidgets import QMainWindow, QLayout
from PyQt5.QtGui import QResizeEvent

from ...widgets import create
from .modal import OverflowModal


class OverflowModalMixin:
    def __init__(self) -> None:
        assert isinstance(self, QMainWindow), "Mixin must be extends from QMainWindow"
        self.overflowModal = OverflowModal(self)
    
    def showModal(
        self, content: QLayout, *,
        closeManually: bool = True,
    ):
        self.overflowModal.show(
            content=content,
            closeManually=closeManually
        )
    
    def hideModal(self):
        self.overflowModal.hide()
    
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
