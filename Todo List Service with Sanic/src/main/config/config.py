import os

# 跟目录(src)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# 名称
PROJECT_NAME = "TodoListService"

# 数据库
SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(BASE_DIR, "resources", "SqliteDatabase", "todoList.db")}'
LIST_NAME = ["title", "description", "status"]

# 端口
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 8000
