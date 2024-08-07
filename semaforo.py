import serial 
arduino = serial.Serial('COMS', 9600)

while True:
    try:
        leitura = arduino.readline().decode().strip()
        if leitura:
            temperatura = float(leitura)
            if temperatura < 10.5:
                arduino.write(b'B') 
                print ("ta escuro 😣")
            elif temperatura >= 10.5 and temperatura <11.5 :
                 arduino.write(b'V') 
                 print (f"A  luz ta normaç ")
            else :
                arduino.write(b'R') 
                print ( " APAGUE!!!")
    except KeyboardInterrupt:
        break
    except Exception as e :
        print("ocoreu um erro ", e)