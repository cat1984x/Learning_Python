from cx_Freeze import setup, Executable

executables = [Executable(script='alien_invasion.py',targetName='alien_invasion.exe',)]

setup(name='alien_invasion',version='1.0',description='alien_invasion',executables=executables)
