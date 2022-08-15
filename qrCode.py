"""
@author: zlh
@file: qrCode.py
@time: 2022/8/12 16:12
@desc: qr create and save png
"""

import pyqrcode
import png # need pip install pypng

if __name__ == '__main__':
    file_path = "QRcode.png"
    qr_code = pyqrcode.create("www.baidu.com")
    qr_code.png(file_path,scale=5)
