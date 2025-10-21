import csv
import streamlit as st

# --- Fungsi untuk load data ---
def load_news(filename):
    """Baca file news_data.csv ke list of dict"""
    with open(filename, 'r', newline='', encoding='utf-8') as datafile:
        reader = csv.DictReader(datafile)
        list_news_data = [row for row in reader]
    return list_news_data


def load_comments(filename):
    """Baca file comment_news.csv ke list of dict"""
    with open(filename, 'r', newline='', encoding='utf-8') as datafile:
        reader = csv.DictReader(datafile)
        comment_news_data = [row for row in reader]
    return comment_news_data


# --- Fungsi untuk memproses data ---
def process_data(news_list, comments_list):
    """
    Gabungkan berita dan komentar,
    hitung jumlah komentar & rata-rata rating.
    Hasilnya list of dict.
    """

    # --- Kumpulkan komentar per idBerita ---
    comments_per_news = {}
    for row in comments_list:
        idb = row['idBerita']
        rating = float(row['Rating'])
        if idb not in comments_per_news:
            comments_per_news[idb] = {
                'ratings': [],
            }
        comments_per_news[idb]['ratings'].append(rating)

    # --- Buat list hasil gabungan ---
    result = []
    for n in news_list:
        idb = n['idBerita']
        headline = n['Headline']

        if idb in comments_per_news:
            ratings = comments_per_news[idb]['ratings']
            jumlah = len(ratings)
            rata = sum(ratings) / jumlah if jumlah > 0 else 0
        else:
            jumlah = 0
            rata = 0

        result.append({
            'ID Berita': idb,
            'Headline': headline,
            'Rata-rata Rating': round(rata, 2),
            'Jumlah Komentar': jumlah
        })

    # --- Urutkan berdasarkan rating tertinggi ---
    result.sort(key=lambda item: item['Rata-rata Rating'], reverse=True)

    return result


# --- Fungsi untuk tampilkan di Streamlit ---
def main():
    st.title("Analisis Sentimen & Popularitas Berita")
    st.write("Menampilkan ID, Headline, Rata-rata Rating, dan Jumlah Komentar, diurutkan dari rating tertinggi.")

    # --- Baca data CSV ---
    news_data = load_news('news_data.csv')
    comment_data = load_comments('comment_news.csv')

    # --- Proses data ---
    hasil = process_data(news_data, comment_data)

    # --- Tampilkan tabel di Streamlit ---
    st.table(hasil)


if __name__ == '__main__':
    main()
