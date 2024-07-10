import models.article.article_register as article_register
import time
import os
import re
def Create_New_Article(title="标题五个字"):
    with open(f"static/notes/{article_register.get_max_id()+1}.md", 'w', encoding='utf-8') as file:
        file.writelines(f"<!--创建于{time.asctime()} -->")
        file.writelines("\n")
        file.writelines(f"# {title}")      
class Article:
    id:int 
    title:str
    brief_inc:str
    def __init__(self,id) -> None:
        self.id=id
    def get_ctime(self)->float:
        return os.path.getctime(article_register.FilePath+f"{self.id}.md")
    def get_mtime(self)->float:
        return os.path.getmtime(article_register.FilePath+f"{self.id}.md")
    def update_info(self):
        buffer=open(article_register.FilePath+f"{self.id}.md",'r',encoding='utf-8').read()
        title_start_index=buffer.find("#")+2
        title_end_index=buffer.find("\n",title_start_index)
        self.title=buffer[title_start_index:title_end_index]
        inc_end=title_end_index+150
        if(inc_end>len(buffer)):
            inc_end=len(buffer)-1
        buffer = re.sub(r'[\n\r]+', ' ', buffer[title_end_index+1:inc_end])
        buffer = re.sub(r'\（[^)]*\）', '', buffer) 
        buffer = re.sub(r'[>#*]+', ' ', buffer)  
        buffer =re.sub(r'\s+', ' ', buffer).strip()
        if(len(buffer)>50):
            inc_end=50
        else:
            inc_end=len(buffer)
        self.brief_inc=buffer[:inc_end]+"..."
        
    

