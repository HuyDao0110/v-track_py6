import streamlit as st

# --- CẤU HÌNH TRANG ---
st.set_page_config(
    page_title="VTrack - Ứng dụng nghe nhạc trực tuyến",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- KHỞI TẠO STATE ĐỂ ĐIỀU HƯỚNG ---
if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"

# Hàm chuyển trang tiện lợi
def navigate_to(page_name):
    st.session_state.current_page = page_name

# --- 1. THANH ĐIỀU HƯỚNG TRÊN CÙNG (TOP NAVIGATION BAR) ---
# Sử dụng st.columns thuần túy chia tỉ lệ để tạo một thanh ngang cân đối
nav_cols = st.columns([1.5, 0.6, 4.5, 1.2, 1.0, 0.6, 0.6, 0.6, 1.2, 1.2])

with nav_cols[0]:
    # Hiển thị Logo ứng dụng YTrack
    st.image("logo.png", use_container_width=True)

with nav_cols[1]:
    # Nút bấm Home dạng icon hình ngôi nhà (sử dụng ảnh D06home.jpg)
    if st.button("Home", key="nav_home_btn", use_container_width=True):
        navigate_to("Home")

with nav_cols[2]:
    # Ô tìm kiếm nghệ sĩ, bài hát...
    st.text_input("Tìm kiếm", placeholder="Tìm kiếm nghệ sĩ, bài hát, ...", label_visibility="collapsed")

with nav_cols[3]:
    if st.button("Giới thiệu", key="nav_about", use_container_width=True):
        st.toast("Trang Giới thiệu đang phát triển!")

with nav_cols[4]:
    if st.button("Hỗ trợ", key="nav_support", use_container_width=True):
        st.toast("Trang Hỗ trợ đang phát triển!")

with nav_cols[5]:
    # Icon Ngôn ngữ
    st.image("D01language.png", width=32)

with nav_cols[6]:
    # Icon Chuông thông báo
    st.image("D02notification.png", width=32)

with nav_cols[7]:
    # Icon User Profile
    st.image("D03user_icon.png", width=32)

with nav_cols[8]:
    if st.button("Đăng nhập", key="nav_login", use_container_width=True):
        navigate_to("Đăng nhập")

with nav_cols[9]:
    if st.button("Đăng ký", key="nav_register", use_container_width=True):
        navigate_to("Đăng ký")

st.write("---") # Đường kẻ chia cách thanh điều hướng với nội dung bên dưới

# --- 2. XỬ LÝ NỘI DUNG TỪNG TRANG THEO TRẠNG THÁI ---

# ================= TRANG HOME =================
if st.session_state.current_page == "Home":
    st.title("Nghe gì hôm nay, User ?")
    st.caption("Hôm nay Thứ bảy, 20-06-2026")
    
    # Khu vực Banner chính (Best Notification)
    st.image("best_notification.png", caption="Sản phẩm mới nhất từ ca nương Kiều Anh", use_container_width=True)
    
    # --- PHẦN 1: NGHỆ SĨ PHỔ BIẾN ---
    st.write("## Nghệ sĩ phổ biến")
    artist_cols = st.columns([2, 2, 2, 2, 1, 1])
    
    with artist_cols[0]:
        st.image("A01son_tung.jpg", use_container_width=True)
        if st.button("Xem Sơn Tùng M-TP", key="home_st"):
            st.toast("Thông tin nghệ sĩ")
    with artist_cols[1]:
        st.image("A02soobin.jpg", use_container_width=True)
        if st.button("Xem SOOBIN", key="home_sb"):
            st.toast("Thông tin nghệ sĩ")
    with artist_cols[2]:
        st.image("A03buitruonglinh.png", use_container_width=True)
        if st.button("Xem bùi trường linh", key="home_btl"):
            st.toast("Thông tin nghệ sĩ")
    with artist_cols[3]:
        st.image("A04trang_phap.jpg", use_container_width=True)
        if st.button("Xem Trang Pháp", key="home_tp"):
            navigate_to("Nghệ sĩ")
    with artist_cols[4]:
        st.image("A05more.png", use_container_width=True)
        if st.button("Thêm nghệ sĩ", key="home_more_art"):
            navigate_to("Thư viện")

    # --- PHẦN 2: ALBUM NỔI BẬT ---
    st.write("## Album nổi bật")
    album_cols = st.columns([2, 2, 2, 2, 2, 1])
    
    with album_cols[0]:
        st.image("B01mtp_mtp.jpg", use_container_width=True)
    with album_cols[1]:
        st.image("B02ai_cung_phai_bat_dau_tu_dau_do.jpg", use_container_width=True)
    with album_cols[2]:
        st.image("B03danh_doi.jpg", use_container_width=True)
    with album_cols[3]:
        st.image("B04bat_no_len.jpg", use_container_width=True)
    with album_cols[4]:
        st.image("B05tung_ngay_nhu_mai_mai.jpg", use_container_width=True)
    with album_cols[5]:
        st.image("B06more.png", use_container_width=True)

    # --- PHẦN 3: BXH BÀI HÁT NỔI BẬT THÁNG NÀY ---
    st.write("## BXH bài hát nổi bật *Tháng này*")
    
    col_bxh_left, col_bxh_right = st.columns([4, 6])
    
    with col_bxh_left:
        # Hiển thị ảnh Bài hát đứng đầu (#1 Come My Way)
        st.image("come_my_way.jpg", use_container_width=True)
        
    with col_bxh_right:
        songs_data = [
            {"rank": "2", "title": "Em", "artist": "Binz"},
            {"rank": "3", "title": "Nếu như ta chẳng còn", "artist": "RPT MCK"},
            {"rank": "4", "title": "IDK", "artist": "RPT MCK"},
            {"rank": "5", "title": "Nguyễn Văn Mười", "artist": "RPT MCK"},
            {"rank": "6", "title": "người còn thương em không", "artist": "Tóc Tiên"},
            {"rank": "7", "title": "LÁ NGỌC CÀNH VÀNG", "artist": "Kiều Anh"},
            {"rank": "8", "title": "Có công mài “sắc” Afrobeats", "artist": "Ngô Lan Hương"},
            {"rank": "9", "title": "Tây Thi", "artist": "RPT MCK"},
            {"rank": "10", "title": "toidaidot", "artist": "GREY D"},
        ]
        
        for song in songs_data:
            c_rank_title, c_artist = st.columns([7, 3])
            with c_rank_title:
                st.write(f"{song['rank']}. {song['title']}")
            with c_artist:
                st.write(f"**{song['artist']}**")

# ================= TRANG NGHỆ SĨ (CHI TIẾT) =================
elif st.session_state.current_page == "Nghệ sĩ":
    header_cols = st.columns([2, 8])
    with header_cols[0]:
        if st.button("⬅ Back", key="artist_back"):
            navigate_to("Home")
    with header_cols[1]:
        st.write("### NGHỆ SĨ PHỔ BIẾN")
        
    st.write("---")
    
    body_left, body_right = st.columns([4, 6])
    with body_left:
        st.image("trang_phap.jpg", use_container_width=True)
    with body_right:
        st.markdown("# Trang Pháp và hành trình trong CHENGFENG 2026")
        
        # Nút chức năng hàng ngang
        action_cols = st.columns([3, 4, 1, 1])
        with action_cols[0]:
            st.button("Phát danh sách", key="play_tp_list")
        with action_cols[1]:
            st.write("7 bài hát • 24 phút 42 giây")
        with action_cols[2]:
            st.image("D04add.png", width=28)
        with action_cols[3]:
            st.image("D05more_setting.png", width=28)
            
        st.write("#### Danh sách bài hát:")
        songs_tp = ["MOONLIGHT", "Nghệ thuật Gia Vị Đại", "Là Anh", "Ego-holic", "Nghịch Chiến", "Sổ Tay Rèn Luyện Thanh Xuân", "DNA"]
        for idx, song_name in enumerate(songs_tp, start=1):
            st.write(f"{idx}. {song_name}")
            
    st.write("---")
    st.write("### Có thể bạn thích")
    like_cols = st.columns([3, 3, 4, 2])
    with like_cols[0]:
        st.image("C01chi_pu.jpg", use_container_width=True)
    with like_cols[1]:
        st.image("C02suni_ha_linh.jpg", use_container_width=True)
    with like_cols[2]:
        st.image("C03lonely_dance.png", use_container_width=True)

# ================= TRANG THƯ VIỆN =================
elif st.session_state.current_page == "Thư viện":
    st.image("thu_vien_yeu_thich.png", use_container_width=True)
    st.write("### Danh sách thư viện yêu thích của bạn đang được đồng bộ...")
    if st.button("Quay lại Trang chủ", key="lib_back_home"):
        navigate_to("Home")

# ================= TRANG ĐĂNG NHẬP / ĐĂNG KÝ =================
elif st.session_state.current_page in ["Đăng nhập", "Đăng ký"]:
    form_col_l, form_col_main, form_col_r = st.columns([3, 6, 3])
    
    with form_col_main:
        if st.session_state.current_page == "Đăng nhập":
            st.image("Đăng nhập.jpg", use_container_width=True)
            st.write("---")
            username = st.text_input("Tên tài khoản (Username)", key="login_user")
            password = st.text_input("Mật khẩu (Password)", type="password", key="login_pass")
            
            c_btn1, c_btn2 = st.columns(2)
            with c_btn1:
                if st.button("Đăng nhập ngay", key="do_login_action"):
                    st.success("Đăng nhập thành công!")
                    navigate_to("Home")
            with c_btn2:
                if st.button("Chuyển sang tạo tài khoản Đăng ký", key="go_reg"):
                    navigate_to("Đăng ký")
                    
        else:
            st.image("Đăng ký.jpg", use_container_width=True)
            st.write("---")
            reg_user = st.text_input("Tên tài khoản (Username)", key="reg_user")
            reg_email = st.text_input("Địa chỉ email (Email address)", key="reg_email")
            reg_pass = st.text_input("Mật khẩu (Password)", type="password", key="reg_pass")
            reg_pass_conf = st.text_input("Xác thực lại mật khẩu", type="password", key="reg_pass_confirm")
            
            c_btn3, c_btn4 = st.columns(2)
            with c_btn3:
                if st.button("Đăng ký ngay", key="do_reg_action"):
                    st.success("Đăng ký tài khoản thành công!")
                    navigate_to("Đăng nhập")
            with c_btn4:
                if st.button("Đã có tài khoản? Đăng nhập", key="go_login"):
                    navigate_to("Đăng nhập")
