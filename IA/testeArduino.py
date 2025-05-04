from tensorflow import keras
from keras.models import load_model
import numpy as np
import cv2
import serial
import time

# Substitua 'COM9' pelo nome da sua porta serial
ser = serial.Serial('COM9', 9600, timeout=1)  

# Função para enviar um comando para o Arduino e ler a resposta
def send_command(command):
    ser.write(command.encode())  # Envia o comando para o Arduino
    print(f"Comando enviado: {command}")  # Confirma que o comando foi enviado
    time.sleep(1)  # Espera um momento para garantir que a resposta seja recebida
    response = ser.readline().decode().strip()  # Lê a resposta do Arduino
    print(f"Resposta recebida: {response}")  # Exibe a resposta recebida
    return response

# Enviando o comando
a = send_command("COMANDO")

# Verificando se o comando foi enviado e a resposta
if a == "Mensagem recebida: COMANDO":
    print("O comando 'Pegar' foi enviado e a resposta foi confirmada.")
else:
    print("A resposta do Arduino não confirmou o comando enviado.")
