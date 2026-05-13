"""
Sistema de Inventario con POO y SQLite
Patrón MVC - Separación de responsabilidades
"""

from inventario.models.producto import Producto
from inventario.database.inventario_db import InventarioDB
from inventario.views.inventario_view import InventarioView

__all__ = ['Producto', 'InventarioDB', 'InventarioView']
