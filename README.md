# dwarf_icon
Generador de imagenes de dwarfs (prototipo)

# Dwarf Icon

**Dwarf Icon** es un generador de imágenes de enanos (dwarfs) que combina diferentes elementos visuales como cabezas, ojos, barbas y sombreros para crear personajes únicos. Este proyecto es un prototipo desarrollado como parte de la integración con [Kobolt Assistant](https://github.com/XabierMatute/KoboltAssistant).

## Características

- Combina automáticamente imágenes de diferentes carpetas para generar personajes únicos.
- Utiliza la biblioteca [Pillow](https://python-pillow.org/) para manipulación de imágenes.
- Selección aleatoria de elementos visuales para cada generación.

## Instalación

1. Clona este repositorio:
```bash
``` git clone https://github.com/XabierMatute/dwarf_icon.git
``` cd dwarf_icon
```

2. Instala las dependencias:
```bash
``` pip install pillow
```

3. Asegúrate de que las carpetas `1_cabezas`, `2_ojos`, `3_barbas`, y `4_sombreros` contengan imágenes `.png`.

## Uso

Ejecuta el script principal para generar una imagen combinada:
```bash
``` python generacaras.py
```

La imagen generada se guardará en la carpeta `caras`.

## Estructura del Proyecto

```
dwarf_icon/
├── 1_cabezas/       # Imágenes de cabezas
├── 2_ojos/          # Imágenes de ojos
├── 3_barbas/        # Imágenes de barbas
├── 4_sombreros/     # Imágenes de sombreros
├── caras/           # Carpeta de salida para las imágenes generadas
├── generacaras.py   # Script principal
└── README.md        # Documentación del proyecto
```

## Créditos

- **Diseño y arte**: [B0redCuerv0](https://github.com/B0redCuerv0)  
  Todas las imágenes utilizadas en este proyecto fueron diseñadas y dibujadas por B0redCuerv0. ¡Gracias por tu increíble trabajo!

- **Desarrollo**: [Xabier Matute](https://github.com/XabierMatute)

## Licencia

Este proyecto es un prototipo y no tiene una licencia específica. Consulta los términos de uso de las imágenes con el diseñador.

---
Este proyecto forma parte de [Kobolt Assistant](https://github.com/XabierMatute/KoboltAssistant).