import pandas as pd

def load_gdp_data(path: str) -> pd.DataFrame:
    """
    Load GDP data dari CSV.
    
    Parameters:
        path (str): Lokasi file CSV
    
    Returns:
        pd.DataFrame: Data GDP
    """
    try:
        df = pd.read_csv(path)
        print(f"Data berhasil di-load. Jumlah baris: {len(df)}")
        return df
    except FileNotFoundError:
        print(f"File tidak ditemukan: {path}")
        return pd.DataFrame()
    except Exception as e:
        print(f"Terjadi error: {e}")
        return pd.DataFrame()
