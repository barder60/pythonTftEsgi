from .utils.fileManager import datafileManagerTft
from easydict import EasyDict as edict
fileManager = datafileManagerTft()
fileManager = edict(fileManager)
