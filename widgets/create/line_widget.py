from PyQt5.QtWidgets import QFrame


def verticalLine():
    line = QFrame()
    line.setGeometry(0, 0, 50, 3)
    line.setFrameShape(QFrame.Shape.HLine)
    line.setFrameShadow(QFrame.Shadow.Sunken)
    return line


def horizontalLine():
    line = QFrame()
    line.setGeometry(0, 0, 3, 50)
    line.setFrameShape(QFrame.Shape.VLine)
    line.setFrameShadow(QFrame.Shadow.Sunken)
    return line
