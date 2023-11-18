# load libraries 

import pandas as pd
import streamlit as st
from pickle import dump
import matplotlib.pyplot as plt

# setup page
st.set_page_config(page_title = "Gration", layout = "wide")

# define function
@st.cache(ttl = 12100)
def load_model():
    model = dump("statis/model/model.pkl")
    return model

def dashboard_page():
    st1, st2, st3 = st.columns(3)

    with st1:
        st.subheader("Feature Distribution")
        st.image("static/image/fig1.png")

    with st2:
        st.subheader("Feature Variance Distribution")
        st.image("static/image/fig2.png")

    with st3:
        st.subheader("Label Distribution")
        st.image("static/image/fig3.png")


def prediction_page():
    st1, st2 = st.columns(2)
    sex = st1.selectbox("Jenis Kelamin", ["", "Laki laki", "Perempuan"])
    parent_status = st2.selectbox("Kondisi Keluarga", ["", "Tunggal", "Hidup Bersama", "Hidup Berjauhan"])
    st3, st4 = st.columns(2)
    travel_time = st3.selectbox("Durasi Perjalanan ke Sekolah", ["", "< 15 Menit", "< 30 Menit", "< 1 Jam", "> 1 Jam"])
    study_time  = st4.selectbox("Durasi Waktu Belajar", ["", "1 s/d 2 Jam", "2 s/d 5 Jam", "5 s/d 10 Jam", "> 10 Jam"])
    st5, st6 = st.columns(2)
    extra_course = st5.selectbox("Mengambil Pembelajaran Ekstra", ["", "Iya", "Tidak"])
    activities   = st6.selectbox("Mengambil Ekstrakurikuler", ["", "Iya", "Tidak"])
    isClick = st.button("Predict")

    if st1 != "" and st2 != "" and st3 != "" and st4 != "" and st5 != "" and st6 != "" and isClick:
        condition_prediction = 1
        if condition_prediction == 0:
            st.error("Siswa anda memiliki potensi gagal ujian, tingkatkan pemahaman pembelajaran siswa dengan cara belajar daring")
        if condition_prediction == 1:
            st.success("Siswa anda memiliki potensi lulus ujian, jaga motivasi belajarnya dengan menambah waktu luang sehabis pulang sekolah")
    else:
        st.error("Silahkan isi semua form diatas")

# global variable

st.title("Gration")
st.write("Grading Estimation with Machine Learning Algorithm")

selection = st.sidebar.selectbox("Menu :", ["", "Dashboard", "Prediction"])

if selection == "Dashboard":
    dashboard_page()

if selection == "Prediction":
    prediction_page()