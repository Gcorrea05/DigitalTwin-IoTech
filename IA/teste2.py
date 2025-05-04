from tensorflow import keras
from keras.models import load_model
import numpy as np
import cv2
import serial
import time

# Carregar o modelo
model = load_model('Model/keras_model.h5')
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# Captura de vídeo
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Erro ao abrir a câmera.")
    exit()

classes = ['Creme De Leite', 'Sabonete', 'Fosforo', 'Gelatina', 'Extrato de tomate', 'Pasta de Dente', 'Toddynho', 'Mesa']

pedido = input("Insira o objeto que deseja ser pego: ")
veri = True
 
while veri:
    if pedido in classes:
        while True:
             # Mandar andar
            andou = True
            if andou:
                start_time = time.time()
                # Verificar objeto
                while True:
                    if time.time() - start_time > 5:
                        break
                    success, img = cap.read()
                    if not success:
                        print("Erro ao capturar a imagem.")
                        break
            
                    imgS = cv2.resize(img, (224, 224))
                    image_array = np.asarray(imgS)
                    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
                    data[0] = normalized_image_array

                    # Realizar a previsão
                    prediction = model.predict(data)
                    indexVal = np.argmax(prediction)

                    # Exibir a classe prevista na imagem
                    cv2.putText(img, str(classes[indexVal]), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                    print(classes[indexVal])

                    # Mostrar a imagem
                    cv2.imshow('img', img)
                    if cv2.waitKey(1) & 0xFF == ord('q'):  # Pressione 'q' para sair
                        break
                    
                    time.sleep(1)
                if classes[indexVal] == pedido:
                    print("Objeto encontardo")
                    andou = False
                    break

        veri = False  # Corrigido: deve usar '=' para atribuição
    else:
        print("Digite um objeto válido")
        pedido = input("Insira o objeto que deseja ser pego: ")
 
# Liberar câmera e fechar janela
cap.release()
cv2.destroyAllWindows()

