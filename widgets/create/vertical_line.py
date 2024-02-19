from PyQt5.QtWidgets import QFrame


def verticalLine():
    line = QFrame()
    line.setGeometry(0, 0, 50, 3)
    line.setFrameShape(QFrame.Shape.HLine)
    line.setFrameShadow(QFrame.Shadow.Sunken)
    return line
