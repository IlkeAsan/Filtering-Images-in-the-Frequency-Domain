import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():
    
    # 1. ve 2. adım
    img = cv2.imread('noisy_image.png', cv2.IMREAD_GRAYSCALE)
    
    if img is None:
        print("Hata: Görüntü okunamadı!")
        return

    f_transform = np.fft.fft2(img)
    f_shift = np.fft.fftshift(f_transform)
    
    # logaritmik spektrum
    log_spectrum = np.log(1 + np.abs(f_shift))

    # koordinatları bulma
    
    plt.figure(figsize=(8, 8))
    plt.imshow(log_spectrum, cmap='gray')
    plt.title("Gürültü")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()

    # 4. ve 5. adım

    rows, cols = img.shape
    # npone ile filtre matrisi oluştururken başlangiçta float olarak oluşturur ancak 
    # cv2.circle ile belirlediğimiz frekanslara nokta ekleme fonkstonu unsigned sayı bekler 
    # bu yuzden veri tipi uint yapılmıştır.
    mask = np.ones((rows, cols), np.uint8)

    y1, x1 = 107, 89 
    y2, x2 = rows - y1, cols - x1 
    
    radius = 7
    cv2.circle(mask, (x1, y1), radius, 0, cv2.FILLED) #belirlediğimiz frekanstaki yeri siyah yapma 0 ile
    cv2.circle(mask, (x2, y2), radius, 0, cv2.FILLED)
       
    y3, x3 = 87, 51 
    y4, x4 = rows - y3, cols - x3 
    radius = 5
    cv2.circle(mask, (x3, y3), radius, 0, cv2.FILLED)
    cv2.circle(mask, (x4, y4), radius, 0, cv2.FILLED)
    
    y5, x5 = 66, 12 
    y6, x6 = rows - y5, cols - x5 
    radius = 3
    cv2.circle(mask, (x5, y5), radius, 0, cv2.FILLED)
    cv2.circle(mask, (x6, y6), radius, 0, cv2.FILLED)

    
    

    f_shift_filtered = f_shift * mask
    filtered_log_spectrum = np.log(1 + np.abs(f_shift_filtered))

    
    # 6. adım ters fourier

    f_tshift = np.fft.ifftshift(f_shift_filtered) 
    img_back = np.fft.ifft2(f_tshift) 
    img_clean = np.real(img_back) 

    # çıktılar
  
    
    plt.imsave('orijinal_goruntu.png', img, cmap='gray')

    raw_magnitude = np.abs(f_shift)
    plt.imsave('genlik_spektrumu.png', raw_magnitude, cmap='gray')

    plt.imsave('logaritmik_spektrum.png', log_spectrum, cmap='gray')

    plt.imsave('filtre_maskesi.png', mask, cmap='gray')

    plt.imsave('filtrelenmis_spektrum.png', filtered_log_spectrum, cmap='gray')

    plt.imsave('temizlenmis_goruntu.png', img_clean, cmap='gray')

    print("Görseller kaydedildi")

if __name__ == "__main__":
    main()
    
 