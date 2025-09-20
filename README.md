# GDP Visualization (2020–2025)

[![Python](https://img.shields.io/badge/python-3.13+-blue?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

Deskripsi Proyek
---
Proyek ini menampilkan tren GDP negara-negara dunia selama 2020–2025 menggunakan animasi, peta interaktif, dan chart Top/Bottom 5. Tujuannya adalah untuk memberikan gambaran cepat tentang pertumbuhan ekonomi global, serta insight yang actionable bagi analisis ekonomi atau bisnis.


---

## 🖥 Peta Interaktif HTML
[Klik di sini untuk visualisasi peta dunia interaktif](https://farhansublimate-arch.github.io/gdp-visualizations/outputs/gdp_world_interaktif.html)

> HTML interaktif memungkinkan zoom, hover, dan melihat nilai GDP tiap negara.


---

## GIF Animasi Peta Dunia
![Peta Dunia](https://farhansublimate-arch.github.io/gdp-visualizations/outputs/gdp_world_map.gif)

> GIF menampilkan perkembangan GDP tiap tahun secara visual di seluruh dunia.  
> Memudahkan melihat tren ekonomi global secara cepat.

---

## Top 5 & Bottom 5 GDP
![Top 5 GDP](https://farhansublimate-arch.github.io/gdp-visualizations/outputs/top5_gdp_charts/top5_gdp.gif)
![Bottom 5 GDP](https://farhansublimate-arch.github.io/gdp-visualizations/outputs/top5_gdp_charts/bottom5_gdp.gif)

## Key Insights:
1. GDP dunia meningkat setiap tahun, menunjukkan pemulihan ekonomi global.
2. Amerika dan China tetap dominan, tapi pertumbuhan tercepat ada di beberapa negara Asia.
3. Perbedaan regional masih signifikan, Afrika dan beberapa negara berkembang memiliki pertumbuhan yang lambat.
4. Beberapa negara menunjukkan pertumbuhan stabil meskipun terjadi fluktuasi global.
5. Negara dengan GDP terbesar tidak selalu mengalami pertumbuhan tercepat
6. Visualisasi interaktif mempermudah melihat perbandingan antar negara dan tren tahunan.



Teknologi yang Digunakan
---
- Python
- Pandas
- Matplotlib
- Plotly
- ImageIO

  
## Cara Menjalankan
---
1. Clone repositori:
git clone https://github.com/farhansublimate-arch/gdp-visualizations.git

2. Install dependencies:
pip install -r requirements.txt

3. Jalankan Script:
python gdp_visualization.py



Requirement:
---
- Python 3.13+
- Pandas, Plotly, Matplotlib, ImageIO, Kaleido, Numpy


Catatan:
---
- Output GIF/PNG/HTML tidak perlu commit → di-generate otomatis dari CSV
- Folder outputs/ bisa dimasukkan .gitignore agar repo tetap ringan
- CSV bisa diupdate kapan saja → jalankan Main.py → visualisasi baru otomatis dibuat



## ⚙️ Cara Menjalankan Script
```bash
cd src
python Main.py
