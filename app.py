from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

# Untuk emoji bisa dilhat disini :https://webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Website saya", page_icon=":frog", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---- Style css ----
def local_css(nama_file):
    with open(nama_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
local_css("style/style.css")

# ---- ASSET Folder ----
lottie_coding = load_lottieurl("https://lottie.host/9dc381c4-28e5-4b13-bf4a-6571f3e94500/2d1u9y22tG.json")
img_mt_tanggung = Image.open("images\mt_tanggung.jpg")
img_mt_kelud = Image.open("images/mt_kelud.jpg")

# ---- Kepala (Atasan) ----
with st.container():
    st.subheader("Hallo, Nama saya Zurais :wave:")
    st.title("Mahasiswa dari Universitas 17 Agustus 1945")
    st.write("Saya memiliki semangat belajar untuk menemukan cara menggunakan python agar lebih efisien dan efektif dalam bisnis")
    st.write("[Instagram saya >](https://www.instagram.com/colexzola_)")
    
with st.container():
    st.write("----")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Mencoba pemrograman dengan Pyhton")
        st.write("##")
        st.write(
            """
            Dari YouTube saya banyak belajar tentang pemrograman web terutama Python Languange:
            - Jika kamu ada kemauan yang diinginkan pasti akan berusaha lebih keras lagi.
            - tidak ada hasil yang mudah.
            - Coba dengan cara Pomodoro sistem.
            - apapun hasil yang didapatkan percayalah, ada hikmah dibalik itu semuanaya"
            
            Jika kamu ingin melihat portofolio mengenai saya, kamu bisa kunjungin profil saya sebagai berikut.
            """
        )
        st.write("[Github Profil >](https://github.com/ZURAISZOLA)")
    with right_column:
        st_lottie(lottie_coding, height=200, key="coding")
        
# ---- PROJEK ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_mt_tanggung)
    with text_column:
        st.subheader("Gunung yang pernah saya naikin yaitu")
        st.write(
            """
            Gunung Tanggung
            Gunung yang terletak pada Kab. Pasuruan yang mempunyai ketinggian 1458Mdpl
            Kamu bisa melihat pemandangan yang sempat kami dokumentasikan
            """
        )
        st.markdown("[Watch Video...](https://www.youtube.com/watch?v=gjkJlOeQIJE)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_mt_kelud)
    with text_column:
        st.subheader("Gunung yang pernah saya naikin yaitu")
        st.write(
            """
            Gunung Kelud
            Gunung yang terletak pada Kab. Blitar yang mempunyai ketinggian 1731Mdpl
            merupakan gunung yang pernah mengalami erupsi pada 13 Februari 2014
            Kamu bisa melihat pemandangan yang sempat kami dokumentasikan
            """
        )
        st.markdown("[Watch Video...](https://www.youtube.com/watch?v=4jUhzz6cibI)")

# ---- KONTAK SAYA ----
with st.container():
    st.write("----")
    st.header("Hubungi saya")
    st.write("##")
    
    # Untuk dokumentasi dan masuk ke dalam email / mengganti email!!
    contact_form = """
    <form action="https://formsubmit.co/colexzola@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="nama" placeholder="Nama kamu" required>
        <input type="email" name="email" placeholder="Email Kamu" required>
        <textarea name="massage" placeholder="Pesan kamu disini" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
