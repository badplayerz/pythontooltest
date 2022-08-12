"""
@author: zlh
@file: autoReading.py
@time: 2022/8/12 14:19
@desc: 1. get content in pdf with PyPDF2
       2. reverse words to audio with pyttsx3
"""

import PyPDF2
import pyttsx3

"""
pdf转文字
"""
def getContent(filePath=str) -> str:
    with open(filePath, 'rb') as file:
        content = ""
        pdfReader = PyPDF2.PdfFileReader(file)
        for pageNum in range(pdfReader.numPages):
            content = content+pdfReader.getPage(pageNum).extractText()
        return content

"""
实时读取pdf
"""
def speaker(filePath=str):
    content = getContent(filePath)
    pyttsx3.speak(content)

"""
转换pdf为音频并保存
"""
def transferAndSave(filePath=str):
    content = getContent(filePath)
    print(content)
    speakerEngine = pyttsx3.init()
    speakerEngine.save_to_file(content,"/Users/sdbean-zlh/Documents/autoRead.mp3")
    speakerEngine.runAndWait()


if __name__ == '__main__':
    file_path = "/Users/sdbean-zlh/Downloads/国内nft市场调研.pdf"
    # transferAndSave(file_path)
    speaker(file_path)
