import pandas as pd

file_path = 'calon_tni.csv'

try:
    df = pd.read_csv(file_path)

    print("=== Data Calon TNI ===")
    print(df)
    print("\n" + "="*30 + "\n")

    print("=== Statistik Dasar Tinggi Badan ===")
    statistik = df['tinggi'].describe()
    print(statistik)
    print("\n" + "="*30 + "\n")

    mean_tinggi = statistik['mean']
    max_tinggi = statistik['max']
    min_tinggi = statistik['min']
    median_tinggi = statistik['50%'] 

    print(f"Rata-rata tinggi: {mean_tinggi:.2f} cm")
    print(f"Tertinggi: {int(max_tinggi)} cm")
    print(f"Terendah: {int(min_tinggi)} cm")
    print(f"Median: {median_tinggi} cm")
    print("\n" + "="*30 + "\n")

    print("=== Calon di atas rata-rata tinggi ===")
    di_atas_rata = df[df['tinggi'] > mean_tinggi]
    print(di_atas_rata.to_string()) 
    print("\n" + "="*30 + "\n")

    print("=== Urutan dari Tertinggi ke Terendah ===")
    sorted_df = df.sort_values(by='tinggi', ascending=False).reset_index(drop=True)
    print(sorted_df)
    print("\n" + "="*30 + "\n")

    print("=== Data dengan Kategori ===")
    bins = [0, statistik['25%'], statistik['75%'], float('inf')]
    labels = ['Pendek', 'Rata-rata', 'Tinggi']
    
    df_kategori = df.copy()
    
    df_kategori['Kategori'] = pd.cut(df_kategori['tinggi'], bins=bins, labels=labels, right=True)
    
    print(df_kategori)
    print("\n" + "="*30 + "\n")

except FileNotFoundError:
    print(f"Error: File '{file_path}' tidak ditemukan.")
except Exception as e:
    print(f"Terjadi error: {e}")