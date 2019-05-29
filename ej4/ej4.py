import os
import shutil
import time

start = time.time()

wd = os.getcwd()
archivos = os.listdir(wd) #enumera los archivos que hay en el wd

#extraigo la ext de los archivos y me quedo con un set de eso
extension = []
for i in archivos:
        extension.append(os.path.splitext(i)[1][1:]) #div el nombre del path en root y ext, y se queda con toda la ext sin el "."
ext = set(extension)

#creo carpetas con el nombre de las extensiones
for i in ext:
        try:
            if not os.path.exists(os.path.dirname(i)):
                os.makedirs(i)
                print("La carpeta", i , "fue creada.")
        except OSError:
            print("La carpeta", i, "ya existe.") #ERROR: si las carpetas existen, ademas de decirme que existen las carpetas jpg, txt y py me tira que una carpeta "" ya existe

#mueve los archivos a las carpetas correspondientes a su ext
#ERROR: esto falla si las carpetas ya existian, no se si es por la carpeta "" porque ahi tira el error
source = os.listdir(wd)
for files in source:
    for j in ext:
        if files.endswith(j):
            destination = wd + "/" + j
            shutil.move(files,destination)

#path de las nuevas carpetas
def get_subdirs(dir):
    return next(os.walk(dir))[1] #ver esto: dirpath, dirnames, filenames -> no me da el path entero
newFolders = get_subdirs(wd)

newFoldersPath = []
for i in newFolders:
    newFoldersPath.append(os.path.join(wd, i))

#encuentra la fecha de la ultima modificacion del archivo -> crea carpeta con ese nombre -> lo mueve ahi
for i in newFoldersPath:
    source = os.listdir(i)
    os.chdir(i) #cambio el wd
    for j in source:
        folderDate = time.ctime(os.path.getmtime(i + "/" + j)) #modification time
        carpeta = (folderDate[8:10] + "_" + folderDate[4:7] + "_" + folderDate[-4:])
        try:
            if not os.path.exists(os.path.dirname(carpeta)):
                os.makedirs(carpeta)
                print("La carpeta", carpeta , "fue creada.")
                destination = i + "/" + carpeta
        except OSError:
            pass
        shutil.move(j,destination)

end = time.time()
print("El programa tardo {} segundos en ejecutarse." .format(end-start))
