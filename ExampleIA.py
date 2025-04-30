import serial
import time

porta_serial = 'COM3'  # Altere para sua porta correta (ex: /dev/ttyUSB0 no Linux)
baud_rate = 9600

try:
    esp = serial.Serial(porta_serial, baud_rate, timeout=1)
    time.sleep(2)  #o Aguarda conexão estabilizar
    print("Conectado ao ESP32 com sucesso!")

    while True:
        comando = input("Deseja ativar o atuador? (sim/não): ").strip().lower()

        if comando == "sim":
            esp.write(b"servo\n")
            print("Comando enviado ao ESP32: servo")
        else:
            print("Nenhum comando enviado.")

        time.sleep(2)  # Aguarda o tempo de execução do servo

except serial.SerialException:
    print("Erro: não foi possível conectar à porta serial.")
except KeyboardInterrupt:
    print("\nEncerrado pelo usuário.")
