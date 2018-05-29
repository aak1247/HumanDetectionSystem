from flask import jsonify
from demjson import encode as encodeJSON
from simplejson import loads as decodeJSON

def strs(*input):
    x = ''
    for i in input:
        x = x + str(i)
    return x

native_jsonify = jsonify

def my_json(obj):
    try:
        json_obj = native_jsonify(obj)
    except Exception as e:
        # print(str(type(e)))
        try:
            json_obj = native_jsonify(obj.__dict__())
        except Exception as e:
            # print(str(type(e)))
            try:
                temp_str = str(obj)
                temp_str = temp_str.translate(str.maketrans("\"\'","\'\""))
                json_obj = native_jsonify(decodeJSON(temp_str))
            except Exception as e:
                # print(str(type(e)))
                print("went wrong")
                json_obj = native_jsonify({"code": -1, "message": "parser error"})
    return json_obj

def parseJson(strObj):
    try:
        dict_obj = decodeJSON(strObj)
    except:
        dict_obj = decodeJSON(strObj.translate(str.maketrans("\"\'","\'\"")))
    return dict_obj

jsonify = my_json