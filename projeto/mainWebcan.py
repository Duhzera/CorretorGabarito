import cv2
import pickle
import extrairGabarito as exG

campos = []
with open ('campos.pkl', 'rb') as arquivo:
    campos = pickle.load(arquivo)

resp = []
with open ('resp.pkl', 'rb') as arquivo:
    resp = pickle.load(arquivo)

respostasCorretas = ["1-A","2-C","3-C","4-D","5-A"]

video = cv2.VideoCapture(1)
