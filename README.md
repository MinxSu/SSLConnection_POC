# Private IP Connection

### 說明
使用 Private IP ＋ 憑證直連資料庫

### 安裝套件
 - sqlalchemy
 - pg8000

### 前置作業
 - 設定 VPC

### 資料庫設定
- 關閉 Public IP
- 開啟 Private IP：設定 VPC
- 開啟 僅允許ＳＳＬ連線
- 產生憑證 （並下載備用）

### Cloud Run 設定
- 掛入要連線的資料庫
- 設定vpc (同資料庫設定)

![連線機制(紅線)](./docs/SSL_Connection.png "SSL connetion with Private IP")

### 參考資料
[SqlAlchemy Samples](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/cloud-sql/postgres/sqlalchemy) <br/>