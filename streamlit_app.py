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
import streamlit as st

st.title("⚖️ Simulasi Menimbang Kimia")

# Input Massa
target_massa = st.number_input("Masukkan massa target (gram):", min_value=0.0, step=0.01)

if st.button("Timbang"):
    # Efek Loading Simulasi
    with st.status("Sedang menimbang...", expanded=True) as status:
        st.write("Menempatkan wadah...")
        time.sleep(1)
        st.write("Menambahkan zat...")
        time.sleep(1)
        status.update(label="Penimbangan Selesai!", state="complete", expanded=False)
    
    # Menampilkan Hasil
    st.success(f"Berhasil menimbang {target_massa} gram.")
    
    # Visualisasi Sederhana (Contoh menggunakan Metric)
    st.metric(label="Massa di Atas Timbangan", value=f"{target_massa} g")
