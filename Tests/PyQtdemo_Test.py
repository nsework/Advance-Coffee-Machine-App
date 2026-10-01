from PySide2.QtWidgets import QWidget

from ..Src import PyQtdemo


def test_main_window(qtbot):
    win = QWidget()
    qtbot.addWidget(win)
    PyQtdemo.Form().MainWindow(win)
    assert win.windowTitle() == "PySide2 GUI"
    assert (win.width(), win.height()) == (400, 300)
