def main():
    #escribe tu código abajo de esta línea
    
    def calculate_area(base, profundidad):
        return (base*profundidad)

    def calculate_volume(altura):
        return (calculate_area(base, profundidad)*altura)

    base = float(input('Dame la base: '))
    altura = float(input('Dame la altura: '))
    profundidad = float(input('Dame la profundidad: '))

    print('El volumen del prisma es:',calculate_volume(altura))
    pass

if __name__=='__main__':
    main()
