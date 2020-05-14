import os
from hurry.filesize import size

def _folders(dir_name, combined=True):
        folders = []
        for folder in os.listdir(dir_name):
            if os.path.isdir(os.path.join(dir_name,folder)):
                if(combined):
                    folders.append(os.path.join(dir_name,folder))
                else:
                    folders.append(folder)
        return folders

def print_size(start_path = 'D:/'):
    total_file_size = 0
    folders = _folders( start_path, False );
    folder_size_map = {}
    # print(folders);
    for folder in folders:
        folder_size = 0
        for dirpath, dirnames, filenames in os.walk( os.path.join(start_path, folder) ):
            #print(dirpath);
            for f in filenames:
                fp = os.path.join(dirpath, f)
                # skip if it is symbolic link
                if not os.path.islink(fp):
                    try:
                        folder_size += os.path.getsize(fp)
                    except:
                        pass
        #print("{0} : {1}".format(folder.ljust(30), size(folder_size) ))
        folder_size_map[folder] = folder_size;
        total_file_size += folder_size
    # print the map
    for key in sorted(folder_size_map, key=folder_size_map.get, reverse=True):
        print("{0} : {1}".format(key.ljust(30), size(folder_size_map[key]) ))
    return total_file_size

print("total size", size(print_size())  )
