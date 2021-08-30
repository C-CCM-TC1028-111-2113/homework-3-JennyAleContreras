def calculate_tarjetas(pliegos, plumones):
    global plieg, plum
    plieg=(pliegos*12)
    plum=(plumones*35)
    return min(plieg, plum)
    
def main():
    #escribe tu código abajo de esta línea

    pliegos = int(input('Dame la cantidad de pliegos de papel albanene: '))
    plumones = int(input('Dame la cantidad de plumones: '))
    print('El número máximo de tarjetas que se pueden hacer es:',calculate_tarjetas(pliegos, plumones))
    
    pass

if __name__=='__main__':
    main()
