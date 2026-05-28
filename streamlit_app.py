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
import time
st.title("⚖️ Simulasi Menimbang Kimia")

# Input Massa
target_massa = st.number_input("Masukkan massa target (gram):", min_value=0.0, step=0.01)

if st.title("Timbang"):
    # Efek Loading Simulasi
    with st.status("Sedang menimbang...", expanded=True) as status:
        st.write("Menempatkan wadah...")
        time.sleep(1)
        st.write("Menambahkan zat...")
        time.sleep(1)
        status.update(label="Penimbangan Selesai!", state="complete", expanded=False)
    
    # Menampilkan Hasil
    st.write(f"Berhasil menimbang {target_massa} gram.")
    
    # Visualisasi Sederhana (Contoh menggunakan Metric)
    st.metric(label="Massa di Atas Timbangan", value=f"{target_massa} g")
    import streamlit as st

st.title("Simulasi Menimbang Kimia")

# Input target dan massa saat ini
target_massa = 0.03
massa_timbangan = st.number_input("Masukkan massa (gram):", min_value=0.0, step=0.01, format="%.2f")
for idx in range (5):
if st.button("Timbang", key=f"timbang_{idx}"):
    st.write(f"Tombol ke-{idx} ditekan")
    # Logika pengecekan
    if massa_timbangan == target_massa:
        st.success(f"Penimbangan Selesai! Berhasil menimbang {massa_timbangan} gram.")
    else:
        # Menangani penimbangan yang salah
        selisih = abs(massa_timbangan - target_massa)
        st.error(f"Penimbangan Salah! Massa saat ini: {massa_timbangan} g.")
        
        if massa_timbangan < target_massa:
            st.warning(f"Kurang {selisih:.2f} gram lagi.")
        else:
            st.warning(f"Kelebihan {selisih:.2f} gram.")
