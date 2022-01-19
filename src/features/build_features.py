#
import random
import shutil
import os

def get_working_dir():
    dir_name = 'emotion_recognition'
    cwd = os.getcwd()
    wd = cwd[:cwd.index(dir_name)+len(dir_name)+1]
    return wd

emotions = ['happy','sad','angry', 'neutral', 'excited']

def make_df():
    file_path = 'data/interim/raw jl corpus (unchecked and unannotated)/JL(wav+txt)/'
    
    wd = get_working_dir()
    
    path = os.path.join(wd, *file_path.split('/'))
    
    if not os.path.exists(os.path.join(wd, 'data','processed', 'train')):
        os.makedirs(os.path.join(wd, 'data','processed', 'train'))
        os.makedirs(os.path.join(wd, 'data', 'processed', 'test'))
    
    # file_names = []
    random.seed(1234)
    
    for file in os.listdir(path):
        if file.endswith('.wav') and any([emotion in file for emotion in emotions]):
            if random.random() < 0.8:
                shutil.copyfile(os.path.join(path, file), os.path.join(wd, 'data', 'processed', 'train', file))
            else:
                shutil.copyfile(os.path.join(path, file), os.path.join(wd, 'data', 'processed', 'test', file))
            # file_names.append(file)

    
    
    
    # df = pd.DataFrame({'file_names':file_names, 'emotion':[x.split('_')[1] for x in file_names]})
    # df['file_names'] = df['file_names'].apply(lambda x: os.path.join(path, x))

    return None

make_df()

