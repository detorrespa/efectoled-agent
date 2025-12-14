# 🚀 Instalación Rápida - Agente IA efectoLED

## Requisitos Previos

- **Python 3.8 o superior**
- **API Key de Anthropic** (para Claude)
  - Obtener en: https://console.anthropic.com/
  - Plan mínimo: Pay-as-you-go

## Instalación Paso a Paso

### 1. Descomprimir archivos

Si descargaste el `.tar.gz`:
```bash
tar -xzf efectoled_agent.tar.gz
cd efectoled_agent
```

O si tienes los archivos sueltos:
```bash
cd efectoled_agent
```

### 2. Instalar dependencias

```bash
# Opción A: pip normal
pip install -r requirements.txt

# Opción B: entorno virtual (recomendado)
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configurar API Key

```bash
# Linux/Mac
export ANTHROPIC_API_KEY='sk-ant-api03-tu-key-aqui'

# Windows PowerShell
$env:ANTHROPIC_API_KEY='sk-ant-api03-tu-key-aqui'

# Windows CMD
set ANTHROPIC_API_KEY=sk-ant-api03-tu-key-aqui
```

**IMPORTANTE**: Guarda la key de forma permanente para no tener que exportarla cada vez:

**Linux/Mac** - Añadir a `~/.bashrc` o `~/.zshrc`:
```bash
echo 'export ANTHROPIC_API_KEY="sk-ant-api03-tu-key-aqui"' >> ~/.bashrc
source ~/.bashrc
```

**Windows** - Variables de entorno del sistema:
1. Panel de Control → Sistema → Configuración avanzada del sistema
2. Variables de entorno → Nueva variable de usuario
3. Nombre: `ANTHROPIC_API_KEY`
4. Valor: `sk-ant-api03-tu-key-aqui`

### 4. Probar instalación

```bash
# Demo rápida (30 segundos)
python quick_demo.py

# Si funciona, verás el análisis completo generado por el agente
```

Si ves un análisis detallado del tipo:
```
🔍 DIAGNÓSTICO
Las ventas de Downlights cayeron 15%...
```

¡Funciona! ✅

## Estructura de Archivos

```
efectoled_agent/
├── README.md                    # Documentación completa
├── INSTALACION.md              # Este archivo
├── RESUMEN_EJECUTIVO.md        # Para enviar a cliente
├── GUIA_PRESENTACION.md        # Para presentar demo
├── requirements.txt            # Dependencias Python
├── config.py                   # Configuración y datos simulados
├── models.py                   # Modelos ML (causal, alertas, simulador, MMM)
├── agent.py                    # Agente LLM orquestador
├── quick_demo.py              # Demo rápida (1 caso de uso)
└── demo.py                     # Demo interactiva completa
```

## Ejecutar Demos

### Demo Rápida (Recomendada para primera vez)

```bash
python quick_demo.py
```

Duración: ~30 segundos
Muestra: Análisis causal completo de caída de conversión

### Demo Interactiva (Todos los casos de uso)

```bash
python demo.py
```

Menú interactivo con 6 casos de uso:
1. Análisis causal
2. Alertas activas
3. Simulador de escenarios
4. Comparación de opciones
5. Optimización presupuesto marketing
6. Consulta ejecutiva

## Solución de Problemas

### Error: "ANTHROPIC_API_KEY no configurada"

```bash
# Verificar que la variable existe
echo $ANTHROPIC_API_KEY  # Linux/Mac
echo %ANTHROPIC_API_KEY%  # Windows CMD
$env:ANTHROPIC_API_KEY    # Windows PowerShell

# Si no aparece nada, configurar de nuevo (ver paso 3)
```

### Error: "No module named 'anthropic'"

```bash
# Reinstalar dependencias
pip install --upgrade anthropic
```

### Error: "API key invalid"

- Verificar que la key empieza con `sk-ant-api03-`
- Verificar que no tiene espacios al principio/final
- Generar nueva key en https://console.anthropic.com/

### Demo muy lenta (>60 segundos)

- Normal la primera vez (modelo carga)
- Si persiste: verificar conexión internet
- Alternativa: ejecutar modo verbose para ver progreso
  ```python
  agent.process_query(query, verbose=True)
  ```

### Warnings de pandas/numpy

- Se pueden ignorar si la demo funciona
- Para eliminarlos:
  ```bash
  pip install --upgrade numpy pandas
  ```

## Próximos Pasos

1. ✅ Ejecutar `quick_demo.py` para verificar
2. ✅ Leer `README.md` para entender arquitectura
3. ✅ Ejecutar `demo.py` para ver todos los casos de uso
4. ✅ Revisar `GUIA_PRESENTACION.md` para preparar demo a cliente
5. ✅ Enviar `RESUMEN_EJECUTIVO.md` al cliente antes de la reunión

## Uso en Producción

Para adaptar a datos reales de efectoLED:

1. **Conectar BigQuery**: Sustituir `config.py` con queries reales
2. **Entrenar modelos**: Sustituir modelos simulados en `models.py`
3. **Integrar sistemas**: Añadir conexiones a Salesforce, Google Ads, etc.
4. **Automatizar**: Configurar Airflow/cron para ejecución periódica

Ver sección "Personalización para Producción" en `README.md`.

## Soporte

- **Documentación completa**: Ver `README.md`
- **Guía de presentación**: Ver `GUIA_PRESENTACION.md`
- **Casos de uso**: Ver código comentado en `models.py` y `agent.py`

---

**Desarrollado para efectoLED - Diciembre 2024**

¿Problemas con la instalación? Revisa la sección de Solución de Problemas arriba.
