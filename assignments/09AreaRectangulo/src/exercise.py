def calculate_area(base, altura):
    return (base*altura)
    
def main():
    #escribe tu código abajo de esta línea
    
    base = float(input('Dame la base: '))
    altura = float(input('Dame la altura: '))
    print('El área del rectángulo es:',calculate_area(base, altura))

    pass

if __name__=='__main__':
    main()
