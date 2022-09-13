


# coding = utf-8
#from tkinter.tix import IMAGE
import pytesseract
from PIL import Image
from util.setting import code_user_info
import base64
import json
import requests

# 仅仅使用简单 没有干扰的图片转化
# image = Image.open('F:/selenium_python/yanzhengma/test1.png')
# text = pytesseract.image_to_string(image)              # 将图片转化成文字
# print(text)

class GetImageCode:

    def base64_api(self, img, typeid=3):
        with open(img, 'rb') as f:
            base64_data = base64.b64encode(f.read())
            b64 = base64_data.decode()
        data = {"username": code_user_info["username"], "password": code_user_info["passwd"], "typeid": typeid, "image": b64}
        result = json.loads(requests.post(code_user_info["url_path"], json=data).text)
        if result['success']:
            return result["data"]["result"]
        else:
            return result["message"]
        return ""




