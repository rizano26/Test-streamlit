import pandas as pd
import scipy

df = pd.read_excel('Kapasitas + Pendidikan.xlsx')

korelasiKapasitasPendidikan = df['Kapasitas terpasang'].corr(df['Persentase Penduduk yang Lulus SMA'])
# korelasiKapasitasPenggunaListrik = df['Kapasitas terpasang'].corr(df['Persentase Penggunaan Listrik Penduduk Indonesia'])
print(korelasiKapasitasPendidikan)
#print(korelasiKapasitasPenggunaListrik)
# df['Tahun'] = df['Tahun'].astype(str)
# df.info()
