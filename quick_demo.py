#!/usr/bin/env python3
"""
Script de demostración rápida del Agente IA efectoLED

Ejecuta un análisis causal completo de la caída de conversión.
Perfecto para mostrar al cliente en una reunión.
"""

import os
import sys
from agent import create_agent


def main():
    """Ejecuta demo rápida"""
    
    # Verificar API key
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("\n❌ ERROR: ANTHROPIC_API_KEY no configurada")
        print("\nConfigura tu API key:")
        print("  export ANTHROPIC_API_KEY='sk-ant-...'")
        print()
        sys.exit(1)
    
    print("""
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║           🤖 AGENTE IA EFECTOLED - DEMOSTRACIÓN RÁPIDA               ║
║                                                                      ║
║  Caso de Uso: Análisis causal de caída de conversión                ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
    """)
    
    # Query del usuario
    query = """
    Las ventas de downlights bajaron esta semana respecto a la anterior.
    Necesito saber:
    1. ¿Qué causó la caída?
    2. ¿Cuánto dinero estamos perdiendo?
    3. ¿Qué acciones concretas debo tomar HOY?
    
    Dame un análisis completo con plan de acción priorizado.
    """
    
    print("📋 CONSULTA DEL CLIENTE efectoLED:")
    print("-" * 70)
    print(query)
    print("-" * 70)
    print()
    
    print("⚙️  PROCESANDO (esto puede tardar 10-30 segundos)...")
    print()
    
    # Crear agente y procesar
    try:
        agent = create_agent()
        response = agent.process_query(query, verbose=True)
        
        # Mostrar respuesta
        print("\n" + "="*70)
        print("  📊 ANÁLISIS DEL AGENTE IA")
        print("="*70 + "\n")
        print(response['analysis'])
        print()
        print("="*70)
        print(f"  ⏱️  Generado: {response['timestamp']}")
        print(f"  🤖 Modelo: {response['model']}")
        print("="*70)
        print()
        
        print("✅ Demo completada exitosamente")
        print()
        print("💡 Para más casos de uso, ejecuta: python demo.py")
        print()
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
