import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.set_page_config(layout="wide")
st.title('Korelasi Antara Infrastruktur Listrik dengan Kualitas Pendidikan di Indonesia')
df = pd.read_excel('Kapasitas + Pendidikan.xlsx')
df['Tahun'] = df['Tahun'].astype(str)
plt.style.use('dark_background')

selectbox = st.selectbox('Pilihan',('Chart Total Kapasitas Terpasang di Indonesia', 'Chart Persentase Penduduk yang Lulus SMA di Indonesia', 'Korelasi Antara Total Kapasitas Terpasang dan Persentase Penduduk yang Lulus SMA di Indonesia ', 'Dataset'))
if selectbox == 'Chart Total Kapasitas Terpasang di Indonesia':
    plt.plot(df['Tahun'], df['Kapasitas terpasang'])
    plt.title('Jumlah Kapasitas Terpasang di Indonesia', pad=40)
    plt.ylabel('in MegaWatt')
    st.pyplot(plt)
    st.divider()
    st.write('Alasan memilih data persentase penduduk Indonesia yang berhasil lulus SMA sebagai barometer kualitas pendidikan di Indonesia adalah Persentase penduduk yang berhasil lulus SMA memberikan gambaran tentang sejauh mana sistem pendidikan di Indonesia berhasil mencapai tujuan utama yaitu memastikan penduduk memiliki kualifikasi pendidikan setara dengan SMA atau disebut wajib belajar 12 tahun. Persentase lulusan SMA juga mencerminkan tingkat keterjangkauan dan kesetaraan pendidikan di Indonesia')
elif selectbox == 'Chart Persentase Penduduk yang Lulus SMA di Indonesia':
    plt.plot(df['Tahun'], df['Persentase Penduduk yang Lulus SMA'])
    plt.title('Persentase Penduduk Indonesia yang Lulus SMA', pad=40)
    plt.ylabel('in Percentage (%)')
    st.pyplot(plt)
    st.divider()
    st.write('Alasan memilih data persentase penduduk Indonesia yang berhasil lulus SMA sebagai barometer kualitas pendidikan di Indonesia adalah Persentase penduduk yang berhasil lulus SMA memberikan gambaran tentang sejauh mana sistem pendidikan di Indonesia berhasil mencapai tujuan utama yaitu memastikan penduduk memiliki kualifikasi pendidikan setara dengan SMA atau disebut wajib belajar 12 tahun. Persentase lulusan SMA juga mencerminkan tingkat keterjangkauan dan kesetaraan pendidikan di Indonesia')
elif selectbox == 'Dataset':
    st.write(df)
else:
    fig, ax1 = plt.subplots()
    ax1.plot(df['Tahun'], df['Kapasitas terpasang'], label='Kapasitas terpasang')
    ax1.set_ylabel('in MegaWatt')
    ax1.set_ylim(55000, 70000)

    ax2 = ax1.twinx()
    ax2.plot(df['Tahun'], df['Persentase Penduduk yang Lulus SMA'], label='Persentase Penduduk yang Lulus SMA', color='orange')
    ax2.set_ylabel('in Percentage (%)')
    ax2.set_ylim(55, 70)

    plt.title('Korelasi Antara Infrastruktur Listrik dan Kualitas Pendidikan di Indonesia', pad=40)
    fig.legend(loc='lower center')
    plt.subplots_adjust(bottom=0.2)
    st.pyplot(plt)
    korelasiKapasitasPendidikan = df['Kapasitas terpasang'].corr(df['Persentase Penduduk yang Lulus SMA'])
    st.subheader('Koefisien Korelasi adalah : ' + str(korelasiKapasitasPendidikan) )
    st.divider()
    st.write('Dari koefisien korelasi diatas dapat disimpulkan bahwa jika angka kapasitas listrik meningkat, maka kualitas pendidikan di Indonesia akan cenderung meningkat juga.')
    st.write('Dengan adanya infrastruktur listrik yang kuat, pendidikan di Indonesia dapat meningkat secara keseluruhan. Stabilitas pasokan daya listrik memungkinkan lembaga pendidikan beroperasi dengan lancar dan efisien. Penggunaan teknologi modern dalam pembelajaran menjadi lebih mudah dan terjangkau, memberikan peluang untuk mengadopsi metode pengajaran yang inovatif.')