def calculo():
    
    x = 7.0 #Cuando X Vale 7
    
    while x <= 9.5: #Hasta que x vale 9.5
        
        dy = 1.06*(x**2) - 17.34*x +71.33 #La derivada de la formula de la curva
        dy2 = abs(2.12*x - 17.34) #El valor absoluto de la segunda derivada
        
        r = (((1+dy**2)**(3/2))/(dy2))*42.12082 #Formula para calcular el radio
        
        ac = (798*(31.8915**2))/r #Formula para calcular la aceleracion centripeda a 31.8915m/s con una masa de 798kg
        
        f = (1.5 * 798 * 9.81 * 0.978) #Formula de la friccion, con el coseno de 20°
        
        
        if ac >= f:
        
            print(f"El radio cuando x = {x} es {r} y la aceleracion centripeda es {ac} y la friccion es {f}") #Si la aceleracion es mayor que la friccion, el carro desliza
            
        else:
            print(f"El radio cuando x = {x} no desliza")
        
        x += 0.1 #Todo en intervalos de 0.1x
        
        
        
calculo()
        