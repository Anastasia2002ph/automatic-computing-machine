from numpy import *
from matplotlib.pyplot import *
rcParams ['font.sans-serif']=[ 'Liberation_Sans']


dt = 0.1
t = arange (0, 1000, dt)
x = np.loadtxt('CxfR.191.txt', skiprows = 10)
Px = abs(fft.rfft (x )/(0.5* len(t)))**2
fn = 1/(2*dt)

for i in range (len(Px)):
    if Px[i] > 0.000002:
        Px[i] = 0

#freq = linspace (0, fn , len(Px)) # массив частот

##fy = Px *-1j #обратное преобразование
##y = fft.irfft(fy)
##plot (y , Px, color ='black')
#plot (freq , Px, color ='black')

Px1 = fft.irfft(Px)

freq1 = linspace (0, fn , len(Px1))
plot (freq1 , Px1, color ='red')
title ('Спектр мощности')
xlabel ('Частота, Гц');
ylabel ('Мощность сигнала')
ylim ([0 , 0.0000003])
show ()

