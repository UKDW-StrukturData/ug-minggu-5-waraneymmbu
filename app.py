import csv
import streamlit as st

# --- Fungsi untuk load data ---
def load_news(filename):
    """Baca file news_data.csv ke list of dict"""
    # TODO: buka file CSV (filename) dan baca dengan csv.DictReader
    with open(filename, 'r', newline='') as datafile:
        reader = csv.DictReader(datafile)
        # print(reader)
        list_news_data = []
        for row in reader:
            list_news_data.append(row)
            # print(row['tahun'])
            # print(row['pria'])
            # print(row['wanita'])
            # print()
    # kembalikan hasilnya dalam bentuk list
    pass

def load_comments(filename):
    """Baca file comment_news.csv ke list of dict"""
    # TODO: sama seperti load_news tapi untuk file komentar
    with open(filename, 'r', newline='') as datafile:
        reader = csv.DictReader(datafile)
        comment_news_data = []
        for row in reader:
            comment_news_data.append(row)
    # st.write(comment_news_data)
    pass
# load_comments('comment_news.csv')
# --- Fungsi untuk memproses data ---
def process_data(news_list, comments_list):
    """
    Gabungkan berita dan komentar,
    hitung jumlah komentar & rata-rata rating.
    Hasilnya list of dict.
    """
    comments_per_news = {}
    # TODO: Buat dictionary untuk kumpulkan komentar per idBerita
    for row in comments_list:
        idBerita = row['idBerita']
        komentar = row['idKomentar']
        rating = row['Rating']
        comments_per_news.append({
            idBerita: komentar, 
        })
        test = idBerita
    
    # TODO: isi comments_per_news dari comments_list
    for i in comments_list
    # hint: per idBerita simpan ratings (list) dan count

    # TODO: Buat list hasil gabungan
    result = []
    for n in news_list:
        idb = n['idBerita']
        headline = n['Headline']
        # TODO: cek apakah idb ada di comments_per_news,
        # hitung rata-rata rating dan jumlah komentar
        rata = 0  # ganti dengan hitungan
        jumlah = 0  # ganti dengan hitungan
        result.append({
            'ID Berita': idb,
            'Headline': headline,
            'Rata-rata Rating': round(rata, 2),
            'Jumlah Komentar': jumlah
        })

    # --- Urutkan berdasarkan rating pakai fungsi biasa ---
    def ambil_rating(item):
        return item['Rata-rata Rating']

    # TODO: urutkan result berdasarkan ambil_rating reverse=True
    return result

# --- Fungsi untuk tampilkan di Streamlit ---
def main():
    st.title("Analisis Sentimen & Popularitas Berita")
    st.write("Menampilkan ID, Headline, Rata-rata Rating, dan Jumlah Komentar, diurutkan dari rating tertinggi.")

    # TODO: baca data CSV
    news_data = []     # ganti dengan pemanggilan load_news
    comment_data = []  # ganti dengan pemanggilan load_comments

    # TODO: proses data
    hasil = []  # ganti dengan pemanggilan process_data

    # TODO: tampilkan tabel di Streamlit
    # hint: gunakan st.table(hasil)
    pass

if __name__ == '__main__':
    main()
