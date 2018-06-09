from functools import wraps
from flask import make_response, request, Response
from werkzeug.datastructures import Headers


def allow_cross_domain(fun):
    @wraps(fun)
    def wrapper_fun(*args, **kwargs):
        rst = make_response(fun(*args, **kwargs))
        rst.headers['Access-Control-Allow-Origin'] = request.headers['Origin']
        rst.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE,PATCH,HEAD'
        rst.headers["Access-Control-Allow-Credentials"] = 'true'
        allow_headers = "Referer,Accept,Origin,User-Agent"
        rst.headers['Access-Control-Allow-Headers'] = allow_headers
        return rst
    return wrapper_fun

class MyResponse(Response):
    def __init__(self, response=None, **kwargs):
        try:
            headers = kwargs.get('headers')
        except:
            kwargs['headers'] = ''
            headers = kwargs.get('headers')
        # 跨域控制 
        print(str(headers))
        origin = ('Access-Control-Allow-Origin', request.headers['Origin'])
        methods = ('Access-Control-Allow-Methods', 'HEAD, OPTIONS, GET, POST, DELETE, PUT')
        credits = ("Access-Control-Allow-Credentials", 'true')
        if headers:
            headers.add(*origin)
            headers.add(*methods)
            headers.add(*credits)
        else:
            headers = Headers([origin, methods, credits])
        kwargs['headers'] = headers
        return super().__init__(response, **kwargs)