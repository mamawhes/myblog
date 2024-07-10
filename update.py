import markdown
import os
def getmd(id):
    filenames=os.listdir("notes")
    for name in filenames:
        if name == id+".md":
            file = open("static/notes/"+name,'r',encoding='utf-8').read()
            return file
    return None
    
filenames=os.listdir("notes")
temp=[]
for name in filenames:
    if name[-3:]==".md":
        temp.append(name)
filenames=temp
for f in filenames:
    file = open("static/notes/"+f,'r',encoding='utf-8').read()
    html = markdown.markdown(file)
    with open("buffer/"+f[:-3]+'.html', 'w', encoding='utf-8') as file:
        file.write(html)