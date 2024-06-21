from datetime import datetime

from src.main.dao.todoListDao import *
from src.main.pojo.result import Result
from src.main.config.config import *


# 检查提交的数据是否完整以及是否符合要求
def checkTodoList(list):
    for name in LIST_NAME:
        if name not in list.keys():
            return False
    if list['title'] is None:
        return False
    if (list['status'] is not None) and (list['status'] not in ['pending', 'completed', 'cancelled']):
        return False
    return True


def getAllListService():
    data = getAllListDao()
    if data is None:
        return Result.error("列表为空")
    return Result.success(data)


def getListByIdService(id):
    if id.isdigit() is False:
        return Result.error(f'id必须为整数')
    data = getListByIdDao(id)
    if data is None:
        return Result.error(f'未找到id为{id}的数据')
    return Result.success(data)


# 检测提交的待添加数据是否合规并对日期数据进行更新
def addListService(list):
    if checkTodoList(list):
        if list['status'] is None:
            list['status'] = "pending"
        list['created_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        list['updated_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        logging.info(f"更新后数据：{list}")
        addListDao(list)
        return Result.success(None)
    else:
        logging.info(f"添加的错误数据：{list}")
        return Result.error("提交数据不完整或status数据错误")


# 检测提交的待更新数据是否合规并对日期数据进行更新
def updateListService(id, list):
    if checkTodoList(list):
        list['updated_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        logging.info(f"更新后数据：{list}")
        if updateListDao(id, list):
            return Result.success(None)
        else:
            return Result.error(f"不存在id为{id}的数据")
    else:
        logging.info(f"更新数据不完整或status数据错误：{list}")
        return Result.error("更新数据不完整或status数据错误")


# 根据id删除数据
def deleteListService(id):
    if deleteListDao(id):
        return Result.success(None)
    else:
        return Result.error(f"不存在id为{id}的数据")
