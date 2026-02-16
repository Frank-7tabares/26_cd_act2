import streamlit as st
import random

st.subheader("Ejercicio: 1 saludo")

nombre = st.text_input("¿Cuál es tu nombre?")


if nombre:
    st.write(f"¡Hola, {nombre}! Bienvenido a Streamlit.")

st.divider()

st.subheader("Ejercicio: 2 Calculadora de Producto")

numero1 = st.number_input("Ingresa el primer número:", value=0)
numero2 = st.number_input("Ingresa el segundo número:", value=0)

producto = numero1 * numero2


st.write(f"El producto es: {producto}")


if numero1 > 100 or numero2 > 100:
    st.warning("Números grandes")

st.divider()

st.subheader("Ejercicio: 3 Conversor de Temperatura")

direccion = st.radio("Elige la dirección de conversión:",
                     ["Celsius a Fahrenheit", "Fahrenheit a Celsius"])


temperatura = st.number_input("Ingresa la temperatura:", value=0.0)


if direccion == "Celsius a Fahrenheit":
    resultado = (temperatura * 9/5) + 32
    unidad_origen = "°C"
    unidad_destino = "°F"
else:
    resultado = (temperatura - 32) * 5/9
    unidad_origen = "°F"
    unidad_destino = "°C"


st.write(f"**{temperatura} {unidad_origen} = {resultado:.2f} {unidad_destino}**")

st.divider()

st.subheader("Ejercicio: 4 Galerí­a de Mascotas")

tab1, tab2, tab3 = st.tabs(["Gatos", "Perros", "Aves"])

with tab1:
    st.header(" Gatos")
    st.image("https://images.unsplash.com/photo-1574158622682-e40e69881006?w=400")
    if st.button("Me gusta", key="gatos"):
        st.toast("Te gusta esta mascota ")


with tab2:
    st.header(" Perros")
    st.image("https://png.pngtree.com/background/20230528/original/pngtree-dog-puppy-hd-wallpapers-hd-images-free-download-picture-image_2777865.jpg")
    if st.button("Me gusta", key="perros"):
        st.toast("Te gusta esta mascota ")


with tab3:
    st.header(" Aves")
    st.image("https://tse1.mm.bing.net/th/id/OIP.430WF1ekbEXY7vDrSNqVhQHaE5?rs=1&pid=ImgDetMain&o=7&rm=3")
    if st.button("Me gusta", key="aves"):
        st.toast("Te gusta esta mascota ")

st.divider()

st.subheader("Ejercicio: 5 Caja de Comentarios")

with st.form("comentarios_form"):
    asunto = st.text_input("Asunto:")
    mensaje = st.text_area("Mensaje:")
    enviar = st.form_submit_button("Enviar")
if enviar:
    if mensaje.strip():
        st.json({"asunto": asunto, "mensaje": mensaje})
    else:
        st.warning("El mensaje no puede estar vacío.")

st.divider()

st.subheader("Ejercicio: 6  Login Simulado")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if st.session_state.logged_in:
    st.success("¡Bienvenido, admin!")
    if st.button("Cerrar Sesión"):
        st.session_state.logged_in = False
else:
    usuario = st.text_input("Usuario:")
    contraseña = st.text_input("Contraseña:", type="password")
    if st.button("Ingresar"):
        if usuario == "admin" and contraseña == "1234":
            st.session_state.logged_in = True
            st.success("¡Login exitoso!")
        else:
            st.error("Usuario o contraseña incorrectos.")

st.divider()

st.subheader("Ejercicio: 7 Lista de Compras")

if "lista_compras" not in st.session_state:
    st.session_state.lista_compras = []

nuevo_producto = st.text_input("Producto:")
col1, col2 = st.columns(2)
with col1:
    if st.button("Agregar"):
        if nuevo_producto.strip():
            st.session_state.lista_compras.append(nuevo_producto)
            st.success(f"{nuevo_producto} agregado a la lista.")
        else:
            st.warning("El producto no puede estar vacío.")
with col2:
    if st.button("Limpiar Lista"):
        st.session_state.lista_compras.clear()
        st.success("Lista de compras limpiada.")
if st.session_state.lista_compras:
    st.write("**Lista de Compras:**")
    for idx, producto in enumerate(st.session_state.lista_compras, start=1):
        st.write(f"{idx}. {producto}")

st.divider()

st.subheader("Ejercicio: 8 Grafico interactivo")

n = st.slider("Selecciona cantidad de números:", 
              min_value=10, 
              max_value=100, 
              value=50)


numeros = [random.randint(1, 100) for _ in range(n)]


st.line_chart(numeros)


if st.button(" Regenerar"):
    st.rerun()

st.divider()    









