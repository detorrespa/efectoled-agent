"""
Configuración y datos simulados para el Agente IA de efectoLED
"""

import os
from datetime import datetime, timedelta
import random

# Configuración API
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")

# Contexto de negocio efectoLED
BUSINESS_CONTEXT = {
    "company": "efectoLED",
    "industry": "Iluminación LED - Ecommerce",
    "segments": ["B2B (electricistas, instaladores)", "B2C (particulares)"],
    "main_categories": ["Downlights", "Tiras LED", "Focos", "Bombillas", "Accesorios"],
    "marketing_channels": ["Google Ads", "Meta Ads", "Email Marketing", "SEO Orgánico", "Directo", "Afiliación"],
    "key_metrics": ["Conversión", "AOV", "Revenue", "CPA", "ROAS"],
    "current_challenges": [
        "Optimizar conversión móvil",
        "Reducir CPA en Google Ads",
        "Aumentar recompra clientes B2B",
        "Mejorar AOV mediante cross-sell"
    ]
}

# Datos históricos simulados (última semana)
def generate_historical_data():
    """Genera datos históricos simulados para análisis"""
    
    # Semana pasada (baseline normal)
    baseline_week = {
        "period": "week_-1",
        "dates": [(datetime.now() - timedelta(days=i)).strftime("%Y-%m-%d") for i in range(14, 7, -1)],
        "metrics": {
            "total_revenue": 46500,
            "total_orders": 183,
            "conversion_rate": 3.2,
            "aov": 254,
            "traffic": 5720,
            "mobile_conversion": 2.8,
            "desktop_conversion": 3.9
        },
        "by_category": {
            "Downlights": {
                "revenue": 18600,
                "orders": 74,
                "conversion": 3.4,
                "traffic": 2175,
                "aov": 251
            },
            "Tiras LED": {
                "revenue": 12400,
                "orders": 52,
                "conversion": 3.1,
                "traffic": 1677,
                "aov": 238
            },
            "Focos": {
                "revenue": 9300,
                "orders": 38,
                "conversion": 3.0,
                "traffic": 1267,
                "aov": 245
            },
            "Otros": {
                "revenue": 6200,
                "orders": 19,
                "conversion": 3.2,
                "traffic": 601,
                "aov": 326
            }
        },
        "by_channel": {
            "Google Ads": {
                "revenue": 16275,
                "spend": 3850,
                "roas": 4.23,
                "cpa": 52
            },
            "Meta Ads": {
                "revenue": 8835,
                "spend": 2650,
                "roas": 3.33,
                "cpa": 68
            },
            "Email": {
                "revenue": 11160,
                "spend": 650,
                "roas": 17.17,
                "cpa": 18
            },
            "Organico": {
                "revenue": 7440,
                "spend": 1500,
                "roas": 4.96,
                "cpa": 45
            },
            "Directo": {
                "revenue": 2790,
                "spend": 0,
                "roas": None,
                "cpa": None
            }
        }
    }
    
    # Semana actual (con problemas simulados)
    current_week = {
        "period": "week_0",
        "dates": [(datetime.now() - timedelta(days=i)).strftime("%Y-%m-%d") for i in range(6, -1, -1)],
        "metrics": {
            "total_revenue": 42300,
            "total_orders": 168,
            "conversion_rate": 2.8,
            "aov": 252,
            "traffic": 6000,
            "mobile_conversion": 2.1,  # ⚠️ Bajó significativamente
            "desktop_conversion": 3.7
        },
        "by_category": {
            "Downlights": {
                "revenue": 15810,  # ⚠️ Bajó -15%
                "orders": 63,
                "conversion": 2.6,  # ⚠️ Problema principal
                "traffic": 2423,
                "aov": 251,
                "top_products": {
                    "Downlight Cuadrado Blanco 12W (ref-245)": {
                        "revenue": 4423,
                        "stock": 12,  # ⚠️ Stock bajo
                        "usual_contribution": 0.28
                    }
                }
            },
            "Tiras LED": {
                "revenue": 13020,  # Subió ligeramente
                "orders": 55,
                "conversion": 3.2,
                "traffic": 1719,
                "aov": 237
            },
            "Focos": {
                "revenue": 8475,
                "orders": 35,
                "conversion": 2.9,
                "traffic": 1207,
                "aov": 242
            },
            "Otros": {
                "revenue": 4995,
                "orders": 15,
                "conversion": 2.5,
                "traffic": 651,
                "aov": 333
            }
        },
        "by_channel": {
            "Google Ads": {
                "revenue": 15255,  # ⚠️ Bajó
                "spend": 4200,  # Subió
                "roas": 3.63,  # ⚠️ Empeoró
                "cpa": 68,  # ⚠️ Subió +31%
                "issues": {
                    "keyword_downlights_led": {
                        "cpc_before": 0.92,
                        "cpc_now": 1.78,  # ⚠️ +93% por competencia
                        "position_before": 1.8,
                        "position_now": 3.2
                    }
                }
            },
            "Meta Ads": {
                "revenue": 8010,
                "spend": 2580,
                "roas": 3.10,
                "cpa": 71
            },
            "Email": {
                "revenue": 12180,  # Subió
                "spend": 680,
                "roas": 17.91,
                "cpa": 17
            },
            "Organico": {
                "revenue": 5070,  # ⚠️ Bajó por SEO
                "spend": 1500,
                "roas": 3.38,
                "cpa": 62
            },
            "Directo": {
                "revenue": 1785,
                "spend": 0,
                "roas": None,
                "cpa": None
            }
        },
        "technical_issues": {
            "mobile_checkout_load_time": {
                "before": 2.1,
                "now": 4.8,  # ⚠️ Bug deploy martes
                "deploy_date": (datetime.now() - timedelta(days=3)).strftime("%Y-%m-%d"),
                "version": "3.2.1"
            },
            "mobile_bounce_rate": {
                "before": 0.42,
                "now": 0.61  # ⚠️ Consecuencia del bug
            }
        }
    }
    
    return {
        "baseline": baseline_week,
        "current": current_week
    }

# Datos de clientes B2B para análisis de churn
B2B_CUSTOMER_DATA = [
    {
        "id": "B2B_001",
        "name": "ElectroInstalaciones García",
        "segment": "electricista",
        "ltv": 3850,
        "last_purchase_days": 72,
        "avg_frequency_days": 45,
        "preferred_category": "Downlights",
        "email_engagement": 0.65,
        "churn_probability": 0.78
    },
    {
        "id": "B2B_002", 
        "name": "Ilumina Pro SL",
        "segment": "instalador",
        "ltv": 5200,
        "last_purchase_days": 68,
        "avg_frequency_days": 42,
        "preferred_category": "Focos",
        "email_engagement": 0.42,
        "churn_probability": 0.82
    },
    # ... más clientes
]

# Escenarios de simulación disponibles
SIMULATION_SCENARIOS = {
    "optimize_mobile_checkout": {
        "name": "Optimizar checkout móvil",
        "description": "Reducir tiempo de carga de 4.8s a 1.5s",
        "investment": 8000,
        "implementation_weeks": 3,
        "expected_impact": {
            "mobile_conversion_increase": 0.28,  # +28%
            "revenue_month_1": 15200,
            "payback_months": 0.5,
            "revenue_year_1": 182000
        }
    },
    "increase_google_ads_tiras_led": {
        "name": "+5K€ Google Ads en Tiras LED",
        "description": "Aumentar presupuesto mensual en campaña Tiras LED",
        "investment": 5000,
        "implementation_weeks": 0,
        "expected_impact": {
            "revenue_month_1": 12000,
            "roas": 2.4,
            "saturation_month": 4,
            "revenue_6_months": 72000
        }
    },
    "b2b_reactivation_campaign": {
        "name": "Campaña reactivación B2B",
        "description": "Email + llamada a 200 clientes dormidos",
        "investment": 3500,
        "implementation_weeks": 2,
        "expected_impact": {
            "reactivation_rate": 0.28,
            "customers_reactivated": 56,
            "revenue_year_1": 103000,
            "roi": 29.4
        }
    },
    "pause_expensive_keywords": {
        "name": "Pausar keywords caras en Google Ads",
        "description": "Pausar 'downlights led' y usar long-tail",
        "investment": 0,
        "implementation_weeks": 0,
        "expected_impact": {
            "cpa_reduction": 0.35,
            "revenue_maintained": 0.68,
            "budget_saved_monthly": 700,
            "alternative_keywords": ["downlights led extraplanos cocina", "downlights empotrables salon"]
        }
    }
}

# Datos de competencia (simulados de scraping)
COMPETITOR_DATA = {
    "IluminacionPro": {
        "price_downlight_similar": 18.90,  # efectoLED: 21.50
        "campaign_detected": True,
        "campaign_start": (datetime.now() - timedelta(days=5)).strftime("%Y-%m-%d"),
        "keywords_shared": ["downlights led empotrar", "downlights led salon", "downlights baratos"]
    },
    "LedShop": {
        "price_downlight_similar": 22.90,
        "stock_issues": True
    }
}

# Marketing Mix Model (datos simulados de último trimestre)
MMM_QUARTERLY_DATA = {
    "period": "Q4_2024",
    "total_revenue": 542000,
    "total_marketing_spend": 52000,
    "base_revenue": 187000,  # Sin marketing
    "channel_contribution": {
        "Google Ads": {
            "spend": 22000,
            "revenue_attributed": 98000,
            "roas": 4.45,
            "saturation_level": 0.68,
            "carryover_weeks": 2.3,
            "incremental_contribution": 0.18
        },
        "Email B2B": {
            "spend": 3000,
            "revenue_attributed": 54000,
            "roas": 18.0,
            "saturation_level": 0.15,
            "carryover_weeks": 1.1,
            "incremental_contribution": 0.10
        },
        "Meta Ads": {
            "spend": 12000,
            "revenue_attributed": 41000,
            "roas": 3.42,
            "saturation_level": 0.42,
            "carryover_weeks": 1.8,
            "incremental_contribution": 0.08
        },
        "SEO Organico": {
            "spend": 8000,
            "revenue_attributed": 82000,
            "roas": 10.25,
            "saturation_level": None,
            "carryover_weeks": None,
            "incremental_contribution": 0.15
        },
        "Email B2C": {
            "spend": 5000,
            "revenue_attributed": 28000,
            "roas": 5.6,
            "saturation_level": 0.35,
            "carryover_weeks": 0.9,
            "incremental_contribution": 0.05
        },
        "Afiliacion": {
            "spend": 2000,
            "revenue_attributed": 12000,
            "roas": 6.0,
            "saturation_level": 0.55,
            "carryover_weeks": 0.5,
            "incremental_contribution": 0.02
        }
    }
}
