import os

name = input('plaese enter name of the file : ')
path = input('please enter path where you want to add a file : ')
os.chdir(path)
open(name, 'w')
