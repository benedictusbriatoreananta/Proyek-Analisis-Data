import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io
# Load dataset
df_day = pd.read_csv('day.csv')
df_hour = pd.read_csv('hour.csv')

# Sidebar for navigation
st.sidebar.title("Navigasi")
page = st.sidebar.selectbox("Pilih Halaman", ["Home", "EDA", "Visualisasi", "Kesimpulan"])

# Home Page
if page == "Home":
    st.title("Proyek Analisis Data: Bike Sharing")
    st.markdown("""
    - **Nama:** Benedictus Briatore Ananta
    - **Email:** briatorenanta45@gmail.com
    - **ID Dicoding:** benedictus_briatore_ananta_2a1K
    """)

# EDA Page
elif page == "EDA":
    st.title("Exploratory Data Analysis (EDA)")
    
    st.subheader("Informasi Dataset Harian")
    buffer = io.StringIO()
    df_day.info(buf=buffer)
    s = buffer.getvalue()
    st.text(s)  # Tambahkan baris ini untuk menampilkan informasi dataset harian
    
    st.subheader("Informasi Dataset Jam")
    buffer = io.StringIO()
    df_hour.info(buf=buffer)
    s = buffer.getvalue()
    st.text(s)
    
    st.subheader("Deskripsi Dataset Harian")
    st.write(df_day.describe())
    
    st.subheader("Deskripsi Dataset Jam")
    st.write(df_hour.describe())
    
    st.subheader("Beberapa Baris Pertama Dataset Harian")
    st.write(df_day.head())
    
    st.subheader("Beberapa Baris Pertama Dataset Jam")
    st.write(df_hour.head())

# Visualisasi Page
elif page == "Visualisasi":
    st.title("Visualisasi Data")
    
    st.subheader("Distribusi Jumlah Pengguna Sepeda (Harian)")
    fig, ax = plt.subplots()
    sns.histplot(df_day['cnt'], bins=30, kde=True, ax=ax)
    ax.set_title('Distribusi Jumlah Pengguna Sepeda (Harian)')
    ax.set_xlabel('Jumlah Pengguna')
    ax.set_ylabel('Frekuensi')
    st.pyplot(fig)
    
    st.subheader("Hubungan Suhu dan Jumlah Pengguna Sepeda Berdasarkan Musim")
    fig, ax = plt.subplots()
    sns.scatterplot(x='temp', y='cnt', data=df_day, hue='season', palette='viridis', ax=ax)
    ax.set_title('Hubungan Suhu dan Jumlah Pengguna Sepeda Berdasarkan Musim')
    ax.set_xlabel('Suhu')
    ax.set_ylabel('Jumlah Pengguna')
    st.pyplot(fig)
    
    st.subheader("Penggunaan Sepeda Berdasarkan Musim (Harian)")
    fig, ax = plt.subplots()
    sns.barplot(x='season', y='cnt', data=df_day, palette='viridis', ax=ax)
    ax.set_title('Penggunaan Sepeda Berdasarkan Musim (Harian)')
    ax.set_xlabel('Musim')
    ax.set_ylabel('Jumlah Pengguna')
    ax.set_xticklabels(['Musim Semi', 'Musim Panas', 'Musim Gugur', 'Musim Dingin'])
    st.pyplot(fig)
    
    st.subheader("Penggunaan Sepeda Berdasarkan Musim (Jam)")
    fig, ax = plt.subplots()
    sns.barplot(x='season', y='cnt', data=df_hour, palette='viridis', ax=ax)
    ax.set_title('Penggunaan Sepeda Berdasarkan Musim (Jam)')
    ax.set_xlabel('Musim')
    ax.set_ylabel('Jumlah Pengguna')
    ax.set_xticklabels(['Musim Semi', 'Musim Panas', 'Musim Gugur', 'Musim Dingin'])
    st.pyplot(fig)

# Kesimpulan Page
elif page == "Kesimpulan":
    st.title("Kesimpulan")
    
    st.subheader("Kesimpulan Pertanyaan 1")
    st.markdown("""
    Penggunaan sepeda berbagi cenderung meningkat pada musim tertentu. Dari visualisasi yang telah dilakukan, terlihat bahwa jumlah pengguna sepeda berbagi lebih tinggi pada musim panas dan musim gugur dibandingkan dengan musim dingin dan musim semi. Hal ini mungkin disebabkan oleh kondisi cuaca yang lebih mendukung untuk bersepeda pada musim panas dan musim gugur.
    """)
    
    st.subheader("Kesimpulan Pertanyaan 2")
    st.markdown("""
    Terdapat beberapa faktor yang memiliki korelasi tinggi dengan jumlah pengguna sepeda berbagi. Dari analisis korelasi yang dilakukan, ditemukan bahwa variabel seperti suhu (temp), suhu yang dirasakan (atemp), dan kelembaban (hum) memiliki korelasi yang signifikan dengan jumlah pengguna sepeda berbagi. Selain itu, variabel seperti hari kerja (workingday) dan kondisi cuaca (weathersit) juga mempengaruhi jumlah pengguna. Secara umum, kondisi cuaca yang baik dan hari kerja cenderung meningkatkan jumlah pengguna sepeda berbagi.
    """)

# Tambahkan petunjuk di file README untuk menjalankan dashboard di lokal
