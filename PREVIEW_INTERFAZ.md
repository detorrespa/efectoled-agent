# 📸 Preview de la Interfaz Streamlit

## Vista Principal - Análisis Causal

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│  🤖 Agente IA efectoLED                                                      │
│  ─────────────────────                                                       │
│                                                                              │
│  🔍 Análisis Causal                        ┌─────────────────────────────┐  │
│  🚨 Alertas Activas                        │   efectoLED                 │  │
│  🎯 Simulador de Escenarios                │   Iluminación LED Online    │  │
│  💰 Marketing Mix Model                    └─────────────────────────────┘  │
│  💬 Consulta Libre                                                           │
│                                            📊 Contexto Actual               │
│                                            ───────────────────               │
│                                            Revenue Semanal    Conversión    │
│                                            42.3K€ ↓-8.2%     2.8% ↓-0.4pp   │
│                                                                              │
│                                            Última actualización:             │
│                                            13/12/2024 12:30                  │
│                                            Datos: Semana actual vs anterior  │
│                                            Modelo: Claude Sonnet 4           │
└──────────────────────────────────────────────────────────────────────────────┘
```

## Análisis Causal - Resultados

```
┌──────────────────────────────────────────────────────────────────────────────┐
│  🔍 Análisis Causal Multidimensional                                         │
│  Identifica las causas raíz de variaciones en métricas clave                 │
│  ──────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  Métrica: [Conversión ▼]        Categoría: [Downlights ▼]                   │
│                                                                              │
│  ┌────────────────────────────────────────────────────────────────────────┐ │
│  │            🚀 Analizar Causas                                          │ │
│  └────────────────────────────────────────────────────────────────────────┘ │
│                                                                              │
│  ✅ Análisis completado exitosamente                                         │
│                                                                              │
│  📊 Variación Detectada                                                      │
│  ──────────────────────                                                      │
│  ┌──────────────┬──────────────┬──────────────┬──────────────┐              │
│  │ Valor Actual │ Valor Anterior│ Variación   │ Confianza    │              │
│  │    2.6%      │     3.2%      │   -18.8%    │     85%      │              │
│  │              │               │  ↓-0.6pp    │              │              │
│  └──────────────┴──────────────┴──────────────┴──────────────┘              │
│                                                                              │
│  🎯 Causas Identificadas                                                     │
│  ─────────────────────                                                       │
│                                                                              │
│  [Gráfico de barras horizontal]                                             │
│  Bug móvil checkout          ████████████████████  60%                       │
│  Competencia Google Ads      ██████████  30%                                 │
│  Stock limitado ref-245      █████  10%                                      │
│                                                                              │
│  ▼ 🔴 Causa 1: Bug móvil checkout (60% impacto)                             │
│    ┌────────────────────────────────────────────────────────────────────┐   │
│    │ Severidad: CRITICAL                                                │   │
│    │                                                                    │   │
│    │ Detalles:                                                          │   │
│    │ • Tiempo de carga checkout: 2.1s → 4.8s (+129%)                   │   │
│    │ • Deploy correlacionado: versión 3.2.1 (martes)                   │   │
│    │ • Bounce rate móvil: 42% → 61%                                    │   │
│    │ • Revenue perdido: 5,200€                                         │   │
│    │                                                                    │   │
│    │ Acciones Recomendadas:                                             │   │
│    │ ┌──────────────────────────────────────────────────────────────┐  │   │
│    │ │ 🔥 Rollback deploy versión 3.2.1                            │  │   │
│    │ │ • Responsable: IT/DevOps                                    │  │   │
│    │ │ • Tiempo estimado: 1-2 horas                                │  │   │
│    │ │ • Impacto: Recuperar 60% conversión móvil en 24h            │  │   │
│    │ └──────────────────────────────────────────────────────────────┘  │   │
│    └────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  ▶ 🟠 Causa 2: Competencia Google Ads (30% impacto)                         │
│  ▶ 🟡 Causa 3: Stock limitado ref-245 (10% impacto)                         │
│                                                                              │
│  💬 Análisis del Agente IA                                                   │
│  ────────────────────────                                                    │
│  🔍 DIAGNÓSTICO                                                              │
│                                                                              │
│  Las ventas de Downlights cayeron 15% (-2.8K€). He identificado 3 causas:   │
│                                                                              │
│  1. **Bug móvil checkout** (60% del impacto)                                │
│     Detecté que el tiempo de carga del checkout en móvil subió de 2.1s a    │
│     4.8s hace 3 días. Esto provocó que el bounce rate móvil pasara del 42%  │
│     al 61%. Como el 58% del tráfico de downlights viene de móvil, esto      │
│     tiene un impacto enorme.                                                 │
│                                                                              │
│     📊 Datos específicos:                                                    │
│     - Conversión móvil: 2.8% → 1.6% (-43%)                                  │
│     - Revenue perdido estimado: 8.2K€ en 3 días                             │
│                                                                              │
│     ✅ ACCIÓN URGENTE:                                                       │
│     Contactar a IT ahora mismo para rollback del deploy del martes.         │
│                                                                              │
│  💰 Impacto Económico                                                        │
│  ─────────────────                                                           │
│  ┌──────────────────────┬──────────────────────┐                            │
│  │ Revenue Afectado     │ Recuperación Estimada│                            │
│  │     2,790€           │      2,149€          │                            │
│  │                      │ siguiendo plan acción│                            │
│  └──────────────────────┴──────────────────────┘                            │
└──────────────────────────────────────────────────────────────────────────────┘
```

## Alertas Activas - Vista

```
┌──────────────────────────────────────────────────────────────────────────────┐
│  🚨 Sistema de Alertas Inteligentes                                          │
│  Monitorización continua con detección automática de anomalías              │
│  ──────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  Filtrar: [Todas ▼]                                                          │
│                                                                              │
│  ┌────────────────────────────────────────────────────────────────────────┐ │
│  │            🔄 Cargar Alertas Activas                                   │ │
│  └────────────────────────────────────────────────────────────────────────┘ │
│                                                                              │
│  📊 Resumen de Alertas                                                       │
│  ──────────────────────                                                      │
│  ┌──────────────┬──────────────┬──────────────┬──────────────┐              │
│  │ Total Alertas│  Críticas    │    Altas     │Revenue Riesgo│              │
│  │      4       │      2       │      1       │    169K€     │              │
│  └──────────────┴──────────────┴──────────────┴──────────────┘              │
│                                                                              │
│  🔔 Alertas Detalladas                                                       │
│  ────────────────────                                                        │
│                                                                              │
│  ┌────────────────────────────────────────────────────────────────────────┐ │
│  │ 🔴 Conversión móvil downlights -25% en 3 días (CRITICAL)              │ │
│  │ ▼                                                                      │ │
│  │ ┌──────────────────┬──────────────────┬──────────────────┐            │ │
│  │ │ Valor Anterior   │ Valor Actual     │ Cambio           │            │ │
│  │ │      2.8         │      2.1         │    -25.0%        │            │ │
│  │ └──────────────────┴──────────────────┴──────────────────┘            │ │
│  │                                                                        │ │
│  │ 🔍 Señales Detectadas:                                                 │ │
│  │ • Tiempo carga checkout móvil: 2.1s → 4.8s (+129%)                    │ │
│  │ • Bounce rate móvil: 42% → 61% (+19pp)                                │ │
│  │ • Deploy versión 3.2.1 correlacionado (martes 10:00)                  │ │
│  │ • 58% tráfico downlights viene de móvil                               │ │
│  │                                                                        │ │
│  │ 💰 Impacto Estimado:                                                   │ │
│  │ Revenue perdido 3 días: 5,200€   Revenue riesgo 7 días: 12,500€       │ │
│  │                                                                        │ │
│  │ ✅ Acciones Recomendadas:                                              │ │
│  │ ┌──────────────────────────────────────────────────────────────────┐  │ │
│  │ │ Prioridad 1: Rollback deploy 3.2.1                              │  │ │
│  │ │ • Urgencia: inmediata                                            │  │ │
│  │ │ • Responsable: IT                                                │  │ │
│  │ └──────────────────────────────────────────────────────────────────┘  │ │
│  └────────────────────────────────────────────────────────────────────────┘ │
│                                                                              │
│  ▶ 🟠 CPA Google Ads +31% vs objetivo (HIGH)                                │
│  ▶ 💡 85 clientes B2B en riesgo churn - 157K€ (OPPORTUNITY)                 │
│  ▶ 💡 Email B2B ROAS 18x pero solo 15% saturación (OPPORTUNITY)             │
└──────────────────────────────────────────────────────────────────────────────┘
```

## Simulador de Escenarios

```
┌──────────────────────────────────────────────────────────────────────────────┐
│  🎯 Simulador de Escenarios                                                  │
│  Predice el impacto de decisiones antes de ejecutar ("What-if analysis")    │
│  ──────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  Escenario: [🚀 Optimizar Checkout Móvil ▼]                                 │
│                                                                              │
│  ℹ️ Descripción: Reducir tiempo de carga de 4.8s a 1.5s                     │
│                                                                              │
│  ┌──────────────────────┬──────────────────────┐                            │
│  │ Inversión Requerida  │ Tiempo Implementación│                            │
│  │      8,000€          │      3 semanas       │                            │
│  └──────────────────────┴──────────────────────┘                            │
│                                                                              │
│  ┌────────────────────────────────────────────────────────────────────────┐ │
│  │            📊 Simular Escenario                                        │ │
│  └────────────────────────────────────────────────────────────────────────┘ │
│                                                                              │
│  ✅ Simulación completada                                                    │
│                                                                              │
│  📊 Resultados de la Simulación                                              │
│  ─────────────────────────────────                                           │
│  ┌──────────────┬──────────────┬──────────────┬──────────────┐              │
│  │ Revenue Mes 1│ Revenue Año 1│     ROI      │   Payback    │              │
│  │   15,200€    │   182,000€   │    26.9x     │  0.5 meses   │              │
│  └──────────────┴──────────────┴──────────────┴──────────────┘              │
│                                                                              │
│  📈 Intervalo de Confianza (80%)                                             │
│  ──────────────────────────────────                                          │
│                                                                              │
│  [Gráfico de barras]                                                         │
│  Pesimista        ████████  14,500€                                          │
│  Esperado         ██████████  15,200€                                        │
│  Optimista        ████████████  21,800€                                      │
│                                                                              │
│  ✅ Supuestos del Modelo           ⚠️ Riesgos Identificados                 │
│  ─────────────────────────         ─────────────────────────                 │
│  • Basado en 24 meses histórico   • Cambios algoritmo Google                │
│  • Benchmark sector ecommerce     • Nuevas campañas competencia             │
│  • Control por estacionalidad     • Variaciones estacionales                │
└──────────────────────────────────────────────────────────────────────────────┘
```

## Colores y Estilo

- **Alertas Críticas**: Fondo rojo claro (#ffe6e6), borde rojo (#d32f2f)
- **Alertas Altas**: Fondo naranja claro (#fff3e0), borde naranja (#f57c00)
- **Oportunidades**: Fondo verde claro (#e8f5e9), borde verde (#388e3c)
- **Acciones**: Fondo azul claro (#e8f4f8), borde azul (#1F4E78)
- **Métricas**: Gris claro (#f0f2f6) con borde redondeado

## Animaciones

- **Progress bars**: Transición suave 0-100%
- **Expanding cards**: Animación de apertura/cierre
- **Hover effects**: Cambio de color al pasar mouse
- **Loading**: Spinner animado mientras procesa

---

**La interfaz es completamente funcional. Ejecuta `streamlit run app.py` para verla en vivo.**
