import streamlit as st
import time

# إعدادات الصفحة
st.set_page_config(page_title="The 4-Minute Trader", page_icon="🦅", layout="centered")

# التنسيق الجمالي (ذهبي وأسود)
st.markdown("""
    <style>
    .main { background-color: #000000; color: #D4AF37; }
    .stButton>button { background-color: #D4AF37; color: black; border-radius: 10px; font-weight: bold; width: 100%; }
    h1 { color: #D4AF37; text-align: center; border-bottom: 2px solid #D4AF37; padding-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🦅 The 4-Minute Trader")
st.subheader("قناص الأربع دقائق")

# مؤقت الـ 4 دقائق
if 'start_time' not in st.session_state:
    st.session_state.start_time = None

if st.button("🚀 ابدأ تحليل الصفقة (4 دقائق)"):
    st.session_state.start_time = time.time()

if st.session_state.start_time:
    elapsed = time.time() - st.session_state.start_time
    remaining = max(0, 240 - int(elapsed))
    
    mins, secs = divmod(remaining, 60)
    st.metric("الوقت المتبقي لقرارك", f"{mins:02d}:{secs:02d}")
    
    if remaining > 0:
        time.sleep(1)
        st.rerun()
    else:
        st.error("⌛ انتهى الوقت! نفذ أو انسحب فوراً.")
        st.session_state.start_time = None

# منطقة رفع الشارت
uploaded_file = st.file_uploader("ارفع صورة الشارت هنا للتحليل السريع", type=['png', 'jpg', 'jpeg'])
if uploaded_file:
    st.image(uploaded_file, caption="شارت الصفقة المستهدفة")

st.info("قاعدة القناص: 1- حلل، 2- قرر، 3- نفذ، 4- اخرج. لا تسمح للمشاعر بالتدخل.")

