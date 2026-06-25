import streamlit as st

st.title("Convertisseur de devises")

rates = {
    "EUR": 1,
    "USD": 1.1,
    "JPY": 130,
    "GBP": 0.85,
    "CAD": 1.5
}


# Initialisation de l'état de session pour les devises
if "from_currency" not in st.session_state:
    st.session_state.from_currency = "EUR"
if "to_currency" not in st.session_state:
    st.session_state.to_currency = "USD"

def swap_currencies():
    temp = st.session_state.from_currency
    st.session_state.from_currency = st.session_state.to_currency
    st.session_state.to_currency = temp

amount = st.number_input("Montant :", min_value=0.0, format="%.2f")

col1, col2 = st.columns(2)
with col1:
    from_currency = st.selectbox("De :", list(rates.keys()), key="from_currency")
with col2:
    to_currency = st.selectbox("Vers :", list(rates.keys()), key="to_currency")

st.button("Inverser les devises ⇄", on_click=swap_currencies)

if st.button("Convertir"):
    if amount <= 0:
        st.error("Le montant doit être supérieur à zéro.")
    elif from_currency == to_currency:
        st.error("La devise source et la devise cible ne doivent pas être identiques.")
    else:
        result = amount * rates[to_currency] / rates[from_currency]
        st.success(f"{amount} {from_currency} = {result:.2f} {to_currency}")
