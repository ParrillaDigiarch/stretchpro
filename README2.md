# StretchPro

Herramienta de escritorio (Windows) para el análisis de imágenes mediante el
algoritmo MCA, con interfaz gráfica construida en [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter).

Este repositorio contiene tanto el **código fuente** como las instrucciones
para generar el **ejecutable (.exe)** distribuible.

## Índice

- [Estructura del proyecto](#estructura-del-proyecto)
- [Instalación (modo desarrollo)](#instalación-modo-desarrollo)
- [Generar el .exe](#generar-el-exe)
- [Cómo citar](#cómo-citar)
- [Licencia](#licencia)

## Estructura del proyecto

```
stretchpro/
├── algorithms/          # Lógica pura de procesamiento (sin GUI)
│   ├── mca.py           # Algoritmo MCA
│   └── utils.py         # Operaciones con numpy / cv2
├── gui/                 # Interfaz gráfica (CustomTkinter)
│   ├── app.py           # Ventana principal
│   └── assets/          # Icono, imágenes de la interfaz
├── tests/               # Tests de algorithms/ (sin depender de la GUI)
├── docs/                # Documentación extra, capturas, etc.
├── main.py              # Punto de entrada (python main.py)
├── stretchpro.spec      # Configuración de PyInstaller para el .exe
├── requirements.txt
├── CITATION.cff
├── LICENSE
└── README.md
```

La separación `algorithms/` vs `gui/` es deliberada: los algoritmos no saben
nada de Tkinter, así que se pueden testear, reutilizar en un script de línea
de comandos, o en un notebook, sin arrastrar la interfaz.

## Instalación (modo desarrollo)

```bash
git clone https://github.com/TU_USUARIO/stretchpro.git
cd stretchpro
python -m venv .venv
.venv\Scripts\activate        # en Windows
pip install -r requirements.txt
python main.py
```

## Generar el .exe

```bash
pip install pyinstaller
pyinstaller stretchpro.spec
```

El ejecutable se genera en `dist/StretchPro.exe`. Es un único fichero
(`onefile=True` en el `.spec`), por lo que el usuario final solo necesita
descargar ese `.exe`, sin instalar Python ni nada más.

**Notas para que el .exe no falle:**
- El `.spec` ya incluye `collect_data_files("customtkinter")`: sin esto, el
  ejecutable arranca pero falla en tiempo de ejecución al no encontrar los
  temas JSON de CustomTkinter.
- Si el tamaño del `.exe` te preocupa, sustituye `opencv-python` por
  `opencv-python-headless` en `requirements.txt` (no necesitas las ventanas
  nativas de OpenCV si toda la GUI la hace CustomTkinter).
- Pon tu icono en `gui/assets/icon.ico` (formato `.ico`, no `.png`) y ajusta
  la ruta en `stretchpro.spec`.
- Prueba siempre el `.exe` generado en una máquina Windows limpia (o una VM)
  antes de distribuirlo: PyInstaller a veces "olvida" dependencias que en tu
  máquina de desarrollo ya estaban instaladas por otro motivo.

## Cómo citar

Si usas StretchPro en un trabajo académico, por favor cítalo así:

> TU_APELLIDO, TU_NOMBRE. (2026). *StretchPro* (versión 0.1.0) [Software].
> https://github.com/TU_USUARIO/stretchpro

```bibtex
@software{stretchpro2026,
  author  = {TU_APELLIDO, TU_NOMBRE},
  title   = {StretchPro},
  year    = {2026},
  version = {0.1.0},
  url     = {https://github.com/TU_USUARIO/stretchpro}
}
```

Si el software acompaña a un paper concreto, añade también la referencia del
paper (ver `CITATION.cff`, que GitHub usa para mostrar el botón
"Cite this repository" automáticamente).

> Consejo: si quieres una cita con DOI (más formal y citable que un simple
> enlace a GitHub), conecta el repositorio con [Zenodo](https://zenodo.org/)
> antes de tu próxima *release*. Zenodo archiva cada versión etiquetada
> (`git tag`) y te da un DOI permanente automáticamente, sin coste.

## Licencia

Código bajo licencia [MIT](LICENSE): libre para usar, modificar y
redistribuir, incluso comercialmente, siempre manteniendo el aviso de
copyright. La licencia MIT no obliga legalmente a citar el software en
publicaciones académicas — para eso está la sección [Cómo citar](#cómo-citar)
y el fichero `CITATION.cff`.
