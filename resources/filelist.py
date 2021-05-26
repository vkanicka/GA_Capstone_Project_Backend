from os import listdir

file_list = listdir('./resources')

string_model_list = [f.replace('.py','') for f in file_list if ".py" in f and 'filelist' not in f]
