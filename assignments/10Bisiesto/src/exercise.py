def calculate_bisiesto(año):
    if(año%400==0)or(año%100!=0)and(año%4==0):
        return ('True')
    else:
        return ('False')
    
def main():
    #escribe tu código abajo de esta línea

    año = int(input())
    print(calculate_bisiesto(año))
    
    pass

if __name__=='__main__':
    main()
