import pygame
import random


genişlik = 750
yükseklik = 500


siyah = (0, 0, 0)
beyaz = (255, 255, 255)
yeşil = (0, 255, 0)

# Yılanın başlangıç konumu ve boyutları
başlangıç_x = genişlik / 2
başlangıç_y = yükseklik / 2
yılan_baş = 10  #genişliği
yılan_yükseklik = 10

# Yılanın hareket hızı
hız = 17

# başlatma
pygame.init()
ekran = pygame.display.set_mode((genişlik, yükseklik))
pygame.display.set_caption("Yılan Oyunu")

# Oyun döngüsü
oyun_sonu = False
saat = pygame.time.Clock()

while not oyun_sonu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            oyun_sonu = True

    # Yılanın hareketi
    tuşlar = pygame.key.get_pressed()
    if tuşlar[pygame.K_LEFT]:
        başlangıç_x -= hız
    if tuşlar[pygame.K_RIGHT]:
        başlangıç_x += hız
    if tuşlar[pygame.K_UP]:
        başlangıç_y -= hız
    if tuşlar[pygame.K_DOWN]:
        başlangıç_y += hız

    # Yılanın ekran sınırlarını aşmasını engelleme
    if başlangıç_x < 0:
        başlangıç_x = 0
    elif başlangıç_x > genişlik - yılan_baş:
        başlangıç_x = genişlik - yılan_baş
    if başlangıç_y < 0:
        başlangıç_y = 0
    elif başlangıç_y > yükseklik - yılan_yükseklik:
        başlangıç_y = yükseklik - yılan_yükseklik

    # Yeniden çizim işlemleri
    ekran.fill(siyah)
    pygame.draw.rect(ekran, yeşil, [başlangıç_x, başlangıç_y, yılan_baş, yılan_yükseklik])
    pygame.display.flip()
    saat.tick(30)

# Oyun döngüsünden çıkıldığında oyunu kapatma
pygame.quit()
