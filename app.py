import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

st.set_page_config(page_title="Smart Invest 2026", layout="wide")

# --- FONCTION DE RÉCUPÉRATION DATA ---
def get_stock_data(ticker):
    try:
        data = yf.Ticker(ticker).history(period="1y")
        return data['Close'].iloc[-1], data['Close'].iloc[-2]
    except:
        return 0, 0

# --- HEADER ---
st.title("🚀 Mon Pilotage Stratégique 2026")
st.caption(f"Dernière mise à jour : {datetime.now().strftime('%d/%m/%Y %H:%M')}")

# --- SECTION 1 : MATRICE DE DÉCISION AUTOMATIQUE ---
st.header("🎯 Matrice de Décision")
btc_price, btc_old = get_stock_data("BTC-EUR")
nd_price, nd_old = get_stock_data("NB2.DE") # Northern Data

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Sentiment Marché", "PEUR (Fear)", "-12% vs hier")
    st.info("💡 Stratégie : Zone d'accumulation. Ne pas vendre.")
with col2:
    st.metric("Bitcoin (Lien Northern Data)", f"{btc_price:,.0f} €", f"{((btc_price/btc_old)-1)*100:.2f}%")
with col3:
    st.metric("Northern Data", f"{nd_price:.2f} €", f"{((nd_price/nd_old)-1)*100:.2f}%")

# --- SECTION 2 : CALENDRIER RISQUES & OPPORTUNITÉS (M+1) ---
st.header("📅 Calendrier Stratégique (Janv/Fév 2026)")
cal_data = {
    "Date": ["19/01", "20/01", "22/01", "28/01", "30/01", "05/02"],
    "Événement": ["MLK Day (Fermeture US)", "Réouverture Wall Street", "Résultats Netflix", "Résultats Microsoft/Google", "Décision Taux (Fed)", "Résultats Kering"],
    "Impact": ["🧊 Nul", "⚡ Volatilité Haute", "🎬 Secteur Streaming", "💻 Crucial pour l'IA", "💵 Tendance Marché", "👜 Luxe / Gucci"],
    "Action": ["Attendre", "Observer le rebond", "Vigilance GAFAM", "Opportunité achat ?", "Gestion du cash", "Surveiller point bas"]
}
st.table(pd.DataFrame(cal_data))

# --- SECTION 3 : PILOTAGE SALESFORCE (BREAK-EVEN) ---
st.header("🧮 Calculateur de Sortie : Salesforce")
col_sf1, col_sf2 = st.columns(2)
with col_sf1:
    prix_achat = st.number_input("Ton prix d'achat moyen ($)", value=259.0)
    quantite = st.number_input("Nombre d'actions possédées", value=0.40) # Env 100€
    prix_actuel, _ = get_stock_data("CRM")
    
    perte_gain = (prix_actuel - prix_achat) * quantite
    st.subheader(f"Statut : {'🔴 Perte' if perte_gain < 0 else '🟢 Gain'}")
    st.write(f"Montant : {perte_gain:.2f} $")

with col_sf2:
    st.write("📈 **Objectif de récupération :**")
    diff = prix_achat - prix_actuel
    if diff > 0:
        st.error(f"L'action doit reprendre **{diff:.2f} $** ({((prix_achat/prix_actuel)-1)*100:.1f}%) pour atteindre ton point mort.")
    else:
        st.success("Tu es en profit !")

# --- SECTION 4 : RADAR PÉPITES ---
st.header("💎 Le Radar à Pépites")
st.write("Actions à surveiller pour tes 150€ restants :")
col_p1, col_p2, col_p3 = st.columns(3)
col_p1.button("ASML (Tech Safe)")
col_p2.button("Exail (Défense/Robotique)")
col_p3.button("Air Liquide (Stabilité)")
