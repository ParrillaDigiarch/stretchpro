# -*- mode: python ; coding: utf-8 -*-
#
# Uso:
#   pyinstaller stretchpro.spec
#

import os
from PyInstaller.utils.hooks import collect_data_files

datas = []
datas += collect_data_files("customtkinter")

datas += [(os.path.join(SPECPATH, "gui", "assets", "icon.ico"), "gui/assets")]

a = Analysis(
    ["main.py"],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name="StretchPro",
    debug=False,
    strip=False,
    upx=True,
    console=False,          # sin consola detrás de la GUI
    icon="gui/assets/icon.ico",
    onefile=True,
)
