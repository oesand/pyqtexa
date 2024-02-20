from PyQt5.QtWidgets import QApplication


def parseClipboard():
    return QApplication.clipboard().text()

def insertClipboard(text: str):
    return QApplication.clipboard().setText(text)
