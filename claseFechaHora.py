#día, mes, año, hora, minutos y segundos, en el formato de 24 horas.
class FechaHora(object):
    __dia=0
    __mes=0
    __año=0
    __hora=0
    __min=0
    __seg=0
    def __init__(self,dia=1,mes=1,año=2021,hora=0,min=0,seg=0):
        if(hora>=0 and hora<24 and min>=-1 and min<=60 and seg>-1 and seg<=60 and mes>0 and mes<13):
            if((año%400==0) or (año%100==0 and año%4==0)):
                mesbisiestos=[31,29,31,30,31,30,31,31,30,31,30,31]
            else:
                mesbisiestos=[31,28,31,30,31,30,31,31,30,31,30,31]
            if(dia<=mesbisiestos[mes-1] and dia>0):
                self.__dia=dia
                self.__mes=mes
                self.__año=año
                self.__hora=hora
                self.__min=min
                self.__seg=seg
            else:
                print("dia mal ingresado")
        
    def Mostrar(self):
        print("--------------")
        print(self.__dia)
        print(self.__mes)
        print(self.__año)
        print(self.__hora)
        print(self.__min)
        print(self.__seg)
        print("--------------")
        print("{}/{}/{}/|{}:{}:{}".format(self.__dia,self.__mes,self.__año,self.__hora,self.__min,self.__seg))
    def PonerEnHora (self,hora=0,minutos=0,h=0):
        if(hora>0 and hora<=24):
            self:__hora=hora
        else:
            print("fuera de rango")
        if(minutos>0 and minutos<=60):
            self.__min=minutos
        if(seg>0 and seg<=60):
            self.__seg=h
    def AdelantarHora (self,h=0,m=0):
        if(h>=0 and h<=60 and m>=1 and m<=60 ):
            self.__hora+=h
            self.__min+=m
        if(self.__hora==24):
            self.__hora-=24
            self.__dia+=1
        if(self.__año%4==0 and self.__año%100==0 and self.__año%400==0):
            print("año bisiesto")
            bi=[31,29,31,30,31,30,31,31,30,31,30,31]
        else:
            bi=[31,28,31,30,31,30,31,31,30,31,30,31]
        if(self.__dia==bi[self.__mes-1]):
            self.__mes+=1
        if(self.__mes==12):
            self.__año+=1
    def test(self ):
        p1=FechaHora(2001,2,3,3,55,23)
        p2=FechaHora(2020,3,4,5,6,78)
        p3=FechaHora(2010,22,23,12,22,22)
        p4=FechaHora(1994,12,20,11,23,45)
        p5=FechaHora(1994,12,20,11,23,45)
        p1.Mostrar()
        p2.Mostrar()
        p3.Mostrar()
        p4.Mostrar()
        p5.Mostrar()

        p1.PonerEnHora()
        p2.PonerEnHora()
        p3.PonerEnHora()
        p4.PonerEnHora()
        p5.PonerEnHora()

        p1.Mostrar()
        p2.Mostrar()
        p3.Mostrar()
        p4.Mostrar()
        p5.Mostrar()

        p1.AdelantarHora()
        p2.AdelantarHora()
        p3.AdelantarHora()
        p4.AdelantarHora()
        p5.AdelantarHora()

        p1.Mostrar()
        p2.Mostrar()
        p3.Mostrar()
        p4.Mostrar()
        p5.Mostrar()

    
        

