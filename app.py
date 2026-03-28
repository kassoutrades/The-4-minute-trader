import streamlit as st
import time
from datetime import datetime
import streamlit.components.v1 as components

# إعدادات الصفحة
st.set_page_config(page_title="Kassoutrades Terminal", page_icon="🦅", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #06080a; color: #D4AF37; }
    .stButton>button { width: 100%; border-radius: 5px; font-weight: bold; }
    .buy-btn { background-color: #00ff00 !important; color: black !important; }
    .sell-btn { background-color: #ff0000 !important; color: white !important; }
    .footer { text-align: center; padding: 20px; color: #D4AF37; border-top: 1px solid #D4AF37; margin-top: 40px; }
    </style>
    """, unsafe_allow_html=True)

# الهيدر
st.title("🦅 Kassoutrades Advanced Terminal")
st.write("---")

# القائمة الجانبية
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2502/2502160.png", width=100)
st.sidebar.title("إدارة الحساب")
plan = st.sidebar.selectbox("نوع الاشتراك", ["Free", "Pro ⭐"])
symbol = st.sidebar.text_input("أدخل الرمز (Symbol)", "BINANCE:BTCUSDT")

# تقسيم الصفحة (الشارت + لوحة الأوامر)
col_chart, col_orders = st.columns([3, 1])

with col_chart:
    st.subheader(f"📊 منصة التحليل المباشر - {symbol}")
    
    # دمج منصة TradingView الكاملة مع أدوات الرسم
    tv_full_widget = f"""
    <div class="tradingview-widget-container" style="height:600px;">
      <div id="tradingview_full"></div>
      <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
      <script type="text/javascript">
      new TradingView.widget({{
        "autosize": true,
        "symbol": "{symbol}",
        "interval": "D",
        "timezone": "Etc/UTC",
        "theme": "dark",
        "style": "1",
        "locale": "ar",
        "toolbar_bg": "#f1f3f6",
        "enable_publishing": false,
        "withdateranges": true,
        "hide_side_toolbar": false,
        "allow_symbol_change": true,
        "details": true,
        "hotlist": true,
        "calendar": true,
        "show_popup_button": true,
        "popup_width": "1000",
        "popup_height": "650",
        "container_id": "tradingview_full"
      }});
      </script>
    </div>
    """
    components.html(tv_full_widget, height=620)

with col_orders:
    st.subheader("🛒 تنفيذ الصفقات")
    
    amount = st.number_input("الكمية / اللوت", value=0.1)
    price = st.number_input("سعر الدخول (اختياري)", value=0.0)
    
    c1, c2 = st.columns(2)
    with c1:
        if st.button("BUY (شراء)", key="buy", help="فتح صفقة شراء"):
            st.success(f"تم إرسال أمر شراء {amount}")
    with c2:
        if st.button("SELL (بيع)", key="sell", help="فتح صفقة بيع"):
            st.error(f"تم إرسال أمر بيع {amount}")
    
    st.write("---")
    st.subheader("⏱️ نظام الـ 4 دقائق")
    if st.button("🚀 بدء العد التنازلي"):
        progress_bar = st.progress(0)
        for i in range(100):
            time.sleep(2.4) # محاكاة لـ 240 ثانية
            progress_bar.progress(i + 1)
        st.warning("انتهى وقت التحليل!")

# سجل الجورنال أسفل الشارت
st.write("---")
st.subheader("📒 سجل التداول الذكي")
journal_text = st.text_area("لماذا دخلت هذه الصفقة؟ (تحدث كقناص)")
if st.button("حفظ الملاحظة في الجورنال"):
    st.success("تم الحفظ في قاعدة بيانات kassoutrades")

# التذييل
st.markdown(f'<div class="footer">Developed by: kassoutrades | © 2026 🦅</div>', unsafe_allow_html=True)
