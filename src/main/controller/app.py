from sanic import Sanic, response
import json

from src.main.service.todoListService import *
from src.main.config.config import PROJECT_NAME
app = Sanic(PROJECT_NAME)


# 根路径，返回一个JSON对象
@app.route("/")
async def root(request):
    return response.text("欢迎使用Todo List Service")


# 获取全部的todo任务列表
@app.route("/get/todos", methods=['GET'])
async def getAllList(request):
    try:
        rt = getAllListService()
        return response.text(json.dumps(rt), content_type='application/json')
    except Exception as e:
        rt = Result.error(str(e))
        return response.text(json.dumps(rt), content_type='application/json')


# 获取指定id的todo任务详情
@app.route("/get/todos/<id>", methods=['GET'])
async def getListById(request, id):
    try:
        rt = getListByIdService(id)
        return response.text(json.dumps(rt), content_type='application/json')
    except Exception as e:
        rt = Result.error(str(e))
        return response.text(json.dumps(rt), content_type='application/json')


# 创建一个新的todo任务
@app.route("/post/todos", methods=['POST'])
async def addList(request):
    try:
        data = request.json
        logging.info(f"接收到的todo数据：{data}")
        rt = addListService(data)
        return response.text(json.dumps(rt), content_type='application/json')
    except Exception as e:
        rt = Result.error(str(e))
        return response.text(json.dumps(rt), content_type='application/json')


# 更新指定id的todo任务
@app.route("/put/todos/<id>", methods=['PUT'])
async def updateList(request, id):
    try:
        data = request.json
        logging.info(f"接收到的todo数据：{data}")
        rt = updateListService(id, data)
        return response.text(json.dumps(rt), content_type='application/json')
    except Exception as e:
        rt = Result.error(str(e))
        return response.text(json.dumps(rt), content_type='application/json')


# 删除指定id的todo任务
@app.route("/delete/todos/<id>", methods=['DELETE'])
async def deleteList(request, id):
    try:
        rt = deleteListService(id)
        return response.text(json.dumps(rt), content_type='application/json')
    except Exception as e:
        rt = Result.error(str(e))
        return response.text(json.dumps(rt), content_type='application/json')