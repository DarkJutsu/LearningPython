import os
import shutil

route="C:/Users/samllo/Documents/code/Python/Pruebas/Automation/Module1/files_order"

folders=["Images", "PDF's", "Videos", "Files Word", "Files TXT"]

for folder in folders:
    route_folder=os.path.join(route, folder)

    if not os.path.exists(route_folder):
        os.makedirs(route_folder)

for file in os.listdir(route):
    if file.endswith(".png") or file.endswith(".jpg") or file.endswith(".jpeg"):
        shutil.move(os.path.join(route, file), os.path.join(route, "Images", file))
    elif file.endswith(".pdf"):
        shutil.move(os.path.join(route, file), os.path.join(route, "PDF's", file))
    elif file.endswith(".mp4"):
        shutil.move(os.path.join(route, file), os.path.join(route, "Videos", file))
    elif file.endswith(".docx"):
        shutil.move(os.path.join(route, file), os.path.join(route, "Files Word", file))
    elif file.endswith(".txt"):
        shutil.move(os.path.join(route, file), os.path.join(route, "Files TXT", file))