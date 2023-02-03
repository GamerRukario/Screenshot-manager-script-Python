import shutil
import os
import re


def dir_extract(src_dir):
    i = 0
    nvidia_file_names = []
    temp_dump = []
    while True:
        if i == 0:
            xbox_file_names = os.listdir(src_dir[0])
        elif i == 1:
            nvidia_dir_names = os.listdir(src_dir[1])
            for nvidia_dir_name in nvidia_dir_names:
                temp_dump = os.listdir(src_dir[1]+ '/' + nvidia_dir_name)
                for temp in temp_dump:
                    nvidia_file_names.append('/' + nvidia_dir_name + '/' + temp)
        else:
            break
        i = i+1
    return(xbox_file_names,nvidia_file_names,nvidia_dir_names)
    
def game_dir(file_names):
    game_names = []
    temp_name = ''
    for file_name in file_names:
        if('.png' in file_name):
            temp_name = re.sub('[ ](\d{1,4}[_])(\d{1,4}[_| ])*[a|p][m]([ ][(]\d[)])*','', file_name)
            temp_name = temp_name.replace('.png','')
            if temp_name  not in game_names:
                game_names.append(temp_name)
    return(game_names)

def file_copy(src_dir,dest_dir,file_names,game_names):
    file_type = ['.png','.jpg','.jpeg']
    try:
        for game_name in game_names:
            os.makedirs(dest_dir+'/'+game_name,exist_ok=True)
        for game_name in game_names: 
            for file_name in file_names:   
                if game_name in file_name and '.png' in file_name:                  
                    try:
                        shutil.copy2(src_dir[0]+'/'+file_name,dest_dir+'/'+game_name+'/'+file_name)
                    except:
                        shutil.copy2(src_dir[1]+'/'+file_name,dest_dir+'/'+file_name)
            print(game_name + ' directory is completed')
    except:
        pass

# START
src_dir = ['','']
dest_dir = ''
game_names = []
check_per = input('Do you want to run the script?: [y|n]')
#check_per = 'y'
if check_per == 'y':
    xbox_file_names, nvidia_file_names, nvidia_dir_names = dir_extract(src_dir)
    game_names = game_dir(xbox_file_names)
    game_names = list(set(nvidia_dir_names + game_names))
    file_names = xbox_file_names + nvidia_file_names  
    file_copy(src_dir,dest_dir,file_names,game_names)
else:
    pass
    