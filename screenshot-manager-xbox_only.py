import shutil
import os
import re


def dir_extract(src_dir, dest_dir):
    file_names = os.listdir(src_dir)
    return(file_names)
    
def game_dir(file_names):
    game_names = []
    temp_name = ''
    for file_name in file_names:
        if('.png' in file_name):
            temp_name = re.sub('[ ](\d{1,4}[_])(\d{1,4}[_| ])*[a|p][m]([ ][(]\d[)])*','', file_name)
            if temp_name.replace('.png','') not in game_names:
                game_names.append(temp_name.replace('.png',''))
    return(game_names)

def file_copy(src_dir,dest_dir,file_names,game_names):
    try:
        for game_name in game_names:
            os.makedirs(dest_dir+'/'+game_name,exist_ok=False)
        for file_name in file_names:
            for game_name in game_names:
                if game_name in file_name and '.png' in file_name:
                    shutil.copy2(src_dir+'/'+file_name,dest_dir+'/'+game_name+'/'+file_name)
    except:
        pass

# START
src_dir = ''
dest_dir = ''
game_names = []
check_per = input('Do you want to run the script?: [y|n]')
#check_per = 'y'
if check_per == 'y':
    file_names = dir_extract(src_dir, dest_dir)
    game_names = game_dir(file_names)
    file_copy(src_dir,dest_dir,file_names,game_names)
else:
    pass
    