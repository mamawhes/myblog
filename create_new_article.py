from models.article.article import Create_New_Article
import sys
if __name__ == '__main__':
    
    if(len(sys.argv)>1):
        Create_New_Article(sys.argv[1])
    else:
        Create_New_Article()