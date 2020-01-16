import os

def rename_files():
    
    #Get files names from a folder:
    file_list = os.listdir(r"img")
    print(file_list)

    #Rename filenames:
    for file_name in file_list:
        table = file_name.maketrans(dict.fromkeys({'0','1','2','3','4','5','7','8','9'}))
        os.rename('img/'+file_name, 'img/'+file_name.translate(table))
        print(file_name.translate(table))

rename_files()
        
        

