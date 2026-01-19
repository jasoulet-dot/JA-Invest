import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import datetime

st.set_page_config(page_title="MyInvest 2026", layout="wide")

# --- RÉCUPÉRATION DATA ---
def get_data(ticker):
    try:
        d = yf.Ticker(ticker).history(period="2d")
        return d['Close'].iloc[-1], ((d['Close'].iloc[-1]/d['Close'].iloc[-2])-1)*100
    except: return 0, 0

# --- TITRE ---
st.title("📱 Mon Pilotage 2026")

# --- CRÉATION DES ONGLETS (TABS) ---
tab_radar, tab_suivi, tab_cal, tab_crypto = st.tabs([
    "💎 Radar Pépites", 
    "📊 Mon Suivi (SF)", 
    "📅 Calendrier M+1", 
    "⚡ Crypto/Northern"
])

# --- TAB 1 : RADAR PÉPITES ---
with tab_radar:
    st.header("💎 Radar Décisionnel (Max 4)")
    st.caption("Données en temps réel (Yahoo Finance)")
    
    # Configuration des pépites et de leurs objectifs analystes
    # On mettra à jour cette liste et les targets ensemble
    pépites_config = {
        "ASML": {"ticker": "ASML", "target": 850.0},
        "Exail Tech": {"ticker": "EXA.PA", "target": 28.0},
        "Air Liquide": {"ticker": "AI.PA", "target": 195.0},
        "Sanofi": {"ticker": "SAN.PA", "target": 110.0}
    }
    
    cols = st.columns(2)
    for i, (nom, config) in enumerate(pépites_config.items()):
        with cols[i % 2]:
            # Récupération des données étendues
            stock = yf.Ticker(config['ticker'])
            hist = stock.history(period="8d") # 8 jours pour avoir 7 jours glissants
            
            if not hist.empty:
                prix_actuel = hist['Close'].iloc[-1]
                var_jour = ((hist['Close'].iloc[-1] / hist['Close'].iloc[-2]) - 1) * 100
                var_7j = ((hist['Close'].iloc[-1] / hist['Close'].iloc[0]) - 1) * 100
                cible = config['target']
                potentiel = ((cible / prix_actuel) - 1) * 100
                
                # Affichage de la carte
                st.subheader(nom)
                st.metric(f"{prix_actuel:.2f} €", f"{var_jour:.2f}% (24h)", delta_color="normal")
                
                st.write(f"📈 **7 jours :** {var_7j:+.2f}%")
                st.write(f"🎯 **Cible :** {cible} €")
                
                # Barre de progression du potentiel
                st.progress(min(max(potentiel/50, 0.0), 1.0)) # 50% max pour la barre
                st.caption(f"Potentiel théorique : **{potentiel:.1f}%**")
                
                keep = st.checkbox(f"Garder {nom}", value=True, key=f"k{i}")
                if not keep:
                    st.info("🔄 À remplacer demain à 8h")
                st.markdown("---")

# --- TAB 2 : SUIVI & BREAK-EVEN ---
with tab_suivi:
    st.header("Focus Salesforce")
    prix_sf, var_sf = get_data("CRM")
    
    col1, col2 = st.columns(2)
    col1.metric("Cours CRM", f"{prix_sf:.2f} $", f"{var_sf:.2f}%")
    
    st.markdown("---")
    st.subheader("Calculateur de Point Mort")
    pa = st.number_input("Ton prix d'achat ($)", value=259.0)
    qty = st.number_input("Quantité", value=0.40)
    
    diff = pa - prix_sf
    if diff > 0:
        st.error(f"Manque {diff:.2f}$ ({((pa/prix_sf)-1)*100:.1f}%) pour être à 0.")
    else:
        st.success("Tu es en profit !")

# --- TAB 3 : CALENDRIER M+1 ---
with tab_cal:
    st.header("Risques & Opportunités")
    data_cal = {
        "Date": ["20/01", "22/01", "28/01", "30/01", "05/02"],
        "Event": ["Réouverture US", "Netflix", "Microsoft/Google", "Décision Fed", "Kering"],
        "Action": ["Observer", "Prudence", "Opportunité IA", "Cash King", "Point bas ?"]
    }
    st.table(pd.DataFrame(data_cal))

# --- TAB 4 : CRYPTO & NORTHERN DATA ---
with tab_crypto:
    st.header("Lien Crypto")
    p_btc, v_btc = get_data("BTC-EUR")
    p_nd, v_nd = get_data("NB2.DE")
    
    st.metric("Bitcoin", f"{p_btc:,.0f} €", f"{v_btc:.2f}%")
    st.metric("Northern Data", f"{p_nd:.2f} €", f"{v_nd:.2f}%")
    
    if v_btc < -2:
        st.warning("⚠️ Baisse crypto : Northern Data risque de suivre.")

