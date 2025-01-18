import json
import os
import random

# 資料檔案
DATA_FILE = "chatbot_data.json"

# 加載資料
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

# 儲存資料
def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# 新增主題
def add_topic(data):
    topic = input("請輸入主題名稱：")
    if topic in data:
        print("主題已存在！")
        return
    keywords = input("請輸入主題關鍵字（以逗號分隔）：").split(",")
    replies = []
    while True:
        reply = input("請輸入回覆內容（輸入 '完成' 結束）：")
        if reply == "完成":
            break
        replies.append(reply)
    data[topic] = {"keywords": [k.strip() for k in keywords], "replies": replies}
    print("主題新增成功！")

# 查詢主題
def list_topics(data):
    if not data:
        print("目前沒有主題。")
    else:
        print("現有主題：")
        for topic, details in data.items():
            print(f"- {topic} (關鍵字：{', '.join(details['keywords'])})")

# 刪除主題
def delete_topic(data):
    topic = input("請輸入要刪除的主題名稱：")
    if topic in data:
        del data[topic]
        print("主題刪除成功！")
    else:
        print("找不到該主題！")

# 聊天功能
def chat(data):
    print("開始聊天吧！（輸入 '退出' 結束）")
    while True:
        user_input = input("你：")
        if user_input == "退出":
            break
        reply_found = False
        for topic, details in data.items():
            # 檢查關鍵字是否在用戶輸入中
            for keyword in details["keywords"]:
                if keyword in user_input:
                    # 隨機選擇回覆
                    reply = random.choice(details["replies"])
                    print(f"機器人：{reply}")
                    reply_found = True
                    break
        if not reply_found:
            print("機器人：我還沒學會這個主題><")

# 主程式
def main():
    data = load_data()
    while True:
        print("\n選擇功能：")
        print("1. 查看主題")
        print("2. 新增主題")
        print("3. 刪除主題")
        print("4. 聊天")
        print("5. 離開")
        choice = input("請輸入選項：")
        if choice == "1":
            list_topics(data)
        elif choice == "2":
            add_topic(data)
        elif choice == "3":
            delete_topic(data)
        elif choice == "4":
            chat(data)
        elif choice == "5":
            save_data(data)
            print("資料已儲存，掰掰！")
            break
        else:
            print("無效選項，請重新輸入！")

if __name__ == "__main__":
    main()
