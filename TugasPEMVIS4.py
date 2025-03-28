# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'percobaan.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5.QtWidgets import *

class POSApplication(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("POS Application")
        self.setGeometry(100, 100, 400, 300)
        
        self.produks = {
            "-" : 0,
            "Bimoli (Rp. 20,000)": 20000,
            "Indomie (Rp. 3,000)": 3000,
            "Beras (Rp. 75,000)": 75000,
            "Kecap (Rp. 7,000)": 7000,
            "Saos Saset (Rp. 2,500)": 2500
        }
        
        self.initUI()
        
    def initUI(self):
        layout = QVBoxLayout()
        
        self.nama_label = QLabel("NAMA : Baiq Sindi Hanjani")
        self.nim_label = QLabel("NIM : F1D022115")
        layout.addWidget(self.nama_label)
        layout.addWidget(self.nim_label)

        produk_layout = QHBoxLayout()
        self.produk_label = QLabel("Produk")
        self.produk_combo = QComboBox()
        self.produk_combo.addItems(self.produks.keys())
        self.produk_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        produk_layout.addWidget(self.produk_label)
        produk_layout.addWidget(self.produk_combo)
        layout.addLayout(produk_layout)
        
        jumlah_layout = QHBoxLayout()
        self.jumlah_label = QLabel("Jumlah Produk")
        self.jumlah_input = QLineEdit()
        self.jumlah_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        jumlah_layout.addWidget(self.jumlah_label)
        jumlah_layout.addWidget(self.jumlah_input)
        layout.addLayout(jumlah_layout)
        
        diskon_layout = QHBoxLayout()
        self.diskon_label = QLabel("Diskon")
        self.diskon_combo = QComboBox()
        self.diskon_combo.addItems(["0%", "5%", "10%", "15%"])
        self.diskon_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        diskon_layout.addWidget(self.diskon_label)
        diskon_layout.addWidget(self.diskon_combo)
        layout.addLayout(diskon_layout)
        
        button_layout = QHBoxLayout()
        self.add_button = QPushButton("Tambah ke Keranjang")
        self.add_button.clicked.connect(self.add_to_cart)
        self.clear_button = QPushButton("Hapus")
        self.clear_button.clicked.connect(self.clear_cart)
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.clear_button)
        layout.addLayout(button_layout)
        
        self.cart_display = QTextEdit()
        self.cart_display.setReadOnly(True)
        layout.addWidget(self.cart_display)
        
        self.total_label = QLabel("Total Belanjaan: Rp. 0")
        layout.addWidget(self.total_label)
        
        self.setLayout(layout)
        self.total = 0
        
    def add_to_cart(self):
        produk = self.produk_combo.currentText()
        jumlah_text = self.jumlah_input.text()
        diskon_text = self.diskon_combo.currentText()
        
        if not jumlah_text.isdigit() or int(jumlah_text) <= 0:
            self.total_label.setText("Invalid Input")
            return
        
        harga = self.produks[produk]
        jumlah = int(jumlah_text)
        diskon = int(diskon_text.replace('%', ''))
        
        total_harga = harga * jumlah
        diskon_amount = total_harga * (diskon / 100)
        final_harga = total_harga - diskon_amount
        
        self.total += final_harga
        
        self.cart_display.append(f"{produk} (Rp. {harga}) - {jumlah} x Rp. {harga} (disc {diskon}%)")
        self.total_label.setText(f"Total Belanjaan: Rp. {int(self.total)}")
        
    def clear_cart(self):
        self.cart_display.clear()
        self.total = 0
        self.total_label.setText("Total Belanjaan: Rp. 0")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = POSApplication()
    window.show()
    sys.exit(app.exec_())
