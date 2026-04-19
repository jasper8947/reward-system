# Reward System API

## 專案簡介

一個簡單的點數兌換系統後端 API。
使用者可以查詢商品並用點數兌換。

---

## 功能

* 使用者註冊 / 登入 / 儲值
* 商品查詢 / 新增
* 點數兌換商品（會檢查點數與庫存）

---

## API 文件

啟動專案後，開啟：

http://127.0.0.1:8000/docs/

可透過 Swagger 直接測試所有 API。

---

## 執行方式

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

## 主要 API

### 註冊

POST /register/

### 登入

POST /login/

### 儲值

POST /topup/

### 商品

GET /products/

POST /products/

### 兌換

POST /redeem/

---
