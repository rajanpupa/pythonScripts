from FileSystem import FileSystem

fs = FileSystem()

# folder under test
trg_folder = "C:\\Users\Raj\Downloads"

#files = fs._files(trg_folder)
#print(files)
file_category=dict({
    '_music': [".mp3"],
    '_video': [".mp4", ".mov", ".mkv", ".flv"],
    '_doc'  : [".txt", ".pdf", ".csv", "doc", ".docx"],
    "_binary": [".exe", ".zip", ".msi", ".iso", ".dll"]
})

for folder,extensions in file_category.items():
    movecount = fs.move_files_with_ext(trg_folder, trg_folder+"\\"+folder, extensions)
    print("{0} moved {1}".format(folder, movecount) )


