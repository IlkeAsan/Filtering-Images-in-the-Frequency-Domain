
# Filtering Images in the Frequency Domain (Frekans Düzleminde Periyodik Gürültü Giderme)

Bu proje; uzay düzleminde piksellerin arasına karışmış ve doğrudan ayrıştırılması zor olan periyodik (tekrarlayan) gürültüleri, **İki Boyutlu Hızlı Fourier Dönüşümü (2D FFT)** kullanarak frekans uzayına taşımayı ve **İdeal Çentik Filtre (Notch Filter)** yardımıyla nokta atışı temizlemeyi amaçlayan bir görüntü işleme uygulamasıdır.

## 🚀 Projenin Çalışma Mantığı

1. **Görüntü Okuma & Frekans Dönüşümü:** Gürültülü görüntü gri tonlamalı (`cv2.IMREAD_GRAYSCALE`) olarak okunur. `np.fft.fft2` ve `np.fft.fftshift` fonksiyonları kullanılarak frekans düzlemine aktarılır ve sıfır frekans (DC bileşeni) matrisin merkezine taşınır.
2. **Koordinat Tespiti:** Matrisin aşırı geniş dinamik aralığı logaritmik dönüşümle daraltılarak gürültü pikselleri parlak noktalar halinde görünür kılınır. İnteraktif Matplotlib penceresi üzerinden bu noktaların $(x, y)$ koordinatları tam olarak okunabilir.
3. **Filtre Maskesi Oluşturma:** Orijinal resimle aynı boyutta, `np.uint8` veri tipinde (bellek optimizasyonu ve OpenCV uyumluluğu için) ve içi 1'lerle dolu bir geçirgen maske matrisi üretilir. `cv2.circle` fonksiyonu kullanılarak tespit edilen simetrik gürültü koordinatlarının içi kapkara (0) dairelerle doldurulur (baskılanır).
4. **Ters Dönüşüm & Çıktı:** Filtrelenen frekans matrisi `np.fft.ifftshift` ve `np.fft.ifft2` fonksiyonlarıyla tekrar uzay düzlemine (piksel dünyasına) döndürülür ve gürültülerden arındırılmış nihai görüntü elde edilir.

## 🛠️ Gereksinimler

Projenin çalışabilmesi için bilgisayarınızda Python 3.x ve aşağıdaki kütüphanelerin kurulu olması gerekmektedir:

```bash
pip install opencv-python numpy matplotlib