from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import declarative_base, sessionmaker
from src.main.config.config import *
import logging

# 创建数据库连接
Base = declarative_base()
engine = create_engine(SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()
logging.basicConfig(level=logging.INFO)


# 创建数据表
class TodoList(Base):
    __tablename__ = 'todo_list'
    id = Column(Integer, primary_key=True)
    title = Column(Text)
    description = Column(Text)
    status = Column(Text)
    created_at = Column(String)
    updated_at = Column(String)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'status': self.status,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }


# 获取数据库表中全部信息
def getAllListDao():
    todoLists = session.query(TodoList).all()
    logging.info(f"从数据库中获取的全部数据共计{len(todoLists)}个")
    todoListsDict = [todo.to_dict() for todo in todoLists]
    return todoListsDict


# 根据id从数据库中获取数据
def getListByIdDao(id):
    todoList = session.query(TodoList).filter(TodoList.id == id).first()
    if todoList is None:
        return None
    todoListDict = todoList.to_dict()
    logging.info(f"从数据库中获取的数据为：{todoListDict}")
    return todoListDict


# 向数据库中添加数据
def addListDao(list):
    newTodoList = TodoList(title=list['title'], description=list['description'], status=list['status'],
                           created_at=list['created_at'], updated_at=list['updated_at'])
    session.add(newTodoList)
    session.commit()
    logging.info(f"向数据库中添加数据：{list}")


# 根据id更改数据库对应的数据
def updateListDao(id, list):
    todoList = session.query(TodoList).filter(TodoList.id == id).first()
    if todoList is None:
        return False
    todoList.title = list['title']
    todoList.description = list['description']
    todoList.status = list['status']
    todoList.created_at = list['created_at']
    todoList.updated_at = list['updated_at']
    logging.info(f"向数据库中更新后数据：{list}")
    session.commit()
    return True


# 根据id删除数据库对应的数据
def deleteListDao(id):
    todoList = session.query(TodoList).filter(TodoList.id == id).first()
    if todoList is None:
        return False
    session.delete(todoList)
    session.commit()
    return True
