from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
import sys

# khoi tao app
app = QApplication(sys.argv)
# khoi tao cua so
window = QWidget()

# trang tri cua so ------------------------------
window.setMinimumSize(500, 500)  # dat size nho nhat cua cua so
window.setWindowTitle("New app")  # tao lai ten cua khung cua so

# them thanh phan cho cua so (element) ----------
button = QPushButton(window) # tao obj button + bo vao window
button.setText("Click me") # tao text cho button
button.setGeometry(100, 100, 100, 30) # vi tri va kich thuoc 

# hien thi cua so
window.show()
# cho app chay lien tuc khong bi tat
app.exec()
