
import streamlit as st

pip_values = {
    "EURUSD": 1.00, "GBPUSD": 1.00, "USDJPY": 0.60, "EURJPY": 0.91,
    "GBPJPY": 0.60, "AUDJPY": 0.91, "CHFJPY": 0.91, "CADJPY": 0.91,
    "NZDJPY": 0.91, "BTCUSD": 1.00, "XAUUSD": 10.00
}

st.set_page_config(page_title="Forex Risk Calculator", layout="centered")

st.title("💹 Forex Lot Size & Risk Calculator")

balance = st.number_input("Account Balance ($)", min_value=1.0, step=1.0)
losing_trades = st.number_input("Lose Account In How Many Trades", min_value=1, step=1)
stop_loss = st.number_input("Stop Loss (pips)", min_value=0.1, step=0.1)
take_profit = st.number_input("Take Profit (pips)", min_value=0.1, step=0.1)
pair = st.selectbox("Currency Pair", list(pip_values.keys()))

if st.button("📊 Calculate Lot Size"):
    pip_value = pip_values.get(pair, 1.0)
    risk_per_trade = balance / losing_trades
    lot_size = risk_per_trade / (stop_loss * pip_value)
    profit = take_profit * lot_size * pip_value

    st.success("✅ Calculation Result")
    st.markdown(f"""
        **Currency Pair:** {pair}  
        **Pip Value per Lot:** ${pip_value:.2f}  
        **Risk per Trade:** ${risk_per_trade:.2f}  
        **Recommended Lot Size:** {lot_size:.2f} lots  
        **Profit if TP Hits:** ${profit:.2f}  
    """)

    st.code(f"Lot Size: {lot_size:.2f} | Profit: ${profit:.2f}", language="text")
