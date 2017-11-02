from cx_Freeze import setup, Executable

executables = [Executable(script='drangon_ball.py',targetName='drangon_ball.exe',)]

setup(name='Drangon_ball',version='1.0',description='By Rice',executables=executables)
