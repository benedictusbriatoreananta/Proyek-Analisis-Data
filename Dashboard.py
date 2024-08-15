import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df_day = pd.read_csv('day.csv')
df_hour = pd.read_csv('hour.csv')

# Title and description
st.title('Bike Sharing Analysis Dashboard')
st.write("""
## Proyek Analisis Data: Bike Sharing Dataset
### Nama: Benedictus Briatore Ananta
### Email: briatoreananta45@gmial.com
### ID Dicoding: benedictus_briatore_ananta_2a1K
""")

# Sidebar for user input
st.sidebar.header('User Input Features')
selected_dataset = st.sidebar.selectbox('Select Dataset', ['Daily', 'Hourly'])

# Display dataset
if selected_dataset == 'Daily':
    st.subheader('Dataset Harian')
    st.write(df_day.head())
else:
    st.subheader('Dataset Jam')
    st.write(df_hour.head())

# Visualization: Penggunaan Sepeda Berdasarkan Musim
st.subheader('Penggunaan Sepeda Berdasarkan Musim')
fig, ax = plt.subplots(figsize=(10, 6))
if selected_dataset == 'Daily':
    sns.barplot(x='season', y='cnt', data=df_day, ax=ax, palette='viridis')  # Menggunakan palet 'viridis'
    ax.set_title('Penggunaan Sepeda Berdasarkan Musim (Harian)')
else:
    sns.barplot(x='season', y='cnt', data=df_hour, ax=ax, palette='viridis')  # Menggunakan palet 'viridis'
    ax.set_title('Penggunaan Sepeda Berdasarkan Musim (Jam)')
ax.set_xlabel('Musim')
ax.set_ylabel('Jumlah Pengguna')
st.pyplot(fig)

# Visualization: Korelasi Antar Variabel
st.subheader('Korelasi Antar Variabel')
fig, ax = plt.subplots(figsize=(12, 8))
if selected_dataset == 'Daily':
    df_corr_day = df_day.drop(columns=['dteday']).corr()
    sns.heatmap(df_corr_day, annot=True, cmap='coolwarm', ax=ax)  # Menggunakan palet 'coolwarm'
    ax.set_title('Korelasi Antar Variabel (Harian)')
else:
    df_corr_hour = df_hour.drop(columns=['dteday']).corr()
    sns.heatmap(df_corr_hour, annot=True, cmap='coolwarm', ax=ax)  # Menggunakan palet 'coolwarm'
    ax.set_title('Korelasi Antar Variabel (Jam)')
st.pyplot(fig)

# Conclusion
st.subheader('Conclusion')
st.write("""
### Kesimpulan Pertanyaan 1
Penggunaan sepeda berbagi cenderung meningkat pada musim tertentu. Dari visualisasi yang telah dilakukan, terlihat bahwa jumlah pengguna sepeda berbagi lebih tinggi pada musim panas dan musim gugur dibandingkan dengan musim dingin dan musim semi. Hal ini mungkin disebabkan oleh kondisi cuaca yang lebih mendukung untuk bersepeda pada musim panas dan musim gugur.

### Kesimpulan Pertanyaan 2
Terdapat beberapa faktor yang memiliki korelasi tinggi dengan jumlah pengguna sepeda berbagi. Dari analisis korelasi yang dilakukan, ditemukan bahwa variabel seperti suhu (temp), suhu yang dirasakan (atemp), dan kelembaban (hum) memiliki korelasi yang signifikan dengan jumlah pengguna sepeda berbagi. Selain itu, variabel seperti hari kerja (workingday) dan kondisi cuaca (weathersit) juga mempengaruhi jumlah pengguna. Secara umum, kondisi cuaca yang baik dan hari kerja cenderung meningkatkan jumlah pengguna sepeda berbagi.
""")