import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nice Window")
        self.setGeometry(400, 300, 400, 400)
        label = QLabel("hello", self)
        label.setFont(QFont("apple", 40))
        label.setGeometry(0, 0, 400, 100)
        label.setStyleSheet("color: #a5fc03;"
                            "background: #93a178;"
                            "font-weight: bold;"
                            "font-style: italic;")
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) #横向纵向对齐
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)#纵向居中，横向Top
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)  # 纵向居中，横向bottom
        label.setAlignment(Qt.AlignLeft | Qt.AlignBottom)  # 左下，相对的有右下，左上，右上


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
