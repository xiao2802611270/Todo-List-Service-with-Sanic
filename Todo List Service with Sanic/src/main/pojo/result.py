class Result:
    # 定义返回结果的格式
    # 状态码和状态信息
    code = None  # 状态码
    msg = None  # 状态信息
    data = None  # 返回的数据

    def __init__(self, code, msg, data=None):
        self.code = code  # 1: 成功, 0: 失败
        self.msg = msg  # 状态信息
        self.data = data  # 返回的数据

    @staticmethod
    def success(data):
        return {
            'code': 1,
            'message': 'success',
            'data': data
        }

    @staticmethod
    def error(msg):
        return {
            'code': 0,
            'message': msg,
            'data': None
        }