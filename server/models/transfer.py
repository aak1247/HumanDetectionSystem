class BaseRtn():
    def __init__(self, code = 0, message = "OK"):
        self.code = code
        self.message = message

    def __dict__(self):
        return {
            "code": self.code,
            "message": self.message
        }

    def __str__(self):
        return str(self.__dict__())


class Rtn(BaseRtn):
    def __init__(self, code = 0, message = "OK", **kw):
        BaseRtn.__init__(self, code, message)
        self.extra = kw
    
    def __dict__(self):
        rtn = dict()
        for k in self.extra:
            rtn[k] = str(self.extra[k])
        rtn['code'] = str(self.code)
        rtn['message'] = str(self.message)

    def __str__(self):
        # rtn = self.extra.copy()
        rtn = self.__dict__()
        return str(rtn)
































