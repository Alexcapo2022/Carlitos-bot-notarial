import os
import uuid
import pandas as pd
import matplotlib.pyplot as plt
from langchain.tools import tool
from pydantic import BaseModel, Field
from sqlalchemy import text
from app.core.database import engine

EXPORT_DIR = "/app/app/static/exports"
BASE_URL = "http://localhost:8001/static/exports"

class ChartInput(BaseModel):
    query: str = Field(description="Consulta SQL válida. DEBE retornar exactamente 2 columnas: la primera para las etiquetas (categorías) y la segunda con valores numéricos.")
    title: str = Field(description="Título que llevará el gráfico.")
    chart_type: str = Field(description="Tipo de gráfico. Valores permitidos: 'bar', 'pie' o 'line'.")

@tool("generate_chart_tool", args_schema=ChartInput)
def generate_chart_tool(query: str, title: str, chart_type: str) -> str:
    """
    Genera un gráfico visual (imagen PNG) a partir de una consulta SQL.
    Solo utilízalo cuando el usuario pida explícitamente dibujar, graficar, o generar una imagen/gráfico.
    """
    try:
        with engine.connect() as connection:
            df = pd.read_sql(text(query), connection)
        
        if df.empty:
            return "La consulta no devolvió resultados. No se puede generar el gráfico."
            
        if len(df.columns) < 2:
            return "Error: La consulta debe devolver al menos 2 columnas (Etiquetas y Valores)."

        labels_raw = df.iloc[:, 0].astype(str).tolist()
        values = df.iloc[:, 1]
        
        # Ajustar dinámicamente la altura si hay muchas categorías (solo para barh)
        fig_height = 7
        if chart_type == 'bar' and len(labels_raw) > 8:
            fig_height = max(7, len(labels_raw) * 0.4)
            
        # Configurar la gráfica con un estilo moderno y premium
        plt.style.use('seaborn-v0_8-whitegrid')
        fig, ax = plt.subplots(figsize=(12, fig_height))
        fig.patch.set_facecolor('#ffffff')
        ax.set_facecolor('#ffffff')
        
        # Ocultar bordes innecesarios
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_color('#e2e8f0')
        ax.spines['bottom'].set_color('#e2e8f0')
        
        # Truncar labels muy largos para no romper el layout
        labels = [str(l)[:35] + '...' if len(str(l)) > 35 else str(l) for l in labels_raw]
        
        # Formateador de números (separador de miles)
        import matplotlib.ticker as ticker
        ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
        ax.set_axisbelow(True) # Grid detrás de las barras
        
        if chart_type == 'pie':
            colors = ['#2A4B5C', '#79b4c9', '#5ca7c1', '#b8d8e3', '#1c2a31', '#cbd5e1', '#64748b', '#334155']
            wedges, texts, autotexts = ax.pie(
                values, 
                autopct='%1.1f%%', 
                startangle=140, 
                textprops=dict(color="w", weight="bold"),
                colors=colors,
                wedgeprops=dict(width=0.4, edgecolor='w') # Estilo Donut
            )
            ax.legend(wedges, labels, title="Categorías", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
            ax.set_title(title.upper(), fontsize=18, fontweight='bold', pad=20, color='#1e293b', loc='left')
            
        elif chart_type == 'line':
            ax.plot(labels, values, marker='o', linewidth=3, markersize=8, color='#2A4B5C')
            ax.fill_between(labels, values, alpha=0.1, color='#2A4B5C')
            plt.xticks(rotation=45, ha="right", fontsize=11, color='#475569')
            plt.yticks(fontsize=11, color='#475569')
            ax.set_title(title.upper(), fontsize=18, fontweight='bold', pad=20, color='#1e293b', loc='left')
            ax.grid(True, axis='y', linestyle='--', alpha=0.5)
            
            # Margen extra arriba para los labels
            ax.margins(y=0.15)
            
            # Añadir data labels a los puntos
            for i, v in enumerate(values):
                ax.text(i, v + (max(values)*0.03), f'{v:,.2f}', ha='center', va='bottom', fontsize=10, fontweight='bold', color='#2A4B5C')
            
        else:
            # Por defecto 'bar'. Si son muchos labels, mejor usar barh (horizontal)
            if len(labels) > 8:
                df_sorted = df.sort_values(by=df.columns[1], ascending=True)
                labels = [str(l)[:35] + '...' if len(str(l)) > 35 else str(l) for l in df_sorted.iloc[:, 0].astype(str).tolist()]
                values = df_sorted.iloc[:, 1].tolist() # Ensure list
                
                y_pos = range(len(labels))
                bars = ax.barh(y_pos, values, color='#2A4B5C', edgecolor='none')
                
                ax.set_yticks(y_pos)
                ax.set_yticklabels(labels, fontsize=11, color='#475569')
                plt.xticks(fontsize=11, color='#475569')
                
                ax.set_title(title.upper(), fontsize=18, fontweight='bold', pad=20, color='#1e293b', loc='left')
                ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
                ax.grid(True, axis='x', linestyle='--', alpha=0.4)
                
                # Margen extra a la derecha para que los labels no se corten
                ax.margins(x=0.15)
                
                # Añadir data labels horizontales
                for bar in bars:
                    width = bar.get_width()
                    ax.text(width + (max(values)*0.015), bar.get_y() + bar.get_height()/2, 
                            f'{width:,.2f}', ha='left', va='center', fontsize=10, fontweight='bold', color='#1e293b')
            else:
                x_pos = range(len(labels))
                bars = ax.bar(x_pos, values, color='#2A4B5C', edgecolor='none', width=0.6)
                
                ax.set_xticks(x_pos)
                ax.set_xticklabels(labels, rotation=45, ha="right", fontsize=11, color='#475569')
                plt.yticks(fontsize=11, color='#475569')
                
                ax.set_title(title.upper(), fontsize=18, fontweight='bold', pad=20, color='#1e293b', loc='left')
                ax.grid(True, axis='y', linestyle='--', alpha=0.4)
                
                # Margen extra arriba para que los labels no se corten
                ax.margins(y=0.15)
                
                # Añadir data labels verticales
                for bar in bars:
                    height = bar.get_height()
                    ax.text(bar.get_x() + bar.get_width()/2, height + (max(values)*0.02),
                            f'{height:,.2f}', ha='center', va='bottom', fontsize=10, fontweight='bold', color='#1e293b')


        plt.tight_layout()

        # Generar archivo
        filename = f"grafico_{uuid.uuid4().hex[:8]}.png"
        filepath = os.path.join(EXPORT_DIR, filename)
        
        # Guardar imagen con alta resolución
        plt.savefig(filepath, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
        plt.close()

        return f"¡Gráfico generado con éxito! El usuario puede verlo/descargarlo en: {BASE_URL}/{filename}"
        
    except Exception as e:
        plt.close()
        return f"Error al generar el gráfico: {str(e)}"
