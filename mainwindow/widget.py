# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QColumnView, QPushButton, QSizePolicy, QWidget, QFileDialog, QListWidget, QListWidgetItem, QMessageBox
from ui_form import Ui_Widget
from PySide6.QtGui import QStandardItemModel
from PySide6.QtGui import QStandardItem

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.ui.openFile.clicked.connect(self.open_file)
        self.ui.showData.clicked.connect(self.show_data)

        # масив де будуть дані
        self.data = []

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt)")
        if filename:
            self.data = []
            with open(filename, "r") as f:
                for line in f:
                    self.data.append(line.strip().split())

    def show_data(self):
        if not self.data:
            QMessageBox.warning(self, "Error", "No data to display!")
            return

        column_view = self.ui.columnView
        # очищення
        if column_view.model() is not None:
            column_view.setModel(None)
            column_view.clear()

        model = QStandardItemModel()

        for row in self.data:
            items = [QStandardItem(str(item)) for item in row]
            model.appendRow(items)

        column_view.setModel(model)
        column_view.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
