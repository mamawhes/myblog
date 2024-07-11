import os
import re
from flask import Flask, jsonify, render_template
import sys
from src import ar
app=Flask(__name__,template_folder='templates',static_folder="static")
# ...
@app.route('/test')
def test():
    return render_template("test.html")

from models.article.article import Article
def get_articles_ele()->str:
    ele_len=5
    if(len(ar.articles)<5):
        ele_len=len(ar.articles)
    res=""
    for i in range(ele_len):
        article:Article=ar.articles[i]
        res+=str(article.id)+"#"+article.title+"#"+article.brief_inc+"|"
    return res
@app.route('/')
def index():
    return render_template("index.html",articles_ele=get_articles_ele())

def getmd(id):
    filenames=os.listdir("static/notes/")
    for name in filenames:
        if name == id+".md":
            file = open("static/notes/"+name,'r',encoding='utf-8').read()
            return re.sub('[\r\n]', '<br>', file)
    return None
@app.route('/article/<id>')
def article(id):
    return render_template("article.html",content=getmd(id))

if __name__ == '__main__':
    app.debug=True
    #app.run(host=sys.argv[1], port=sys.argv[2])
    #app.run(host="0.0.0.0",port= 443,ssl_context=("/root/ssl/full_chain.pem","/root/ssl/private.key"))
    app.run(host="0.0.0.0",port= 8080)