import streamlit as st
import streamlit.components.v1 as components

# إعدادات الصفحة
st.set_page_config(page_title="KASSOUTRADES LIVE", layout="wide")

# --- 1. الذاكرة الداخلية للتطبيق (Session State) ---
if 'current_symbol' not in st.session_state:
    st.session_state.current_symbol = "FX:XAUUSD"  # الرمز الافتراضي (الذهب)
if 'trades_history' not in st.session_state:
    st.session_state.trades_history = []  # سجل الصفقات

# --- 2. دالة تغيير العملة (Update Chart) ---
def change_market(new_symbol):
    st.session_state.current_symbol = new_symbol

# --- 3. تصميم الواجهة (CSS) ---
st.markdown("""
    <style>
    .stApp { background-color: #040608; }
    .market-btn {
        background: #131722; border: 1px solid #2a2e39; color: white;
        width: 100%; padding: 10px; text-align: left; border-radius: 5px; margin-bottom: 5px;
    }
    .market-btn:hover { border-color: #D4AF37; cursor: pointer; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. توزيع المحتوى ---
col_watch, col_chart, col_exec = st.columns([1, 3, 1])

# --- القائمة الجانبية (Watchlist التفاعلية) ---
with col_watch:
    st.markdown("<h3 style='color:#D4AF37;'>WATCHLIST</h3>", unsafe_allow_html=True)
    
    # أزرار حقيقية لتغيير السوق
    if st.button("🟡 GOLD (XAUUSD)", use_container_width=True):
        change_market("FX:XAUUSD")
    if st.button("🔵 NASDAQ (NAS100)", use_container_width=True):
        change_market("CAPITALCOM:US100")
    if st.button("₿ BITCOIN (BTCUSDT)", use_container_width=True):
        change_market("BINANCE:BTCUSDT")
    if st.button("🍎 APPLE (AAPL)", use_container_width=True):
        change_market("NASDAQ:AAPL")

# --- منطقة الشارت (تتغير ديناميكياً) ---
with col_chart:
    st.subheader(f"📊 {st.session_state.current_symbol} Analysis")
    
    # الكود ديال TradingView كياخد الرمز من الذاكرة
    tv_code = f"""
    <div style="height: 600px;">
        <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
        <script type="text/javascript">
        new TradingView.widget({{
          "autosize": true, "symbol": "{st.session_state.current_symbol}", 
          "interval": "15", "theme": "dark", "style": "1", "locale": "ar", "container_id": "tv_main"
        }});
        </script><div id="tv_main"></div>
    </div> """
    components.html(tv_code, height=610)

# --- لوحة التنفيذ (Execution) ---
with col_exec:
    st.markdown("<h4 style='text-align:center;'>EXECUTION</h4>", unsafe_allow_html=True)
    lot = st.number_input("LOT", value=0.10, step=0.01)
    
    # تفعيل أزرار البيع والشراء
    if st.button("BUY 🟢", use_container_width=True):
        new_trade = {"type": "BUY", "symbol": st.session_state.current_symbol, "lot": lot, "time": "Now"}
        st.session_state.trades_history.append(new_trade)
        st.toast(f"Executed BUY on {st.session_state.current_symbol}")

    if st.button("SELL 🔴", use_container_width=True):
        new_trade = {"type": "SELL", "symbol": st.session_state.current_symbol, "lot": lot, "time": "Now"}
        st.session_state.trades_history.append(new_trade)
        st.toast(f"Executed SELL on {st.session_state.current_symbol}")

    st.write("---")
    st.markdown("**Recent Trades:**")
    for trade in reversed(st.session_state.trades_history[-3:]):
        st.write(f"{trade['type']} {trade['symbol']} ({trade['lot']})")
