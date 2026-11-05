import streamlit as st
from modulos.login import login
from modulos.VENTAS import mostrar_venta
from modulos.INVENTARIO import mostrar_inventario

# Inicializar variables de sesión si no existen
if "sesion_iniciada" not in st.session_state:
    st.session_state["sesion_iniciada"] = False
if "usuario" not in st.session_state:
    st.session_state["usuario"] = ""

# Comprobar si el usuario inició sesión
if st.session_state["sesion_iniciada"]:
    st.sidebar.title("Menú")
    st.sidebar.write(f"Usuario: {st.session_state['usuario']}")
    
    # Agregamos la nueva opción al menú lateral
    opciones = [
        "Ventas",
        "Inventario",    # <--- NUEVO MÓDULO AGREGADO
        "Información"
    ]
    
    seleccion = st.sidebar.selectbox(
        "Seleccione una opción",
        opciones
    )
    
    # Mostrar módulo de ventas
    if seleccion == "Ventas":
        mostrar_venta()
        
    # Mostrar el módulo de inventario llamando a su función
    elif seleccion == "Inventario":
        mostrar_inventario()  # <--- LLAMADA A LA FUNCIÓN DEL MÓDULO INVENTARIO
        
    # Mostrar módulo de información
    elif seleccion == "Información":
        st.header("Información del sistema")
        st.write("Aplicación desarrollada durante el Laboratorio de SGI.")
        
    # Cerrar sesión
    if st.sidebar.button("Cerrar sesión"):
        st.session_state["sesion_iniciada"] = False
        st.session_state["usuario"] = ""
        st.rerun()
else:
    login()
