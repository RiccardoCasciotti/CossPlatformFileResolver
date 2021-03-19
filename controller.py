import os
import webloc as webloc
import files_dirs as fd

total = 0
ops = 0
done = 0
root_path = ""

def space_del(name):
    global ops
    final = ""
    for letter in name: 
        if ord(letter) == ord('|') or letter == "*" or letter == ":" or letter == "<" or letter == ">" or letter == "?" or letter == "\\" or letter == "/" or letter == '"' or letter == '”':
            letter = "_"
            ops = ops + 1
        final = final + letter
    return final

def error(name, status):
    global root_path
    f = open( os.path.join( root_path, "log.txt"), "a+")
    f.write("Error with status=" + status + " : " + name + "\n\n")
    f.close()

def printProgressBar (iteration, total, prefix = ' ', suffix = ' ', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    if float(percent) >  100.0:
        percent = str(100.0)
    filledLength = int(length * iteration// total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)

    

def find_file(path):
    global done
    global total
    files = []
    weblocs = []
    directories = []
    #directories.append(path)
    directory = os.scandir(path)
    #tmp = os.scandir(path)
    space = " "
    for entry in directory:
        nome = str(entry.name)
        if  not entry.name.startswith('.') and entry.is_file() and entry.name[-6:] == "webloc":
            weblocs.append(os.path.join(path, entry.name))
        elif not entry.name.startswith('.') and entry.is_file() and (entry.name[:1] == " " or "|" in nome or "*" in nome or ":" in nome or "<" in nome or ">" in nome or "?" in nome or "\\" in nome or "/" in nome or '"' in nome or '”' in nome):
            files.append(os.path.join(path, entry.name))
        elif not entry.name.startswith('.') and entry.is_dir() and (entry.name[:1] == " " or entry.name[-1] == " "):
            directories.append(os.path.join(path, entry.name))

    
    #done = done + len(list(tmp))
    #printProgressBar(done, total)
    #tmp.close()
    directory.close()
    return [files, weblocs, directories]


def execution(path):
    global ops
    elements = find_file(path)
    weblocs = elements[1]
    directories = elements[2]
    files = elements[0]
    ops = ops + len(files) + len(weblocs) + len(directories)
    for web in weblocs:
        array = webloc.url(web, "")
        webloc.webloc_url(array)
    fd.file_fixer(files)
    
    fd.dir_fixer(directories)
    return

def navigator(path):
    execution(path)
    global done
    global total
    for root, subdirs, files in os.walk(path):
        execution(root)
        scan = os.scandir(root) 
        scan = filter(lambda x: x.is_dir(), scan)
        subdirs = []
        tmp = os.scandir(root)
        done += len(list(tmp))
        tmp.close()
        printProgressBar(done, total)
        for e in scan: 
            subdirs.append(e.name)
        for s in subdirs:
            current = os.path.join(root, s)
            execution(current)
            # scan = os.scandir(root) 
            # scan = filter(lambda x: x.is_dir(), scan)
            # subdirs = []
            # for e in scan: 
            #     subdirs.append(e.name)
    return

def controller(path):
    global total
    global done
    global ops
    global root_path 
    root_path = path
    print("Wait, I am analyzing the data...")
    for root, subdirs, files in os.walk(path):
        #for f in files:
        tmp = os.scandir(root)
        total += len(list(tmp))
        tmp.close()
    print("Done\n")
    print("\nData to be analyzed: " + str(int(total)) + "\n")
    navigator(path)
    print()
    if done >= total:
        done = total
    print("\nData analyzed: " + str(int(done)) + "\n")
    print("\nNumber of operations performed: " + str(ops) + "\n")
    return


