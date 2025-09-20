import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import imageio
import os

# -----------------------------
# 1. Path project
# -----------------------------
data_path = os.path.join("..", "data", "gdp_2020_2025.csv")
df = pd.read_csv(data_path)

# Ubah ke long format
df_long = df.melt(id_vars=['Country'], var_name='Year', value_name='GDP')
df_long['Year'] = df_long['Year'].astype(int)
df_long['GDP'] = pd.to_numeric(df_long['GDP'], errors='coerce')

# -----------------------------
# 2. Peta dunia interaktif HTML
# -----------------------------
output_html = os.path.join("..", "outputs", "gdp_world_interaktif.html")
fig = px.choropleth(
    df_long,
    locations='Country',
    locationmode='country names',
    color='GDP',
    hover_name='Country',
    animation_frame='Year',
    color_continuous_scale='Viridis',
    title='GDP Dunia 2020-2025'
)
fig.write_html(output_html)
print(f"Peta dunia interaktif dibuat: {output_html}")

# -----------------------------
# 3. Top/Bottom 5 GDP charts + GIF
# -----------------------------
output_top5 = os.path.join("..", "outputs", "top5_gdp_charts")
os.makedirs(output_top5, exist_ok=True)

images_top = []
images_bottom = []

years = sorted(df_long['Year'].unique())
for year in years:
    data_year = df_long[df_long['Year'] == year]
    
    # Top 5 tertinggi
    top5 = data_year.nlargest(5, 'GDP')
    plt.figure(figsize=(8,5))
    plt.bar(top5['Country'], top5['GDP'], color='green')
    plt.title(f"Top 5 GDP Tertinggi - {year}")
    plt.ylabel("GDP (USD)")
    plt.xlabel("Negara")
    plt.xticks(rotation=45)
    plt.tight_layout()
    temp_top = os.path.join(output_top5, f"top5_{year}.png")
    plt.savefig(temp_top)
    plt.close()
    images_top.append(imageio.imread(temp_top))

    # Top 5 terendah
    bottom5 = data_year.nsmallest(5, 'GDP')
    plt.figure(figsize=(8,5))
    plt.bar(bottom5['Country'], bottom5['GDP'], color='red')
    plt.title(f"Top 5 GDP Terendah - {year}")
    plt.ylabel("GDP (USD)")
    plt.xlabel("Negara")
    plt.xticks(rotation=45)
    plt.tight_layout()
    temp_bottom = os.path.join(output_top5, f"bottom5_{year}.png")
    plt.savefig(temp_bottom)
    plt.close()
    images_bottom.append(imageio.imread(temp_bottom))

# Buat GIF
gif_top5_path = os.path.join(output_top5, "top5_gdp.gif")
gif_bottom5_path = os.path.join(output_top5, "bottom5_gdp.gif")
imageio.mimsave(gif_top5_path, images_top, duration=30)
imageio.mimsave(gif_bottom5_path, images_bottom, duration=3)
print(f"GIF Top/Bottom 5 GDP tersimpan di: {output_top5}")

# -----------------------------
# 4. Peta dunia GIF (Plotly -> PNG -> GIF)
# -----------------------------
output_gif_map = os.path.join("..", "outputs", "gdp_world_map.gif")
map_images = []

for year in years:
    data_year = df_long[df_long['Year']==year]
    fig = px.choropleth(
        data_year,
        locations='Country',
        locationmode='country names',
        color='GDP',
        hover_name='Country',
        color_continuous_scale='Viridis',
        title=f"GDP Dunia {year}"
    )
    temp_file = os.path.join("..", "outputs", f"map_{year}.png")
    fig.write_image(temp_file, width=800, height=500)  # perlu kaleido
    map_images.append(imageio.imread(temp_file))
    os.remove(temp_file)

imageio.mimsave(output_gif_map, map_images, duration=3)  # 3 detik/frame
print(f"GIF Peta Dunia tersimpan di: {output_gif_map}")

print("Semua visualisasi selesai: gambar + GIF + peta interaktif")
