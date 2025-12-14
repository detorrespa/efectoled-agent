@echo off
REM Script de lanzamiento rápido de la demo Streamlit (Windows)
REM Uso: launch_demo.bat

echo.
echo 🤖 Agente IA efectoLED - Lanzando Demo Streamlit
echo ==================================================
echo.

REM Verificar API key
if "%ANTHROPIC_API_KEY%"=="" (
    echo ❌ ERROR: ANTHROPIC_API_KEY no configurada
    echo.
    echo Por favor, configura tu API key:
    echo   set ANTHROPIC_API_KEY=sk-ant-api03-...
    echo.
    echo O configúrala permanentemente en Variables de Entorno del Sistema
    pause
    exit /b 1
)

echo ✅ API Key configurada
echo.

REM Verificar que streamlit está instalado
streamlit --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ⚠️  Streamlit no encontrado. Instalando...
    pip install streamlit plotly anthropic
    echo.
)

echo ✅ Dependencias verificadas
echo.
echo 🚀 Lanzando interfaz Streamlit...
echo    Se abrirá automáticamente en tu navegador
echo    URL: http://localhost:8501
echo.
echo 💡 Tips:
echo    • Selecciona casos de uso en el sidebar
echo    • Click en 'Analizar' o 'Simular' para ver resultados
echo    • Cierra esta ventana para detener el servidor
echo.

REM Lanzar Streamlit
streamlit run app.py

pause
