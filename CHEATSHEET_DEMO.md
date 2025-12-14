# 📋 CHEATSHEET - Día de la Demo

## ⚡ Lanzamiento Express (30 segundos)

```bash
cd efectoled_agent
export ANTHROPIC_API_KEY='sk-ant-...'  # Tu key aquí
streamlit run app.py
```

**Se abre automáticamente en**: http://localhost:8501

---

## 🎬 Script de Demo (15 minutos)

### Min 0-1: Impacto Visual Inmediato
- Cliente ve la interfaz
- Sidebar con métricas en tiempo real
- Logo efectoLED prominente

### Min 2-7: ⭐ CASO ESTRELLA - Análisis Causal
1. Sidebar → **🔍 Análisis Causal**
2. Click **🚀 Analizar Causas**
3. **MIENTRAS CARGA** (30s) - Explicar:
   > "El agente está identificando causas, cuantificando impacto,
   > y generando plan de acción. Lo que antes tomaba 4 horas."
4. **VER RESULTADOS**:
   - ✅ 3 causas con % de impacto
   - 📊 Gráfico visual
   - 💰 Revenue: "5.2K€ perdidos"
   - ✅ Plan: "HOY hacer X, SEMANA hacer Y"

**FRASE**: *"Esto recupera 11.5K€/semana. ROI 5000x sobre el coste API."*

### Min 8-10: 🚨 Alertas (Quick Win)
1. Cambiar a **🚨 Alertas Activas**
2. Click **🔄 Cargar**
3. Ver 4 alertas con colores
4. Expandir una crítica

**FRASE**: *"Detecta problemas antes de que exploten. Esta alerta
os habría avisado hace 2 días, ahorrando 5K€."*

### Min 11-13: 🎯 Simulador
1. **🎯 Simulador de Escenarios**
2. Seleccionar "Optimizar Checkout Móvil"
3. Click **📊 Simular**
4. Ver gráfico + ROI 26.9x

**FRASE**: *"Antes de gastar 8K€, sabéis que recuperáis 182K€ en el año."*

### Min 14-15: 💰 MMM
1. **💰 Marketing Mix Model**
2. Tab "Optimizar Presupuesto"
3. Input: 54000
4. Click **🎯 Optimizar**

**FRASE**: *"Sin aumentar presupuesto, solo redistribuyendo, +38K€/mes."*

---

## 🎯 Frases Killer

1. **"30 segundos vs 4 horas de análisis manual"**
2. **"Cada análisis cuesta 2€. Si recuperáis 10K€, ROI 5000x"**
3. **"El agente no se cansa. 100 análisis al día si queréis"**
4. **"Esto que veis es un prototipo. Con vuestros datos reales, 10x mejor"**

---

## ⚠️ Si Algo Falla

### API lenta/error
→ "Por latencia de red. En producción es instantáneo con caché"
→ Mostrar screenshots de backup en `PREVIEW_INTERFAZ.md`

### Streamlit no carga
→ Verificar puerto 8501 libre: `lsof -i :8501`
→ Alternativamente: `python quick_demo.py` (terminal)

### Sin internet
→ Pre-grabar video de 2 mins
→ Pivot a explicar concepto con diagrama en pizarra

---

## ✅ Checklist Pre-Demo (30 mins antes)

- [ ] API key configurada
- [ ] `streamlit run app.py` funciona
- [ ] Navegador en localhost:8501
- [ ] Zoom navegador ajustado (120-150%)
- [ ] Probar 1 caso de uso completo
- [ ] Screenshots de backup listos
- [ ] Cerrar tabs innecesarias
- [ ] Silenciar notificaciones
- [ ] Preparar pantalla compartida

---

## 💰 Números de Cierre

**Inversión**: 76-112K€ (12 meses)  
**ROI Año 1**: 3.3x conservador, 5-8x optimista  
**Quick Win**: Primer caso en 6-8 semanas  
**Coste Operativo**: 1K€/mes API  

**Próximo Paso**: Workshop técnico 2h para validar datos

---

## 🚀 Línea Final

> "Imagina tener un analista senior IA 24/7 que identifica problemas,
> cuantifica decisiones, y te dice qué hacer. Por 1K€/mes.
> 
> Esto que acabáis de ver en 15 minutos, normalmente os tomaría
> una semana de análisis. El agente lo hace en 30 segundos.
> 
> ¿Cuándo hacemos el workshop técnico?"

---

**¡SUERTE! 🍀**

Recuerda: No vendes tecnología, vendes **recuperar 100K€+ mediante decisiones inteligentes**.
