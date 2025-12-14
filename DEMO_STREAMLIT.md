# 🎨 DEMO VISUAL CON STREAMLIT - Guía Rápida

## Por Qué Streamlit Para la Demo

✅ **Visual e Interactivo**: Gráficos, métricas, cards de colores
✅ **Profesional**: Se ve como una app real, no terminal
✅ **Sin código frontend**: 0 líneas de HTML/CSS/JS necesarias
✅ **Impacto inmediato**: El cliente lo ve y dice "quiero esto"
✅ **Demos en vivo**: Cambiar parámetros y ver resultados al instante

## Instalación Express (2 minutos)

```bash
# 1. Instalar dependencias
pip install streamlit plotly anthropic

# 2. Configurar API key
export ANTHROPIC_API_KEY='tu-key-aqui'

# 3. Ejecutar app
streamlit run app.py
```

Se abrirá automáticamente en tu navegador en `http://localhost:8501`

## 🎯 Casos de Uso en la Interfaz

### 1. 🔍 Análisis Causal
- **Visual**: Gráfico de barras horizontal con % de impacto
- **Interactive**: Expandir/colapsar cada causa
- **Cards**: Acciones recomendadas en tarjetas de colores
- **Métricas**: Delta con flechas (↑↓)

**Screenshot mental**:
```
┌─────────────────────────────────────┐
│ Conversión Actual: 2.6% ↓-0.6pp     │
│ Conversión Anterior: 3.2%           │
│ Variación: -18.75%                  │
│ Confianza: 85%                      │
└─────────────────────────────────────┘

[Gráfico barras horizontal]
🔴 Bug móvil checkout     ████████████ 60%
🟠 Competencia Google Ads ██████ 30%
🟡 Stock limitado ref-245 ███ 10%

📋 Causa 1: Bug móvil checkout (60% impacto)
  ├─ Tiempo carga: 2.1s → 4.8s
  ├─ Revenue perdido: 5.2K€
  └─ Acción urgente: Rollback deploy 3.2.1
```

### 2. 🚨 Alertas Activas
- **Color coding**: Rojo (críticas), Naranja (altas), Verde (oportunidades)
- **Métricas destacadas**: Revenue en riesgo en grande
- **Progress bars**: Estado de cada alerta
- **Expandibles**: Click para ver detalles

### 3. 🎯 Simulador de Escenarios
- **Dropdowns**: Seleccionar escenario a simular
- **Gráfico intervalo confianza**: Pesimista | Esperado | Optimista
- **Métricas ROI**: Destacadas en verde si >10x
- **Comparación visual**: Barras lado a lado

### 4. 💰 Marketing Mix Model
- **Tabs**: Atribución Actual | Optimizar Presupuesto
- **Gráfico contribución**: Stacked bars por canal
- **Tabla interactiva**: Expandir para ver detalles
- **Recomendaciones**: Cards con ↑↓ según cambio

### 5. 💬 Consulta Libre
- **Text area grande**: Escribir pregunta en natural
- **Ejemplos clickeables**: Cargar query pre-hecha
- **Streaming visual**: "🔍 Analizando..." → "🧠 Procesando..." → "✅ Listo"
- **Markdown rich**: Bold, listas, emojis en respuesta

## 🎬 Flujo de Demo Recomendado (15 mins)

### Minuto 1-2: Impacto Visual
```bash
streamlit run app.py
```
1. Cliente ve la interfaz → WOW inmediato
2. Sidebar muestra métricas en tiempo real
3. Logo de efectoLED prominente

### Minuto 3-7: Caso Estrella (Análisis Causal)
1. Seleccionar "🔍 Análisis Causal" en sidebar
2. Click "🚀 Analizar Causas"
3. **Progress bar animado**: 
   - "📊 Cargando datos..." (1s)
   - "🔍 Identificando patrones..." (1s)
   - "🧠 Modelo causal procesando..." (2s)
   - "💬 Generando recomendaciones..." (1s)
4. **Resultados aparecen**:
   - Métricas con deltas
   - Gráfico de causas
   - Cards expandibles
   - Narrativa del agente

**MIENTRAS CORRE (crucial)**:
> "Ahora el agente está llamando al modelo causal, identificando 
> las 3 causas principales, cuantificando el impacto de cada una,
> y generando un plan de acción priorizado. Todo esto en 30 segundos."

### Minuto 8-10: Alertas (Quick Win)
1. Cambiar a "🚨 Alertas Activas"
2. Click "🔄 Cargar Alertas"
3. Ver 4 alertas con colores:
   - 🔴 Crítica: Conversión móvil -25%
   - 🟠 Alta: CPA Google Ads +31%
   - 💡 Oportunidad: Email B2B infrautilizado

**MENSAJE**:
> "Esto detecta problemas antes de que exploten. 
> Hoy están perdiendo 5.2K€ por el bug móvil. La alerta 
> os habría avisado hace 2 días."

### Minuto 11-13: Simulador (Decisiones)
1. Cambiar a "🎯 Simulador"
2. Seleccionar "Optimizar Checkout Móvil"
3. Click "📊 Simular"
4. Ver gráfico de intervalo de confianza
5. **ROI 26.9x destacado en grande**

**MENSAJE**:
> "Antes de gastar 8K€, sabéis que recuperaréis 182K€ 
> en el primer año. Podéis simular cualquier decisión."

### Minuto 14-15: MMM (Optimización)
1. Cambiar a "💰 Marketing Mix Model"
2. Tab "Optimizar Presupuesto"
3. Input: 54.000€
4. Click "🎯 Optimizar"
5. Ver tabla con recomendaciones:
   - Google Ads: 22K€ → 19K€ (-3K€)
   - Email B2B: 3K€ → 6K€ (+3K€)

**MENSAJE**:
> "Sin aumentar presupuesto, solo redistribuyendo, 
> podéis generar 38K€ extra al mes. ROAS sube de 4.1x a 5.2x."

## 💡 Tips Para Maximizar Impacto

### Preparación Pre-Demo

1. **Pantalla compartida en 1080p mínimo**
   - Streamlit se ve MAL en resoluciones bajas
   - Aumentar zoom del navegador si es necesario

2. **Probar conexión API antes**
   ```bash
   # Test rápido
   python quick_demo.py
   ```
   Si funciona → La demo Streamlit funcionará

3. **Tener backup**:
   - Screenshots de cada sección
   - Video grabado de 2 minutos

### Durante la Demo

1. **NO LEER CÓDIGO**: Solo mostrar interfaz
2. **DEJAR QUE CARGUE**: Los progress bars son parte del show
3. **EXPANDIR CAUSAS**: Click en cada una para mostrar detalles
4. **SEÑALAR NÚMEROS EN €**: "Mira, 5.2K€ perdidos aquí"
5. **CAMBIAR PARÁMETROS**: Selecciona otra categoría para mostrar flexibilidad

### Frases Killer

- "**Esto que acabáis de ver en 30 segundos, normalmente os tomaría 4 horas de análisis manual**"
- "**El agente acaba de llamar a 3 modelos ML diferentes y sintetizó los resultados en lenguaje natural**"
- "**Cada análisis cuesta ~2€ de API. Si recuperáis 10K€, el ROI es 5000x**"
- "**Podéis hacer esto 100 veces al día. El agente no se cansa**"

## 🚨 Solución de Problemas Visuales

### Streamlit no carga
```bash
# Verificar puerto 8501 libre
lsof -i :8501

# Usar otro puerto
streamlit run app.py --server.port 8502
```

### Gráficos no se ven
```bash
# Reinstalar plotly
pip install --upgrade plotly
```

### CSS roto / Sin colores
- Refrescar navegador (Cmd+Shift+R / Ctrl+Shift+R)
- Limpiar caché de Streamlit:
  ```bash
  rm -rf ~/.streamlit/cache
  ```

### Demo muy lenta
- Normal la primera vez
- Segunda llamada será más rápida (caché de Claude)
- Para impresionar: pre-calentar llamando una vez antes

## 📊 Comparación: Terminal vs Streamlit

| Aspecto | Terminal | Streamlit |
|---------|----------|-----------|
| **Impacto visual** | 3/10 | 10/10 |
| **Comprensión** | Requiere leer | Inmediato |
| **Interactividad** | 0 | Alta |
| **Profesionalismo** | Técnico | Producto |
| **WOW factor** | Bajo | Alto |
| **Probabilidad cierre** | 40% | 85% |

## 🎯 Objetivo de la Demo

**NO es** enseñar tecnología
**SÍ es** vender la visión de:

> "Imagina tener un analista senior IA que trabaja 24/7, 
> identifica problemas antes que tú, cuantifica cada decisión,
> y te dice exactamente qué hacer. Por 1K€/mes."

**Streamlit hace esto tangible.**

## 🚀 Siguiente Nivel

Si quieren WOW máximo:

1. **Deployment en cloud** (5 mins):
   ```bash
   # Streamlit Cloud (gratis)
   # 1. Push a GitHub
   # 2. Conectar en share.streamlit.io
   # 3. Compartir URL pública
   ```

2. **Custom domain**: `demo.albertogarcia.ai/efectoled`

3. **Datos reales simulados de efectoLED**:
   - Usar sus categorías exactas
   - Sus rangos de revenue reales
   - Sus canales de marketing

## 📝 Checklist Pre-Demo

- [ ] `pip install streamlit plotly anthropic`
- [ ] `export ANTHROPIC_API_KEY='...'`
- [ ] Ejecutar `streamlit run app.py` localmente
- [ ] Probar los 5 casos de uso
- [ ] Aumentar zoom del navegador si necesario
- [ ] Cerrar tabs innecesarias del navegador
- [ ] Preparar pantalla compartida
- [ ] Screenshots de backup
- [ ] Practicar el flujo 1-2 veces

---

**¡La demo Streamlit es tu arma secreta! Úsala bien y efectoLED firma. 🚀**
