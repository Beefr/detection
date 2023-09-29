
from detecteur import Detecteur

def start_processing():
    frames_to_skip=20
    path_of_my_model_to_detect_cats="./haarcascade_frontalcatface.xml"
    ddc=Detecteur(path_of_my_model_to_detect_cats, frames_to_skip)
    


if __name__ == '__main__':
    start_processing()
