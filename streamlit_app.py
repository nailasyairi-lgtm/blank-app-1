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
import random

st.set_page_config(layout="wide")

st.title("⚗️ Simulasi Menimbang Zat")

# ======================
# CSS biar mirip lab
# ======================

st.markdown("""
<style>
.lab-container{
    background-color:#eef3f7;
    height:500px;
    border-radius:10px;
    position:relative;
}

.balance{
    position:absolute;
    left:120px;
    bottom:80px;
    width:180px;
    height:120px;
    background:#d9d9d9;
    border-radius:10px;
    text-align:center;
    padding-top:10px;
    box-shadow:2px 2px 10px gray;
}

.screen{
    background:black;
    color:lime;
    width:100px;
    margin:auto;
    padding:8px;
    border-radius:5px;
    font-size:20px;
}

.beaker{
    position:absolute;
    left:500px;
    bottom:80px;
    width:80px;
    height:100px;
    border:4px solid #444;
    border-top:none;
    background:rgba(0,150,255,0.3);
}
</style>
""", unsafe_allow_html=True)

# ======================
# Pilihan zat
# ======================

zat = st.selectbox(
    "Pilih sampel",
    ["NaCl", "Gula", "KOH", "CuSO4"]
)

# massa random
massa = {
    "NaCl": 2.351,
    "Gula": 5.124,
    "KOH": 1.876,
    "CuSO4": 3.442
}

if st.button("Timbang"):
    st.session_state["massa"] = massa[zat]

nilai = st.session_state.get("massa", 0.000)

# ======================
# Visualisasi
# ======================

html = f"""
<div class="lab-container">

    <div class="balance">
        <h4>Neraca Digital</h4>

        <div class="screen">
            {nilai:.3f} g
        </div>
    </div>

    <div class="beaker"></div>

</div>
"""

st.markdown(html, unsafe_allow_html=True)
