from datetime import datetime
from models.article import article_register
from models.article.article import Article
import time
print(article_register.get_max_id())
a=Article(3)
a.update_info()
print(a.title)
print(a.brief_inc)