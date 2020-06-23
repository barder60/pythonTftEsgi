from os import walk
import os
# TODO: Surement ici mettre l'extracteur de json
from os.path import splitext


class FileManager(object):
    def __init__(self):
        self.val = None

    def __str__(self):
        return 'self' + self.val

    instance = None


    def __new__(cls):
        if not FileManager.instance:
            FileManager.instance = datafileManagerTft()
        return FileManager.instance


def datafileManagerTft():
    fileManager = {}
    for (dirpath, dirnames, filenames) in walk(os.getcwd() + '\\ressources'):
        for filename in filenames:
            name = splitext(filename)[0].strip().lower()
            extension = splitext(filename)[1][1:].strip().lower()

            if extension in fileManager:
                fileManager[extension][name] = os.path.join(dirpath, filename)
            else:
                fileManager[extension] = {}
                fileManager[extension][name] = os.path.join(dirpath, filename)

    return fileManager
