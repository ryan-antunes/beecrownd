a,b,c = input().split()
a1 = float(a)
a2 = float(b)
a3 = float(c)
pi = 3.14159

triangulo = (a1*a3)/2
circulo = pi*(a3*a3)
trapezio = ((a1+a2)*a3)/2
quadrado = a2*a2
retangulo = a1*a2
print(f"TRIANGULO: {triangulo:.3f}")
print(f"CIRCULO: {circulo:.3f}")
print(f"TRAPEZIO: {trapezio:.3f}")
print(f"QUADRADO: {quadrado:.3f}")
print(f"RETANGULO: {retangulo:.3f}")