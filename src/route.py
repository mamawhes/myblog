from flask import render_template,url_for
from run import app
from src import ar
import os
import re
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
