import pandas as pd
import os

def make_df():
    file_path = 'data/interim/raw jl corpus (unchecked and unannotated)/JL(wav+txt)/'
    dir_name = 'emotion_recognition'
    cwd = os.getcwd()
    path = os.path.join(cwd[:cwd.index(dir_name)+len(dir_name)+1], *file_path.split('/'))

    file_names = []
    for file in os.listdir(path):
        if file.endswith('.wav'):
            file_names.append(file)

    df = pd.DataFrame({'file_names':file_names, 'emotion':[x.split('_')[1] for x in file_names]})
    df['file_names'] = df['file_names'].apply(lambda x: os.path.join(path, x))

    return df

