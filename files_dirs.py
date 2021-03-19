import os
import json
import xmltodict
import controller as cont

def file_fixer(files):
    array = []
    for f in files:
        tmp = f.split("/")
        oldName = tmp[-1]
        index = len(oldName)
        newName = cont.space_del(str(file_aux(oldName)))
        os.rename(f, os.path.join(f[:-index], newName) )
        array.append(newName)
    return
def file_aux(name):
    if not name[0] == " ":
        return name
    name = name[1:]
    return file_aux(name)

def dir_fixer(dirs):
    array = []
    for f in dirs: 
        tmp = f.split("/")
        oldName = tmp[-1]
        index = len(oldName)
        newName = cont.space_del(dir_aux(oldName))
        os.rename(f, os.path.join(f[:-index], newName) )
        array.append(newName)
    return array
    

def dir_aux(name):
    if not name[0] == " " and not name[-1] == " ":
        return name
    elif name[0] == " ":
        name = name[1:]
    elif name[-1] == " ":
        name = name[:-1]
    
    return dir_aux(name)
