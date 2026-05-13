"""
Punto de entrada para el Sistema de Inventario
Patrón MVC - Separación de responsabilidades
"""

from inventario.database.inventario_db import InventarioDB
from inventario.views.inventario_view import InventarioView


def main():
    """Función principal para ejecutar el sistema"""
    print("\n" + "="*60)
    print("         🚀 INICIANDO SISTEMA DE INVENTARIO")
    print("="*60)
    
    # Inicializa la BD
    db = InventarioDB('inventario.db')
    
    # Inicializa la vista
    vista = InventarioView(db)
    
    # Muestra el menú
    vista.mostrar_menu()


if __name__ == "__main__":
    main()
