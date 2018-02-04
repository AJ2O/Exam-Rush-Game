# -*- mode: python -*-

block_cipher = None


a = Analysis(['adventure.py'],
             pathex=['c:\\Users\\Owner\\Downloads\\UTM\\TBVG\\Exam Rush!'],
             binaries=[],
             datas=[('map.txt', 'data'), ('locations.txt', 'data'), ('items.txt', 'data')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='adventure',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='adventure')
