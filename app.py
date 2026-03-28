import streamlit as st
import streamlit.components.v1 as components

# إعدادات الصفحة
st.set_page_config(page_title="KASSOUTRADES | Pro Watchlist", layout="wide")

# --- CSS لتنسيق الـ Watchlist بحال TradingView ---
st.markdown("""
    <style>
    .stApp { background-color: #040608; }
    .watchlist-container {
        background: #131722;
        border-radius: 10px;
        padding: 10px;
        border: 1px solid #2a2e39;
    }
    .market-item {
        display: flex;
        justify-content: space-between;
        padding: 12px 8px;
        border-bottom: 1px solid #2a2e39;
        transition: 0.3s;
    }
    .market-item:hover { background: #1e222d; cursor: pointer; }
    .symbol-name { font-weight: bold; color: #d1d4dc; }
    .price-up { color: #089981; }
    .price-down { color: #f23645; }
    .gold-glow { color: #D4AF37; font-weight: 900; text-align: center; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- الهيكل الرئيسي (Layout) ---
col_watch, col_chart, col_exec = st.columns([1.2, 3, 1], gap="small")

with col_watch:
    st.markdown('<h3 class="gold-glow">WATCHLIST 📊</h3>', unsafe_allow_html=True)
    
    # محاكاة قائمة المراقبة (Watchlist)
    markets = [
        {"name": "NQ1!", "desc": "Nasdaq 100", "price": "24,291.75", "change": "-0.3%", "up": False},
        {"name": "NAS100", "desc": "NASDAQ 100 Index", "price": "23,068.6", "change": "-2.34%", "up": False},
        {"name": "XAUUSD", "desc": "Gold Spot", "price": "4,493.68", "change": "+2.64%", "up": True},
        {"name": "BTCUSDT", "desc": "Bitcoin", "price": "66,376.91", "change": "-0.15%", "up": False},
    ]
    
    st.markdown('<div class="watchlist-container">', unsafe_allow_html=True)
    for m in markets:
        color_class = "price-up" if m["up"] else "price-down"
        st.markdown(f"""
            <div class="market-item">
                <div>
                    <div class="symbol-name">{m['name']}</div>
                    <div style="font-size: 10px; color: #868993;">{m['desc']}</div>
                </div>
                <div style="text-align: right;">
                    <div class="symbol-name">{m['price']}</div>
                    <div class="{color_class}" style="font-size: 12px;">{m['change']}</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.write("")
    st.button("+ Add Symbol", use_container_width=True)

with col_chart:
    # الشارت الرئيسي
    tv_code = """
    <div style="height: 650px;">
        <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
        <script type="text/javascript">
        new TradingView.widget({
          "autosize": true, "symbol": "FX:XAUUSD", "interval": "15",
          "theme": "dark", "style": "1", "locale": "ar", "container_id": "tv_main"
        });
        </script><div id="tv_main"></div>
    </div> """
    components.html(tv_code, height=660)

with col_exec:
    st.markdown("<h4 style='color: white; text-align:center;'>EXECUTION</h4>", unsafe_allow_html=True)
    st.number_input("LOT", value=0.10)
    st.button("BUY", key="b1")
    st.button("SELL", key="s1")
    st.write("---")
    st.markdown("<p style='text-align:center; font-size:10px;'>KASSOUTRADES V3.0</p>", unsafe_allow_html=True)
