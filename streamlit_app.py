import streamlit as st
st.title("🧪 VirtualChem Lab")

st.write("Simulasi Praktikum Kimia Virtual")
menu = st.selectbox(
    "Pilih Praktikum",
    ["Menimbang", "Titrasi"]
)

# Simulasi Menimbang
if menu == "Menimbang":

    st.header("Simulasi Menimbang")

    massa = st.number_input(
        "Masukkan massa (gram)",
        min_value=0.0
    )

    if st.button("Timbang"):
        st.success(
            f"Berhasil menimbang {massa} gram"
        )

# Simulasi Titrasi
if menu == "Titrasi":

    st.header("Simulasi Titrasi")

    if st.button("Mulai Titrasi"):
        st.info(
            "Larutan berubah warna menjadi pink"
        )
mport streamlit as st
import time

st.title("🧪 VirtualChem Lab: Pro")

# Sidebar untuk pengaturan
with st.sidebar:
    st.header("Pengaturan Alat")
    kapasitas_max = st.number_input("Kapasitas Max (g)", value=100)

st.subheader("Simulasi Menimbang Analitik")

# Inisialisasi state untuk tombol Tare
if 'berat_wadah' not in st.session_state:
    st.session_state.berat_wadah = 0.0

col1, col2 = st.columns(2)

with col1:
    massa_input = st.number_input("Masukkan massa zat (gram)", min_value=0.0, step=0.01)
    
    if st.button("Timbang"):
        with st.spinner('Menimbang...'):
            time.sleep(0.5) # Animasi loading
            total = massa_input + st.session_state.berat_wadah
            st.success(f"Berhasil menimbang: {massa_input} gram")
st.metric(label="Display Timbangan", value=f"{total} g")

with col2:
    if st.button("Tare (Nolkan)"):
        st.session_state.berat_wadah = 0.0
        st.rerun()
    
    st.info("Tips: Pastikan pintu kaca timbangan tertutup untuk akurasi tinggi.")
