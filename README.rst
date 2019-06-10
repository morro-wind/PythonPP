=============
留言板應用
======================

目的
=====

練習開發通過web瀏覽器提交的web 應用程序

工具版本
======================

:Python:        2.7.16
:pip:           19.1.1
:virtualenv:    16.5.0

安裝與啓動方法
=======================

從版本庫獲取代碼，然後在該目錄下搭建virtualenv 環境::

$ git clone https://git
$ cd guestbook
$ virtualenv .venv
$ source .venv/bin/activate
(.venv)$ pip install .
(.venv)$ guestbook
* Running on http://127.0.0.1:8000/

開發流程
===========

用於開發的安裝
------------------
1. 檢測
2. 按以下流程安裝
(.venv)$ pip install -e

變更依賴庫時
------------------

1. 更新``setup.py``的``install_requires``
2. 按以下流程更新環境::

    (.venv)$ virtualenv --clear .venv
    (.venv)$ pip install -e ./guestbook
    (.venv)$ pip freeze > requirements.txt

3. 將setup.py 和requirements.txt 提交到版本庫
