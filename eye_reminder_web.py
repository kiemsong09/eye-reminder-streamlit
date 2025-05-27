import streamlit as st
import time

st.set_page_config(page_title="Nhắc nghỉ mắt 20-20-20", layout="centered")

st.title("👁️‍🗨️ Nhắc nghỉ mắt 20-20-20")
st.markdown("**Cứ mỗi 20 phút, hãy nhìn xa 20 feet trong 20 giây để bảo vệ mắt.**")

interval = st.number_input("⏱️ Khoảng thời gian giữa mỗi lần nhắc (phút)", min_value=1, value=20)

if "running" not in st.session_state:
    st.session_state.running = False

def start_timer():
    st.session_state.running = True

def stop_timer():
    st.session_state.running = False

col1, col2 = st.columns(2)
with col1:
    st.button("▶️ Bắt đầu nhắc", on_click=start_timer, disabled=st.session_state.running)
with col2:
    st.button("⏹️ Dừng", on_click=stop_timer, disabled=not st.session_state.running)

placeholder = st.empty()

if st.session_state.running:
    minutes = interval
    start_time = time.time()
    while st.session_state.running:
        elapsed = (time.time() - start_time) / 60  # phút
        if elapsed >= minutes:
            placeholder.warning("👁️ Đã đến giờ nghỉ! Hãy nhìn xa 20 feet trong 20 giây!", icon="🔔")
            st.audio("https://www.soundjay.com/button/beep-07.wav", format="audio/wav")
            start_time = time.time()  # reset
        else:
            remaining = int(minutes - elapsed)
            placeholder.info(f"⏳ Còn {remaining} phút đến lần nghỉ tiếp theo...")
        time.sleep(5)
        st.experimental_rerun()
