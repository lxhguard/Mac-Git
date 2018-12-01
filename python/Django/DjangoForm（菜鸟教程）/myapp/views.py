from django.shortcuts import render
from . import models
import json
from django.core import serializers
from django.http import HttpResponse
import pymongo

def success(request):
    return render(request, "success.html")

def index1(request):
    return render(request, "submit.html")

def index2(request):
    # return HttpResponse()
    # if request.method == 'GET':
        # web_id = json.loads(request.body.decode().replace("'", "\"")).get('id')
        # client = pymongo.MongoClient(host='localhost', port=8000)
        # db = client.webdata
        # my_set = db.webchinadata
        # values = []
        # # print(web_id)
        # print(request.body.decode())
    return render(request, "success.html")




    #
    #     for val in my_set.find():
    #         # value = value.decode('utf-8')
    #         # val = json.loads(value)
    #         val["_id"] = str(val["_id"])
    #         val["date"] = str(val["date"])
    #         discount = (''.join(val["discounts"])).split('\n')
    #         dis = [x.strip(' ') for x in discount if x != '']
    #         val["discounts"] = dis
    #         val["accept_coins"] = val["accept_coins"].split(",")
    #         details = (''.join(val["details"])).replace('\n', '')
    #         val["details"] = details
    #         # print(val["_id"])
    #         if val["_id"] == web_id:
    #             values.append(val)
    #     print(json.dumps(values, ensure_ascii=False), content_type="application/json;charset=utf-8")


        # return HttpResponse(json.dumps(values, ensure_ascii=False), content_type="application/json;charset=utf-8")

