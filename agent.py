"""
Agente LLM Orquestador para efectoLED

Este agente usa Claude Sonnet 4 para:
1. Entender consultas de negocio en lenguaje natural
2. Llamar a los modelos ML apropiados
3. Sintetizar resultados en recomendaciones accionables
"""

import json
import os
from anthropic import Anthropic
from datetime import datetime

from models import (
    CausalAnalysisModel,
    AlertsModel,
    ScenarioSimulator,
    MarketingMixModel
)

from config import BUSINESS_CONTEXT


class EfectoLEDAgent:
    """
    Agente IA principal para análisis de datos de efectoLED
    """
    
    def __init__(self, api_key=None):
        """
        Inicializa el agente
        
        Args:
            api_key: Anthropic API key (o usa ANTHROPIC_API_KEY de env)
        """
        self.api_key = api_key or os.environ.get("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ValueError("ANTHROPIC_API_KEY no configurada")
        
        self.client = Anthropic(api_key=self.api_key)
        
        # Inicializar modelos ML
        self.models = {
            'causal': CausalAnalysisModel(),
            'alerts': AlertsModel(),
            'simulator': ScenarioSimulator(),
            'mmm': MarketingMixModel()
        }
        
        # Definir herramientas disponibles
        self.tools = self._define_tools()
        
        # System prompt
        self.system_prompt = self._create_system_prompt()
    
    def _define_tools(self):
        """Define las herramientas que el agente puede usar"""
        
        return [
            {
                "name": "analizar_causa_variacion",
                "description": """Identifica las causas raíz de una variación en conversión, ventas u otra métrica.
                
                Usa este tool cuando el usuario pregunte:
                - "¿Por qué bajó la conversión?"
                - "¿Qué pasó con las ventas de X?"
                - "¿Por qué subió/bajó [métrica]?"
                
                El modelo devuelve:
                - Causas principales con % de impacto
                - Detalles técnicos de cada causa
                - Acciones recomendadas priorizadas
                - Estimación de revenue afectado
                """,
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "metric": {
                            "type": "string",
                            "description": "Métrica a analizar: 'conversion', 'revenue', 'aov', etc.",
                            "enum": ["conversion", "revenue", "aov"]
                        },
                        "category": {
                            "type": "string",
                            "description": "Categoría de producto (opcional): 'Downlights', 'Tiras LED', 'Focos', etc. Null para analizar total.",
                        },
                        "period_current": {
                            "type": "string",
                            "description": "Período actual a analizar (default: 'week_0' = esta semana)",
                            "default": "week_0"
                        },
                        "period_comparison": {
                            "type": "string",
                            "description": "Período de comparación (default: 'week_-1' = semana pasada)",
                            "default": "week_-1"
                        }
                    },
                    "required": ["metric"]
                }
            },
            {
                "name": "obtener_alertas_activas",
                "description": """Obtiene las alertas activas del sistema de monitorización.
                
                Usa este tool cuando el usuario pregunte:
                - "¿Qué alertas hay activas?"
                - "¿Qué problemas hay ahora?"
                - "¿Qué debo revisar urgente?"
                
                El sistema devuelve alertas de 3 tipos:
                - CRÍTICAS: Requieren acción inmediata
                - ALTAS: Requieren acción pronto
                - OPORTUNIDADES: Acciones recomendadas para mejorar
                """,
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "severity_threshold": {
                            "type": "string",
                            "description": "Nivel mínimo de severidad: 'critical', 'high', 'medium', 'low'",
                            "enum": ["critical", "high", "medium", "low"],
                            "default": "medium"
                        }
                    }
                }
            },
            {
                "name": "simular_escenario",
                "description": """Simula el impacto de una decisión de negocio.
                
                Usa este tool cuando el usuario pregunte:
                - "¿Qué pasa si invierto X en Y?"
                - "¿Cuánto ganaría si mejoro Z?"
                - "¿Qué debería priorizar?"
                
                Escenarios disponibles:
                - optimize_mobile_checkout: Mejorar velocidad móvil
                - increase_google_ads_tiras_led: Aumentar presupuesto Google Ads
                - b2b_reactivation_campaign: Reactivar clientes B2B
                - pause_expensive_keywords: Optimizar keywords Google Ads
                
                Devuelve:
                - Inversión requerida
                - Revenue esperado (mes 1 y año 1)
                - ROI y payback
                - Análisis de sensibilidad
                """,
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "scenario_type": {
                            "type": "string",
                            "description": "Tipo de escenario a simular",
                            "enum": [
                                "optimize_mobile_checkout",
                                "increase_google_ads_tiras_led",
                                "b2b_reactivation_campaign",
                                "pause_expensive_keywords"
                            ]
                        }
                    },
                    "required": ["scenario_type"]
                }
            },
            {
                "name": "comparar_escenarios",
                "description": """Compara múltiples escenarios y los ordena por ROI.
                
                Usa este tool cuando el usuario quiera decidir entre opciones:
                - "¿Qué debería hacer primero?"
                - "Compara estas opciones"
                - "¿Dónde invierto el próximo presupuesto?"
                
                Devuelve ranking de escenarios por ROI esperado.
                """,
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "scenario_types": {
                            "type": "array",
                            "description": "Lista de escenarios a comparar",
                            "items": {
                                "type": "string",
                                "enum": [
                                    "optimize_mobile_checkout",
                                    "increase_google_ads_tiras_led",
                                    "b2b_reactivation_campaign",
                                    "pause_expensive_keywords"
                                ]
                            },
                            "minItems": 2
                        }
                    },
                    "required": ["scenario_types"]
                }
            },
            {
                "name": "optimizar_presupuesto_marketing",
                "description": """Recomienda distribución óptima del presupuesto de marketing usando Marketing Mix Modeling.
                
                Usa este tool cuando el usuario pregunte:
                - "¿Cómo distribuyo mi presupuesto de marketing?"
                - "¿Qué canal funciona mejor?"
                - "¿Dónde pongo el próximo euro?"
                
                Analiza:
                - Contribución incremental de cada canal
                - Nivel de saturación
                - ROAS por canal
                - Efectos de carryover
                
                Devuelve:
                - Distribución actual vs recomendada
                - Impacto esperado en revenue
                - Mejora en ROAS global
                """,
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "total_budget": {
                            "type": "number",
                            "description": "Presupuesto total de marketing a distribuir (€)"
                        }
                    },
                    "required": ["total_budget"]
                }
            },
            {
                "name": "obtener_atribucion_canales",
                "description": """Obtiene la atribución actual de revenue por canal de marketing.
                
                Usa este tool cuando el usuario pregunte:
                - "¿Qué canal genera más ventas?"
                - "¿Cuál es el ROAS de cada canal?"
                - "¿Qué canales están saturados?"
                
                Devuelve atribución incremental real (no last-click).
                """,
                "input_schema": {
                    "type": "object",
                    "properties": {}
                }
            }
        ]
    
    def _create_system_prompt(self):
        """Crea el system prompt del agente"""
        
        return f"""Eres un analista de datos senior especializado en ecommerce de iluminación LED, trabajando para efectoLED.

## CONTEXTO DE NEGOCIO

efectoLED es una tienda online de productos de iluminación LED con:
- **Clientes**: B2B (electricistas, instaladores profesionales) y B2C (particulares)
- **Catálogo**: {', '.join(BUSINESS_CONTEXT['main_categories'])}
- **Canales marketing**: {', '.join(BUSINESS_CONTEXT['marketing_channels'])}
- **Métricas clave**: {', '.join(BUSINESS_CONTEXT['key_metrics'])}

## TU ROL

Tu trabajo es ayudar al equipo de efectoLED a:
1. **Entender qué está pasando**: Identificar causas raíz de cambios en métricas
2. **Tomar decisiones**: Recomendar acciones concretas priorizadas
3. **Predecir impactos**: Simular escenarios antes de ejecutar
4. **Optimizar inversión**: Maximizar ROI de marketing

## METODOLOGÍA

1. **Usa las herramientas** para obtener datos precisos de los modelos ML
2. **Analiza holísticamente**: Considera múltiples dimensiones (producto, canal, dispositivo, temporal)
3. **Prioriza acciones**: Quick wins primero (ROI rápido, implementación fácil)
4. **Cuantifica impactos**: Siempre que sea posible, estima revenue/ahorro
5. **Explica en lenguaje de negocio**: Sin jerga técnica de ML

## ESTILO DE COMUNICACIÓN

- **Directo y accionable**: Empieza con la conclusión, luego detalles
- **Específico**: "Pausar keyword X" no "revisar Google Ads"
- **Cuantificado**: "Recuperar 8K€/semana" no "mejorar ventas"
- **Estructurado**: Usa emojis para claridad (🔍 análisis, ✅ acción, 💰 impacto, ⚠️ riesgo)
- **Conciso**: Máximo 3-4 párrafos por sección

## RESTRICCIONES IMPORTANTES

- **NO inventes datos**: Si no tienes un dato, di "necesito más información"
- **NO prometas resultados**: Usa "esperado", "estimado", "basado en modelo"
- **SÍ reconoce limitaciones**: Los modelos tienen incertidumbre
- **SÍ contextualiza**: Menciona si hay eventos externos (Black Friday, competencia, etc.)

## EJEMPLO DE BUENA RESPUESTA

Usuario: "Las ventas de downlights bajaron esta semana, ¿qué hago?"

[Llamas a analizar_causa_variacion con metric='conversion', category='Downlights']

Tú respondes:

🔍 **DIAGNÓSTICO**
Las ventas de Downlights cayeron 15% (-2.8K€). He identificado 3 causas:

1. **Bug móvil checkout** (60% del impacto)
   - Tiempo carga: 2.1s → 4.8s desde deploy martes
   - Conversión móvil: -25%
   - Revenue perdido: 5.2K€ en 3 días

2. **Competencia Google Ads** (30% del impacto)  
   - Competidor subió CPC +93% en keyword principal
   - Tu posición cayó: 1.8 → 3.2
   - Revenue perdido: 3.1K€

3. **Stock bajo producto top** (10% del impacto)
   - Ref-245 (28% de tráfico) con stock crítico
   - "Últimas unidades" genera rebote

✅ **PLAN DE ACCIÓN (priorizado)**

**HOY MISMO:**
1. Rollback deploy 3.2.1 → Recuperar 5.2K€/semana
2. Destacar ref-248 como alternativa

**ESTA SEMANA:**
3. Pausar keyword cara, activar long-tail → Ahorrar 700€/semana
4. Adelantar pedido ref-245 a proveedor

💰 **IMPACTO ESPERADO**
Ejecutando todo: Recuperar 11.5K€/semana (77% de la caída)

¿Quieres que simule algún escenario adicional?

---

Fecha/hora actual: {datetime.now().strftime("%Y-%m-%d %H:%M")}

Ahora responde a la consulta del usuario usando las herramientas cuando sea necesario.
"""
    
    def process_query(self, user_query, context=None, verbose=False):
        """
        Procesa una consulta del usuario
        
        Args:
            user_query: Pregunta o solicitud del usuario
            context: Contexto adicional opcional
            verbose: Si True, imprime el proceso paso a paso
        
        Returns:
            Respuesta del agente en texto
        """
        
        messages = [{"role": "user", "content": user_query}]
        
        if verbose:
            print(f"\n{'='*60}")
            print(f"USUARIO: {user_query}")
            print(f"{'='*60}\n")
        
        # Loop de agente (hasta 5 iteraciones max para evitar loops infinitos)
        iteration = 0
        max_iterations = 5
        
        while iteration < max_iterations:
            iteration += 1
            
            if verbose:
                print(f"\n--- Iteración {iteration} ---")
            
            # Llamar a Claude
            response = self.client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=4096,
                system=self.system_prompt,
                tools=self.tools,
                messages=messages
            )
            
            # Si Claude quiere usar herramientas
            if response.stop_reason == "tool_use":
                
                # Ejecutar todas las herramientas solicitadas
                tool_results = []
                
                for content_block in response.content:
                    if content_block.type == "tool_use":
                        
                        tool_name = content_block.name
                        tool_input = content_block.input
                        
                        if verbose:
                            print(f"\n🔧 Llamando a: {tool_name}")
                            print(f"   Input: {json.dumps(tool_input, indent=2, ensure_ascii=False)}")
                        
                        # Ejecutar herramienta
                        result = self._execute_tool(tool_name, tool_input)
                        
                        if verbose:
                            print(f"   ✓ Resultado obtenido ({len(json.dumps(result))} chars)")
                        
                        tool_results.append({
                            "type": "tool_result",
                            "tool_use_id": content_block.id,
                            "content": json.dumps(result, ensure_ascii=False)
                        })
                
                # Añadir respuesta de Claude y resultados al historial
                messages.append({"role": "assistant", "content": response.content})
                messages.append({"role": "user", "content": tool_results})
                
            else:
                # Claude terminó, extraer respuesta final
                if verbose:
                    print(f"\n✅ Análisis completado\n")
                
                return self._format_final_response(response)
        
        # Si llegamos aquí, superamos max_iterations
        return {
            "error": "El agente superó el número máximo de iteraciones",
            "partial_response": self._format_final_response(response)
        }
    
    def _execute_tool(self, tool_name, tool_input):
        """Ejecuta una herramienta (modelo ML)"""
        
        try:
            if tool_name == "analizar_causa_variacion":
                return self.models['causal'].analyze_variation(
                    metric=tool_input.get('metric'),
                    category=tool_input.get('category'),
                    period_current=tool_input.get('period_current', 'week_0'),
                    period_comparison=tool_input.get('period_comparison', 'week_-1')
                )
            
            elif tool_name == "obtener_alertas_activas":
                return self.models['alerts'].get_active_alerts(
                    severity_threshold=tool_input.get('severity_threshold', 'medium')
                )
            
            elif tool_name == "simular_escenario":
                return self.models['simulator'].simulate_scenario(
                    scenario_type=tool_input.get('scenario_type')
                )
            
            elif tool_name == "comparar_escenarios":
                return self.models['simulator'].compare_scenarios(
                    scenario_types=tool_input.get('scenario_types', [])
                )
            
            elif tool_name == "optimizar_presupuesto_marketing":
                return self.models['mmm'].optimize_budget(
                    total_budget=tool_input.get('total_budget')
                )
            
            elif tool_name == "obtener_atribucion_canales":
                return self.models['mmm'].get_channel_attribution()
            
            else:
                return {"error": f"Herramienta '{tool_name}' no reconocida"}
        
        except Exception as e:
            return {"error": f"Error ejecutando {tool_name}: {str(e)}"}
    
    def _format_final_response(self, response):
        """Formatea la respuesta final del agente"""
        
        # Extraer texto
        text_parts = []
        for block in response.content:
            if hasattr(block, 'text'):
                text_parts.append(block.text)
        
        final_text = "\n".join(text_parts)
        
        return {
            "analysis": final_text,
            "timestamp": datetime.now().isoformat(),
            "model": "claude-sonnet-4-20250514",
            "iterations": 1  # En producción, rastrearíamos esto mejor
        }


# Función helper para uso fácil
def create_agent(api_key=None):
    """Crea una instancia del agente"""
    return EfectoLEDAgent(api_key=api_key)
