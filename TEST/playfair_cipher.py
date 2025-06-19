import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from templates.playfair import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)
        self.ui.btn_create_matrix.clicked.connect(self.call_api_create_matrix)
        
    def call_api_create_matrix(self):
        url = "http://127.0.0.1:5000/api/playfair/creatematrix"
        payload = {
            "key": self.ui.txt_key_1.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                if "playfair_matrix" in data and isinstance(data["playfair_matrix"], list):
                    matrix_string = "\n".join(str(row) for row in data["playfair_matrix"])
                    self.ui.txt_matrix.setText(matrix_string)
                    
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Tạo ma trận thành công")
                    msg.exec_()
                else:
                    print("Lỗi: 'playfair_matrix' không tồn tại hoặc không phải danh sách")
            else:
                print(f"Lỗi gọi API: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Lỗi: {str(e)}")
        
    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/playfair/encrypt"
        payload = {
            "plain_text": self.ui.txt_plain_text.toPlainText(),
            "key": self.ui.txt_key_2.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_cipher_text.setText(data["encrypt_text"])
                
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Encrypt successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e.message)
            
    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/playfair/decrypt"
        payload = {
            "cipher_text": self.ui.txt_cipher_text.toPlainText(),
            "key": self.ui.txt_key_2.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_plain_text.setText(data["decrypt_text"])
                
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Decrypt successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e.message)
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())