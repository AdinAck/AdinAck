import numpy as np
import os
import time
from pynput import keyboard

class Node:
    def __init__(self,data,children,rank):
        self.children = []
        self.data = data
        self.rank = rank

    def addChild(self,data):
        self.children.append(Node(data,0,self.rank+1))

    def addChilren(self,data):
        for i in data:
            self.children.append(Node(i,0,self.rank+1))

    def printTree(self):
        str = ""
        for i in range(self.rank):
            str += "---"
        print("\n",str,self.data)
        for i in self.children:
            i.printTree()
            print(1)

    def printChildred(self):
        for i in self.children:
            print(i)


root = Node("root",0,0)
root.addChild(["bin","boot","dev","etc","home","init","lib","lib64","media","mnt","opt","proc","root","run","sbin","snap","srv","sys","tmp","usr","var"])
root.printTree()
# boot_msg = ["ed0: 6 enabled, 6 configurable",
#             "ed1: 1 enabled, 0 configurable",
#             "\nDecrypting private key",
#             "This will take a long time",
#             "....+...+.+...............+.....+..+.++..........+.",
#             "+...+..++..........+.+.....+..........+............",
#             "............+.................+++........+.++......",
#             "....+.+++...........+..........+..........+......+.",
#             "....+...+.+...............+.....+..+.++..........+.",
#             "+..................+.+.....+..........+............",
#             "..............................+.+........+.++......",
#             "......+.....+.......+..........+..........+......+.",
#             "Complete",
#             "",
#             "SSH connection with remote host established",
#             "",
#             "",
#             ""]
#
# for i in range(len(boot_msg)):
#     print(boot_msg[i])
#     time.sleep(np.random.random())
#
# for i in range(50):
#     print("")
#     time.sleep(.01)
#
# os.system("cls")
