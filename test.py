from ctypes import *
from sys import platform

bridge = CDLL('./libPosAPI.so')
# bridge = cdll.LoadLibrary('./libPosAPI.so')

result = bridge.sendData
result.restype = c_char_p
print(result().decode('utf-8'))