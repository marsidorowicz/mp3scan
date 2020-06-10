import os
import fnmatch
import id3reader_p3 as id3


def find_file_name(root, filename=None, start=None, ext=None):
    if filename:
        if start:
            for path, directories, files in os.walk(root):
                if start in path:
                    for file in (f for f in files if fnmatch.fnmatch(f, filename)):
                        if ext:
                            file_name, file_ext = os.path.splitext(file)
                            if ext in file_ext:
                                yield os.path.abspath(path) + "\\" + file
                        else:
                            yield os.path.abspath(path) + "\\" + file
        else:
            for path, directories, files in os.walk(root):
                for file in (f for f in files if fnmatch.fnmatch(f, filename)):
                    if ext:
                        file_name, file_ext = os.path.splitext(file)
                        if ext == file_ext:
                            yield os.path.abspath(path) + "\\" + file
                    else:
                        yield os.path.abspath(path) + "\\" + file
    else:
        if start:
            for path, directories, files in os.walk(root):
                if start in path:
                    for file in files:
                        file_name, file_ext = os.path.splitext(file)
                        if ext:
                            if ext == file_ext:
                                yield os.path.abspath(path) + "\\" + file
                        else:
                            yield os.path.abspath(path) + "\\" + file
        else:
            for path, directories, files in os.walk(root):
                for file in files:
                    file_name, file_ext = os.path.splitext(file)
                    if ext:
                        if ext == file_ext:
                            yield os.path.abspath(path) + "\\" + file
                    else:
                        yield os.path.abspath(path) + "\\" + file


file_list = find_file_name("Polskie",  ext=".mp3")


def get_tag(filelist):
    errors = []
    for f in file_list:
        try:
            id3r = id3.Reader(f)
            print("Artist: {}, Album: {}, Track: {}, Song: {}".format(
                id3r.get_value('performer'),
                id3r.get_value('album'),
                id3r.get_value('track'),
                id3r.get_value('title')
            ))
        except:
            errors.append(f)


get_tag(file_list)
