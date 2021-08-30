def calculate_area(base,profundidad):
    global area
    area = (base*profundidad)

def calculate_volume(area,altura):
    global volume
    volume = calculate_area(base,profundidad)*altura

def main():
    #escribe tu código abajo de esta línea

    base = float(input('Dame la base: '))
    profundidad = float(input('Dame la profundidad: '));
    altura = float(input('Dame la altura: '))
    area = float  (base*profundidad)
    print('El volumen del prisma es:', (area*profundidad))
    pass

if __name__=='__main__':
    main()
