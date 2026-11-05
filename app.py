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
        
    # Mostrar el nuevo módulo adicional
    elif seleccion == "Inventario":
        st.header("Módulo de Inventario")
        st.write("Aquí puedes consultar el control de inventario de la tienda.")
        # Opcional: puedes llamar a una función externa como mostrar_inventario()
        
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
