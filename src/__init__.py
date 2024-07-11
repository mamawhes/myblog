from flask import Flask
from models.article.article_register import Article_Register
app=Flask(__name__,template_folder='../templates',static_folder="../static")
ar=Article_Register()
from src import route