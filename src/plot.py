import matplotlib.pyplot as plt
import imageio
import plotly.express as px
import os

def create_gif(df, output_path="E:/gdp_visualization/outputs/gdp_animation.gif"):
    """
    Membuat GIF animasi dari DataFrame GDP.
    df: DataFrame dengan kolom 'Country', 'Year', 'GDP'
    output_path: lokasi file GIF yang dihasilkan
    """
    try:
        images = []
        years = sorted(df['Year'].unique())
        for year in years:
            fig, ax = plt.subplots(figsize=(8,5))
            data_year = df[df['Year']==year]
            ax.bar(data_year['Country'], data_year['GDP'])
            ax.set_title(f"GDP Tahun {year}")
            ax.set_ylabel("GDP (USD)")
            ax.set_xlabel("Negara")
            plt.xticks(rotation=45)
            # Simpan gambar sementara
            temp_file = f"temp_{year}.png"
            plt.savefig(temp_file)
            plt.close(fig)
            images.append(imageio.imread(temp_file))
            os.remove(temp_file)
        imageio.mimsave(output_path, images, duration=1)
        print(f"GIF berhasil dibuat: {output_path}")
    except Exception as e:
        print(f"Error membuat GIF: {e}")


def create_interactive_chart(df, output_path="E:/gdp_visualization/outputs/gdp_world_interaktif.html"):
    """
    Membuat chart interaktif menggunakan Plotly
    df: DataFrame dengan kolom 'Country', 'Year', 'GDP'
    output_path: lokasi file HTML yang dihasilkan
    """
    try:
        fig = px.line(df, x="Year", y="GDP", color="Country", title="GDP Interaktif Dunia")
        fig.write_html(output_path)
        print(f"Chart interaktif berhasil dibuat: {output_path}")
    except Exception as e:
        print(f"Error membuat chart interaktif: {e}")
