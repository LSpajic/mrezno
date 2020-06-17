#!/usr/bin/python3.6
import os
from os import listdir
from os.path import isfile, join

def give_dir_items(path):
    lista = os.listdir(path)
    result = []

    for dat in lista:

        datPath = os.path.join(path, dat)
        # print(datPath)
        if os.path.isfile(datPath):
            result.append((dat, "file"))
        elif os.path.isdir(datPath):
            result.append((dat, "directory"))
        elif not os.path.exists(datPath):
            raise Exception("NE POSTOJI {}".format(str(datPath)))
        else:
            result.append((dat, "special"))

    return result

def main():
    path = "."
    result = give_dir_items(path)
    print(result)

if __name__ == "__main__":
    main()