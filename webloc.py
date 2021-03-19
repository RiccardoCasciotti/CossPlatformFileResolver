import os
import json
import xmltodict
import controller as cont


#Opens the file named name and changes the extension from .webloc to .xml, then creates json out of the file to extract the link address.
def url(name, status):
    try:
        oldName = name

        if name[-6:] == "webloc":
            name  = name[:-7] 
        newName = name + ".xml"
        boneName = name
        os.rename(oldName,newName)
        fd = open(newName,"r")
        obj = xmltodict.parse(fd.read())
        jsonObj = json.dumps(obj)
        fd.close()
        return [boneName, obj["plist"]["dict"]["string"]]
    except Exception as e:
        status = fixer(newName)
        cont.error(newName, status)
        return []

#Creates url file and deletes the old one
def webloc_url(array):
    try:
        if array == []:
            return
        name = array[0]
        link = array[1]

        tmp = name.split("/")
        fixer = name
        actualName = tmp[-1]
        index = len(actualName)
        cleaned_name = cont.space_del(actualName)
        name = name[:-index]
        name = name + cleaned_name

        urlName = name  + ".url"
        f =  open(urlName, "w")
        f.write('[InternetShortcut]\n')
        f.write('URL=%s\n' % link)
        f.write("IconIndex=0")
        os.remove(fixer + ".xml")
        f.close()
        return "FIXED"
    except Exception as e:
        return "NOT FIXED"

def fixer(path):
    tmp = path.split("/")
    name = tmp[-1]
    if path[-3:] == "xml":
        n = path[:-3] + "txt"
        os.rename(path,n)
        f = open(n, "r")
        f.seek(18)
        s = f.read()
        final = ""
        for letter in s: 
            if ord(letter) == 8:
                break
            final = final + letter
        if final[:4] == "http":
            os.rename(n,path)
            status = webloc_url([path[:-4], final])
        else: 
            status = "NOT FIXED"
    else: 
        status = "NOT FIXED"
    return status
