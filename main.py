import os

downloads_path = r"C:\\Users\\Lenovo\Downloads"
# list of supported extension
supported_ext = ("png", "svg", "jpg", "jpeg", "pdf",
                 "exe", "xlsx", "csv", "mp4", "mp3", "msi", "zip", "html", "json", "webp")
files = os.listdir(downloads_path)


def ask_for_renaming(file: str, newpath: str, current_path: str) -> dict:
    print(f"--- {file} already exists in the {newpath} directory ---")
    permission = None
    while True:
        print("--- Enter y for Yes n for No ---")
        permission = input(
            "Would you like to save this file with different name: ").lower()
        if permission == "y" or permission == "n":
            break
    if permission == "y":
        tmpfiles = []
        # getting the list of files from the path and if the every time we find the file with the same fielname passed as parameter append that in the tmpfiles list
        for _, __, files in os.walk(newpath):
            if file in files:
                tmpfiles.append(file)
        # renaming the file by prepending the len of tmp files in the name
        renamedfile = f"{len(tmpfiles)}{file}"
        # renaming the file and storing it in the new folder
        os.rename(current_path, os.path.join(newpath, renamedfile))
        return {"success": 0, "name": renamedfile}
    return {"success": 1, "name": "Action terminated"}


# creating the folder with the name of extension only if the folder dosen't exists
for ext in supported_ext:
    if not os.path.exists(os.path.join(downloads_path, ext)):
        os.mkdir(os.path.join(downloads_path, ext))


for file in files:
    # os.path.splitext return a tuple 1'st element is the name of file last element is the extension name
    # unpacking the tuple _ gets the name of file file_extension get's the file extension
    _, file_extension = os.path.splitext(file)
    # slicing the string because the first character is the dot and we do not want the dot
    file_extension = file_extension[1:].lower()
    # checking if the file_extension is in supported_ext
    if file_extension in supported_ext:
        # current path of the file we are looping
        current_path = os.path.join(downloads_path, file)
        # new path for the file
        newpath = os.path.join(downloads_path, file_extension, file)
        # if file does not exists in the new path and exists in the current path, only then replace other wise do not do replacing
        if not os.path.exists(newpath) and os.path.exists(current_path):
            os.replace(current_path, newpath)
        else:
            newpath = os.path.join(downloads_path, file_extension)
            success = ask_for_renaming(file, newpath, current_path)
            if success["success"] == 0:
                print(f"File rename to {
                      success['name']} and saved successfully")
            elif success["success"] == 1:
                print(f"File rename to {
                      success['name']} and saved successfully")


print("Action Completed Successfuly")
