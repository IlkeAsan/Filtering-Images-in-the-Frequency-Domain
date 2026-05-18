import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():
    # ---------------------------------------------------------
    # 1. ve 2. ADIM: Okuma ve Fourier Dönüşümü
    # ---------------------------------------------------------
    img = cv2.imread('noisy_image.png', cv2.IMREAD_GRAYSCALE)
    
    if img is None:
        print("Hata: Görüntü okunamadı!")
        return

    f_transform = np.fft.fft2(img)
    f_shift = np.fft.fftshift(f_transform)
    
    # Rapor için logaritmik spektrum
    magnitude_spectrum = np.log(1 + np.abs(f_shift))

    # ---------------------------------------------------------
    # 4. ve 5. ADIM: Filtre Maskesi Oluşturma ve Uygulama
    # ---------------------------------------------------------
    rows, cols = img.shape
    mask = np.ones((rows, cols), np.uint8)

    # ÖNEMLİ: Koordinatları buradan değiştireceksin!
    noise_y1, noise_x1 = 108, 89 
    noise_y2, noise_x2 = rows - noise_y1, cols - noise_x1 
    
    radius = 7
    cv2.circle(mask, (noise_x1, noise_y1), radius, 0, -1)
    cv2.circle(mask, (noise_x2, noise_y2), radius, 0, -1)
    
    noise_y3, noise_x3 = 87, 52 
    noise_y4, noise_x4 = rows - noise_y3, cols - noise_x3 
    radius = 5
    cv2.circle(mask, (noise_x3, noise_y3), radius, 0, -1)
    cv2.circle(mask, (noise_x4, noise_y4), radius, 0, -1)
    noise_y5, noise_x5 = 67, 14 
    noise_y6, noise_x6 = rows - noise_y5, cols - noise_x5 
    radius = 4
    cv2.circle(mask, (noise_x5, noise_y5), radius, 0, -1)
    cv2.circle(mask, (noise_x6, noise_y6), radius, 0, -1)


    f_shift_filtered = f_shift * mask
    filtered_magnitude_spectrum = np.log(1 + np.abs(f_shift_filtered))

    # ---------------------------------------------------------
    # 6. ADIM: Geri Dönüşüm (Ters Fourier)
    # ---------------------------------------------------------
    f_ishift = np.fft.ifftshift(f_shift_filtered) 
    img_back = np.fft.ifft2(f_ishift) 
    img_clean = np.real(img_back) 

    # ---------------------------------------------------------
    # ÇIKTILARI GÖSTERME VE KAYDETME
    # ---------------------------------------------------------
    plt.figure(figsize=(15, 10))

    plt.subplot(2, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title('1. Gürültülü Görüntü')

    plt.subplot(2, 2, 2)
    plt.imshow(magnitude_spectrum, cmap='gray')
    plt.title('2. Orijinal Fourier Spektrumu')

    plt.subplot(2, 2, 3)
    plt.imshow(filtered_magnitude_spectrum, cmap='gray')
    plt.title('3. Filtrelenmiş Spektrum (Noktalar Silindi)')

    plt.subplot(2, 2, 4)
    plt.imshow(img_clean, cmap='gray')
    plt.title('4. Temizlenmiş Görüntü')

    plt.tight_layout()
    
    # DİKKAT: Burada plt.show() KESİNLİKLE YOK! Sadece kaydediyoruz.
    plt.savefig('rapor_ciktisi.png', bbox_inches='tight')
    print("Grafikler 'rapor_ciktisi.png' dosyasına başarıyla kaydedildi!")

if __name__ == "__main__":
    main()