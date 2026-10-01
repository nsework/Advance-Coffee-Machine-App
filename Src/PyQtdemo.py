import sys
from PySide2.QtWidgets import QApplication, QWidget


class Form():
    def MainWindow(self, Window):
        Window.setWindowTitle("PySide2 GUI")
        Window.resize(400, 300)


# __Main__
if __name__ == '__main__':
    app = QApplication(sys.argv)
    F = Form()
    win = QWidget()
    F.MainWindow(win)
    win.show()
    sys.exit(app.exec_())
