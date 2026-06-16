# Sales Management System - Café Andrómeda 

Este repositorio contiene un sistema de gestión de ventas e inventario basado en consola, desarrollado en Python. El proyecto implementa estructuras de datos avanzadas, manejo de archivos locales para la persistencia de información y control de excepciones para garantizar la estabilidad del software ante entradas inválidas de usuario.

El objetivo principal fue aplicar lógica de programación estructurada para simular un punto de venta (POS) funcional.

##  Tecnologías y Conceptos Aplicados
* **Python 3** (Lógica de desarrollo)
* **Persistencia de Datos**: Manipulación de archivos de texto (`.txt`) mediante lectura y escritura con el gestor de contextos `with open()`.
* **Manejo de Excepciones**: Bloques `try-except` para validar datos numéricos y prevenir fallos en tiempo de ejecución.
* **Estructuras de Datos**: Uso estratégico de Listas, Diccionarios y Tuplas inmutables para la organización de la información.

##  Estructura del Código

El script está diseñado bajo un enfoque modular, dividiendo las responsabilidades en funciones específicas:

1. **`mostrar_menu()`**: Controla la interfaz de usuario en consola y la navegación del sistema.
2. **`registrar_pedido()`**: Captura las ventas de los clientes, valida los datos de entrada (cantidad y precio) mediante el manejo de errores y encapsula la información en diccionarios dinámicos.
3. **`mostrar_total()`**: Procesa y calcula de forma iterativa los subtotales y el gran total acumulado de la sesión actual.
4. **`guardar_en_archivo()`**: Exporta y anexa de manera ordenada la información de las ventas a un archivo físico (`pedidos.txt`) para evitar la pérdida de datos.
5. **`leer_desde_archivo()`**: Consulta el historial histórico almacenado, deserializando las cadenas de texto del archivo local para presentarlas en pantalla.

## 🚀 Características Técnicas
* **Robustez**: Validación estricta para evitar nombres de productos vacíos o valores numéricos negativos.
* **Modularidad**: Estructurado bajo el estándar de ejecución `if __name__ == "__main__":`.
* **Optimización**: Uso del módulo integrado `os` para verificar la existencia previa de archivos antes de intentar lecturas en memoria.

---
Desarrollado por [Marco Romero](https://github.com/marcoromero8)
