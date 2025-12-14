"""
Interfaz Streamlit para el Agente IA de efectoLED

Ejecutar con: streamlit run app.py
"""

import streamlit as st
import json
import time
from datetime import datetime
import plotly.graph_objects as go
import plotly.express as px
from agent import create_agent
from models import (
    CausalAnalysisModel,
    AlertsModel,
    ScenarioSimulator,
    MarketingMixModel
)

# Configuración de página
st.set_page_config(
    page_title="Agente IA efectoLED",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1F4E78;
        margin-bottom: 0;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        margin-top: 0;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .action-card {
        background-color: #e8f4f8;
        padding: 15px;
        border-left: 4px solid #1F4E78;
        margin: 10px 0;
        border-radius: 5px;
    }
    .cause-card {
        background-color: #fff;
        padding: 15px;
        border: 1px solid #ddd;
        border-radius: 8px;
        margin: 10px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .alert-critical {
        background-color: #ffe6e6;
        border-left: 4px solid #d32f2f;
        padding: 15px;
        border-radius: 5px;
        margin: 10px 0;
    }
    .alert-high {
        background-color: #fff3e0;
        border-left: 4px solid #f57c00;
        padding: 15px;
        border-radius: 5px;
        margin: 10px 0;
    }
    .alert-opportunity {
        background-color: #e8f5e9;
        border-left: 4px solid #388e3c;
        padding: 15px;
        border-radius: 5px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# Inicializar session state
if 'agent' not in st.session_state:
    st.session_state.agent = None
if 'analysis_done' not in st.session_state:
    st.session_state.analysis_done = False

# Sidebar
with st.sidebar:
    st.markdown("### 🤖 Agente IA efectoLED")
    st.markdown("---")
    
    # Logo simulado
    st.markdown("""
    <div style='text-align: center; padding: 20px; background-color: #1F4E78; border-radius: 10px; margin-bottom: 20px;'>
        <h2 style='color: white; margin: 0;'>efectoLED</h2>
        <p style='color: #ccc; margin: 0; font-size: 0.9rem;'>Iluminación LED Online</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Selector de caso de uso
    caso_uso = st.selectbox(
        "Selecciona caso de uso:",
        [
            "🔍 Análisis Causal",
            "🚨 Alertas Activas",
            "🎯 Simulador de Escenarios",
            "💰 Marketing Mix Model",
            "💬 Consulta Libre"
        ]
    )
    
    st.markdown("---")
    
    # Métricas de contexto
    st.markdown("### 📊 Contexto Actual")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Revenue Semanal", "42.3K€", "-8.2%", delta_color="inverse")
    with col2:
        st.metric("Conversión", "2.8%", "-0.4pp", delta_color="inverse")
    
    st.markdown("---")
    st.markdown("""
    <div style='font-size: 0.85rem; color: #666;'>
    <b>Última actualización:</b><br>
    {}<br><br>
    <b>Datos:</b> Semana actual vs anterior<br>
    <b>Modelo:</b> Claude Sonnet 4
    </div>
    """.format(datetime.now().strftime("%d/%m/%Y %H:%M")), unsafe_allow_html=True)


# Main content
st.markdown("<h1 class='main-header'>Agente IA para Análisis de Decisiones</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-header'>Transformando datos en acciones mediante IA</p>", unsafe_allow_html=True)

st.markdown("---")

# Renderizar caso de uso seleccionado
if caso_uso == "🔍 Análisis Causal":
    st.markdown("## 🔍 Análisis Causal Multidimensional")
    st.markdown("Identifica las causas raíz de variaciones en métricas clave")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        metric = st.selectbox(
            "Métrica a analizar:",
            ["Conversión", "Revenue", "AOV"],
            help="Selecciona la métrica que quieres analizar"
        )
    
    with col2:
        category = st.selectbox(
            "Categoría:",
            ["Downlights", "Tiras LED", "Focos", "Total"],
            help="Filtra por categoría de producto"
        )
    
    if st.button("🚀 Analizar Causas", type="primary", use_container_width=True):
        
        # Spinner mientras procesa
        with st.spinner("🔄 Analizando datos multidimensionales..."):
            time.sleep(1)  # Simular procesamiento inicial
            
            # Crear agente si no existe
            if st.session_state.agent is None:
                try:
                    st.session_state.agent = create_agent()
                except Exception as e:
                    st.error(f"❌ Error al inicializar agente: {str(e)}")
                    st.info("💡 Asegúrate de que ANTHROPIC_API_KEY esté configurada")
                    st.stop()
            
            # Progreso visual
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            status_text.text("📊 Cargando datos históricos...")
            progress_bar.progress(20)
            time.sleep(0.5)
            
            status_text.text("🔍 Identificando patrones...")
            progress_bar.progress(40)
            time.sleep(0.5)
            
            status_text.text("🧠 Modelo causal procesando...")
            progress_bar.progress(60)
            
            # Llamar al modelo directamente para tener datos estructurados
            causal_model = CausalAnalysisModel()
            metric_map = {"Conversión": "conversion", "Revenue": "revenue", "AOV": "aov"}
            category_param = None if category == "Total" else category
            
            analysis = causal_model.analyze_variation(
                metric=metric_map[metric],
                category=category_param
            )
            
            # Si el modelo no tiene datos para esa combinación, mostrar aviso y parar limpio
            if isinstance(analysis, dict) and "message" in analysis and "suggestion" in analysis and "causes" not in analysis:
                st.warning(analysis["message"])
                st.info(analysis["suggestion"])
                st.stop()
            
            status_text.text("💬 Generando recomendaciones con LLM...")
            progress_bar.progress(80)
            
            # Ahora llamar al agente para la narrativa
            query = f"Analiza la variación de {metric} en {category}. Dame un análisis ejecutivo conciso."
            agent_response = st.session_state.agent.process_query(query, verbose=False)
            
            progress_bar.progress(100)
            status_text.text("✅ Análisis completado")
            time.sleep(0.3)
            
            # Limpiar progreso
            progress_bar.empty()
            status_text.empty()
        
        # Mostrar resultados
        st.success("✅ Análisis completado exitosamente")
        
        # Métricas principales
        st.markdown("### 📊 Variación Detectada")
        col1, col2, col3, col4 = st.columns(4)

        def pick(d, *keys, default=None):
            for k in keys:
                if k in d and d[k] is not None:
                    return d[k]
            return default

        current_value = pick(analysis, "current_value", "current")
        baseline_value = pick(analysis, "baseline_value", "baseline")
        variation_pct = pick(analysis, "variation_percentage", "variation_pct")
        variation_abs = pick(analysis, "variation_absolute", "variation_abs")
        confidence = pick(analysis, "confidence_score", "confidence", default=0)

        # Si falta algo crítico, muestra el dict para depurar y corta
        missing = [k for k, v in {
            "current_value": current_value,
            "baseline_value": baseline_value,
            "variation_percentage": variation_pct,
            "variation_absolute": variation_abs,
        }.items() if v is None]

        if missing:
            st.error(f"Faltan claves en 'analysis': {missing}")
            st.json(analysis)
            st.stop()

        suffix = "%" if metric == "Conversión" else "€"
        delta_text = f"{variation_abs:.2f}pp" if metric == "Conversión" else f"{variation_abs:,.0f}€"

        with col1:
            st.metric("Valor Actual", f"{current_value:.1f}{suffix}", delta=None)
        with col2:
            st.metric("Valor Anterior", f"{baseline_value:.1f}{suffix}", delta=None)
        with col3:
            st.metric("Variación", f"{variation_pct:.1f}%", delta=delta_text, delta_color="inverse")
        with col4:
            st.metric("Confianza Modelo", f"{confidence*100:.0f}%", delta=None)
        if 'causes' in analysis and len(analysis['causes']) > 0:
            st.markdown("### 🎯 Causas Identificadas")
            
            # Crear gráfico de impacto
            fig = go.Figure()
            
            causes_names = [c['cause_name'] for c in analysis['causes']]
            causes_impact = [c['impact_percentage'] * 100 for c in analysis['causes']]
            causes_colors = ['#d32f2f', '#f57c00', '#fbc02d'][:len(causes_names)]
            
            fig.add_trace(go.Bar(
                x=causes_impact,
                y=causes_names,
                orientation='h',
                marker=dict(color=causes_colors),
                text=[f"{imp:.1f}%" for imp in causes_impact],
                textposition='auto',
            ))
            
            fig.update_layout(
                title="Contribución de cada causa al cambio total",
                xaxis_title="% de Impacto",
                yaxis_title="",
                height=300,
                margin=dict(l=0, r=0, t=40, b=0)
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
            # Detalles de cada causa
            for i, cause in enumerate(analysis['causes'], 1):
                severity_class = "cause-card"
                if cause['severity'] == 'critical':
                    severity_emoji = "🔴"
                    severity_color = "#d32f2f"
                elif cause['severity'] == 'high':
                    severity_emoji = "🟠"
                    severity_color = "#f57c00"
                else:
                    severity_emoji = "🟡"
                    severity_color = "#fbc02d"
                
                with st.expander(f"{severity_emoji} **Causa {i}: {cause['cause_name']}** ({cause['impact_percentage']*100:.0f}% impacto)", expanded=(i==1)):
                    st.markdown(f"**Severidad:** <span style='color: {severity_color};'>{cause['severity'].upper()}</span>", unsafe_allow_html=True)
                    
                    # Detalles
                    if 'details' in cause:
                        st.markdown("**Detalles:**")
                        details = cause['details']
                        
                        if isinstance(details, dict):
                            for key, value in details.items():
                                if key not in ['confidence']:
                                    st.markdown(f"- **{key.replace('_', ' ').title()}:** {value}")
                    
                    # Acciones recomendadas
                    if 'recommended_actions' in cause and len(cause['recommended_actions']) > 0:
                        st.markdown("**Acciones Recomendadas:**")
                        for action in cause['recommended_actions']:
                            priority_emoji = "🔥" if action['priority'] == 'urgent' else "⚡" if action['priority'] == 'high' else "📌"
                            st.markdown(f"""
                            <div class='action-card'>
                                {priority_emoji} <b>{action['action']}</b><br>
                                <small>
                                • Responsable: {action.get('owner', 'N/A')}<br>
                                • Tiempo estimado: {action.get('estimated_time', 'N/A')}<br>
                                • Impacto esperado: {action.get('expected_impact', 'N/A')}
                                </small>
                            </div>
                            """, unsafe_allow_html=True)
        
        # Narrativa del agente
        st.markdown("### 💬 Análisis del Agente IA")
        st.markdown(agent_response['analysis'])
        
        # Revenue en riesgo
        if 'revenue_at_risk' in analysis:
            st.markdown("### 💰 Impacto Económico")
            col1, col2 = st.columns(2)
            with col1:
                st.metric(
                    "Revenue Afectado",
                    f"{abs(analysis['revenue_at_risk']):,.0f}€",
                    delta=None
                )
            with col2:
                if analysis['revenue_at_risk'] < 0:
                    recovery = abs(analysis['revenue_at_risk']) * 0.77  # 77% según summary
                    st.metric(
                        "Recuperación Estimada",
                        f"{recovery:,.0f}€",
                        delta="siguiendo plan de acción"
                    )

elif caso_uso == "🚨 Alertas Activas":
    st.markdown("## 🚨 Sistema de Alertas Inteligentes")
    st.markdown("Monitorización continua con detección automática de anomalías")
    
    severity_filter = st.selectbox(
        "Filtrar por severidad:",
        ["Todas", "Críticas", "Altas", "Medias"],
        help="Selecciona el nivel mínimo de severidad a mostrar"
    )
    
    if st.button("🔄 Cargar Alertas Activas", type="primary", use_container_width=True):
        
        with st.spinner("🔍 Escaneando sistema..."):
            time.sleep(1)
            
            alerts_model = AlertsModel()
            severity_map = {
                "Todas": "low",
                "Críticas": "critical",
                "Altas": "high",
                "Medias": "medium"
            }
            
            alerts_data = alerts_model.get_active_alerts(
                severity_threshold=severity_map[severity_filter]
            )
        
        # Resumen de alertas
        st.markdown("### 📊 Resumen de Alertas")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Alertas", alerts_data['total_alerts'])
        with col2:
            st.metric("Críticas", alerts_data['critical_count'], delta=None)
        with col3:
            st.metric("Altas", alerts_data['high_count'], delta=None)
        with col4:
            if alerts_data['total_revenue_at_risk'] > 0:
                st.metric("Revenue en Riesgo", f"{alerts_data['total_revenue_at_risk']/1000:.0f}K€", delta_color="inverse")
        
        # Mostrar cada alerta
        st.markdown("### 🔔 Alertas Detalladas")
        
        for alert in alerts_data['alerts']:
            # Determinar clase CSS según severidad
            if alert['severity'] == 'critical':
                alert_class = "alert-critical"
                emoji = "🔴"
            elif alert['severity'] == 'high':
                alert_class = "alert-high"
                emoji = "🟠"
            else:
                alert_class = "alert-opportunity"
                emoji = "💡"
            
            with st.expander(f"{emoji} **{alert['title']}** ({alert['severity'].upper()})", expanded=(alert['severity']=='critical')):
                
                # Métricas de la alerta
                col1, col2, col3 = st.columns(3)
                if 'baseline_value' in alert:
                    with col1:
                        st.metric("Valor Anterior", alert['baseline_value'])
                    with col2:
                        st.metric("Valor Actual", alert['current_value'])
                    with col3:
                        st.metric("Cambio", f"{alert['change_percentage']:.1f}%", delta_color="inverse")
                
                # Señales detectadas
                if 'signals_detected' in alert:
                    st.markdown("**🔍 Señales Detectadas:**")
                    for signal in alert['signals_detected']:
                        st.markdown(f"- {signal}")
                
                # Impacto estimado
                if 'impact_estimated' in alert:
                    st.markdown("**💰 Impacto Estimado:**")
                    impact = alert['impact_estimated']
                    cols = st.columns(len(impact))
                    for i, (key, value) in enumerate(impact.items()):
                        with cols[i]:
                            label = key.replace('_', ' ').title()
                            st.metric(label, f"{value:,.0f}€" if isinstance(value, int) and value > 100 else value)
                
                # Acciones recomendadas
                if 'recommended_actions' in alert:
                    st.markdown("**✅ Acciones Recomendadas:**")
                    for action in alert['recommended_actions']:
                        st.markdown(f"""
                        <div class='action-card'>
                            <b>Prioridad {action['priority']}:</b> {action['action']}<br>
                            <small>
                            • Urgencia: {action.get('urgency', 'N/A')}<br>
                            • Responsable: {action.get('owner', 'N/A')}<br>
                            {f"• ROI esperado: {action.get('expected_roi', 'N/A')}x" if 'expected_roi' in action else ''}
                            </small>
                        </div>
                        """, unsafe_allow_html=True)

elif caso_uso == "🎯 Simulador de Escenarios":
    st.markdown("## 🎯 Simulador de Escenarios")
    st.markdown('Predice el impacto de decisiones antes de ejecutar ("What-if analysis")')
    
    scenario_names = {
        "optimize_mobile_checkout": "🚀 Optimizar Checkout Móvil",
        "increase_google_ads_tiras_led": "📈 Aumentar Google Ads (Tiras LED)",
        "b2b_reactivation_campaign": "📧 Campaña Reactivación B2B",
        "pause_expensive_keywords": "⏸️ Pausar Keywords Caras"
    }
    
    selected_scenario = st.selectbox(
        "Selecciona escenario a simular:",
        list(scenario_names.keys()),
        format_func=lambda x: scenario_names[x]
    )
    
    # Mostrar descripción del escenario
    simulator = ScenarioSimulator()
    scenario_info = simulator.scenarios[selected_scenario]
    
    st.info(f"**Descripción:** {scenario_info['description']}")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Inversión Requerida", f"{scenario_info['investment']:,.0f}€")
    with col2:
        st.metric("Tiempo Implementación", f"{scenario_info['implementation_weeks']} semanas")
    
    if st.button("📊 Simular Escenario", type="primary", use_container_width=True):
        
        with st.spinner("🔮 Simulando 10,000 escenarios con Monte Carlo..."):
            progress = st.progress(0)
            for i in range(100):
                time.sleep(0.01)
                progress.progress(i + 1)
            
            result = simulator.simulate_scenario(selected_scenario)
            progress.empty()
        
        st.success("✅ Simulación completada")
        
        # Resultados principales
        st.markdown("### 📊 Resultados de la Simulación")
        
        prediction = result['prediction']
        
        # Métricas clave
        cols = st.columns(4)
        metrics_to_show = []
        
        if 'revenue_month_1' in prediction:
            metrics_to_show.append(("Revenue Mes 1", f"{prediction['revenue_month_1']:,.0f}€"))
        if 'revenue_year_1' in prediction:
            metrics_to_show.append(("Revenue Año 1", f"{prediction['revenue_year_1']:,.0f}€"))
        if 'roi' in prediction:
            metrics_to_show.append(("ROI", f"{prediction['roi']:.1f}x"))
        if 'payback_months' in prediction:
            metrics_to_show.append(("Payback", f"{prediction['payback_months']:.1f} meses"))
        if 'roas' in prediction:
            metrics_to_show.append(("ROAS", f"{prediction['roas']:.1f}x"))
        
        for i, (label, value) in enumerate(metrics_to_show[:4]):
            with cols[i]:
                st.metric(label, value)
        
        # Gráfico de intervalo de confianza
        if 'confidence_interval_80' in prediction:
            st.markdown("### 📈 Intervalo de Confianza (80%)")
            
            interval = prediction['confidence_interval_80']
            expected = prediction.get('revenue_month_1') or prediction.get('revenue_year_1', 0)
            
            fig = go.Figure()
            
            fig.add_trace(go.Bar(
                x=['Escenario Pesimista', 'Esperado', 'Escenario Optimista'],
                y=[interval[0], expected, interval[1]],
                marker_color=['#f57c00', '#1F4E78', '#388e3c'],
                text=[f"{v:,.0f}€" for v in [interval[0], expected, interval[1]]],
                textposition='outside'
            ))
            
            fig.update_layout(
                title="Rango de resultados esperados",
                yaxis_title="Revenue (€)",
                height=400,
                margin=dict(l=0, r=0, t=40, b=0)
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        # Supuestos y riesgos
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### ✅ Supuestos del Modelo")
            for assumption in result['assumptions']:
                st.markdown(f"- {assumption}")
        
        with col2:
            st.markdown("### ⚠️ Riesgos Identificados")
            for risk in result['risks']:
                st.markdown(f"- {risk}")
        
        # Botón para comparar con otros escenarios
        if st.button("🔄 Comparar con Otros Escenarios"):
            st.info("💡 Usa la opción 'Comparación de Escenarios' para ver todas las opciones lado a lado")

elif caso_uso == "💰 Marketing Mix Model":
    st.markdown("## 💰 Marketing Mix Modeling")
    st.markdown("Optimiza la distribución de presupuesto entre canales de marketing")
    
    tab1, tab2 = st.tabs(["📊 Atribución Actual", "🎯 Optimizar Presupuesto"])
    
    with tab1:
        st.markdown("### Contribución Incremental por Canal (Q4 2024)")
        
        if st.button("📈 Cargar Análisis MMM", key="load_mmm"):
            with st.spinner("🔄 Calculando contribución incremental..."):
                time.sleep(1.5)
                
                mmm = MarketingMixModel()
                attribution = mmm.get_channel_attribution()
            
            # Métricas globales
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Revenue Total", f"{attribution['total_revenue']/1000:.0f}K€")
            with col2:
                st.metric("Inversión Marketing", f"{attribution['total_marketing_spend']/1000:.0f}K€")
            with col3:
                st.metric("ROAS Global", f"{attribution['overall_roas']:.2f}x")
            
            # Gráfico de contribución
            st.markdown("### 📊 Contribución por Canal")
            
            channels_data = attribution['channel_attribution']
            
            fig = go.Figure()
            
            fig.add_trace(go.Bar(
                name='Revenue Atribuido',
                x=[c['channel'] for c in channels_data],
                y=[c['revenue_attributed'] for c in channels_data],
                text=[f"{c['revenue_attributed']/1000:.0f}K€" for c in channels_data],
                textposition='outside',
                marker_color='#1F4E78'
            ))
            
            fig.update_layout(
                title="Revenue Incremental por Canal",
                yaxis_title="Revenue (€)",
                height=400,
                margin=dict(l=0, r=0, t=40, b=0)
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
            # Tabla detallada
            st.markdown("### 📋 Detalle por Canal")
            
            for channel in channels_data:
                with st.expander(f"**{channel['channel']}** - {channel['status']}", expanded=False):
                    col1, col2, col3, col4 = st.columns(4)
                    
                    with col1:
                        st.metric("Inversión", f"{channel['spend']/1000:.0f}K€")
                    with col2:
                        st.metric("Revenue", f"{channel['revenue_attributed']/1000:.0f}K€")
                    with col3:
                        st.metric("ROAS", f"{channel['roas']:.1f}x")
                    with col4:
                        if channel['saturation_level']:
                            st.metric("Saturación", f"{channel['saturation_level']*100:.0f}%")
                    
                    if channel['carryover_weeks']:
                        st.markdown(f"**Efecto carryover:** {channel['carryover_weeks']:.1f} semanas")
    
    with tab2:
        st.markdown("### Optimización de Presupuesto")
        
        budget_input = st.number_input(
            "Presupuesto total a distribuir (€):",
            min_value=10000,
            max_value=200000,
            value=54000,
            step=1000,
            help="Introduce el presupuesto total de marketing"
        )
        
        if st.button("🎯 Optimizar Distribución", type="primary", key="optimize_budget"):
            with st.spinner("🧮 Optimizando distribución..."):
                time.sleep(1.5)
                
                mmm = MarketingMixModel()
                optimization = mmm.optimize_budget(budget_input)
            
            st.success("✅ Optimización completada")
            
            # Impacto esperado
            st.markdown("### 💰 Impacto Esperado")
            col1, col2, col3, col4 = st.columns(4)
            
            impact = optimization['expected_impact']
            with col1:
                st.metric("Revenue Actual", f"{impact['current_revenue']/1000:.0f}K€")
            with col2:
                st.metric("Revenue Esperado", f"{impact['expected_revenue']/1000:.0f}K€", 
                         delta=f"+{impact['revenue_increase']/1000:.0f}K€")
            with col3:
                st.metric("ROAS Actual", f"{impact['current_roas']:.2f}x")
            with col4:
                st.metric("ROAS Esperado", f"{impact['expected_roas']:.2f}x",
                         delta=f"+{impact['roas_improvement_pct']:.1f}%")
            
            # Tabla de recomendaciones
            st.markdown("### 📊 Recomendaciones por Canal")
            
            recommendations = optimization['channel_recommendations']
            
            for rec in recommendations:
                if rec['change_amount'] != 0:
                    action_emoji = "📈" if rec['change_amount'] > 0 else "📉"
                    
                    with st.expander(f"{action_emoji} **{rec['channel']}** - {rec['action']}", expanded=(abs(rec['change_amount']) > 2000)):
                        col1, col2, col3 = st.columns(3)
                        
                        with col1:
                            st.metric("Actual", f"{rec['current_spend']:,.0f}€")
                        with col2:
                            st.metric("Recomendado", f"{rec['recommended_spend']:,.0f}€",
                                     delta=f"{rec['change_amount']:+,.0f}€")
                        with col3:
                            st.metric("ROAS", f"{rec['current_roas']:.1f}x")
                        
                        st.markdown(f"**Razón:** {rec['reason']}")

else:  # Consulta Libre
    st.markdown("## 💬 Consulta Libre al Agente")
    st.markdown("Pregunta cualquier cosa sobre el negocio en lenguaje natural")
    
    # Input de consulta
    query = st.text_area(
        "Escribe tu consulta:",
        height=100,
        placeholder="Ejemplo: ¿Qué 3 acciones debería priorizar esta semana para recuperar ventas?",
        help="El agente analizará tu pregunta y llamará a los modelos necesarios"
    )
    
    # Ejemplos de consultas
    with st.expander("💡 Ver ejemplos de consultas"):
        st.markdown("""
        - ¿Por qué bajó la conversión de downlights esta semana?
        - Dame un resumen ejecutivo de la situación del ecommerce
        - ¿Qué alertas críticas tengo activas?
        - Compara: optimizar móvil vs aumentar Google Ads vs campaña B2B
        - ¿Cómo debería distribuir 50K€ de presupuesto de marketing?
        - ¿Qué acciones tienen mejor ROI esta semana?
        """)
    
    if st.button("🚀 Consultar al Agente", type="primary", disabled=(not query), use_container_width=True):
        
        if st.session_state.agent is None:
            try:
                st.session_state.agent = create_agent()
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
                st.info("💡 Configura ANTHROPIC_API_KEY como variable de entorno")
                st.stop()
        
        with st.spinner("🤖 El agente está procesando tu consulta..."):
            
            # Status updates
            status = st.empty()
            progress = st.progress(0)
            
            status.text("🔍 Analizando consulta...")
            progress.progress(20)
            time.sleep(0.3)
            
            status.text("🧠 Llamando a modelos ML...")
            progress.progress(50)
            
            # Procesar consulta
            response = st.session_state.agent.process_query(query, verbose=False)
            
            status.text("💬 Generando respuesta...")
            progress.progress(90)
            time.sleep(0.2)
            
            progress.progress(100)
            status.empty()
            progress.empty()
        
        st.success("✅ Respuesta generada")
        
        # Mostrar respuesta
        st.markdown("### 💬 Respuesta del Agente")
        st.markdown(response['analysis'])
        
        # Metadata
        with st.expander("ℹ️ Información técnica"):
            st.markdown(f"**Timestamp:** {response['timestamp']}")
            st.markdown(f"**Modelo:** {response['model']}")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; font-size: 0.9rem;'>
    🤖 <b>Agente IA efectoLED</b> | Prototipo Demo<br>
    Desarrollado por Alkemy<br>
    Powered by Claude Sonnet 4 + ML Models
</div>
""", unsafe_allow_html=True)
