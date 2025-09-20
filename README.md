# GDP Visualization

Visualisasi GDP dunia (2020–2025) dengan GIF, chart klasik top/bottom 5, dan peta interaktif.

## GIF animasi
![Peta Dunia](outputs/gdp_world.gif)

## Top 5 GDP & Bottom 5 GDP
![Top 5 GDP](outputs/top5_gdp_charts/top5_gdp.png)
![Bottom 5 GDP](outputs/top5_gdp_charts/worst5_gdp.png)

## Interaktif HTML
[Klik di sini untuk visualisasi peta dunia interaktif](https://farhansublimate-arch.github.io/gdp-visualizations/)


---


## Cara Pakai

1. Clone repo:
git clone https://github.com/farhansublimate-arch/gdp-visualization.git
cd gdp_visualization/src

2. Install requirements:
python -m pip install -r requirements.txt

3.Jalankan Main.py:
python Main.py

Semua GIF dan chart interaktif otomatis dibuat di folder outputs

```bash

Requirement:
Python 3.13+
Pandas, Plotly, Matplotlib, ImageIO, Kaleido, Numpy


Catatan:
-Output GIF / PNG tidak perlu commit → generate otomatis dari CSV
-Folder outputs/ bisa dimasukkan ke .gitignore agar repo ringan
-Bisa update data CSV kapan saja → jalankan Main.py → visualisasi baru otomatis dibuat



