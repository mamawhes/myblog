from flask import jsonify 
import json
import os
class article_controller:
    pass
app_info=json.loads(open("../data/info.json",'r',encoding='utf-8').read())
def create_new_article():
    global app_info
    article_info={}
    article_info["id"]=app_info["articleId_count"]+1
    