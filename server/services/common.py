from flask import jsonify

def strs(*input):
    x = ''
    for i in input:
        x = x + str(i)
    return x

native_jsonify = jsonify

def my_json(obj):
    try:
        json_obj = native_jsonify(obj)
    except:
        try:
            json_obj = native_jsonify(obj.__dict__())
        except:
            print("went wrong")
            json_obj = native_jsonify({"code": -1, "message": "parser error"})
    return json_obj
jsonify = my_json