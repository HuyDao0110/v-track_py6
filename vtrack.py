import streamlit as st

# --- KHỞI TẠO ĐIỀU HƯỚNG ---
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Thanh điều hướng hàng ngang đơn giản
nav = st.columns([2, 4, 2, 2])

with nav[0]:
    try:
        st.image("logo.png", width=110)
    except:
        st.write("### 🎵 YTrack")

with nav[1]:
    st.text_input("Tìm kiếm...", label_visibility="collapsed")

with nav[2]:
    c1, c2 = st.columns(2)
    if c1.button("🏠 Home"):
        st.session_state.page = "Home"
    if c2.button("📚 Thư viện"):
        st.session_state.page = "Thư viện"

with nav[3]:
    c3, c4 = st.columns(2)
    if c3.button("Đăng nhập"):
        st.session_state.page = "Đăng nhập"
    if c4.button("Đăng ký"):
        st.session_state.page = "Đăng ký"

st.write("---")

# --- QUẢN LÝ HIỂN THỊ TRANG ---
if st.session_state.page == "Home":
    st.write("# Nghe gì hôm nay, User?")
    
    try:
        st.image("best_notification.png")
    except:
        st.info("[Banner: LÁ NGỌC CÀNH VÀNG]")

    st.write("## Nghệ sĩ phổ biến")
    art_cols = st.columns(5)
    artists = [
        ("Sơn Tùng M-TP", "A01son_tung.jpg"),
        ("SOOBIN", "A02soobin.jpg"),
        ("bùi trường linh", "A03buitruonglinh.png"),
        ("Trang Pháp", "A04trang_phap.jpg"),
        ("Xem thêm", "A05more.png")
    ]
    for i, (name, img_file) in enumerate(artists):
        with art_cols[i]:
            try:
                st.image(img_file)
            except:
                st.write(f"[{name}]")
            if st.button(name, key=f"art_{i}"):
                if name == "Trang Pháp":
                    st.session_state.page = "Nghệ sĩ"

    st.write("## Album nổi bật")
    alb_cols = st.columns(6)
    albums = ["B01mtp_mtp.jpg", "B02ai_cung_phai_bat_dau_tu_dau_do.jpg", "B03danh_doi.jpg", "B04bat_no_len.jpg", "B05tung_ngay_nhu_mai_mai.jpg", "B06more.png"]
    for i, alb in enumerate(albums):
        with alb_cols[i]:
            try:
                st.image(alb)
            except:
                st.write(f"[Album {i+1}]")

    st.write("## BXH bài hát nổi bật *Tháng này*")
    bxh_l, bxh_r = st.columns([4, 6])
    with bxh_l:
        try:
            st.image("come_my_way.jpg")
        except:
            st.write("[#1 Come My Way]")
            
    with bxh_r:
        songs = [("2", "Em", "Binz"), ("3", "Nếu như ta chẳng còn", "RPT MCK"), ("4", "IDK", "RPT MCK"), ("5", "Nguyễn Văn Mười", "RPT MCK"), ("6", "người còn thương em không", "Tóc Tiên")]
        for rank, title, artist in songs:
            sl, sr = st.columns([8, 2])
            sl.write(f"{rank}. {title}")
            sr.write(f"**{artist}**")

elif st.session_state.page == "Nghệ sĩ":
    if st.button("⬅ Quay lại"):
        st.session_state.page = "Home"
    st.write("---")
    l, r = st.columns([4, 6])
    with l:
        try:
            st.image("trang_phap.jpg")
        except:
            st.write("[Ảnh Trang Pháp]")
    with r:
        st.write("# Trang Pháp và hành trình")
        st.write("▶ Phát tất cả | 7 bài hát")
        st.write("---")
        for i, s in enumerate(["MOONLIGHT", "Nghệ thuật Gia Vị Đại", "Là Anh", "Ego-holic"], 1):
            st.write(f"{i}. {s}")

elif st.session_state.page == "Thư viện":
    try:
        st.image("thu_vien_yeu_thich.png")
    except:
        st.title("Thư viện yêu thích")
    if st.button("Trở về"):
        st.session_state.page = "Home"

elif st.session_state.page in ["Đăng nhập", "Đăng ký"]:
    if st.button(" Trở về"):
        st.session_state.page = "Home"
    st.write(f"### Trang {st.session_state.page}")
    st.text_input("Username")
    st.text_input("Password", type="password")
    if st.button("Xác nhận"):
        st.session_state.page = "Home"
