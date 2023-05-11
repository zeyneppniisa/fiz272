import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Rectangle

#elipsin yarıçapları:
R=1
R_2=3 #random değer verdim

#dikdörtgenin 3 köşesinin koordinatları
köşe_1ZNS=(0,0) #sol_alt_köşe
köşe_2ZNS=(R,0) #sağ_alt_köşe
köşe_3ZNS=(0,R_2) #sol_üst_köşe

# Elips ve dikdörtgeni çizdirme
fig, ax = plt.subplots()
elips_ZNS = Ellipse((0, 0), 2*R, 2*R_2, color='purple', alpha=0.2)
dikdörtgen_ZNS = Rectangle(köşe_1ZNS, R, R_2, linewidth=1, edgecolor='black', facecolor='none')
ax.add_artist(elips_ZNS)
ax.add_artist(dikdörtgen_ZNS)
plt.xlim(0, 2)
plt.ylim(0, 3)
#k değerlerini ve piZNS değerlerini saklamak için boş listeler oluşturalım
k_values = []
pi_valuesZNS = []

#farklı k değerleri için pi hesaplama işlemleri
for k in range(1, 7):
    N = 10**k
    x = np.random.uniform(0, 1, N)
    y = np.random.uniform(0,3, N)

    M = 0
    #nokta elipsin içindeyse M+=1
    for i in range(N):
        if ((x[i]**2) / (R**2) + (y[i]**2) / ((R_2)**2)) <= 1:
            M += 1
            
    #pi değerlerini hesaplayıp listeye ekleyelim
    piZNS = (4 * M) / N
    pi_valuesZNS.append(piZNS)
    
    #k değerlerini de saklayalım
    k_values.append(k)
    
    #grafik çizimi
    plt.figure()
    plt.scatter(x, y, s=1, color='blue')
    for i in range(N):
        #nokta elipsin içindeyse yeşil nokta dışındaysa kırmızı
        if ((x[i]**2) / (R**2) + (y[i]**2) / ((R_2)**2)) <= 1:
            plt.plot(x[i], y[i], 'go', markersize=1)
        else:
            plt.plot(x[i], y[i], 'ro', markersize=1)
    plt.xlim(0, 2) #eksen boyutu
    plt.ylim(0, 3)
    plt.title(f'k={k}, piZNS={piZNS}')
    plt.show()

#tüm pi değerlerini ve k değerlerini ekrana yazdıralım
print(f"k values: {k_values}")
print(f"piZNS values: {pi_valuesZNS}")
# piZNS değerlerinin grafiği
plt.plot(k_values, pi_valuesZNS, 'ro-')
plt.xlabel('k values')
plt.ylabel('piZNS values')
plt.title('Approximation of pi using Monte Carlo Simulation')
plt.show()



#Cricket chrips-temperature exercise
#ninovadaki verileri numpy dizisi olarak okutalım
data = np.loadtxt("sleeplessnights.txt")

#Verilen sıcaklık değerlerini Celcius'a çevirelim Celciues=(fahrenheit-32)5/9
data[:, 1] = (data[:, 1] - 32) * 5 / 9

#dakikada verilen kriket cılıtsı sayısını saniyedeki sayıysa dönüştürelim
data[:, 0] /= 60

#fonksiyonu tanımlayalım
# x=saniyedeki kriket cıvıltı sayısını, a ve b=eğim ve y-kesit katsayılarını
def model_function(x, a, b):
    return a * x + b

#En küçük kareler yöntemini kullanarak eğim ve y-kesit katsayılarını hesaplayalım.
popt, _ = np.polyfit(data[:, 0], data[:, 1], 1, cov=True)

#Bu satırlar, hesaplanan eğim ve y-kesit katsayılarını a ve b değişkenlerine atar.
a = popt[0]
b = popt[1]
per_second_cıvıltı = data[:, 0]
celciuss = data[:, 1]

print("saniyedeki cıvıltı sayısı",per_second_cıvıltı)
print("sıcaklık(celcius)",celciuss)

print("The function that fits the data is: temperature = {:.2f} * chirps per second + {:.2f}".format(a, b))
plt.scatter(data[:, 0], data[:, 1], label="data")
x = np.linspace(data[:, 0].min(), data[:, 0].max(), 100)
y = model_function(x, a, b)
plt.plot(x, y, color="red", label="fitting function")
plt.xlabel("Chirps per second")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.show()

#chi-square testi ile test etme
beklenen_sıcaklıkZNS = 77.38 * per_second_cıvıltı + 5.30

#chi-square=((beklenen-gözlenen)^2)/beklenen
print("beklenen sıcaklık",beklenen_sıcaklıkZNS)
diff = (beklenen_sıcaklıkZNS-celciuss)**2
ratio = diff / beklenen_sıcaklıkZNS
chi_squareZNS=np.sum(ratio)
    
print("chisquare",chi_squareZNS)

#alfa seviyesi belirlicem
alfa_ZNS=0.05 #kabul edilebilir hata oranı %5 demek
#serbestlik derecesi 6 
kritik_değerZNS=3.84
if chi_squareZNS<kritik_değerZNS:
    print("H1=Saniyedeki kriket cıvıltı sayısı ile sıcaklık arasında bir ilişki vardır")
else:
    print("H0==Saniyedeki kriket cıvıltı sayısı ile sıcaklık arasında bir ilişki yoktur.")
