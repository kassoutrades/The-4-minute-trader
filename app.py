import streamlit as st
import time
from datetime import datetime
import streamlit.components.v1 as components

# إعدادات الصفحة
st.set_page_config(page_title="The 4-Minute Trader | kassoutrades", page_icon="🦅", layout="wide")

# التنسيق الجمالي الذهبي
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #D4AF37; }
    h1, h2, h3 { color: #D4AF37 !important; text-align: center; font-weight: bold; }
    .developer-footer { text-align: center; padding: 15px; color: #D4AF37; border-top: 1px solid #D4AF37; margin-top: 30px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- العنوان الرئيسي ---
st.title("🦅 The 4-Minute Trader")
st.markdown("<h3 style='text-align: center;'>بواسطة المطور: kassoutrades</h3>", unsafe_allow_html=True)

# --- القائمة الجانبية ---
st.sidebar.header("🕹️ لوحة التحكم")
symbol = st.sidebar.text_input("اكتب رمز الزوج (مثال: BTCUSD أو EURUSD)", "BTCUSD")
journal_type = st.sidebar.selectbox("📒 نوع السجل", ["اليومي", "الأسبوعي", "الشهري", "السنوي"])

# --- القسم الأول: الشارت الحي (TradingView) ---
st.header(f"📈 الرسم البياني المباشر: {symbol}")

# كود HTML لدمج TradingView
tradingview_widget = f"""
<div class="tradingview-widget-container" style="height:500px;">
  <div id="tradingview_12345" style="height:500px;"></div>
  <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
  <script type="text/javascript">
  new TradingView.widget({{
    "autosize": true,
    "symbol": "{symbol}",
    "interval": "15",
    "timezone": "Etc/UTC",
    "theme": "dark",
    "style": "1",
    "locale": "ar",
    "toolbar_bg": "#f1f3f6",
    "enable_publishing": false,
    "hide_side_toolbar": false,
    "allow_symbol_change": true,
    "container_id": "tradingview_12345"
  }});
  </script>
</div>
"""
components.html(tradingview_widget, height=520)

st.write("---")

# --- القسم الثاني: المؤقت والجورنال ---
col1, col2 = st.columns([1, 1])

with col1:
    st.header("⏱️ مؤقت الـ 4 دقائق")
    if st.button('🚀 ابدأ التحليل الآن'):
        end_time = time.time() + 240
        t = st.empty()
        while time.time() < end_time:
            remaining = int(end_time - time.time())
            mins, secs = divmod(remaining, 60)
            t.metric("الوقت المتبقي", f"{mins:02d}:{secs:02d}")
            time.sleep(1)
        st.error("⌛ انتهى الوقت! نفذ قرارك.")

with col2:
    st.header(f"📝 {journal_type}")
    trade_notes = st.text_area("سجل ملاحظاتك الفنية هنا...")
    if st.button("حفظ الملاحظة"):
        st.success(f"تم الحفظ بنجاح يا {symbol}!")

# --- التذييل ---
st.markdown(f'<div class="developer-footer">حقوق التطوير محفوظة © 2026 | kassoutrades 🦅</div>', unsafe_allow_html=True)
