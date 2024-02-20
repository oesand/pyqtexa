from PyQt5.QtWidgets import QApplication, QMainWindow


def getMainWindow() -> QMainWindow | None:
    # Global function to find the (open) QMainWindow in application
    app = QApplication.instance()
    for widget in app.topLevelWidgets():
        if isinstance(widget, QMainWindow):
            return widget
    return None
