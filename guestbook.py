# coding: utf-8
import shelve
from datetime import datetime

from flask import Flask, request, render_template, redirect, escape, Markup

application = Flask(__name__)

DATA_FILE = 'guestbook.dat'

def save_data(name, comment, create_at):
    """保存提交的數據
    """
    # 通過shelve 模塊打開數據庫文件
    database = shelve.open(DATA_FILE)
    # 如果數據庫中沒有greeting_list,就新建一個表
    if 'greeting_list' not in database:
        greeting_list = []
    else:
        # 從數據庫獲取數據
        greeting_list = database['greeting_list']
    # 將提交的數據添加到表頭
    greeting_list.insert(0, {
        'name': name,
        'comment': comment,
        'create_at': create_at,
        })
    # 更新數據庫
    database['greeting_list'] = greeting_list
    # 關閉數據庫文件
    database.close()

def load_data():
    """返回已提交的數據
    """
    # 通過shelve模塊打開數據庫文件
    database = shelve.open(DATA_FILE)
    # 返回greeting_list。如果沒有數據則返回空表
    greeting_list = database.get('greeting_list', [])
    database.close()
    return greeting_list

@application.route('/')
def index():
    """首頁
    使用模板顯示頁面
    """
    # 讀取已提交的數據
    greeting_list = load_data()
    return render_template('index.html', greeting_list=greeting_list)

@application.route('/post', methods=['POST'])
def post():
    """用於提交評論的URL
    """
    # 獲取已提交的數據
    name = request.form.get('name') # 名字
    comment = request.form.get('comment')   # 留言
    create_at = datetime.now()  # 投稿時間(當前時間)
    # 保存數據
    save_data(name, comment, create_at)
    # 保存後重定向到首頁
    return redirect('/')

@application.template_filter('nl2br')
def nl2br_filter(s):
    """將換行符置換爲br標籤的模板過濾器
    """
    return escape(s).replace('\n', Markup('<br>'))

@application.template_filter('datetime_fmt')
def datetime_fmt_filter(dt):
    """使datetime 對象更容易分辨的模板過濾器
    """
    return dt.strftime('%Y/%m/%d %H:%M:%S')
if __name__ == '__main__':
    # 在Ip地址127.0.0.1 的8000端口運行應用程序
    application.run('127.0.0.1', 8000, debug=True)
