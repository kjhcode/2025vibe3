import streamlit as st
from streamlit_folium import st_folium
import folium

# 세션 상태 초기화
if "locations" not in st.session_state:
    st.session_state.locations = []

st.set_page_config(page_title="나만의 북마크 지도", page_icon="🗺️", layout="centered")
st.title("🗺️ 나만의 북마크 지도")
st.markdown("**장소 이름과 위도/경도를 입력해 북마크를 추가해보세요!**")

# 입력 폼
with st.form("add_location"):
    name = st.text_input("📍 장소 이름")
    lat = st.number_input("위도 (latitude)", format="%.6f")
    lon = st.number_input("경도 (longitude)", format="%.6f")
    add_btn = st.form_submit_button("✅ 북마크 추가")

    if add_btn and name:
        st.session_state.locations.append({"name": name, "lat": lat, "lon": lon})
        st.success(f"'{name}'이(가) 북마크에 추가되었습니다!")

# 지도 생성
default_center = [37.5665, 126.9780]  # 서울 기본 좌표
m = folium.Map(location=default_center, zoom_start=11)

# 마커 추가
for loc in st.session_state.locations:
    folium.Marker(
        location=[loc["lat"], loc["lon"]],
        popup=loc["name"],
        tooltip=loc["name"],
        icon=folium.Icon(color="blue", icon="bookmark")
    ).add_to(m)

# 지도 출력
st_folium(m, width=700, height=500)

# 북마크 목록
if st.session_state.locations:
    st.subheader("📌 북마크 목록")
    for i, loc in enumerate(st.session_state.locations, 1):
        st.markdown(f"{i}. **{loc['name']}** - ({loc['lat']}, {loc['lon']})")
