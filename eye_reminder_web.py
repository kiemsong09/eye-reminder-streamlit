import streamlit as st
from streamlit_autorefresh import st_autorefresh
import datetime

st.set_page_config(page_title="Nhắc nghỉ mắt", layout="centered")

# Tự động refresh mỗi 60 giây
st_autorefresh(interval=60 * 1000, key="auto_refresh")

st.title("👁️ Nhắc nghỉ mắt 20-20-20")
st.markdown("Cứ mỗi khoảng thời gian bạn đặt, hãy nhìn xa **20 feet (6 mét)** trong **20 giây** để thư giãn mắt!")

# Cho phép nhập số phút nhắc nghỉ bằng tay
remind_interval = st.number_input(
    "⏱️ Nhập số phút sau mỗi lần nhắc nghỉ:",
    min_value=1,
    max_value=180,
    value=20,
    step=1,
    key="interval_input"
)

# Lưu thời điểm bắt đầu vào session
if "start_time" not in st.session_state:
    st.session_state.start_time = datetime.datetime.now()

# Nút bắt đầu lại
if st.button("🔄 Bắt đầu lại"):
    st.session_state.start_time = datetime.datetime.now()

# Tính thời gian trôi qua
elapsed = (datetime.datetime.now() - st.session_state.start_time).total_seconds()
minutes = int(elapsed // 60)
seconds = int(elapsed % 60)

st.markdown(f"⏳ Đã làm việc: **{minutes} phút {seconds} giây**")

# Nhắc khi đủ thời gian
if elapsed >= remind_interval * 60:
    st.warning("👁️ Đã đến lúc nghỉ! Hãy nhìn xa 20 feet trong 20 giây!")
else:
    remain = remind_interval * 60 - int(elapsed)
    st.info(f"⏲️ Còn {remain // 60} phút {remain % 60} giây nữa sẽ nhắc nghỉ.")

st.caption("Made with ❤️ bằng Streamlit")
