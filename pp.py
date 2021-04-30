from claseFechaHora import FechaHora
if __name__ == '__main__':

    d=int(input("Ingrese Dia: "))

    mes=int(input("Ingrese Mes: "))

    a=int(input("Ingrese Año: "))

    h=int(input("Ingrese Hora: "))

    m=int(input("Ingrese Minutos: "))

    s=int(input("Ingrese Segundos: "))
    
    r = FechaHora () 

    r1 = FechaHora(d,mes,a); # inicializar con 0h 0m 0s

    r2= FechaHora(d,mes,a,h, m, s)
    #r2.test()

    r.Mostrar()

    r1.Mostrar()

    r2.Mostrar()

    poner_hora=int(input("ingresar hora: "))

    r.PonerEnHora(poner_hora) # solamente la hora

    r.Mostrar()

    a=int(input("ingresar hora: "))
    b=int(input("ingresar minutos: "))

    r2.PonerEnHora(a,b) #hora y minutos

    r2.Mostrar()
    a=int(input("ingresar hora: "))
    b=int(input("ingresar minutos: "))
    j=int(input("ingresar segundos: "))

    p.PonerEnHora(a, b, j) #hora, minutos y segundos

    p.Mostrar()

    x=int(input("sumar 3 horas: "))

    r.AdelantarHora(x) #sumar 3 horas a la hora actual

    r.Mostrar()

    x=int(input("ingresar horas para sumar: "))
    y=int(input("sumar minutos: "))

    r1.AdelantarHora(x,y) #sumar 1 hora y 15 minutos a la hora actual

    r1.Mostrar()

    