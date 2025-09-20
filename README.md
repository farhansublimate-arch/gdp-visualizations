# GDP Visualization (2020–2025)

[![Python](https://img.shields.io/badge/python-3.13+-blue?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

Visualisasi GDP dunia dari 2020–2025, lengkap dengan:  
- Peta interaktif HTML yang bisa di-zoom dan di-hover
- GIF animasi peta dunia 
- Chart klasik Top 5 & Bottom 5 GDP

Project ini menunjukkan kemampuan **data cleaning, transformasi, visualisasi interaktif, dan insight analisis**.


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

> **Insight:**  
> - **Top 5 GDP** biasanya didominasi negara dengan ekonomi besar seperti: USA, China, Jepang, Jerman, India  
> - **Bottom 5 GDP** menunjukkan negara dengan ekonomi kecil atau berkembang lambat  
> - Chart membantu melihat disparitas ekonomi antar negara secara instan  

---

---

## Instalasi & Requirement

Clone repo:
- git clone https://github.com/farhansublimate-arch/gdp-visualizations.git
- cd gdp_visualization/src

Install requirements:
- python -m pip install -r requirements.txt

Jalankan script:
- python Main.py

Requirement:
- Python 3.13+
- Pandas, Plotly, Matplotlib, ImageIO, Kaleido, Numpy

Catatan:
- Output GIF/PNG/HTML tidak perlu commit → di-generate otomatis dari CSV
- Folder outputs/ bisa dimasukkan .gitignore agar repo tetap ringan
- CSV bisa diupdate kapan saja → jalankan Main.py → visualisasi baru otomatis dibuat

Insight Tambahan:
- Dengan GIF dan peta interaktif, tren GDP dunia lebih mudah diamati dari tahun ke tahun
- Top/Bottom chart membantu memahami disparitas ekonomi antar negara secara cepat
- Visualisasi ini siap dipakai untuk analisis data ekonomi, presentasi, atau laporan interaktif

## ⚙️ Cara Menjalankan Script
```bash
cd src
python Main.py
