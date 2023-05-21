# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
from ui_form import Ui_Widget
from PySide6.QtGui import QStandardItemModel
from PySide6.QtGui import QStandardItem
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtGui import QImage
import pandas as pd
import matplotlib.pyplot as plt
import cv2
import numpy as np

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.ui.openFile.clicked.connect(self.open_file)
        self.ui.showData.clicked.connect(self.show_data)
        self.ui.showSummaryStatistics.clicked.connect(self.show_summary_statistics)
        self.ui.graphDiagramRozkid.clicked.connect(self.display_scatter_matrix)
        self.ui.graphHystograma.clicked.connect(self.display_hystograma)
        self.ui.openImage.clicked.connect(self.display_picture)
        self.ui.distributionColour.clicked.connect(self.display_distribution_colour)
        self.ui.greyScale.clicked.connect(self.display_grey_scale)
        self.ui.blurGraphs.clicked.connect(self.display_blur)
        # масив масиву де будуть дані
        self.data = [[]]

    def open_file(self):  # зчитування
        filename, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt)")
        if filename:
            self.data = [[]]
            with open(filename, "r") as f:
                for line in f:
                    values = [float(val) for val in line.strip().split()]
                    self.data.append(values)
            self.data.pop(0)  # видаляю порожній список з початку

    def show_data(self):  # вивід даних
        # перевірка чи масив не пустий
        if not self.data:
            QMessageBox.warning(self, "Error", "No data to display!")
            return

        table_view = self.ui.tableView
        # Очищення, якщо table view заповнений
        if table_view.model() is not None:
            table_view.setModel(None)

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

    def show_summary_statistics(self):  # отримуємо основні дані
        if not self.data:  # верифікація, що self.data не пустий
            QMessageBox.warning(self, "Error", "No data to display!")
            return

        tableView = self.ui.tableView
        tableView.setModel(None)  # очищаємо
        df = pd.DataFrame(self.data)
        statistics = df.describe()  # отримуємо основні дані
        model = QStandardItemModel()
        headers = list(statistics.columns)
        model.setHorizontalHeaderLabels(headers)

        # Додаємо дані
        for index, row in enumerate(statistics.index):
            items = [QStandardItem(str("%.2f" % statistics.loc[row, col])) for col in range(len(headers))]
            model.appendRow(items)
        # основні характеристики
        items = [QStandardItem("Count"), QStandardItem("Mean"), QStandardItem("Std"),
                 QStandardItem("Min"), QStandardItem("25%"), QStandardItem("50%"),
                 QStandardItem("75%"), QStandardItem("Max")]
        model.appendColumn(items)

        tableView.setModel(model)
        tableView.show()

    def display_scatter_matrix(self):  # матриця розкиду
        df = pd.DataFrame(self.data)
        file1 = 'data.csv'
        df.to_csv(file1, index=False)  # зберігаю дані в CSV-файлі с ім'ям data.csv
        data1 = pd.read_csv(file1)
        fig, ax = plt.subplots(figsize=(8, 8))  # fig - фігура, ах - вісі
        pd.plotting.scatter_matrix(data1, ax=ax)
        plt.show()  # Вивід графіка

    def display_hystograma(self):  # гістограма
        number = self.ui.spinBox.value()
        if number > len(self.data[0]):  # верифікація spinBox
            QMessageBox.warning(None, "Error", "Spin box value must be equal or less than data length")
        else:
            plt.hist([row[number - 1] for row in self.data])  # витягуємо стовпчик self.data
            plt.title("Гістограма для number = %d" % number)
            plt.show()  # Вивід графіка

    def display_picture(self):  # зчитування і відображення фотографії
        file, check = QFileDialog.getOpenFileName(None, "Select image file", "", "Image Files (*.jpg);;Image Files (*.png);;All Files (*)")
        if file:
            pixmap = QPixmap(file)
            label = QLabel(self)
            label.setPixmap(pixmap)
            label.setScaledContents(True)
            self.ui.gridLayout.addWidget(label, 0, 0, 1, 1)  # вивід фото
            width = pixmap.width()
            height = pixmap.height()
            self.ui.width_picture.setText("Width = %s" % width)
            self.ui.height_picture.setText("Height = %s" % height)

    def display_distribution_colour(self): # графіки розподілу кольорів
        image_widget = self.ui.gridLayout.itemAtPosition(0, 0).widget()
        image_pixmap = image_widget.pixmap()
        image = image_pixmap.toImage()
        image = image.convertToFormat(QImage.Format_RGB888)  # перероблюю в формат RG
        width, height = image.width(), image.height() # отримаю довжину і ширину image
        buffer = bytes(image.bits())
        buffer_np = np.frombuffer(buffer, dtype=np.uint8)
        buffer_np = buffer_np.reshape((height, width, 3)) # numpy змінює форму для подальшого користування

        value_combo_box = self.ui.comboBox.currentText()
        if value_combo_box == 'Red':
            channel_index = 0
            color1 = 'red'
        elif value_combo_box == 'Green':
            channel_index = 1
            color1 = 'green'
        elif value_combo_box == 'Blue':
            channel_index = 2
            color1 = 'blue'

        hist = cv2.calcHist([buffer_np], [channel_index], None, [256], [0, 256])

        plt.plot(hist, color=color1)
        plt.show()

    def display_grey_scale(self): # перетворення зображення в gray scale.
        image_widget = self.ui.gridLayout.itemAtPosition(0, 0).widget()
        image_pixmap = image_widget.pixmap()
        image = image_pixmap.toImage()
        image = image.convertToFormat(QImage.Format_RGB888)

        width, height = image.width(), image.height()
        buffer = bytes(image.bits())
        buffer_np = np.frombuffer(buffer, dtype=np.uint8)
        buffer_np = buffer_np.reshape((height, width, 3))

        gray_img = cv2.cvtColor(buffer_np, cv2.COLOR_BGR2GRAY)
        plt.imshow(gray_img, cmap='gray')
        plt.show()

    def display_blur(self):# Згладжування зображення
        image_widget = self.ui.gridLayout.itemAtPosition(0, 0).widget()
        image_pixmap = image_widget.pixmap()
        image = image_pixmap.toImage()
        image = image.convertToFormat(QImage.Format_RGB888)

        width, height = image.width(), image.height()
        buffer = bytes(image.bits())
        buffer_np = np.frombuffer(buffer, dtype=np.uint8)
        buffer_np = buffer_np.reshape((height, width, 3))

        value = self.ui.spinBox_2.value()
        blurred_img = cv2.blur(buffer_np, (value, value))
        plt.imshow(blurred_img)
        plt.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
