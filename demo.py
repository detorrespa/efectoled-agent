"""
Script de demostración del Agente IA de efectoLED

Ejecuta varios casos de uso reales para mostrar las capacidades del agente.
"""

import os
import sys
from agent import create_agent


def print_separator(title=""):
    """Imprime un separador visual"""
    print("\n" + "="*80)
    if title:
        print(f"  {title}")
        print("="*80)
    print()


def demo_caso_1_analisis_causal():
    """CASO DE USO 1: Análisis causal de caída de conversión"""
    
    print_separator("CASO DE USO 1: ¿Por qué cayó la conversión de downlights?")
    
    query = """
    Las ventas de downlights bajaron esta semana respecto a la semana pasada.
    ¿Qué está pasando y qué debo hacer urgente?
    """
    
    print("CONSULTA DEL USUARIO:")
    print(query)
    print("\nPROCESANDO...\n")
    
    agent = create_agent()
    response = agent.process_query(query, verbose=True)
    
    print_separator("RESPUESTA DEL AGENTE")
    print(response['analysis'])
    

def demo_caso_2_alertas():
    """CASO DE USO 2: Revisar alertas activas"""
    
    print_separator("CASO DE USO 2: ¿Qué alertas tengo activas?")
    
    query = """
    ¿Qué problemas críticos o importantes tengo ahora mismo que deba atender?
    Dame un resumen ejecutivo de las alertas activas.
    """
    
    print("CONSULTA DEL USUARIO:")
    print(query)
    print("\nPROCESANDO...\n")
    
    agent = create_agent()
    response = agent.process_query(query, verbose=True)
    
    print_separator("RESPUESTA DEL AGENTE")
    print(response['analysis'])


def demo_caso_3_simulador():
    """CASO DE USO 3: Simular escenario de decisión"""
    
    print_separator("CASO DE USO 3: Simular optimización checkout móvil")
    
    query = """
    Estoy pensando en invertir en mejorar el checkout móvil para reducir 
    el tiempo de carga. ¿Cuánto me costaría y qué impacto tendría en las ventas?
    """
    
    print("CONSULTA DEL USUARIO:")
    print(query)
    print("\nPROCESANDO...\n")
    
    agent = create_agent()
    response = agent.process_query(query, verbose=True)
    
    print_separator("RESPUESTA DEL AGENTE")
    print(response['analysis'])


def demo_caso_4_comparacion():
    """CASO DE USO 4: Comparar múltiples escenarios"""
    
    print_separator("CASO DE USO 4: ¿Dónde invierto primero?")
    
    query = """
    Tengo presupuesto limitado este mes. Compara estas opciones y dime cuál 
    debería priorizar:
    
    1. Optimizar el checkout móvil
    2. Aumentar presupuesto de Google Ads en Tiras LED
    3. Hacer campaña de reactivación de clientes B2B
    
    ¿Cuál me da mejor ROI?
    """
    
    print("CONSULTA DEL USUARIO:")
    print(query)
    print("\nPROCESANDO...\n")
    
    agent = create_agent()
    response = agent.process_query(query, verbose=True)
    
    print_separator("RESPUESTA DEL AGENTE")
    print(response['analysis'])


def demo_caso_5_mmm():
    """CASO DE USO 5: Marketing Mix Modeling"""
    
    print_separator("CASO DE USO 5: Optimizar distribución presupuesto marketing")
    
    query = """
    Tengo 54.000€ de presupuesto de marketing para el próximo mes.
    ¿Cómo debería distribuirlo entre canales para maximizar el retorno?
    
    Dame la recomendación específica por canal y explícame el porqué.
    """
    
    print("CONSULTA DEL USUARIO:")
    print(query)
    print("\nPROCESANDO...\n")
    
    agent = create_agent()
    response = agent.process_query(query, verbose=True)
    
    print_separator("RESPUESTA DEL AGENTE")
    print(response['analysis'])


def demo_caso_6_conversacional():
    """CASO DE USO 6: Consulta conversacional abierta"""
    
    print_separator("CASO DE USO 6: Consulta abierta sobre el negocio")
    
    query = """
    Necesito un resumen ejecutivo de la situación actual del ecommerce.
    ¿Qué está funcionando bien, qué está fallando, y cuáles son las 
    3 acciones prioritarias que debería tomar esta semana?
    """
    
    print("CONSULTA DEL USUARIO:")
    print(query)
    print("\nPROCESANDO...\n")
    
    agent = create_agent()
    response = agent.process_query(query, verbose=True)
    
    print_separator("RESPUESTA DEL AGENTE")
    print(response['analysis'])


def main():
    """Ejecuta la demostración"""
    
    # Verificar API key
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("\n⚠️  ERROR: ANTHROPIC_API_KEY no configurada")
        print("\nPor favor, configura tu API key:")
        print("  export ANTHROPIC_API_KEY='tu-api-key'\n")
        sys.exit(1)
    
    print("""
╔════════════════════════════════════════════════════════════════════════════╗
║                                                                            ║
║              🤖 AGENTE IA PARA EFECTOLED - DEMOSTRACIÓN                   ║
║                                                                            ║
║  Este agente combina modelos ML especializados con Claude Sonnet 4        ║
║  para proporcionar análisis de negocio accionables en lenguaje natural.   ║
║                                                                            ║
╚════════════════════════════════════════════════════════════════════════════╝
    """)
    
    # Menú de casos de uso
    print("\nCASOS DE USO DISPONIBLES:\n")
    print("  1. Análisis causal - ¿Por qué cayó la conversión?")
    print("  2. Alertas activas - ¿Qué problemas hay ahora?")
    print("  3. Simulador - ¿Qué pasa si optimizo el móvil?")
    print("  4. Comparación - ¿Dónde invierto primero?")
    print("  5. MMM - ¿Cómo distribuyo el presupuesto marketing?")
    print("  6. Consulta ejecutiva - Resumen general del negocio")
    print("  7. DEMO COMPLETA - Ejecutar todos los casos")
    print("  0. Salir")
    
    while True:
        print("\n" + "-"*80)
        choice = input("\nSelecciona un caso de uso (0-7): ").strip()
        
        if choice == "0":
            print("\n¡Hasta pronto! 👋\n")
            break
        
        elif choice == "1":
            demo_caso_1_analisis_causal()
        
        elif choice == "2":
            demo_caso_2_alertas()
        
        elif choice == "3":
            demo_caso_3_simulador()
        
        elif choice == "4":
            demo_caso_4_comparacion()
        
        elif choice == "5":
            demo_caso_5_mmm()
        
        elif choice == "6":
            demo_caso_6_conversacional()
        
        elif choice == "7":
            print("\n🚀 Ejecutando DEMO COMPLETA...\n")
            demo_caso_1_analisis_causal()
            input("\n[Presiona ENTER para continuar...]")
            
            demo_caso_2_alertas()
            input("\n[Presiona ENTER para continuar...]")
            
            demo_caso_3_simulador()
            input("\n[Presiona ENTER para continuar...]")
            
            demo_caso_4_comparacion()
            input("\n[Presiona ENTER para continuar...]")
            
            demo_caso_5_mmm()
            input("\n[Presiona ENTER para continuar...]")
            
            demo_caso_6_conversacional()
            
            print_separator("DEMO COMPLETA FINALIZADA")
        
        else:
            print("\n⚠️  Opción no válida. Por favor selecciona 0-7.")


if __name__ == "__main__":
    main()
