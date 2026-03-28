import streamlit as st
import time
from datetime import datetime
import streamlit.components.v1 as components

# إعدادات الصفحة الاحترافية (كامل العرض)
st.set_page_config(page_title="Kassoutrades Pro Terminal | Real Trading & Replay", page_icon="🦅", layout="wide")

# --- محرك التصميم المتقدم (Dark Mode + Neon) ---
st.markdown("""
    <style>
    .stApp { background: #06080a; color: #e0e0e0; font-family: 'Inter', sans-serif; }
    
    /* تصميم الهيدر الذهبي المتوهج */
    .terminal-header {
        background: rgba(255, 255, 255, 0.03);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid rgba(212, 175, 55, 0.2);
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0px 4px 15px rgba(212, 175, 55, 0.1);
    }
    
    .gold-text { color: #D4AF37 !important; text-shadow: 0px 0px 10px rgba(212, 175, 55, 0.5); }
    
    /* تصميم القائمة الجانبية (Darkest Mode) */
    section[data-testid="stSidebar"] {
        background-color: #030405 !important;
        border-right: 1px solid rgba(212, 175, 55, 0.2);
    }
    
    /* أزرار التداول الاحترافية المتوهجة */
    .stButton>button { border-radius: 8px !important; height: 3.5em !important; font-weight: bold !important; transition: all 0.3s ease !important; border: none !important; }
    
    /* زر الشراء */
    div.stButton > button:first-child[key="buy_btn"] {
        background: linear-gradient(135deg, #00c853 0%, #b2ff59 100%) !important;
        color: black !important;
        box-shadow: 0 4px 15px rgba(0, 200, 83, 0.4) !important;
    }
    div.stButton > button:first-child[key="buy_btn"]:hover { box-shadow: 0 8px 25px rgba(0, 200, 83, 0.7) !important; transform: translateY(-3px); }

    /* زر البيع */
    div.stButton > button:first-child[key="sell_btn"] {
        background: linear-gradient(135deg, #d50000 0%, #ff5252 100%) !important;
        color: white !important;
        box-shadow: 0 4px 15px rgba(213, 0, 0, 0.4) !important;
    }
    div.stButton > button:first-child[key="sell_btn"]:hover { box-shadow: 0 8px 25px rgba(213, 0, 0, 0.7) !important; transform: translateY(-3px); }
    
    /* تنسيق التبويبات (Tabs) */
    .stTabs [data-baseweb="tab-list"] { gap: 15px; background: transparent; }
    .stTabs [data-baseweb="tab"] {
        height: 55px;
        background-color: rgba(255, 255, 255, 0.05);
        border-radius: 10px 10px 0px 0px;
        color: #D4AF37;
        font-weight: bold;
    }
    .stTabs [aria-selected="true"] { background-color: rgba(212, 175, 55, 0.1) !important; color: #f1c40f !important; }
    </style>
    """, unsafe_allow_html=True)

# --- الهيدر الاحترافي ---
st.markdown("""
    <div class="terminal-header">
        <h1 class="gold-text">🦅 KASSOUTRADES ADVANCED TERMINAL</h1>
        <p style="font-size: 0.9em; opacity: 0.7;">The Ultimate Trading & Backtesting Engine | Real-Time Data & Replay</p>
    </div>
    """, unsafe_allow_html=True)

# --- القائمة الجانبية (لوحة التحكم) ---
st.sidebar.markdown("<h2 style='text-align: center; color: #D4AF37;'>لوحة التحكم</h2>", unsafe_allow_html=True)
st.sidebar.write("---")
symbol = st.sidebar.text_input("💎 الرمز (مثال: GOLD, EURUSD)", "GOLD")
user_plan = st.sidebar.selectbox("💳 العضوية", ["Premium ⭐", "Free"])

# --- توزيع محتوى الصفحة (Layout) ---
tab1, tab2, tab3 = st.tabs(["📊 التداول الحي (Live Trading)", "🧪 نظام الباكتيست والـ Replay", "📒 الجورنال الذكي"])

with tab1:
    col_main, col_tools = st.columns([3.5, 1])
    
    with col_main:
        st.header(f"📈 السعر المباشر: {symbol}")
        # شارت TradingView الفخم بكل أدواته
        tv_html = f"""
        <div class="tradingview-widget-container" style="height:600px;"><div id="tv_full"></div>
        <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
        <script type="text/javascript">new TradingView.widget({{"autosize": true,"symbol": "{symbol}","interval": "15","timezone": "Etc/UTC","theme": "dark","style": "1","locale": "ar","toolbar_bg": "#f1f3f6","enable_publishing": false,"withdateranges": true,"hide_side_toolbar": false,"allow_symbol_change": true,"studies": ["RSI@tv-basicstudies", "MASimple@tv-basicstudies"],"details": true,"hotlist": true,"calendar": true,"show_popup_button": true,"container_id": "tv_full"}});</script>
        </div>"""
        components.html(tv_html, height=620)

    with col_tools:
        st.markdown("<h3 style='text-align: center;'>🛒 لوحة التنفيذ</h3>", unsafe_allow_html=True)
        lot_size = st.number_input("اللوت (Lot)", 0.01, 10.0, 0.10)
        
        c1, c2 = st.columns(2)
        with c1:
            if st.button("BUY 🟢", key="buy_btn"):
                st.toast(f"🚀 تم فتح صفقة شراء {lot_size}R")
        with c2:
            if st.button("SELL 🔴", key="sell_btn"):
                st.toast(f"🔻 تم فتح صفقة بيع {lot_size}R")
        
        st.write("---")
        st.markdown("<h4 style='text-align: center;'>⏳ مؤقت الـ 4 دقائق</h4>", unsafe_allow_html=True)
        if st.button("ابدأ تحليل الصفقة"):
            placeholder = st.empty()
            for i in range(240, -1, -1):
                placeholder.metric("الوقت المتبقي", f"{i//60:02d}:{i%60:02d}")
                time.sleep(1)
            st.error("⌛ انتهى الوقت!")

with tab2:
    if user_plan == "Premium ⭐":
        st.header("🧪 وحدة الباكتيست والـ Replay الاحترافية")
        col_replay, col_results = st.columns([2, 1])
        
        with col_replay:
            st.subheader("إعادة تشغيل حركة السعر (Price Replay)")
            replay_symbol = st.text_input("أدخل الزوج للباكتيست", symbol)
            # دمج أداة الباكتيست من TradingView
            tv_replay_widget = f"""
            <div class="tradingview-widget-container" style="height:450px;"><div id="tv_replay"></div>
            <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
            <script type="text/javascript">new TradingView.widget({{"autosize": true,"symbol": "{replay_symbol}","interval": "5","theme": "dark","style": "1","locale": "ar","toolbar_bg": "#f1f3f6","withdateranges": true,"hide_side_toolbar": false,"allow_symbol_change": true,"studies": ["MASimple@tv-basicstudies"],"container_id": "tv_replay"}});</script>
            </div>"""
            components.html(tv_replay_widget, height=470)
            
            st.info("💡 استخدم أدوات الشارت (إعادة تشغيل البار) داخل TradingView لتفعيل خاصية الريبلاي (البار بار).")

        with col_results:
            st.subheader("📊 تحليل النتائج")
            wins = st.number_input("الناجحة", 0)
            losses = st.number_input("الخاسرة", 0)
            rr = st.number_input("العائد للمخاطرة (RR)", 2.0)
            
            if st.button("احسب العائد"):
                total_r = (wins * rr) - losses
                st.success(f"النتيجة المتوقعة: {total_r:.1f}R")
                if total_r > 0: st.write("✅ استراتيجية رابحة.")
    else:
        st.warning("⚠️ خاصية الباكتيست والـ Replay متاحة فقط للمشتركين Premium ⭐.")
        if st.button("الترقية الآن"): st.balloons()

with tab3:
    st.header("📒 سجل التداول اليومي الذكي")
    trade_summary = st.text_area("تحدث كقناص (لماذا دخلت؟ ماذا تعلمت؟)")
    if st.button("حفظ في الجورنال"): st.success("تم الحفظ بنجاح!")

# --- التذييل الإبداعي (Creative Footer) ---
st.markdown(f"""
    <div style="text-align: center; padding: 40px; opacity: 0.5; font-size: 0.8em; border-top: 1px dashed rgba(212, 175, 55, 0.3); margin-top: 50px;">
        Designed & Developed by <span style="color: #D4AF37; font-weight: bold;">KASSOUTRADES</span> | © 2026<br>
        Eagle Eye Accuracy - Predator Speed
    </div>
    """, unsafe_allow_html=True)
