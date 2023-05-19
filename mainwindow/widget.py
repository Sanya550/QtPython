# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QColumnView, QPushButton, QSizePolicy, QWidget, QFileDialog, QListWidget, QListWidgetItem, QMessageBox
from ui_form import Ui_Widget
from PySide6.QtGui import QStandardItemModel
from PySide6.QtGui import QStandardItem
import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
# import math

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.ui.openFile.clicked.connect(self.open_file)
        self.ui.showData.clicked.connect(self.show_data)

        # масив масиву де будуть дані
        self.data = [[]]

    # зчитування
    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt)")
        if filename:
            self.data = [[]]
            with open(filename, "r") as f:
                for line in f:
                    values = [float(val) for val in line.strip().split()]
                    self.data.append(values)
            self.data.pop(0) # видаляю порожній список з початку

    def show_data(self):
        # перевірка чи масив не пустий
        if not self.data:
            QMessageBox.warning(self, "Error", "No data to display!")
            return

        table_view = self.ui.tableView
        # Очищення, якщо table view заповнений
        if table_view.model() is not None:
            table_view.setModel(None)
            table_view.clear()

        model = QStandardItemModel()

        # Встановлюю кількість рядків та стовпчиків
        num_rows = len(self.data)
        num_cols = len(self.data[0])
        model.setRowCount(num_rows)
        model.setColumnCount(num_cols)

        for i, row in enumerate(self.data):
            for j, item in enumerate(row):
                index = model.index(i, j)
                model.setData(index, str(item))

        table_view.setModel(model)
        table_view.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
