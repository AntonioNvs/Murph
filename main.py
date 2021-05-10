from Functions import news, weather, finance_actions
import eel
import cv2
import os
import psutil
import _thread as th
import webbrowser

class Recognition_and_Data:
    def __init__(self):
        self.ids = {
            1: {
                'name': 'Antonio',
                'number-timers': 0,
                'sex': 'male'
            },
            2: {
                'name': 'Maria Clara',
                'number-timers': 0,
                'sex': 'female'
            }
        }
        self.name = 0
        self.camera = cv2.VideoCapture(0)
        self.path = os.path.dirname(os.path.realpath(__file__))
        self.temp = None
        self.news = None
        self.actions = None

    def recognition(self):
        # Instanciando as classes de reconhecimento
        classifier = cv2.CascadeClassifier(f"{self.path}\\haarcascade_frontalface_default.xml")
        recognition = cv2.face.LBPHFaceRecognizer_create()
        recognition.read(f'{self.path}\\classificator.yml')

        # Loop infinito até encontrar a mesma face 5 vezes
        while True:
            conected, image = self.camera.read() # Lendo a imagem da câmera
            imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # Transformando-a em cinza
            faceDetecteds = classifier.detectMultiScale(imageGray, scaleFactor=1.5) # Detectando as faces

            detection_people = False

            # Percorrendo todas as faces detectadas
            for (x, y, l, a) in faceDetecteds:
                # Recortando a imagem detectada
                imageFace = cv2.resize(imageGray[y:y + a, x:x + l], (100, 100))
                # cv2.rectangle(image, (x, y), (x + l, y + a), (0, 0, 255), 2)

                id, confience = recognition.predict(imageFace) # Conferindo com a base de dados

                self.ids[id]['number-timers'] += 1 # Somando um a variável das amostras já coletadas
                name = self.ids[id]['name']
                # cv2.putText(image, name, (x, y + (a + 30)), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255))

                # Verificando se passou já do limite de amostras, se sim, o ciclo é encerrado
                if self.ids[id]['number-timers'] > 5:
                    self.name = name
                    detection_people = True
                    break

            if detection_people:
                break

            # cv2.imshow("Face", imagem)
            if cv2.waitKey(1) == ord('q'):
                break

        self.camera.release()
        cv2.destroyAllWindows()

eel.init('web')
classManipulation = Recognition_and_Data() # Instanciando a classe de Reconhecimento

# Função de carregamento dos dados gráficos de CPU, RAM e Disk
@eel.expose()
def get_data_graphs():
    def loadData():
        while True:
            disk = psutil.disk_usage('/')
            disk = (disk[1] / disk[0])*100
            eel.loadDataGraphs(int(psutil.cpu_percent()), int(psutil.virtual_memory()[2]), int(disk))
            eel.sleep(1)
            
    th.start_new_thread(loadData, ())

# Função de carregamento dos dados do clima
@eel.expose()
def get_weather(type):
    def lD():
        if not classManipulation.temp:
            classManipulation.temp = weather.get_info_weather()

        temp = int(classManipulation.temp["main"]["temp"]) - 273
        description = classManipulation.temp["weather"][0]["description"].capitalize()

        if not type == "init":
            eel.loadWeather(temp, description)

    th.start_new_thread(lD, ())

# Função de captura das notícias
@eel.expose()
def get_news(type):
    def loadDataNews():
        if not classManipulation.news:
            classManipulation.news = news.news()
        news_selected = []

        news_already_selected = 0
        for new in classManipulation.news:
            description = new['description']
            url_image = new['urlToImage']
            url = new['url']
            title = new['title']

            if description != None and url_image != None and title != None and url != None:
                news_selected.append({
                    'title': title if len(title) < 70 else title[:68] + '..',
                    'description': description if len(description) < 100 else description[:98] + '..',
                    'url': url,
                    'url_image': url_image,
                })
                news_already_selected += 1

            if news_already_selected >= 4:
                break
        
        if not type == "init":
            eel.loadNews(news_selected)
    th.start_new_thread(loadDataNews, ())

# Função de acesso a notícia
@eel.expose()
def access_new(url):
    webbrowser.open(url)

# Função inicializadora do processo de reconhecimento facial
@eel.expose()
def recognition():
    def wait_recognition():
        classManipulation.recognition()

        while classManipulation.news == None or classManipulation.temp == None or classManipulation.actions == None:
            eel.modifyText()
            pass
        eel.passName()

    th.start_new_thread(wait_recognition, ())

# Função de captura dos valores das ações
@eel.expose()
def get_value_actions(type):
    def load_value_actions():
        if not classManipulation.actions:
            classManipulation.actions = finance_actions.get_values_actions()

        if not type == "init":
            eel.loadActions(classManipulation.actions)
    th.start_new_thread(load_value_actions, ())

# Função de retorno do nome da pessoa detectada
@eel.expose()
def get_name():
    return classManipulation.name

eel.start(f'{classManipulation.path}\\web\\init.html')
