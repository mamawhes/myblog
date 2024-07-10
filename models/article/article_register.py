import os

FilePath:str="static/notes/"
def get_max_id():
    filesNames=os.listdir(FilePath)
    l=[]
    for name in filesNames:
        l.append(int(name[:-3]))
    if(len(l)==0):
        return -1
    else:
        return max(l)
class Article_Register:
    articles:list
    def __init__(self) -> None:
        from models.article.article import Article
        self.articles=[]
        filesNames=os.listdir(FilePath)
        for names in filesNames:
            id=int(names[:-3])
            a=Article(id)
            a.update_info()
            self.articles.append(a)


        
