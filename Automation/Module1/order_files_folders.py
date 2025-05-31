import os
import shutil

route="C:/Users/samllo/Documents/code/Python/Pruebas/Automation/Module1/files_order"

folders=["Images", "PDF's", "Video", "Files Word", "Files TXT"]

for folder in folders:
    route_folder=os.path.join(route, folder)

    if not os.path.exists(route_folder):
        os.makedirs(route_folder)