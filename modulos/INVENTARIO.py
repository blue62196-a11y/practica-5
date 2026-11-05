import streamlit as st
from config.conexion import obtener_conexion

def mostrar_inventario():
    st.header("Módulo de Inventario")
    st.write("Consulta y control de los productos disponibles en el sistema.")
    
    # 1. Mostrar la lista actual de inventario desde la base de datos
    conexion = obtener_conexion()
    if conexion is not None:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT Id_Item, Nombre_Producto, Stock, Precio FROM INVENTARIO")
            resultados = cursor.fetchall()
            
            if resultados:
                st.subheader("Productos Registrados")
                st.dataframe(resultados, use_container_width=True)
            else:
                st.info("No hay productos registrados en el inventario actualmente.")
                
            cursor.close()
            conexion.close()
        except Exception as error:
            st.error(f"Error al cargar el inventario: {error}")

    st.markdown("---")

    # 2. Formulario para agregar nuevos productos al inventario
    with st.form("form_inventario"):
        st.subheader("Agregar Nuevo Producto")
        nombre = st.text_input("Nombre del producto")
        stock = st.number_input("Cantidad en stock", min_value=0, step=1)
        precio = st.number_input("Precio unitario", min_value=0.0, format="%.2f")
        
        guardar_item = st.form_submit_button("Registrar producto")
        
        if guardar_item:
            if nombre.strip() == "":
                st.warning("Debe ingresar el nombre del producto.")
            else:
                try:
                    conexion_db = obtener_conexion()
                    if conexion_db is not None:
                        cursor_db = conexion_db.cursor()
                        consulta = """
                        INSERT INTO INVENTARIO (Nombre_Producto, Stock, Precio) 
                        VALUES (%s, %s, %s)
                        """
                        cursor_db.execute(consulta, (nombre, int(stock), float(precio)))
                        conexion_db.commit()
                        cursor_db.close()
                        conexion_db.close()
                        st.success("¡Producto registrado en el inventario correctamente!")
                        st.rerun()
                except Exception as error:
                    st.error(f"Error al registrar el producto: {error}")
