from os import sep, listdir, mkdir, remove
from os.path import exists,  isdir, isfile, expanduser
from shutil import rmtree, move


HOME = expanduser('~')


class Material:
    def __init__(self, path:str):
        self.path = path
        self.name = self.path.split(sep)[-1]


    def create(self):
        mkdir(self.path)


    def exists(self):
        return exists(self.path)

    def delete(self):
        pass # Overrite this method

    def move(self, target):
        move(self.path, sep.join([target, self.name]))


class Directory(Material):
    def get_all_of_them(self):
        return listdir(self.path)

    def delete(self):
        try:
            rmtree(self.path)
        except FileNotFoundError:
            print("Path doesn't exists: {}".format(self.path))

        except PermissionError:
            print("You have not permission here!")



class File(Material):
    def delete(self):
        try:
            remove(self.path)
        except FileNotFoundError:
            print("Path doesn't exists: {}".format(self.path))

        except PermissionError:
            print("You have not permission here!")




def check_files(path):
    item_list = listdir(path)
    files = []
    dirs = []

    for item in item_list:
        if isdir(sep.join([path,item])):
            dirs.append(Directory(sep.join([path,item])))

        elif isfile(sep.join([path,item])):
            files.append(File(sep.join([path,item])))

        else:
            print(f"Not matched any kind item(file, dir): {item}")

    return {'files': files, 'dirs': dirs}




if __name__ == "__main__":
    print("This module for development, not use!")
    