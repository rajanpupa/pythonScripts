import os, shutil
import send2trash
from typing import List

class FileSystem:
    def move_files_with_ext(self, src_dir: str, trg_dir: str, ext: List[str])->int:
        count = 0
        if not os.path.isdir(src_dir):
            print("src_dir does not exist")
            return count
        if self._create_if_not_exist(trg_dir):
            for file in self._files(src_dir):
                if self._has_extension(file, ext):
                    self._move(file, trg_dir);
                    count += 1
        return count

    def _create_if_not_exist(self, trg_dir)->bool:
        if os.path.isdir(trg_dir):
             return True
        elif os.path.isfile(trg_dir):
            return False
        else:
            os.makedirs(trg_dir);

    # return list of files of a directory
    def _files(self, dir_name):
        files = []
        for filename in os.listdir(dir_name):
            if os.path.isfile(os.path.join(dir_name, filename)):
                files.append( os.path.join(dir_name,filename))
        return files
    # return list of folders of a directory
    def _folders(self, dir_name):
        folders = []
        for folder in os.listdir(dir_name):
            if os.path.isdir(os.path.join(dir_name,folder)):y
                folders.append(os.path.join(dir_name,folder))
        return folders
    # delete a file to recycle bin
    # # delete a folder to recycle bin
    def _soft_delete(self, filename):
        send2trash.send2trash(filename)
    # move a file from one location to another
    def _move(self, srcFile, dstFolder):
        if self._create_if_not_exist(dstFolder):
            shutil.move(srcFile, dstFolder);
    
    def _has_extension(self, filename: str, ext_list: List)->bool:
        ext = os.path.splitext(filename)[1]
        return ext in ext_list

fs = FileSystem()
trg_folder = "C:\\Users\Raj\Downloads"
music_folder = trg_folder+"\\_music"

# ans = fs._has_extension("abc.txt", [".txt", ".pdf"])
ans = fs.move_files_with_ext(trg_folder, music_folder, [".mp3"])
print(ans)