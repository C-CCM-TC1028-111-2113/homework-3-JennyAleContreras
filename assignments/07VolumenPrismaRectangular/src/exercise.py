def calculate_area(base,altura):
    global area
    area = (base*altura)

def calculate_volume(area,profundidad):
    global volume
    volume = calculate_area(base,altura)*profundidad

def main():
    #escribe tu código abajo de esta línea

    base = float(input('Dame la base: '))
    profundidad = float(input('Dame la profundidad: '));
    altura = float(input('Dame la altura: '))
    area = float  (base*altura)
    print('El volumen del prisma es:', (area*altura*profundidad))
    pass

if __name__=='__main__':
    main()
