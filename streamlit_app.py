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
<!DOCTYPE html>
<html>
<head>
    <title>VirtualChem Lab</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>

<body>

<h1>VirtualChem Lab</h1>

<div class="menu">
    <a href="/timbang">Simulasi Menimbang</a>
</div>

<div class="menu">
    <a href="/titrasi">Simulasi Titrasi</a>
</div>

</body>
</html>
