import math

def distancia_euclidiana(x_1, y_1, x_2, y_2):
    x = (x_2 - x_1) **2
    y = (y_2 - y_1) **2
    distancia = math.sqrt(x + y)
    return distancia

def particulas_mas_cercanas(particulas_list)->list:
    resultado=[]
    for particula_i in particulas_list:
        x1=particula_i[0]
        y1=particula_i[1]
        r=particula_i[2]
        g=particula_i[3]
        b=particula_i[4]
        min=1000
        cercano=(0,0)
        for particula_j in particulas_list:
            if particula_i != particula_j:
                x2=particula_j[0]
                y2=particula_j[1]
                d=distancia_euclidiana(x1,y1,x2,y2)
                if d < min:
                    min = d
                    cercano=(x2,y2)

        resultado.append((particula_i,cercano,r,g,b))
    return resultado
