import streamlit as st
import io
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import simpleSplit

def inject_custom_css():
    st.markdown("""
    <style>
        /* Gradient Background */
        .stApp {
            background: radial-gradient(circle at top right, #1e293b, #0f172a);
            font-family: 'Inter', sans-serif;
        }
        /* Dashboard Card Look */
        .stCard {
            background: rgba(30, 41, 59, 0.7);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 16px;
            padding: 25px;
            backdrop-filter: blur(10px);
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
            margin-bottom: 20px;
        }
        /* Custom Typography */
        h1, h2, h3 { color: #f8fafc !important; font-weight: 700 !important; }
        .stMetric { background: rgba(255,255,255,0.05); padding: 15px; border-radius: 12px; }
        /* Professional Buttons */
        .stButton>button {
            background: linear-gradient(90deg, #3b82f6, #2563eb);
            border: none; border-radius: 8px; color: white; padding: 12px 24px;
            font-weight: 600; transition: all 0.3s ease;
        }
        .stButton>button:hover { transform: translateY(-2px); box-shadow: 0 5px 15px rgba(59,130,246,0.4); }
        /* Tab Styling */
        .stTabs [data-baseweb="tab-list"] { gap: 10px; }
        .stTabs [data-baseweb="tab"] {
            background-color: rgba(255,255,255,0.05);
            border-radius: 4px;
            color: #cbd5e1;
        }
    </style>
    """, unsafe_allow_html=True)

def generate_pdf_report(report_text, coin):
    """Generates a professional PDF document from the AI report text."""
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter
    
    # Title
    p.setFont("Helvetica-Bold", 18)
    p.drawString(50, height - 50, f"CryptoInsight Pro Analysis: {coin}")
    p.line(50, height - 60, width - 50, height - 60)
    
    # Body Content
    p.setFont("Helvetica", 11)
    y = height - 100
    
    # Wrap text to fit page width
    lines = simpleSplit(report_text, "Helvetica", 11, width - 100)
    
    for line in lines:
        if y < 50: # New page if bottom reached
            p.showPage()
            p.setFont("Helvetica", 11)
            y = height - 50
        p.drawString(50, y, line)
        y -= 15
        
    p.save()
    buffer.seek(0)
    return buffer
    