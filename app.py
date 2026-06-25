import streamlit as st
import requests

API_KEY = "2a924481071b02bcdbd8ac49"  # Remplacer par votre clé sur https://www.exchangerate-api.com

st.title("Convertisseur de devises")

@st.cache_data(ttl=3600)
def get_rates(base="EUR"):
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{base}"
    response = requests.get(url)
    data = response.json()
    if data["result"] != "success":
        return None
    return data["conversion_rates"]

rates = get_rates("EUR")

if rates is None:
    st.error("Impossible de récupérer les taux de change. Vérifiez votre clé API.")
else:
    devises = ["EUR", "USD", "JPY", "GBP", "CAD"]
    amount = st.number_input("Montant :", min_value=0.0, format="%.2f")
    from_currency = st.selectbox("De :", devises)
    to_currency = st.selectbox("Vers :", devises)

    if st.button("Convertir"):
        if amount <= 0:
            st.error("Le montant doit être supérieur à zéro.")
        elif from_currency == to_currency:
            st.error("La devise source et la devise cible ne doivent pas être identiques.")
        else:
            rate = rates[to_currency] / rates[from_currency]
            result = amount * rate
            st.success(f"{amount} {from_currency} = {result:.2f} {to_currency}")
