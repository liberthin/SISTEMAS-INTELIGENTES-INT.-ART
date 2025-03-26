import serial, time
arduino = serial.Serial("COM2", 9600)
time.sleep(2)

try:
    while True:
        print("\nindique la funcion \n"
        "1: encendido\n"
        "2: apagado\n"
        "3: salir\n")

        ea = input("ingrese el valor indicado:")
        if ea == '1':
            arduino.write(b'e')
            print("se encendio el led")
        elif ea =='2':
            arduino.write(b'a')
            print("se apago el led")
        elif ea == '3':
            print("saliendo del archivo")
            break
        else:
            print("escriba un valor valido")
except:
    print("error")