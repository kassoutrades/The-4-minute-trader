import streamlit as st
import time
import streamlit.components.v1 as components

# إعدادات الشاشة الكاملة وإخفاء قوائم ستريمليت الافتراضية
st.set_page_config(page_title="KASSOUTRADES | Ultra Terminal", layout="wide", initial_sidebar_state="collapsed")

# --- CSS السحري (تصميم من كوكب آخر) ---
st.markdown("""
    <style>
    /* خلفية داكنة مع لمسات إضاءة نيون */
    .stApp {
        background: #020202;
        background-image: radial-gradient(circle at 20% 30%, #1a1a1a 0%, #020202 100%);
    }

    /* إخفاء عناصر ستريمليت المزعجة */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* الحاويات الزجاجية (Glass Cards) */
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(212, 175, 55, 0.1);
        border-radius: 20px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.8);
    }

    /* أزرار النيون (Neon Buttons) */
    .stButton > button {
        width: 100%;
        border-radius: 12px !important;
        height: 60px !important;
        font-size: 18px !important;
        font-weight: 900 !important;
        text-transform: uppercase;
        letter-spacing: 2px;
        transition: 0.4s all ease !important;
        border: none !important;
    }

    /* زر الشراء المتوهج */
    div[data-testid="stVerticalBlock"] > div:nth-child(2) button {
        background: linear-gradient(90deg, #00ff87 0%, #60efff 100%) !important;
        color: #000 !important;
        box-shadow: 0px 0px 20px rgba(0, 255, 135, 0.3) !important;
    }

    /* زر البيع المتوهج */
    div[data-testid="stVerticalBlock"] > div:nth-child(4) button {
        background: linear-gradient(90deg, #f12711 0%, #f5af19 100%) !important;
        color: #fff !important;
        box-shadow: 0px 0px 20px rgba(241, 39, 17, 0.3) !important;
    }

    /* مؤقت القناص الرقمي */
    .timer-display {
        font-family: 'Courier New', Courier, monospace;
        font-size: 48px;
        font-weight: bold;
        color: #D4AF37;
        text-align: center;
        text-shadow: 0px 0px 15px rgba(212, 175, 55, 0.5);
    }
    </style>
    """, unsafe_allow_html=True)

# --- الهيدر الاحترافي (بدون خلفية ستريمليت) ---
st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 0px;">
        <h2 style="color: #D4AF37; letter-spacing: 3px; font-weight: 900;">🦅 KASSOUTRADES <span style="color: white; font-weight: 100;">TERMINAL</span></h2>
        <div style="background: rgba(212,175,55,0.1); padding: 5px 15px; border-radius: 50px; border: 1px solid #D4AF37; color: #D4AF37; font-size: 12px;">SERVER: LIVE 🟢</div>
    </div>
    """, unsafe_allow_html=True)

# --- توزيع المساحات (Main Layout) ---
col_left, col_right = st.columns([4, 1.2], gap="medium")

with col_left:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    # دمج TradingView مع تفعيل "Full Toolbar" والمؤشرات
    tv_code = """
    <div style="height: 700px;">
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
          "enable_publishing": false,
          "withdateranges": true,
          "hide_side_toolbar": false,
          "allow_symbol_change": true,
          "studies": ["RSI@tv-basicstudies", "MASimple@tv-basicstudies"],
          "container_id": "tv_chart"
        });
        </script>
        <div id="tv_chart"></div>
    </div>
    """
    components.html(tv_code, height=710)
    st.markdown('</div>', unsafe_allow_html=True)

with col_right:
    # لوحة الأوامر
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: white;'>EXECUTION</h4>", unsafe_allow_html=True)
    st.number_input("QUANTITY", value=0.10, step=0.01)
    st.button("BUY / LONG")
    st.write("")
    st.button("SELL / SHORT")
    st.markdown('</div>', unsafe_allow_html=True)

    # مؤقت القناص
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 12px; color: #888;'>PREDATOR TIMER</p>", unsafe_allow_html=True)
    if st.button("START 4-MIN SCAN"):
        t_display = st.empty()
        for i in range(240, -1, -1):
            m, s = divmod(i, 60)
            t_display.markdown(f'<p class="timer-display">{m:02d}:{s:02d}</p>', unsafe_allow_html=True)
            time.sleep(1)
    st.markdown('</div>', unsafe_allow_html=True)

# الجورنال أسفل الشاشة بشكل ممتد
st.markdown('<div class="glass-card">', unsafe_allow_html=True)
st.subheader("📒 JOURNAL LOGS")
st.text_area("Analyze your entry psychology here...", placeholder="Why now? What's the plan?")
if st.button("SAVE TO DATABASE"):
    st.success("Entry Secured.")
st.markdown('</div>', unsafe_allow_html=True)
