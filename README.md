# 🤖 Agente IA para efectoLED - Prototipo Funcional

## Descripción

Este es un prototipo funcional de un **Agente IA Orquestador** que combina modelos de Machine Learning especializados con Claude Sonnet 4 para proporcionar análisis de negocio accionables a efectoLED.

El agente puede:
- 🔍 Identificar causas raíz de variaciones en métricas (conversión, ventas, etc.)
- 🚨 Detectar y explicar alertas críticas del negocio
- 🎯 Simular escenarios "qué pasa si..." antes de tomar decisiones
- 💰 Optimizar distribución de presupuesto de marketing (MMM)
- 💬 Responder consultas en lenguaje natural y generar planes de acción

## Arquitectura

```
┌─────────────────────────────────────────────────────────┐
│              USUARIO (efectoLED team)                   │
│         "¿Por qué bajó la conversión?"                  │
└─────────────────┬───────────────────────────────────────┘
                  │
         ┌────────▼────────────┐
         │  AGENTE LLM (Claude) │
         │  • Entiende query    │
         │  • Orquesta modelos  │
         │  • Sintetiza insights│
         └────────┬────────────┘
                  │
         ┌────────┴────────────────────────────────────┐
         │                                              │
    ┌────▼─────┐  ┌─────▼─────┐  ┌──────▼──────┐  ┌──────▼──────┐
    │  Modelo  │  │  Modelo   │  │   Modelo    │  │   Modelo    │
    │  Causal  │  │  Alertas  │  │  Simulador  │  │    MMM      │
    │ (SHAP)   │  │ (LSTM +   │  │  (Causal +  │  │ (Bayesian)  │
    │          │  │ Isolation │  │  Monte      │  │             │
    │          │  │  Forest)  │  │  Carlo)     │  │             │
    └────┬─────┘  └─────┬─────┘  └──────┬──────┘  └──────┬──────┘
         │              │                │                │
         └──────────────┴────────────────┴────────────────┘
                               │
                    ┌──────────▼───────────┐
                    │ RESPUESTA ACCIONABLE  │
                    │ en lenguaje natural   │
                    └──────────────────────┘
```

## Componentes

### 1. **agent.py** - Agente LLM Orquestador
- Usa Claude Sonnet 4 con tool use
- Coordina llamadas a modelos ML
- Genera explicaciones en lenguaje de negocio
- Prioriza acciones y cuantifica impactos

### 2. **models.py** - Modelos ML Especializados
- **CausalAnalysisModel**: Análisis causal multidimensional (simula SHAP + Causal Inference)
- **AlertsModel**: Sistema de alertas predictivas (simula LSTM + Anomaly Detection)
- **ScenarioSimulator**: Simulador de decisiones (simula Causal Forecasting + Monte Carlo)
- **MarketingMixModel**: MMM para optimización de presupuesto (simula Bayesian MMM)

*Nota: En este prototipo los modelos usan datos simulados. En producción se sustituirían por modelos reales entrenados con datos de efectoLED.*

### 3. **config.py** - Configuración y Datos Simulados
- Contexto de negocio de efectoLED
- Datos históricos simulados (semana actual vs baseline)
- Escenarios de simulación predefinidos
- Datos de competencia

### 4. **demo.py** - Script de Demostración
- 6 casos de uso completos
- Modo interactivo
- Modo verbose para ver el proceso paso a paso

## Instalación

### Requisitos
- Python 3.8+
- API Key de Anthropic (Claude)

### Pasos

1. **Clonar o descargar los archivos**
```bash
cd efectoled_agent
```

2. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

3. **Configurar API Key**
```bash
export ANTHROPIC_API_KEY='tu-api-key-aqui'
```

## Uso

### 🎨 Interfaz Visual con Streamlit (RECOMENDADO PARA DEMOS)

La forma más impactante de demostrar el agente es con la interfaz web interactiva:

```bash
# Opción 1: Script de lanzamiento (más fácil)
./launch_demo.sh          # Linux/Mac
launch_demo.bat           # Windows

# Opción 2: Comando directo
streamlit run app.py
```

Se abrirá automáticamente en `http://localhost:8501`

**Interfaz incluye**:
- ✅ Gráficos interactivos con Plotly
- ✅ Cards visuales con código de colores
- ✅ Progress bars en tiempo real
- ✅ 5 casos de uso con tabs
- ✅ Métricas destacadas con deltas
- ✅ Sidebar con contexto de negocio

**Ver guía completa**: `DEMO_STREAMLIT.md`

### Modo Terminal (Alternativa)

```bash
# Demo rápida (1 caso de uso)
python quick_demo.py

# Demo interactiva (menú con 6 casos)
python demo.py
```

### Uso Programático

```python
from agent import create_agent

# Crear agente
agent = create_agent()

# Hacer una consulta
response = agent.process_query(
    "¿Por qué bajó la conversión de downlights esta semana?",
    verbose=True  # Ver el proceso
)

# Ver respuesta
print(response['analysis'])
```

## Casos de Uso Implementados

### CASO 1: Análisis Causal Multidimensional

**Pregunta**: "¿Por qué bajó la conversión de downlights?"

**Qué hace el agente**:
1. Llama al modelo causal
2. Identifica 3 causas principales con % de impacto:
   - Bug móvil checkout (60%)
   - Competencia Google Ads (30%)
   - Stock limitado producto top (10%)
3. Para cada causa:
   - Detalles técnicos
   - Revenue afectado
   - Acciones recomendadas priorizadas
4. Genera plan de acción estructurado

**Output ejemplo**:
```
🔍 DIAGNÓSTICO
Las ventas de Downlights cayeron 15% (-2.8K€). Causas:

1. Bug móvil checkout (60% impacto)
   • Tiempo carga: 2.1s → 4.8s
   • Revenue perdido: 5.2K€

✅ PLAN DE ACCIÓN
HOY: Rollback deploy 3.2.1
ESTA SEMANA: Pausar keyword cara Google Ads

💰 IMPACTO: Recuperar 11.5K€/semana
```

### CASO 2: Sistema de Alertas Inteligentes

**Pregunta**: "¿Qué alertas críticas tengo ahora?"

**Qué hace el agente**:
1. Obtiene alertas del modelo de detección
2. Filtra por severidad
3. Contextualiza cada alerta:
   - Señales detectadas
   - Impacto estimado
   - Revenue en riesgo
4. Prioriza acciones

**Tipos de alertas**:
- **Críticas**: Requieren acción inmediata (conversión móvil -25%)
- **Altas**: Requieren acción pronto (CPA +31%)
- **Oportunidades**: Mejoras recomendadas (Email B2B infrautilizado)

### CASO 3: Simulador de Escenarios

**Pregunta**: "¿Qué pasa si optimizo el checkout móvil?"

**Qué hace el agente**:
1. Llama al simulador con escenario específico
2. Predice:
   - Inversión requerida (8K€)
   - Revenue incremental mes 1 (15.2K€)
   - ROI (26.9x)
   - Payback (0.5 meses)
3. Análisis de sensibilidad
4. Comparación con alternativas

### CASO 4: Comparación de Escenarios

**Pregunta**: "Compara: optimizar móvil vs aumentar Google Ads vs campaña B2B"

**Qué hace el agente**:
1. Simula los 3 escenarios
2. Calcula ROI de cada uno
3. Ordena por prioridad
4. Recomienda con justificación

**Output ejemplo**:
```
📊 COMPARACIÓN

1º Campaña B2B: ROI 29x (RECOMENDADO)
2º Optimizar móvil: ROI 26x
3º Google Ads: ROI 2.4x

💡 RECOMENDACIÓN:
Empieza por campaña B2B (quick win + alto impacto)
```

### CASO 5: Marketing Mix Modeling (MMM)

**Pregunta**: "Tengo 54K€ de presupuesto, ¿cómo lo distribuyo?"

**Qué hace el agente**:
1. Analiza contribución incremental de cada canal
2. Identifica saturación
3. Optimiza distribución
4. Predice impacto en revenue y ROAS

**Output**:
- Distribución actual vs recomendada
- Cambios específicos por canal ("Google Ads: -3K€, Email B2B: +3K€")
- Mejora esperada en ROAS global
- Revenue incremental estimado

### CASO 6: Consulta Ejecutiva General

**Pregunta**: "Dame un resumen ejecutivo de la situación"

**Qué hace el agente**:
1. Obtiene alertas críticas
2. Analiza principales variaciones
3. Identifica oportunidades
4. Genera top 3 acciones prioritarias

## Personalización para Producción

Para adaptar este prototipo a efectoLED real:

### 1. Conectar Datos Reales

Sustituir `config.py` con conexión a:
```python
# BigQuery
from google.cloud import bigquery

def get_real_data():
    client = bigquery.Client()
    query = """
    SELECT 
        category,
        SUM(revenue) as revenue,
        AVG(conversion_rate) as conversion
    FROM `efectoled.analytics.daily_metrics`
    WHERE date BETWEEN DATE_SUB(CURRENT_DATE(), INTERVAL 14 DAY) 
                  AND CURRENT_DATE()
    GROUP BY category, DATE_TRUNC(date, WEEK)
    """
    return client.query(query).to_dataframe()
```

### 2. Entrenar Modelos Reales

```python
# Ejemplo: Modelo Causal Real
import shap
from lightgbm import LGBMRegressor

class RealCausalModel:
    def __init__(self):
        self.model = LGBMRegressor()
        self.explainer = None
    
    def train(self, X, y):
        self.model.fit(X, y)
        self.explainer = shap.TreeExplainer(self.model)
    
    def explain(self, X_current):
        shap_values = self.explainer.shap_values(X_current)
        # Procesar SHAP values para identificar causas
        return self._format_causes(shap_values)
```

### 3. Integrar con Sistemas Existentes

```python
# Ejemplo: Integración con Salesforce
from simple_salesforce import Salesforce

def send_alert_to_salesforce(alert):
    sf = Salesforce(username='...', password='...', security_token='...')
    sf.Task.create({
        'Subject': alert['title'],
        'Description': alert['recommended_actions'],
        'Priority': 'High' if alert['severity'] == 'critical' else 'Normal'
    })
```

### 4. Automatizar Ejecución

```python
# Ejemplo: Airflow DAG
from airflow import DAG
from airflow.operators.python import PythonOperator

def run_daily_analysis():
    agent = create_agent()
    
    # Análisis automático diario
    response = agent.process_query(
        "Analiza las métricas de ayer vs semana pasada y envía alertas si hay desviaciones >10%"
    )
    
    # Enviar por email/Slack
    send_to_team(response['analysis'])

dag = DAG('efectoled_daily_analysis', schedule_interval='@daily')
task = PythonOperator(task_id='analyze', python_callable=run_daily_analysis, dag=dag)
```

## Costes Estimados

### Coste API Claude

- **Modelo**: Claude Sonnet 4 (`claude-sonnet-4-20250514`)
- **Coste aproximado por análisis**: $0.50 - $3.00
  - Análisis simple (1 tool call): ~$0.50
  - Análisis complejo (3-5 tool calls): ~$1.50
  - Análisis exhaustivo (comparaciones): ~$3.00

### Proyección mensual

- **Uso interactivo** (10 análisis/día): ~$450/mes
- **Alertas automáticas** (1 análisis/día): ~$45/mes
- **TOTAL estimado**: **$500-1,000/mes**

**ROI esperado**: Si un análisis identifica una acción que recupera 10K€, el ROI es >1000x

## Ventajas de esta Arquitectura

### ✅ Agente LLM vs Reglas Hardcoded

| Aspecto | Reglas Hardcoded | Agente LLM |
|---------|-----------------|------------|
| Lenguaje | Técnico ("SHAP value -0.3") | Natural ("Bug móvil causó 60% caída") |
| Adaptabilidad | Requiere código para nuevos casos | Se adapta a consultas no previstas |
| Contexto | Limitado | Integra múltiples fuentes |
| Explicaciones | Plantillas fijas | Personalizadas al usuario |
| Mantenimiento | Alto (cada cambio = código) | Bajo (actualizar prompts) |

### 🎯 Ventajas Específicas para efectoLED

1. **Explica en lenguaje de negocio**: El equipo no técnico entiende las recomendaciones
2. **Prioriza acciones**: No solo detecta problemas, dice qué hacer primero
3. **Cuantifica impactos**: Siempre estima revenue/ahorro en euros
4. **Integra contexto**: Considera competencia, estacionalidad, eventos
5. **Flexible**: Se adapta a nuevas preguntas sin código

## Próximos Pasos

### Corto Plazo (1-2 meses)
- [ ] Conectar con data warehouse real de efectoLED
- [ ] Entrenar primer modelo causal con datos reales
- [ ] Dashboard demo en Looker Studio
- [ ] Integración con email para alertas

### Medio Plazo (3-6 meses)
- [ ] Entrenar modelos de todos los casos de uso
- [ ] Integración con Salesforce para acciones automáticas
- [ ] Sistema de feedback (¿fue útil la recomendación?)
- [ ] Refinamiento continuo basado en uso

### Largo Plazo (6-12 meses)
- [ ] Automatización de acciones (emails, ajustes pujas)
- [ ] Expansión a más casos de uso (churn, pricing, etc.)
- [ ] Multi-agente (agentes especializados por área)
- [ ] API pública para integraciones

## Soporte

Para preguntas o issues:
- **Email**: [tu-email]
- **Documentación adicional**: Ver archivos `models.py` y `agent.py` (comentados)

## Licencia

Prototipo para demostración. Todos los derechos reservados.

---

**Desarrollado para efectoLED - Diciembre 2024**
