import glob
import os

dir_name = os.path.dirname(__file__)
tracking_dir = os.path.join(dir_name, 'corona_tracking/')

def FindByDate(date):
    os.chdir(tracking_dir)
    try:
        file_name = glob.glob('*' + date + '*')
        file_name = tracking_dir + file_name[0]
    except IndexError:
        print("File not found!")
    return file_name

def AllFiles():
    os.chdir(tracking_dir)
    all_files = glob.glob('*.csv')
    try:
        fpath = []
        for file in all_files:
            file = tracking_dir + file
            fpath.append(file)
    except IndexError:
        print("No tracking file")
    return fpath