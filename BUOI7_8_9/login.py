# them thu vien cho app
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6 import uic
import sys


class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        # load ui ----------------
        self.ui = uic.loadUi(
            "C:\\Users\\diepa\\OneDrive\\Documents\\Working\\MindX\\3_Python\\2_advanced\PTA01\\BUOI7\\ui\\login.ui",
            self,
        )

        # xu ly dang nhap ---------------
        # bat su kien khi bam chuot vao nut login
        self.ui.login_button.clicked.connect()
        # bat su kien khi bam vao "Register"

        # tao 1 thong bao
        self.msg_box = QMessageBox()

    # kiem tra thong tin dang nhap
    def check_login(self):
        # lay thong tin tu giao dien nguoi
        # email
        username = self.ui.username_input.text()
        # password
        password = self.ui.password_input.text()

        # validate form - kiem tra cac truong nhap day du chua?
        if not username:
            # Chua nhap username
            self.msg_box.setText("Vui long nhap username")
            self.msg_box.exec()
            return
        if not password:
            # Chua nhap password
            self.msg_box.setText("Vui long nhap password")
            self.msg_box.exec()
            return

        # kiem tra thong tin nguoi dung dung khong (admin - admin)
        if username == 'admin' and password == 'admin':
            # dang nhap thanh cong
            # chuyen sang giao dien chinh

            # dong cua so login
            self.close()
        else:
            # dang nhap khong thanh cong
            # hien message loi
            self.msg_box.setText('Username hoac mat khau khong chinh xac!')
            self.msg_box.exec()


if __name__ == "__main__":
    # khoi tao giao dien
    app = QApplication(sys.argv)
    login_form = Login()

    # chay giao dien
    login_form.show()
    app.exec()
