import streamlit as st
import time
import streamlit.components.v1 as components

# إعدادات الشاشة الكاملة وإخفاء هوية Streamlit تماماً
st.set_page_config(page_title="KASSOUTRADES | Ultra Terminal", layout="wide", initial_sidebar_state="collapsed")

# --- CSS هندسة الواجهة (Ultra-Dark UI) ---
st.markdown("""
    <style>
    /* إخفاء القوائم الافتراضية لتركيز كامل على المنصة */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .stApp {
        background: #020406;
        color: #e0e0e0;
    }

    /* الحاويات الزجاجية (Glassmorphism) */
    .trade-container {
        background: rgba(13, 17, 23, 0.8);
        border: 1px solid rgba(212, 175, 55, 0.15);
        border-radius: 12px;
        padding: 15px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.5);
    }

    /* تصميم أزرار التنفيذ الفوري */
    .stButton > button {
        width: 100%;
        border-radius: 8px !important;
        height: 55px !important;
        font-weight: 800 !important;
        text-transform: uppercase;
        border: none !important;
        transition: 0.3s ease-in-out !important;
    }

    /* زر الشراء النيوني */
    div[data-testid="stVerticalBlock"] > div:has(button:contains("BUY")) button {
        background: linear-gradient(90deg, #00c853, #64ffda) !important;
        color: #000 !important;
        box-shadow: 0 0 15px rgba(0, 200, 83, 0.3) !important;
    }

    /* زر البيع النيوني */
    div[data-testid="stVerticalBlock"] > div:has(button:contains("SELL")) button {
        background: linear-gradient(90deg, #ff1744, #f50057) !important;
        color: #fff !important;
        box-shadow: 0 0 15px rgba(255, 23, 68, 0.3) !important;
    }

    /* مؤقت القناص الاحترافي */
    .timer-text {
        font-family: 'Monaco', monospace;
        font-size: 3rem;
        color: #D4AF37;
        text-align: center;
        text-shadow: 0 0 10px rgba(212, 175, 55, 0.4);
    }
    </style>
    """, unsafe_allow_html=True)

# --- الهيدر (Topbar) ---
cols = st.columns([2, 5, 2])
with cols[0]:
    st.markdown("<h2 style='color: #D4AF37; margin:0;'>🦅 KASSOUTRADES</h2>", unsafe_allow_html=True)
with cols[2]:
    st.markdown("<div style='text-align:right; color:#00ff87; font-size:12px;'>● CONNECTED TO DATA CENTER</div>", unsafe_allow_html=True)

st.markdown("---")

# --- توزيع المساحات: الشارت ومركز العمليات ---
col_left, col_right = st.columns([4, 1.2])

with col_left:
    # الشارت المدمج مع خاصية Bar Replay
    st.markdown('<div class="trade-container">', unsafe_allow_html=True)
    tv_code = """
    <div style="height: 720px;">
        <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
        <script type="text/javascript">
        new TradingView.widget({
          "autosize": true,
          "symbol": "BINANCE:BTCUSDT",
          "interval": "15",
          "theme": "dark",
          "style": "1",
          "locale": "ar",
          "toolbar_bg": "#f1f3f6",
          "withdateranges": true,
          "hide_side_toolbar": false,
          "allow_symbol_change": true,
          "save_image": true,
          "studies": ["RSI@tv-basicstudies", "MASimple@tv-basicstudies"],
          "container_id": "tv_chart_main"
        });
        </script>
        <div id="tv_chart_main"></div>
    </div>
    """
    components.html(tv_code, height=730)
    st.markdown('</div>', unsafe_allow_html=True)

with col_right:
    # لوحة التحكم في التنفيذ (Execution Desk)
    st.markdown('<div class="trade-container">', unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#888; font-size:12px;'>ORDER TYPE: MARKET</p>", unsafe_allow_html=True)
    lot = st.number_input("LOT SIZE", value=0.10, step=0.01)
    
    if st.button("BUY / LONG"):
        st.toast("ORDER EXECUTED: BUY AT MARKET")
    
    st.write("")
    if st.button("SELL / SHORT"):
        st.toast("ORDER EXECUTED: SELL AT MARKET")
    st.markdown('</div>', unsafe_allow_html=True)

    # مؤقت القناص (Predator Timer)
    st.markdown('<div class="trade-container" style="margin-top:20px;">', unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#D4AF37; margin-bottom:0;'>4-MIN SCANNER</p>", unsafe_allow_html=True)
    if st.button("ACTIVATE SCAN"):
        placeholder = st.empty()
        for i in range(240, -1, -1):
            m, s = divmod(i, 60)
            placeholder.markdown(f'<p class="timer-text">{m:02d}:{s:02d}</p>', unsafe_allow_html=True)
            time.sleep(1)
    st.markdown('</div>', unsafe_allow_html=True)

# الجورنال الاحترافي في الأسفل
st.markdown('<div class="trade-container" style="margin-top:20px;">', unsafe_allow_html=True)
st.subheader("📒 PRO JOURNAL LOGS")
notes = st.text_area("Analyze the 'Bar Replay' findings and entry psychology...", height=150)
if st.button("COMMIT TO DATABASE"):
    st.success("Analysis Archived Successfully.")
st.markdown('</div>', unsafe_allow_html=True)
