from src.main.controller.app import app
from src.main.config.config import SERVER_HOST, SERVER_PORT

# 启动后端服务
if __name__ == '__main__':
    app.run(host=SERVER_HOST, port=SERVER_PORT)