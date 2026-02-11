@echo off
title IBL App Launcher
echo ==========================================
echo   Verificando Ambiente para App IBL
echo ==========================================

:: 1. Verifica se Python esta instalado
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [X] Python nao encontrado.
    echo.
    echo Baixando Python 3.11...
    curl -L -o python_installer.exe https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe
    
    echo.
    echo ========================================================
    echo AVISO: O instalador do Python vai abrir.
    echo IMPORTANTE: Marque a opcao "Add python.exe to PATH"
    echo antes de clicar em "Install Now".
    echo ========================================================
    echo.
    pause
    
    echo Iniciando instalador...
    start /wait python_installer.exe
    
    echo.
    echo Apos a instalacao, por favor feche esta janela e execute o arquivo novamente.
    pause
    exit
) else (
    echo [V] Python detectado.
)

:: 2. Instala dependencias
echo.
echo [!] Verificando bibliotecas necessarias...
pip install fastapi uvicorn

:: 3. Executa o servior
echo.
echo ==========================================
echo   Iniciando Servidor IBL...
echo   Acesse: http://localhost:8000
echo ==========================================
python execution/server.py

pause
