# -- coding: utf-8 --
import requests
from datetime import datetime, timedelta
import pytz
import os

# 定義 token 檔案名稱
file_path = "token/line_token"


class Entrance:
    def __init__(self):
        self.line_token = open(file_path, "r").read()  # 跟line申請權杖

    def run(self):

        # 设置時區為 GMT+8
        tz = pytz.timezone('Asia/Taipei')

        # 獲取當前時間，並轉換為 GMT+8 時區
        current_time = datetime.now(tz)

        msg = "今天是 " + current_time.strftime('%Y/%m/%d')

        # 判斷是上午還是下午
        if current_time.hour < 12:
            msg += "，天才少年早上好，要記得打卡上班！"
        else:
            msg += "，天才少年晚上好，要記得打卡下班！"

        self.line_notify_message(msg)

    def line_notify_message(self, msg):
        # 跟line申請權杖
        token = self.line_token

        headers = {
            "Authorization": "Bearer " + token,
            "Content-Type": "application/x-www-form-urlencoded"
        }

        payload = {'message': msg}
        r = requests.post("https://notify-api.line.me/api/notify", headers=headers, params=payload)
        return r.status_code


if __name__ == '__main__':
    # 檢查檔案是否存在
    if not os.path.exists(file_path):
        # 如果檔案不存在，創建一個新檔案
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # 建立檔案
        with open(file_path, 'w') as file:
            file.write('')  # 可以在這裡寫入初始內容

        print(f"已創建新的 line_token 檔案，請填入 Line taken。")
    else:
        execute = Entrance()
        execute.run()
