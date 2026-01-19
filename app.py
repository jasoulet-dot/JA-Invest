import streamlit as st
import pandas as pd

# Configuration de la page pour mobile
st.set_page_config(page_title="Invest Dash 2026", page_icon="🚀", layout="wide")

# --- STYLE PERSONNALISÉ ---
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

st.title("📊 Mon Pilotage Stratégique")

# --- BARRE LATÉRALE (SIDEBAR) ---
st.sidebar.header("💰 Capital & Flux")
st.sidebar.metric("Réserve de chasse", "150 €")
st.sidebar.write("---")
st.sidebar.write("**Plans Auto :**")
st.sidebar.caption("💧 Xylem : 10€ / semaine")
st.sidebar.caption("💻 GAFAM : 100€ / mois")

# --- ONGLET 1 : PORTEFEUILLE & VIGILANCE ---
tab1, tab2, tab3 = st.tabs(["🎯 Suivi Actif", "💎 Radar Pépites", "📈 Sentiment & Crypto"])

with tab1:
    st.subheader("Mes Positions en Cours")
    
    # Données de ton portefeuille
    df = pd.DataFrame({
        "Actif": ["Salesforce", "Kering", "Northern Data", "Xylem"],
        "Statut": ["🔴 Vigilance", "🟡 Patience", "👀 Observation", "✅ DCA Actif"],
        "Action": ["Attendre rebond US", "Support 280€", "Suivre BTC", "Lissage auto"]
    })
    st.table(df)

    st.info("**💡 Note d'anticipation :** Wall Street était fermé ce lundi (MLK Day). Attention à la réouverture du mardi 20/01 à 15h30 pour confirmer la tendance sur la Tech.")

# --- ONGLET 2 : RADAR PÉPITES ---
with tab2:
    st.subheader("Opportunités à saisir (Hors GAFAM)")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("🚢 **Exail Technologies (EXAIL)**")
        st.caption("Pépite Robotique/Défense. Carnet de commandes record pour drones marins. Très solide face à la purge Tech.")
        
        st.write("🔬 **Sanofi**")
        st.caption("Alternative stable à Zealand. Gros dividende et moins de volatilité.")

    with col2:
        st.write("🏗️ **Air Liquide**")
        st.caption("Le 'Airbus' des gaz industriels. Idéal pour sécuriser tes futures entrées d'argent.")
        
        st.write("🛡️ **Waste Management**")
        st.caption("Secteur déchets. L'action anti-crise par excellence.")

# --- ONGLET 3 : SENTIMENT & CRYPTO ---
with tab3:
    st.subheader("Analyse du Marché")
    
    s1, s2 = st.columns(2)
    with s1:
        st.metric("Sentiment Global", "Peur (22/100)", "-5%")
        st.caption("Zone d'opportunité historique si on a une vision long terme.")
        
    with s2:
        st.metric("Bitcoin (BTC)", "79 600 €", "-2.4%")
        st.caption("Impact direct sur Northern Data. Support clé à surveiller.")

    st.markdown("---")
    st.write("🔔 **Prochaine Analyse :** Demain à 08:00")