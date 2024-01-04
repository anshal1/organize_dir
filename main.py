import os

downloads_path = r"C:\\Users\\Lenovo\Downloads"
# list of supported extension
supported_ext = ("png", "svg", "jpg", "jpeg", "pdf",
                 "exe", "xlsx", "csv", "mp4", "mp3", "msi", "zip", "html", "json", "webp")
files = os.listdir(downloads_path)

# creating the folder with the name of extension only if the folder dosen't exists
for ext in supported_ext:
    if not os.path.exists(os.path.join(downloads_path, ext)):
        os.mkdir(os.path.join(downloads_path, ext))


for file in files:
    # os.path.splitext return a typle 1element is name of file last element is the extension name
    _, file_extension = os.path.splitext(file)
    # slicing the string because the first character is the dot and we so not want the dot
    file_extension = file_extension[1:].lower()
    # checking if the file_extension is in supported_ext
    if file_extension in supported_ext:
        # current path of the file we are looping
        current_path = os.path.join(downloads_path, file)
        # new path of the file
        newpath = os.path.join(downloads_path, file_extension, file)
        # if file does not exists in the new path and exists in the current path only then replace other wise do not do replacing
        if not os.path.exists(newpath) and os.path.exists(current_path):
            os.replace(current_path, newpath)
