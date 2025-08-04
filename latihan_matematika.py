import streamlit as st
import random

st.title("🧮 Latihan Matematika - 4 Operasi Dasar")

# Pilih jenis operasi
operasi = st.selectbox("Pilih jenis soal:", ["Penjumlahan", "Pengurangan", "Perkalian", "Pembagian"])

# Fungsi membuat soal baru
def buat_soal(operasi):
    if operasi == "Penjumlahan":
        a = random.randint(10, 99)
        b = random.randint(10, 99)
        hasil = a + b
        simbol = "+"
    elif operasi == "Pengurangan":
        a = random.randint(10, 99)
        b = random.randint(10, a)  # Supaya hasil tidak negatif
        hasil = a - b
        simbol = "-"
    elif operasi == "Perkalian":
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        hasil = a * b
        simbol = "×"
    elif operasi == "Pembagian":
        b = random.randint(1, 10)
        hasil = random.randint(1, 10)
        a = b * hasil  # Supaya hasilnya bulat
        simbol = "÷"
    return a, b, hasil, simbol

# Inisialisasi soal di session state
if "a" not in st.session_state or st.button("Soal Baru"):
    a, b, hasil, simbol = buat_soal(operasi)
    st.session_state.a = a
    st.session_state.b = b
    st.session_state.hasil = hasil
    st.session_state.simbol = simbol
    st.session_state.jawaban_status = ""

# Tampilkan soal
st.subheader(f"Berapakah {st.session_state.a} {st.session_state.simbol} {st.session_state.b}?")

# Input jawaban
jawaban = st.number_input("Jawaban kamu:", step=1)

# Tombol cek jawaban
if st.button("Cek Jawaban"):
    if jawaban == st.session_state.hasil:
        st.success("✅ Benar!")
    else:
        st.error(f"❌ Salah. Jawaban yang benar adalah {st.session_state.hasil}.")
