# 🎯 GUÍA PARA PRESENTAR EL PROTOTIPO A EFECTOLED

## Preparación Pre-Reunión

### 1. Verificar que todo funciona (15 minutos antes)

```bash
# Terminal 1: Ir al directorio
cd efectoled_agent

# Terminal 2: Configurar API key
export ANTHROPIC_API_KEY='tu-key-aqui'

# Terminal 3: Probar demo rápida
python quick_demo.py
```

Si funciona, estás listo. Si hay error, verifica:
- Python 3.8+ instalado
- anthropic package instalado (`pip install anthropic`)
- API key válida

### 2. Preparar pantalla compartida

- **Opción A** (recomendada): Compartir terminal con fuente grande
  - Aumentar tamaño fuente del terminal (CMD/CTRL + +)
  - Modo claro si es posible (mejor contraste)
  
- **Opción B**: Tener output pre-ejecutado en un Google Doc
  - Por si hay problemas de conexión/latencia API

---

## Estructura de la Presentación (30-40 mins)

### PARTE 1: Contexto y Problema (5 mins)

**Mensaje clave**: "Los dashboards muestran QUÉ pasa, pero no POR QUÉ ni QUÉ HACER"

**Script**:
```
Hoy tenéis dashboards que os dicen:
- "La conversión de downlights bajó 18%"
- "El CPA de Google Ads subió 31%"

Pero lo que realmente necesitáis es:
- ¿POR QUÉ bajó?
- ¿CUÁNTO dinero estáis perdiendo?
- ¿QUÉ hago HOY para solucionarlo?

Esto es lo que hace el Agente IA que os voy a mostrar.
```

### PARTE 2: Demo en Vivo - Caso de Uso 1 (10 mins)

**Ejecutar**: `python quick_demo.py`

**Mientras corre (10-30 segundos), explica**:
```
El agente está:
1. Llamando al modelo de análisis causal
2. Identificando las 3 causas principales
3. Cuantificando el impacto de cada una
4. Generando un plan de acción priorizado
```

**Cuando salga el resultado, destaca**:
- 🔍 **Las 3 causas** con % de impacto (60%, 30%, 10%)
- 💰 **Revenue en riesgo**: números concretos en euros
- ✅ **Plan de acción**: "HOY", "ESTA SEMANA" (priorizado)
- 📊 **Estimación de recuperación**: "11.5K€/semana"

**Mensaje clave**: "No es un dashboard más. Es un analista senior que trabaja 24/7"

### PARTE 3: Arquitectura Simplificada (5 mins)

**Mostrar en pizarra/diapositiva**:
```
TU CONSULTA
    ↓
AGENTE LLM (Claude)
    ↓
┌─────────┬─────────┬─────────┬─────────┐
│ Modelo  │ Modelo  │ Modelo  │ Modelo  │
│ Causal  │ Alertas │Simulador│  MMM    │
└─────────┴─────────┴─────────┴─────────┘
    ↓
RECOMENDACIÓN EN LENGUAJE NATURAL
```

**Script**:
```
Detrás hay 4 modelos ML especializados:
1. Causal: Identifica causas de variaciones
2. Alertas: Detecta problemas antes de que exploten
3. Simulador: Predice "qué pasa si..."
4. MMM: Optimiza distribución de presupuesto marketing

El Agente LLM (Claude) coordina todo y traduce 
resultados técnicos a lenguaje de negocio.
```

### PARTE 4: Otros Casos de Uso (10 mins)

**Opción A**: Ejecutar `python demo.py` y mostrar menú interactivo

**Opción B**: Mostrar outputs pre-generados de:
- Caso 2: Alertas activas
- Caso 4: Comparación de escenarios
- Caso 5: MMM - Optimización presupuesto

**Para cada caso, enfatiza**:
- **El problema real** que resuelve
- **El valor en €** que genera
- **Lo fácil que es usarlo** (pregunta en lenguaje natural)

### PARTE 5: Roadmap de Implementación (5 mins)

**Mostrar timeline clara**:
```
MES 1-2: Conexión datos + Modelo Causal
  → Primera alerta funcionando
  → Dashboard demo tangible

MES 3-4: MMM + Simulador
  → Optimizar presupuesto marketing
  → Simular decisiones antes de ejecutar

MES 5-6: Automatización
  → Alertas automáticas por email/Slack
  → Recomendaciones semanales automáticas
```

**Mensaje clave**: "Quick wins en 2 meses, valor completo en 6"

### PARTE 6: Q&A y Siguiente Paso (5 mins)

**Preguntas típicas y respuestas**:

**Q**: "¿Cuánto cuesta?"
**A**: "API Claude: ~1K€/mes. Desarrollo: 76-112K€ total proyecto (12 meses). ROI esperado: >10x en primer año"

**Q**: "¿Qué datos necesitáis?"
**A**: "Lo que ya tenéis: GA4, Google Ads, ERP, Salesforce. Los unificamos en BigQuery"

**Q**: "¿Cuánto tarda en estar listo?"
**A**: "Primer caso de uso (análisis causal) funcionando en 6-8 semanas"

**Q**: "¿Depende 100% de la API de Claude?"
**A**: "El agente sí, pero los modelos ML funcionan independiente. Si Claude falla, los modelos siguen dando resultados (solo menos 'bonitos')"

**Siguiente paso propuesto**:
```
1. Workshop técnico (2h):
   - Revisar datos disponibles en ERP/GA4
   - Validar viabilidad técnica
   - Refinar alcance exacto

2. Dashboard "cartón-piedra" (2 semanas):
   - Looker Studio con datos simulados
   - Muestra cómo se vería en producción
   - Sin desarrollo pesado aún

3. Decisión Go/No-Go basada en demo tangible
```

---

## Tips para la Demo

### ✅ DO's

1. **Enfatiza el valor en €**: Siempre traduce a dinero
   - "Esto recupera 8K€/semana" es mejor que "mejora conversión 12%"

2. **Usa ejemplos de su negocio**: Downlights, Tiras LED, clientes B2B
   - No digas "productos", di "downlights"
   - No digas "usuarios", di "electricistas profesionales"

3. **Muestra el proceso**: Dejar que vean cómo el agente "piensa"
   - Modo verbose es tu amigo
   - Explica qué está haciendo mientras esperas

4. **Conecta con sus dolores**: Usa el feedback que te dieron
   - "Queríais análisis causal multidimensional → aquí está"
   - "Queríais alertas contextuales → mira esto"

5. **Sé honesto sobre limitaciones**:
   - "Esto es un prototipo con datos simulados"
   - "En producción necesitamos 2 meses para entrenar modelos reales"
   - "Los modelos tienen incertidumbre, por eso siempre damos intervalos"

### ❌ DON'Ts

1. **No te vayas por las ramas técnicas**
   - No expliques SHAP values salvo que pregunten
   - No hables de Bayesian inference
   - Céntrate en el valor de negocio

2. **No hagas promesas imposibles**
   - No digas "100% precisión"
   - No prometas "decisiones 100% autónomas"
   - Sé realista con timings

3. **No menosprecies su setup actual**
   - Su proyecto de dashboards está bien
   - Esto es la "siguiente capa" encima

4. **No compares con chatbots tontos**
   - No es "un ChatGPT para efectoLED"
   - Es un "analista senior con acceso a modelos ML"

---

## Script de Cierre Potente

```
Para resumir:

Hoy habéis visto un agente que:
✅ Identifica causas raíz en minutos (no horas de análisis manual)
✅ Cuantifica impactos en euros (no solo %)
✅ Prioriza acciones (qué hacer HOY vs esta semana)
✅ Simula decisiones antes de ejecutar (sin riesgo)
✅ Optimiza vuestros 50K€/mes de marketing (MMM)

Todo en lenguaje natural. Sin dashboards complicados.

El ROI es claro:
- Si una sola recomendación recupera 10K€ → El agente se paga solo
- Si optimizáis marketing un 15% → Son 90K€/año extra

Próximo paso: Workshop técnico para validar viabilidad con vuestros datos reales.

¿Cuándo os viene bien?
```

---

## Checklist Pre-Demo

- [ ] API key configurada y probada
- [ ] `quick_demo.py` ejecutado con éxito
- [ ] Terminal con fuente grande
- [ ] Backup: output pre-generado en Google Doc
- [ ] Pizarra/pantalla para dibujar arquitectura
- [ ] Timeline de implementación impreso/visible
- [ ] Presupuesto estimado a mano
- [ ] Calendario para agendar workshop técnico

---

## Plan B si Falla la Demo en Vivo

### Si la API es lenta/falla:

1. **Tener pre-generados 2-3 outputs** en Google Doc
2. **Explicar**: "Por latencia de API lo muestro pre-generado, pero en producción es tiempo real"
3. **Enfatizar**: "Lo importante es la calidad del análisis, no la velocidad"

### Si hay errores de código:

1. **Tener video grabado** de 2 minutos mostrando funcionamiento
2. **Pivot al valor**: "Demos técnicos son complicados en vivo, pero lo clave es el concepto"
3. **Ofrecer**: "Os envío acceso al prototipo funcionando para que lo probéis vosotros"

---

## Materiales Post-Reunión

Enviar el mismo día:

1. **Resumen ejecutivo** (1 página):
   - Qué vieron hoy
   - Valor esperado
   - Próximos pasos

2. **Caso de uso detallado** (PDF):
   - Ejemplo de análisis causal completo
   - Capturas del output del agente
   - Explicación de cada sección

3. **Propuesta de workshop técnico**:
   - Agenda (2h)
   - Participantes necesarios (IT, Marketing, Ecommerce Manager)
   - Objetivos del workshop

4. **Calendario sugerido**:
   - Semana 1: Workshop técnico
   - Semana 2-3: Dashboard demo
   - Semana 4: Decisión Go/No-Go

---

**¡Mucha suerte con la demo! 🚀**

Esto es punta de lanza. Si lo ejecutas bien, efectoLED verá valor inmediato.

Recuerda: No vendes tecnología, vendes **recuperar 100K€+ al año mediante decisiones más inteligentes**.
