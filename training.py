import cv2
import os
import numpy as np

# Importando sistema de reconhecimento para o treino
lbph = cv2.face.LBPHFaceRecognizer_create()

# Captura das imagens com seus respectivos identificadores
def getImagesWithId():
    # Caminhos os quais as fotos estão
    paths = [os.path.join('Fotos', f) for f in os.listdir('Fotos')]
    faces = []
    ids = []
    for path_image in paths:
        # Lendo a imagem e transformando ela em cinza
        image_face = cv2.cvtColor(cv2.imread(path_image), cv2.COLOR_BGR2GRAY)

        # Capturando id correspondente da face e adicionando-o no vetor
        id = int(os.path.split(path_image)[-1].split('.')[1])
        ids.append(id)
        faces.append(image_face)
    return np.array(ids), faces

ids, faces = getImagesWithId()

print("Tô treinando, calma aí....")

# Treinando o modelo
lbph.train(faces, ids)
lbph.write('classificator.yml')

print("Pronto, terminei...")