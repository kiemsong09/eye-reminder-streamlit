import streamlit as st
from streamlit_autorefresh import st_autorefresh
import datetime

# Tự động refresh mỗi 60 giây
st_autorefresh(interval=60 * 1000, key="auto_refresh")

st.title("👁️ Nhắc nghỉ mắt 20-20-20")
st.write("Cứ mỗi 20 phút, hãy nhìn xa 20 feet (6 mét) trong 20 giây để bảo vệ mắt.")

# Lưu thời gian bắt đầu
if "start_time" not in st.session_state:
    st.session_state.start_time = datetime.datetime.now()

# Cho phép người dùng reset thời gian
if st.button("🔄 Bắt đầu lại"):
    st.session_state.start_time = datetime.datetime.now()

# Tính thời gian đã trôi qua
elapsed = (datetime.datetime.now() - st.session_state.start_time).total_seconds()
minutes = int(elapsed // 60)
seconds = int(elapsed % 60)

st.markdown(f"⏱️ Đã làm việc: **{minutes} phút {seconds} giây**")

# Nếu >= 20 phút thì hiện thông báo
if elapsed >= 20 * 60:
    st.warning("👁️ Đã 20 phút! Hãy nhìn xa 20 feet trong 20 giây!")
else:
    remaining = 20*60 - int(elapsed)
    st.info(f"Còn {remaining//60} phút {remaining%60} giây nữa sẽ nhắc nghỉ.")

st.caption("Made with ❤️ using Streamlit")
