import cv2

# Importando o classificador e iniciando a câmera
classificator = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
web_camera = cv2.VideoCapture(0)
 
# Input de informações importantes
sample = 1
id = input("Digite seu identificador: ")
number_samples = int(input("Quantas vezes quer tirar foto? "))

while True:
    _, image = web_camera.read() # Lendo o vídeo da câmera
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # Transformando a imagem em cinza

    # Detectando as faces na imagem 
    detecteds_face = classificator.detectMultiScale(image_gray, scaleFactor=1.5, minSize=(150, 150))

    # Percorrendo todas as faces detectadas
    for (x, y, l, a) in detecteds_face:
        # Desenhando um retângulo sobre a face
        cv2.rectangle(image, (x, y), (x + l, y + a), (0, 0, 255), 2)

        # Caso aperte 'c', é tirado uma foto para análise
        if cv2.waitKey(1) & 0xFF == ord('c'):
            # Recortando somente o rosto
            image_face = cv2.resize(image_gray[y:y + a, x:x + l], (220, 220))

            # Escrevendo a imagem
            cv2.imwrite("Pictures/pessoa." + str(id) + "." + str(image) + ".jpg", image_face)
            print("[Foto " + str(sample) + " capturada com sucesso]")
            sample += 1

    cv2.imshow("Face", image)
    cv2.waitKey(1)
    if sample >= number_samples + 1:
        break
        
print("Faces capturadas com sucesso")
web_camera.release()
cv2.destroyAllWindows()