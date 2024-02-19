from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLayout
from PyQt5.QtGui import QFont, QIcon
from .create import widget as create_widget


class QBMainWindow(QMainWindow):
    
    def __init__(
        self, *,
        parent: QMainWindow | None = None,
        icon: str | None = None,
        title: str | None = None,
        size: tuple[int, int] | int | None = None,
        font: QFont | tuple[str, int] | None = None,
        stylesheet: str | None = None,
    ):
        super(QMainWindow, self).__init__(parent=parent)
        if icon: self.setWindowIcon(QIcon(str(icon)))
        if title: self.setWindowTitle(title)
        if size:
            if isinstance(size, tuple):
                self.resize(size[0], size[1])
            else:
                self.resize(size, size)
        if font is not None:
            if isinstance(font, tuple):
                font = QFont(font[0], font[1])
            if isinstance(font, QFont):
                self.setFont(font)
        if stylesheet:
            self.setStyleSheet(stylesheet)
        
        root = self.render()
        if root:
            if isinstance(root, QLayout):
                root = create_widget(layout=root)
            if isinstance(root, QWidget):
                self.setCentralWidget(root)

    def render(self) -> QWidget:
        return None
    
    @classmethod
    def execute(cls):
        app = QApplication([])
        window = cls()
        window.show()
        return app.exec_()
