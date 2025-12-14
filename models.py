"""
Modelos ML simulados para el Agente IA de efectoLED

Estos modelos simulan análisis ML pero usan datos predefinidos.
En producción, se sustituirían por modelos reales entrenados.
"""

import json
from datetime import datetime, timedelta
from config import (
    generate_historical_data,
    B2B_CUSTOMER_DATA,
    SIMULATION_SCENARIOS,
    COMPETITOR_DATA,
    MMM_QUARTERLY_DATA
)


class CausalAnalysisModel:
    """
    Modelo de análisis causal multidimensional
    En producción: SHAP + Causal Inference (DoWhy)
    """
    
    def __init__(self):
        self.data = generate_historical_data()
    
    def analyze_variation(self, metric, category=None, period_current="week_0", period_comparison="week_-1"):
        """
        Analiza las causas de una variación en una métrica
        
        Args:
            metric: 'conversion', 'revenue', 'aov', etc.
            category: 'Downlights', 'Tiras LED', etc. o None para total
            period_current: período actual
            period_comparison: período de comparación
        
        Returns:
            Dict con análisis causal estructurado
        """
        
        baseline = self.data["baseline"]
        current = self.data["current"]
        
        # Caso específico: Conversión de Downlights
        if metric == "conversion" and category == "Downlights":
            return self._analyze_downlights_conversion(baseline, current)
        
        # Caso general: Revenue total
        elif metric == "revenue" and category is None:
            return self._analyze_total_revenue(baseline, current)
        
        else:
            return self._generic_analysis(metric, category, baseline, current)
    
    def _analyze_downlights_conversion(self, baseline, current):
        """Análisis específico de conversión de downlights"""
        
        baseline_conv = baseline["by_category"]["Downlights"]["conversion"]
        current_conv = current["by_category"]["Downlights"]["conversion"]
        variation_pp = current_conv - baseline_conv
        variation_pct = (variation_pp / baseline_conv) * 100
        
        # Causas identificadas (simuladas por SHAP en producción)
        causes = [
            {
                "cause_id": "mobile_performance",
                "cause_name": "Rendimiento móvil",
                "impact_percentage": 0.60,
                "impact_pp": variation_pp * 0.60,
                "severity": "critical",
                "details": {
                    "metric_affected": "mobile_conversion",
                    "baseline_value": 2.8,
                    "current_value": 2.1,
                    "change_percentage": -25.0,
                    "root_cause": "Tiempo de carga checkout móvil",
                    "technical_details": current["technical_issues"]["mobile_checkout_load_time"],
                    "correlation": 0.94,
                    "confidence": 0.89
                },
                "recommended_actions": [
                    {
                        "priority": "urgent",
                        "action": "Rollback deploy versión 3.2.1",
                        "owner": "IT/DevOps",
                        "estimated_time": "1-2 horas",
                        "expected_impact": "Recuperar 60% conversión móvil en 24h",
                        "estimated_revenue_recovery": 5200
                    },
                    {
                        "priority": "urgent",
                        "action": "Fix bug carga imágenes en checkout móvil",
                        "owner": "Desarrollo",
                        "estimated_time": "4-6 horas",
                        "expected_impact": "Solución definitiva",
                        "estimated_revenue_recovery": 8200
                    }
                ]
            },
            {
                "cause_id": "google_ads_competition",
                "cause_name": "Competencia en Google Ads",
                "impact_percentage": 0.30,
                "impact_pp": variation_pp * 0.30,
                "severity": "high",
                "details": {
                    "metric_affected": "paid_traffic_quality",
                    "keyword": "downlights led empotrar",
                    "cpc_change": current["by_channel"]["Google Ads"]["issues"]["keyword_downlights_led"],
                    "competitor": "IluminacionPro",
                    "competitor_data": COMPETITOR_DATA["IluminacionPro"],
                    "impressions_change": -0.32,
                    "position_change": 1.8,
                    "confidence": 0.82
                },
                "recommended_actions": [
                    {
                        "priority": "high",
                        "action": "Pausar keyword 'downlights led empotrar' temporalmente",
                        "owner": "Marketing",
                        "estimated_time": "15 minutos",
                        "expected_impact": "Ahorro 700€/semana",
                        "budget_reallocation": "Long-tail keywords"
                    },
                    {
                        "priority": "medium",
                        "action": "Activar keywords long-tail alternativas",
                        "owner": "Marketing",
                        "alternatives": ["downlights led extraplanos cocina", "downlights empotrar salon", "downlights regulables led"],
                        "expected_cpc": 0.45,
                        "expected_revenue": 2100,
                        "estimated_time": "1 hora"
                    },
                    {
                        "priority": "medium",
                        "action": "Mejorar Quality Score landing page downlights",
                        "owner": "Marketing + UX",
                        "improvements": ["Añadir calculadora lúmenes", "Incluir más reviews", "Mejorar mobile UX"],
                        "expected_time": "2 semanas",
                        "expected_cpc_reduction": -0.25
                    }
                ]
            },
            {
                "cause_id": "stock_limitation",
                "cause_name": "Stock limitado producto top",
                "impact_percentage": 0.10,
                "impact_pp": variation_pp * 0.10,
                "severity": "medium",
                "details": {
                    "product": "Downlight Cuadrado Blanco 12W (ref-245)",
                    "current_stock": 12,
                    "usual_contribution": 0.28,
                    "revenue_affected": 4423,
                    "customer_behavior": "Mensaje 'Últimas unidades' genera urgencia pero también rebote",
                    "confidence": 0.71
                },
                "recommended_actions": [
                    {
                        "priority": "medium",
                        "action": "Adelantar pedido a proveedor",
                        "owner": "Supply Chain",
                        "estimated_time": "Contacto inmediato",
                        "expected_impact": "Stock completo en 5-7 días"
                    },
                    {
                        "priority": "medium",
                        "action": "Destacar alternativa ref-248 con stock",
                        "owner": "Marketing",
                        "estimated_time": "30 minutos",
                        "expected_impact": "Mantener 70% conversión de categoría"
                    }
                ]
            }
        ]
        
        return {
            "metric": "conversion_rate",
            "category": "Downlights",
            "baseline_value": baseline_conv,
            "current_value": current_conv,
            "variation_absolute": variation_pp,
            "variation_percentage": variation_pct,
            "period_baseline": baseline["period"],
            "period_current": current["period"],
            "analysis_timestamp": datetime.now().isoformat(),
            "causes": causes,
            "total_impact_explained": sum([c["impact_percentage"] for c in causes]),
            "confidence_score": 0.85,
            "revenue_at_risk": -2790,  # 18600 - 15810
            "summary": f"La conversión de Downlights cayó {abs(variation_pp):.1f}pp ({variation_pct:.1f}%). Las 3 causas principales son: (1) Bug móvil checkout - 60% impacto, (2) Competencia Google Ads - 30%, (3) Stock limitado ref-245 - 10%."
        }
    
    def _analyze_total_revenue(self, baseline, current):
        """Análisis de revenue total"""
        
        baseline_rev = baseline["metrics"]["total_revenue"]
        current_rev = current["metrics"]["total_revenue"]
        variation_abs = current_rev - baseline_rev
        variation_pct = (variation_abs / baseline_rev) * 100
        
        causes = [
            {
                "cause_id": "downlights_category_drop",
                "cause_name": "Caída ventas Downlights",
                "impact_percentage": 0.67,
                "impact_absolute": -2790,
                "details": "Ver análisis detallado de conversión Downlights",
                "recommended_action": "Ver recomendaciones específicas de categoría"
            },
            {
                "cause_id": "tiras_led_growth",
                "cause_name": "Crecimiento Tiras LED",
                "impact_percentage": -0.15,
                "impact_absolute": 620,
                "details": "Tiras LED crecieron por campaña email exitosa",
                "recommended_action": "Escalar campaña email Tiras LED"
            }
        ]
        
        return {
            "metric": "revenue",
            "category": None,
            "baseline_value": baseline_rev,
            "current_value": current_rev,
            "variation_absolute": variation_abs,
            "variation_percentage": variation_pct,
            "causes": causes,
            "confidence_score": 0.78,
            "summary": f"Revenue total cayó {abs(variation_abs):,.0f}€ ({variation_pct:.1f}%). Principal causa: caída Downlights por problemas móvil y Google Ads."
        }
    
    def _generic_analysis(self, metric, category, baseline, current):
        """Análisis genérico para otros casos"""
        return {
            "metric": metric,
            "category": category,
            "message": "Análisis no disponible para esta combinación métrica-categoría",
            "suggestion": "Probar con metric='conversion' category='Downlights' o metric='revenue' category=None"
        }


class AlertsModel:
    """
    Modelo de alertas predictivas
    En producción: LSTM + Isolation Forest + Autoencoders
    """
    
    def __init__(self):
        self.data = generate_historical_data()
    
    def get_active_alerts(self, severity_threshold="medium"):
        """
        Obtiene alertas activas según nivel de severidad
        
        Args:
            severity_threshold: 'critical', 'high', 'medium', 'low'
        
        Returns:
            Lista de alertas activas
        """
        
        alerts = [
            {
                "alert_id": "ALERT_001",
                "timestamp": datetime.now().isoformat(),
                "severity": "critical",
                "type": "reactive",
                "title": "Conversión móvil downlights -25% en 3 días",
                "metric_affected": "mobile_conversion_downlights",
                "baseline_value": 2.8,
                "current_value": 2.1,
                "change_percentage": -25.0,
                "confidence": 0.94,
                "signals_detected": [
                    "Tiempo carga checkout móvil: 2.1s → 4.8s (+129%)",
                    "Bounce rate móvil: 42% → 61% (+19pp)",
                    "Deploy versión 3.2.1 correlacionado (martes 10:00)",
                    "58% tráfico downlights viene de móvil"
                ],
                "impact_estimated": {
                    "revenue_lost_3_days": 5200,
                    "revenue_at_risk_7_days": 12500,
                    "customers_affected": 450
                },
                "recommended_actions": [
                    {
                        "priority": 1,
                        "action": "Rollback deploy 3.2.1",
                        "urgency": "inmediata",
                        "owner": "IT"
                    }
                ],
                "days_since_detected": 3
            },
            {
                "alert_id": "ALERT_002",
                "timestamp": datetime.now().isoformat(),
                "severity": "high",
                "type": "reactive",
                "title": "CPA Google Ads +31% vs objetivo",
                "metric_affected": "cpa_google_ads",
                "baseline_value": 52,
                "current_value": 68,
                "change_percentage": 30.8,
                "confidence": 0.87,
                "signals_detected": [
                    "CPC keyword principal +93%: 0.92€ → 1.78€",
                    "Posición promedio cayó: 1.8 → 3.2",
                    "Competidor IluminacionPro lanzó campaña agresiva hace 5 días",
                    "Impresiones -32%, Clics -28%"
                ],
                "impact_estimated": {
                    "budget_wasted_weekly": 700,
                    "revenue_lost": 3100
                },
                "recommended_actions": [
                    {
                        "priority": 1,
                        "action": "Pausar keyword cara, activar long-tail",
                        "urgency": "alta",
                        "owner": "Marketing"
                    }
                ],
                "days_since_detected": 5
            },
            {
                "alert_id": "ALERT_003",
                "timestamp": datetime.now().isoformat(),
                "severity": "medium",
                "type": "opportunity",
                "title": "85 clientes B2B en riesgo churn - 157K€ en juego",
                "metric_affected": "b2b_churn_rate",
                "confidence": 0.76,
                "signals_detected": [
                    "85 clientes B2B > 65 días sin comprar (patrón: 45 días)",
                    "Frecuencia compra cayó 40% vs trimestre anterior",
                    "Email engagement: abren pero no clickean",
                    "Segmento principal: electricistas compradores downlights"
                ],
                "impact_estimated": {
                    "revenue_at_risk": 157000,
                    "ltv_average": 1850,
                    "customers_at_risk": 85
                },
                "recommended_actions": [
                    {
                        "priority": 1,
                        "action": "Campaña reactivación B2B personalizada",
                        "estimated_cost": 3500,
                        "expected_roi": 29.4,
                        "urgency": "alta"
                    }
                ]
            },
            {
                "alert_id": "ALERT_004",
                "timestamp": datetime.now().isoformat(),
                "severity": "low",
                "type": "opportunity",
                "title": "Email B2B tiene ROAS 18x pero solo 15% saturación",
                "metric_affected": "email_b2b_saturation",
                "confidence": 0.81,
                "signals_detected": [
                    "ROAS Email B2B: 18.0x (vs Google Ads: 4.5x)",
                    "Saturación: 15% (muy bajo, amplio margen)",
                    "Presupuesto actual: 3K€/mes",
                    "Potencial escalar a 6-8K€/mes sin saturar"
                ],
                "impact_estimated": {
                    "revenue_potential_monthly": 54000,
                    "budget_increase_recommended": 3000
                },
                "recommended_actions": [
                    {
                        "priority": 2,
                        "action": "Escalar Email B2B +3K€/mes",
                        "expected_revenue_increase": 54000,
                        "urgency": "media"
                    }
                ]
            }
        ]
        
        # Filtrar por severity
        severity_order = ["critical", "high", "medium", "low"]
        threshold_index = severity_order.index(severity_threshold)
        
        filtered_alerts = [
            a for a in alerts 
            if severity_order.index(a["severity"]) <= threshold_index
        ]
        
        return {
            "alerts": filtered_alerts,
            "total_alerts": len(filtered_alerts),
            "critical_count": sum(1 for a in filtered_alerts if a["severity"] == "critical"),
            "high_count": sum(1 for a in filtered_alerts if a["severity"] == "high"),
            "total_revenue_at_risk": sum(
                a.get("impact_estimated", {}).get("revenue_at_risk", 0) 
                for a in filtered_alerts
            ),
            "timestamp": datetime.now().isoformat()
        }


class ScenarioSimulator:
    """
    Simulador de escenarios "qué pasa si..."
    En producción: Causal Forecasting + Monte Carlo
    """
    
    def __init__(self):
        self.scenarios = SIMULATION_SCENARIOS
    
    def simulate_scenario(self, scenario_type, custom_params=None):
        """
        Simula un escenario de decisión de negocio
        
        Args:
            scenario_type: Tipo de escenario (key de SIMULATION_SCENARIOS)
            custom_params: Parámetros custom para override
        
        Returns:
            Resultado de la simulación con predicciones
        """
        
        if scenario_type not in self.scenarios:
            return {
                "error": f"Escenario '{scenario_type}' no encontrado",
                "available_scenarios": list(self.scenarios.keys())
            }
        
        scenario = self.scenarios[scenario_type]
        
        # En producción, aquí iría el modelo de simulación
        # Por ahora, devolvemos los expected_impact predefinidos
        
        return {
            "scenario_type": scenario_type,
            "scenario_name": scenario["name"],
            "description": scenario["description"],
            "investment_required": scenario["investment"],
            "implementation_time_weeks": scenario["implementation_weeks"],
            "prediction": {
                **scenario["expected_impact"],
                "confidence_level": 0.82,
                "confidence_interval_80": self._calculate_confidence_interval(
                    scenario["expected_impact"].get("revenue_month_1", scenario["expected_impact"].get("revenue_year_1", 0)),
                    0.15
                )
            },
            "assumptions": [
                "Basado en 24 meses histórico efectoLED",
                "Benchmark sector ecommerce incluido",
                "Control por estacionalidad",
                "Competencia sin cambios significativos asumida"
            ],
            "risks": [
                "Cambios algoritmo Google",
                "Nuevas campañas competencia",
                "Variaciones estacionales no previstas"
            ],
            "sensitivity_analysis": self._sensitivity_analysis(scenario),
            "comparison_rank": None,  # Se llena si comparamos múltiples escenarios
            "timestamp": datetime.now().isoformat()
        }
    
    def compare_scenarios(self, scenario_types):
        """Compara múltiples escenarios y los ordena por ROI"""
        
        results = []
        for scenario_type in scenario_types:
            sim = self.simulate_scenario(scenario_type)
            if "error" in sim:
                continue
            
            # Calcular ROI
            investment = sim["investment_required"]
            revenue = sim["prediction"].get("revenue_year_1") or sim["prediction"].get("revenue_6_months", 0)
            
            roi = ((revenue - investment) / investment) if investment > 0 else float('inf')
            
            results.append({
                "scenario_type": scenario_type,
                "scenario_name": sim["scenario_name"],
                "investment": investment,
                "expected_revenue": revenue,
                "roi": roi,
                "payback_months": sim["prediction"].get("payback_months"),
                "implementation_weeks": sim["implementation_time_weeks"],
                "confidence": sim["prediction"]["confidence_level"]
            })
        
        # Ordenar por ROI
        results = sorted(results, key=lambda x: x["roi"], reverse=True)
        
        # Añadir rank
        for i, r in enumerate(results, 1):
            r["rank"] = i
        
        return {
            "scenarios_compared": len(results),
            "recommendation": results[0] if results else None,
            "all_scenarios": results,
            "timestamp": datetime.now().isoformat()
        }
    
    def _calculate_confidence_interval(self, value, margin):
        """Calcula intervalo de confianza"""
        lower = value * (1 - margin)
        upper = value * (1 + margin)
        return [round(lower, 0), round(upper, 0)]
    
    def _sensitivity_analysis(self, scenario):
        """Análisis de sensibilidad básico"""
        return {
            "best_case": "Adopción completa + efectos de red",
            "worst_case": "Adopción lenta o resistencia al cambio",
            "most_likely": "Adopción gradual según roadmap"
        }


class MarketingMixModel:
    """
    Marketing Mix Modeling (MMM)
    En producción: Bayesian MMM (PyMC)
    """
    
    def __init__(self):
        self.data = MMM_QUARTERLY_DATA
    
    def get_channel_attribution(self):
        """Obtiene la atribución de revenue por canal"""
        
        channels = self.data["channel_contribution"]
        
        # Formatear output
        attribution = []
        for channel_name, channel_data in channels.items():
            attribution.append({
                "channel": channel_name,
                "spend": channel_data["spend"],
                "revenue_attributed": channel_data["revenue_attributed"],
                "roas": channel_data["roas"],
                "saturation_level": channel_data["saturation_level"],
                "carryover_weeks": channel_data["carryover_weeks"],
                "incremental_contribution_pct": channel_data["incremental_contribution"],
                "status": self._assess_channel_status(channel_data)
            })
        
        # Ordenar por contribution
        attribution = sorted(attribution, key=lambda x: x["revenue_attributed"], reverse=True)
        
        return {
            "period": self.data["period"],
            "total_revenue": self.data["total_revenue"],
            "total_marketing_spend": self.data["total_marketing_spend"],
            "base_revenue": self.data["base_revenue"],
            "base_revenue_pct": self.data["base_revenue"] / self.data["total_revenue"],
            "overall_roas": (self.data["total_revenue"] - self.data["base_revenue"]) / self.data["total_marketing_spend"],
            "channel_attribution": attribution,
            "timestamp": datetime.now().isoformat()
        }
    
    def optimize_budget(self, total_budget):
        """
        Recomienda distribución óptima de presupuesto
        
        En producción: Optimización con constraint de suma = total_budget
        """
        
        channels = self.data["channel_contribution"]
        
        # Estrategia de optimización simple:
        # - Reducir canales saturados (>60%)
        # - Aumentar canales con bajo saturation y alto ROAS
        
        recommendations = []
        
        for channel_name, channel_data in channels.items():
            current_spend = channel_data["spend"]
            saturation = channel_data.get("saturation_level", 0.5)
            roas = channel_data["roas"]
            
            # Lógica de recomendación
            if saturation and saturation > 0.65:
                # Saturado → reducir
                recommended_spend = current_spend * 0.85
                action = "REDUCIR"
                reason = f"Saturación alta ({saturation:.0%}), rendimientos decrecientes"
            elif saturation and saturation < 0.25 and roas > 10:
                # Poco saturado + alto ROAS → escalar agresivamente
                recommended_spend = current_spend * 2.0
                action = "ESCALAR FUERTE"
                reason = f"Saturación baja ({saturation:.0%}) + ROAS excelente ({roas:.1f}x)"
            elif saturation and saturation < 0.50 and roas > 5:
                # Margen para crecer
                recommended_spend = current_spend * 1.3
                action = "AUMENTAR"
                reason = f"Aún tiene margen (saturación {saturation:.0%})"
            else:
                # Mantener
                recommended_spend = current_spend
                action = "MANTENER"
                reason = "Balance óptimo"
            
            recommendations.append({
                "channel": channel_name,
                "current_spend": current_spend,
                "recommended_spend": round(recommended_spend, 0),
                "change_amount": round(recommended_spend - current_spend, 0),
                "change_pct": round(((recommended_spend - current_spend) / current_spend) * 100, 1) if current_spend > 0 else 0,
                "action": action,
                "reason": reason,
                "current_roas": roas,
                "saturation_level": saturation
            })
        
        # Ajustar para que sume exactamente total_budget
        total_recommended = sum(r["recommended_spend"] for r in recommendations)
        adjustment_factor = total_budget / total_recommended
        
        for rec in recommendations:
            rec["recommended_spend"] = round(rec["recommended_spend"] * adjustment_factor, 0)
            rec["change_amount"] = round(rec["recommended_spend"] - rec["current_spend"], 0)
        
        # Calcular impacto esperado
        # Simplificación: ROAS se mantiene
        new_revenue = self.data["base_revenue"] + sum(
            r["recommended_spend"] * r["current_roas"] 
            for r in recommendations
        )
        
        revenue_increase = new_revenue - self.data["total_revenue"]
        new_roas = (new_revenue - self.data["base_revenue"]) / total_budget
        roas_improvement = ((new_roas - (self.data["total_revenue"] - self.data["base_revenue"]) / self.data["total_marketing_spend"]) / 
                           ((self.data["total_revenue"] - self.data["base_revenue"]) / self.data["total_marketing_spend"])) * 100
        
        return {
            "current_budget": self.data["total_marketing_spend"],
            "proposed_budget": total_budget,
            "budget_change": total_budget - self.data["total_marketing_spend"],
            "channel_recommendations": sorted(recommendations, key=lambda x: abs(x["change_amount"]), reverse=True),
            "expected_impact": {
                "current_revenue": self.data["total_revenue"],
                "expected_revenue": round(new_revenue, 0),
                "revenue_increase": round(revenue_increase, 0),
                "current_roas": round((self.data["total_revenue"] - self.data["base_revenue"]) / self.data["total_marketing_spend"], 2),
                "expected_roas": round(new_roas, 2),
                "roas_improvement_pct": round(roas_improvement, 1)
            },
            "timestamp": datetime.now().isoformat()
        }
    
    def _assess_channel_status(self, channel_data):
        """Evalúa el estado de un canal"""
        saturation = channel_data.get("saturation_level")
        roas = channel_data["roas"]
        
        if saturation and saturation > 0.65:
            return "⚠️ Saturado - considerar reducir"
        elif saturation and saturation < 0.25 and roas > 10:
            return "✅✅ Excelente oportunidad - escalar"
        elif saturation and saturation < 0.50:
            return "✅ Margen para crecer"
        else:
            return "→ Mantener"
