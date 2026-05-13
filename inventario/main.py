from inventario.database.inventario_db import InventarioDB
from inventario.views.inventario_view import InventarioView

def main():
    db = InventarioDB('inventario.db')
    vista = InventarioView(db)
    vista.mostrar_menu()

if __name__ == "__main__":
    main()
