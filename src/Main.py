from data_loader import load_gdp_data
from plots import create_gif, create_interactive_chart
import os

# Lokasi file CSV
csv_path = os.path.join("..", "data", "gdp_2020_2025.csv")

# Load data
df = load_gdp_data(csv_path)

# Buat GIF animasi
create_gif(df)

# Buat chart interaktif HTML
create_interactive_chart(df)

print("Semua visualisasi selesai dibuat.")
