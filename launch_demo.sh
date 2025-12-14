#!/bin/bash

# Script de lanzamiento rápido de la demo Streamlit
# Uso: ./launch_demo.sh

echo "🤖 Agente IA efectoLED - Lanzando Demo Streamlit"
echo "=================================================="
echo ""

# Verificar que streamlit está instalado
if ! command -v streamlit &> /dev/null
then
    echo "⚠️  Streamlit no encontrado. Instalando..."
    pip install streamlit plotly anthropic
    echo ""
fi

# Verificar API key
if [ -z "$ANTHROPIC_API_KEY" ]; then
    echo "❌ ERROR: ANTHROPIC_API_KEY no configurada"
    echo ""
    echo "Por favor, configura tu API key:"
    echo "  export ANTHROPIC_API_KEY='sk-ant-api03-...'"
    echo ""
    echo "O añádela permanentemente a tu .bashrc/.zshrc"
    exit 1
fi

echo "✅ API Key configurada"
echo "✅ Dependencias verificadas"
echo ""
echo "🚀 Lanzando interfaz Streamlit..."
echo "   Se abrirá automáticamente en tu navegador"
echo "   URL: http://localhost:8501"
echo ""
echo "💡 Tips:"
echo "   • Selecciona casos de uso en el sidebar"
echo "   • Click en 'Analizar' o 'Simular' para ver resultados"
echo "   • Usa Ctrl+C para detener el servidor"
echo ""

# Lanzar Streamlit
streamlit run app.py
