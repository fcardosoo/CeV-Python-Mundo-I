#converter temperatura de celsius para fahrenheit

t = float(input('Informe a temperatura em graus Celsius: '))
f = (t*1.8)+32

print('A temperatura de {:.1f}ºC corresposde à {:.1f}ºF.'.format(t,f))