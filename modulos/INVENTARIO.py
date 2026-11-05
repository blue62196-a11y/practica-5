import streamlit as st
from modulos.login import login
from modulos.VENTAS import mostrar_venta
from modulos.INVENTARIO import mostrar_inventario  # <--- 1. IMPORTAR EL NUEVO MÓDULO

# Inicializar variables de sesión
if "sesion_iniciada" not in st.session_state:
    st.session_state["sesion_iniciada"] = False
if "usuario" not in st.session_state:
    st.session_state["usuario"] = ""

# Comprobar si el usuario inició sesión
if st.session_state["sesion_iniciada"]:
    st.sidebar.title("Menú")
    st.sidebar.write(f"Usuario: {st.session_state['usuario']}")
    
    # 2. AGREGAR "Inventario" EN LAS OPCIONES DEL MENÚ LATERAL
    opciones = [
        "Ventas",
        "Inventario",
        "Información"
    ]
    
    seleccion = st.sidebar.selectbox(
        "Seleccione una opción",
        opciones
    )
    
    # Mostrar módulo de ventas
    if seleccion == "Ventas":
        mostrar_venta()
        
    # 3. LLAMAR A LA FUNCIÓN DEL NUEVO MÓDULO
    elif seleccion == "Inventario":
        mostrar_inventario()
        
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
