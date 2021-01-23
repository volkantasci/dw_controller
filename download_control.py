#!/usr/bin/python3


import materials
from os import listdir, sep
from time import sleep
import logging
logging.root.setLevel(logging.NOTSET)


class DownloadControl():
    def __init__(self, path):
        self.path = path
        self.validate_dirs()


    def validate_dirs(self):
        has_to_be = ['Document', 'Compressed', 'Playable', 'Image', 'SourceCode']
        in_path = listdir(self.path)

        for i in has_to_be:
            if i not in in_path:
                _dir = materials.Directory(sep.join([self.path, i]))
                _dir.create()


if __name__ == "__main__":
    c = DownloadControl(sep.join([materials.HOME, 'Downloads']))
    logging.info("Service Started!")

    source_code_ends = ('html', 'css', 'py', 'c', 'cpp', 'js', 'php', 'md')
    image_ends = ('jpeg', 'jpg', 'png', 'svg')
    playable_ends = ('mp4', 'mp3', 'ogg', 'avi', 'mkv', 'flv')
    document_ends = ('docx', 'xlsx', 'pdf', 'epub', 'txt')

    while True:
        sleep(1)
        files = materials.check_files(c.path)['files']

        for file in files:
            for extension in source_code_ends:
                if file.path.endswith(extension.upper()) or file.path.endswith(extension):
                    c.validate_dirs()
                    file.move(sep.join([c.path, 'SourceCode']))
                    logging.info("File moved")
                    break

            for extension in image_ends:
                if file.path.endswith(extension.upper()) or file.path.endswith(extension):
                    c.validate_dirs()
                    file.move(sep.join([c.path, 'Image']))
                    logging.info("File moved")
                    break

            for extension in document_ends:
                if file.path.endswith(extension.upper()) or file.path.endswith(extension):
                    c.validate_dirs()
                    file.move(sep.join([c.path, 'Document']))
                    logging.info("File moved")
                    break

            for extension in playable_ends:
                if file.path.endswith(extension.upper()) or file.path.endswith(extension):
                    c.validate_dirs()
                    file.move(sep.join([c.path, 'Playable']))
                    logging.info("File moved")
                    break