# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('mp3', 'mp3')],  # Agrega la carpeta mp3
    hiddenimports=[
        'yt_dlp', 
        'mutagen', 
        'brotli', 
        'secretstorage',
        'requests',
        'urllib3',
    ],
    hookspath=[],
    hooksconfig={},
    excludes=['curl_cffi', 'multiprocessing.util'],  # Excluye módulos
    runtime_hooks=[],
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['icono.ico'],
)
