import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ตั้งค่าหน้าจอโปรแกรม
st.set_page_config(
    page_title="Ultimate Track-Master Pro: Complete Master Edition v2.0",
    page_icon="🏆",
    layout="wide"
)

# --- SYSTEM HEADER & ACTIVE TEAM VAULT ---
st.markdown("### 🏆 SYSTEM HEADER: ACTIVE TEAM VAULT & ROLE MANAGEMENT")
col_head1, col_head2 = st.columns([3, 1])
with col_head1:
    team_vault = st.selectbox(
        "เลือกโปรไฟล์รถ / ทีมแข่ง",
        ["สำนักแต่ง R15 Open Class (คันหลัก - ทีม A)", "GPX GR200R Superbike (คันสำรอง - ทีม B)"]
    )
with col_head2:
    user_role = st.selectbox("บทบาทผู้ใช้งาน", ["หัวหน้าช่าง / Race Engineer", "นักแข่ง (Rider)"])

st.markdown("---")

# --- STICKY TOP BAR (REAL-TIME MONITOR) ---
st.markdown("#### 🔴 STICKY REAL-TIME MONITOR BAR")
m1, m2, m3, m4 = st.columns(4)
m1.metric("พีคม้าปัจจุบัน (Spec B)", "27.2 HP", "+2.4 HP")
m2.metric("แรงบิดสูงสุด", "18.2 Nm", "8,500 RPM")
m3.metric("EGT Thermal Safety", "845°C", "🟢 ปลอดภัย")
m4.metric("GPS Top Speed (สนาม)", "162.5 กม./ชม.", "📈 ล่าสุด")

st.markdown("---")

# --- STICKY DYNO CURVE & A/B COMPARISON SUITE (แสดงผลตลอดเวลาด้านบนสุด) ---
st.markdown("### 📈 STICKY LIVE DYNO CURVE & A/B COMPARISON SUITE (แสดงผลตลอดเวลา)")

col_dyno_ctrl, col_dyno_view = st.columns([1, 3])

with col_dyno_ctrl:
    st.info("💡 **AI Dyno Analysis:** สเปก B ให้ม้าปลายพุ่งสูงขึ้น เหมาะกับทางตรงยาว แต่อาจสูญเสียแรงบิดรอบต้นเล็กน้อย (-0.8 Nm)")
    run_dyno_btn = st.button("▶ รันเทสไดโน่สด (Live Dyno Run)")
    compare_mode = st.checkbox("เปิดโหมดเปรียบเทียบ A/B Testing", value=True)

with col_dyno_view:
    fig, ax = plt.subplots(figsize=(8, 3.5))
    rpm = np.array([4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000])
    hp_spec_a = np.array([10.2, 14.1, 18.5, 21.0, 23.5, 24.5, 24.8, 23.0, 20.0])
    hp_spec_b = np.array([9.5, 13.2, 17.8, 21.5, 24.2, 26.0, 27.0, 27.2, 22.5])
    
    ax.plot(rpm, hp_spec_a, label="Spec A (ลูกเดิม / แคมเดิม)", linestyle="--", color="gray", linewidth=2)
    if compare_mode:
        ax.plot(rpm, hp_spec_b, label="Spec B (ลูก 67มม. + แคมแต่งพิเศษ)", color="red", linewidth=2.5)
        
    ax.set_title("Horsepower Curve Comparison (RPM vs HP)")
    ax.set_xlabel("Engine RPM")
    ax.set_ylabel("Power (HP)")
    ax.grid(True, linestyle=":", alpha=0.6)
    ax.legend()
    st.pyplot(fig)

st.markdown("---")

# --- COLLAPSIBLE ACCORDION CATEGORIES (รวมทุกฟังก์ชันย่อยแบบสมบูรณ์รวมถึง GPS ใหม่) ---

# หมวดที่ 1: Engine Core, Weight Setup & Weather Density (DA)
with st.expander("🛠️ หมวดหมู่ที่ 1: ENGINE CORE, WEIGHT SETUP & WEATHER DENSITY (DA)", expanded=True):
    st.subheader("ข้อมูลพื้นฐานเครื่องยนต์, น้ำหนัก และสภาพอากาศ")
    
    c_e1, c_e2, c_e3 = st.columns(3)
    with c_e1:
        st.text_input("ขนาดลูกสูบ (มม.)", "67.0")
        st.text_input("ช่วงชัก (มม.)", "63.1")
    with c_e2:
        st.text_input("น้ำหนักรถเปล่า (กก.)", "128.0")
        st.text_input("น้ำหนักนักแข่งรวมชุด (กก.)", "68.0")
    with c_e3:
        st.text_input("อุณหภูมิแวดล้อม (°C)", "32.5")
        st.text_input("ความดันบรรยากาศ (hPa)", "1013")
        
    st.info("📊 **ผลการคำนวณอัตโนมัติ:** ความจุ 222.4 ซีซี | น้ำหนักรวม 196 กก. (สัดส่วน 48% หน้า / 52% หลัง) | Density Altitude (DA): +650 เมตร (ชดเชยน้ำมันอัตโนมัติ +1.2%)")

# หมวดที่ 2: ECU Tuning, Fuel Map, AFR & EGT Thermal Warning
with st.expander("💻 หมวดหมู่ที่ 2: ECU TUNING, FUEL MAP, AFR & EGT THERMAL WARNING SUITE", expanded=False):
    st.subheader("ระบบจูนกล่อง ECU, ตารางน้ำมัน, ไฟจุดระเบิด และระบบ AI OCR")
    
    ecu_brand = st.selectbox("เลือกกล่องแต่งหลัก", ["API Tech Stand Alone", "Aracer RC Super2", "BRD Tuned ECU"])
    uploaded_file = st.file_uploader("📷 [AI OCR Image-to-Data] อัปโหลดรูปตารางจูนกล่องหรือแคปหน้าจอ", type=["png", "jpg", "jpeg"])
    
    col_t1, col_t2 = st.columns(2)
    with col_t1:
        st.write("📊 **ตาราง Fuel Map (% Correction)**")
        fuel_data = {
            "TPS \\ RPM": ["20%", "60%", "100%"],
            "4,000": ["+0.0%", "+1.5%", "+4.0%"],
            "8,000": ["+2.0%", "+6.5%", "+10.2%"],
            "11,500": ["+0.5%", "+4.0%", "+8.0%"]
        }
        st.dataframe(pd.DataFrame(fuel_data))
    with col_t2:
        st.write("⚡ **ตาราง Ignition Timing Map (องศาไฟ BTDC)**")
        ign_data = {
            "TPS \\ RPM": ["20%", "60%", "100%"],
            "4,000": ["18°", "22°", "10°"],
            "8,000": ["32°", "28°", "22°"],
            "11,500": ["33°", "29°", "23°"]
        }
        st.dataframe(pd.DataFrame(ign_data))
        
    st.warning("⚠️ **EGT Thermal Warning:** อุณหภูมิไอเสียคาดการณ์ 845°C (สถานะ: ปลอดภัย ไม่มีความเสี่ยงสูบทะลุ) | **AI Auto-Correction:** ย่าน 8k-10k RPM คันเร่งเต็ม AFR หนาไป (11.4) แนะนำลดน้ำมัน -3.5%")

# หมวดที่ 3: Drivetrain, 6-Speed Ratio & Fuel Burn Stint Calculator
with st.expander("🏎️ หมวดหมู่ที่ 3: DRIVETRAIN, 6-SPEED RATIO & FUEL BURN STINT CALCULATOR", expanded=False):
    st.subheader("ระบบส่งกำลัง 6 เกียร์, อัตราทดสเตอร์ และคำนวณน้ำมันเรซยาวตามสเปกเครื่อง")
    
    gear_data = {
        "เกียร์": ["เกียร์ 1", "เกียร์ 2", "เกียร์ 3", "เกียร์ 4", "เกียร์ 5", "เกียร์ 6"],
        "อัตราทด": [2.833, 1.875, 1.421, 1.143, 0.955, 0.840],
        "Top Speed (กม./ชม.)": [52.0, 78.5, 104.2, 126.8, 145.0, 160.0],
        "สถานะรอบตก": ["ออกตัว", "🟢 ในพาวเวอร์แบนด์", "🟢 ในพาวเวอร์แบนด์", "🟢 ในพาวเวอร์แบนด์", "🟡 ต่ำเล็กน้อย", "🔴 รอรอบ"]
    }
    st.dataframe(pd.DataFrame(gear_data))
    
    c_f1, c_f2 = st.columns(2)
    with c_f1:
        st.text_input("สเตอร์หน้า / หลัง (ฟัน)", "14 / 43")
        st.selectbox("ยางแข่งขันในไทย", ["Pirelli SC1 Slick (110/70-R17)", "IRC Formula S (110/70-R17)"])
    with c_f2:
        st.text_input("แผนการแข่งขัน (Race Stint)", "15 รอบสนาม")
        st.info("🛢️ **คำนวณน้ำมันเรซยาว (ลิงก์สเปกแต่ง 222.4cc):** อัตราใช้ 0.14 ลิตร/รอบ | ต้องเติมน้ำมันลงถัง **2.1 ลิตร** (+ สำรอง 15% = **2.4 ลิตร**) ป้องกันน้ำมันหมดกลางเรซ")

# หมวดที่ 4: Suspension, Clicker Suite & AI "Grip & Handling Doctor"
with st.expander("🔍 หมวดหมู่ที่ 4: SUSPENSION, CLICKER SUITE & GRIP & HANDLING DOCTOR", expanded=False):
    st.subheader("ระบบเซ็ตช่วงล่าง คลิกเกอร์โช้ค และ AI วิเคราะห์อาการรถ")
    
    c_s1, c_s2 = st.columns(2)
    with c_s1:
        st.write("**โช้คอัพหน้า (USD Fork)**")
        st.slider("Compression Clicker (คลิกจากแข็งสุด)", 1, 20, 10)
        st.slider("Rebound Clicker (คลิกจากแข็งสุด)", 1, 20, 12)
        st.text_input("Rider Sag หน้า (มม.)", "32.0")
    with c_s2:
        st.write("**โช้คอัพหลัง (Monoshock)**")
        st.text_input("Spring Rate หลัง (lbs/in)", "650")
        st.slider("Compression Hi/Lo", 1, 20, 12)
        st.text_input("Rider Sag หลัง (มม.)", "28.0")
        
    st.selectbox("เลือกอาการรถที่นักแข่งฟีดแบ็กหน้างาน", ["อาการเข้าโค้งแล้วหน้าดื้อ / ไม่ยอมเลี้ยว", "เปิดคันเร่งออกจากโค้งแล้วล้อฟรี", "เบรกหนักแล้วท้ายสะบัด"])
    st.info("🤖 **AI Grip & Handling Doctor:** แนะนำให้ **เพิ่ม Preload สปริงหลังขึ้น +1 มม.** หรือ **ยกโช้คหน้าขึ้น 2 มม.** เพื่อเพิ่มมุมจิก (Rake Angle) ช่วยให้รถเลี้ยวคมขึ้นทันที")

# หมวดที่ 5: Tire Pyrometer Log, Pit Safety Checklist & Mechanic Sheet
with st.expander("⏱️ หมวดหมู่ที่ 5: TIRE LOG, PIT SAFETY CHECKLIST & MECHANIC SHEET GENERATOR", expanded=False):
    st.subheader("บันทึกอุณหภูมิยาง, เช็กลิสต์ความปลอดภัยก่อนปล่อยรถ และพิมพ์ใบงานพิท")
    
    st.write("**🌡️ บันทึกอุณหภูมิหน้ายาง (Pyrometer - ซ้าย / กลาง / ขวา) & แรงดันลมยางร้อน**")
    t_c1, t_c2 = st.columns(2)
    with t_c1:
        st.text_input("อุณหภูมิหน้ายาง (°C)", "78°C / 85°C / 80°C")
    with t_c2:
        st.text_input("แรงดันลมยาง (หน้า / หลัง บาร์)", "1.9 / 1.7")
        
    st.markdown("---")
    st.write("**🛡️ Pre-Flight Pit Safety Checklist (เช็กลิสต์ความปลอดภัยก่อนออกตัว)**")
    st.checkbox("☑️ ตรวจสอบความแน่นน็อตสเตอร์หน้า-หลังและคาลิปเปอร์เบรก", value=True)
    st.checkbox("☑️ ตรวจสอบระยะฟรีสายคันเร่งและการคืนตัวของลิ้นปีกผีเสื้อ", value=True)
    st.checkbox("☑️ ตรวจสอบการล็อกท่อไอเสีย, แดปเปอร์ และอุณหภูมิหม้อน้ำ", value=True)
    
    st.markdown("---")
    if st.button("🖨️ พิมพ์ใบงานหน้าพิท (Pit Sheet) และส่งสรุปสเปกเข้า Line สำนักแต่ง"):
        st.success("สร้างเอกสาร Pit Sheet สำเร็จและส่งข้อมูลเข้าสู่ระบบคลาวด์สำนักแต่งเรียบร้อยแล้ว!")

# หมวดที่ 6 ใหม่แกะกล่อง: Smartphone IMU, GPS Telemetry & Racing Line Suite
with st.expander("🛰️ หมวดหมู่ที่ 6: SMARTPHONE IMU, GPS TELEMETRY & RACING LINE SUITE (NEW!)", expanded=False):
    st.subheader("ระบบวัดแรง G, ความเร็ว GPS, การมาร์กจุด และจำลองแผนที่เส้นทาง (Racing Line)")
    
    gps_col1, gps_col2 = st.columns(2)
    with gps_col1:
        st.write("📍 **GPS & IMU Sensor Status (เชื่อมต่อมือถือ)**")
        st.success("🟢 เชื่อมต่อเซ็นเซอร์ IMU (Gyro/Accel) และ GPS 10Hz สำเร็จ")
        st.text_input("ค่าสูงสุด Longitudinal G (เบรก/เร่ง)", "+1.15G (Brk) / +0.82G (Acc)")
        st.text_input("ค่าสูงสุด Lateral G (แรงเหวี่ยงเข้าโค้ง)", "1.45 G (โค้ง 3 พีระฯ)")
        st.selectbox("โหมดการมาร์กจุดเหตุการณ์ (Markers)", ["มาร์กอัตโนมัติด้วย GPS Start/Finish Line", "กดปุ่มรีโมตบลูทูธที่แฮนด์ (Live Marker)", "มาร์กช่วงเวลาหลังวิ่งเสร็จ (Post-Session Trim)"])
    
    with gps_col2:
        st.write("🗺️ **จำลองแผนที่แสดงเส้นทางวิ่ง (Google Maps Racing Line Integration)**")
        st.info("🗺️ **สนาม:** Bira International Circuit (พัทยา) | **รอบที่ดีที่สุด:** 1:13.5")
        # จำลองกราฟแผนที่สนามคร่าวๆ ด้วย Matplotlib
        fig_map, ax_map = plt.subplots(figsize=(4, 3))
        track_x = [0, 2, 4, 5, 4, 2, 0, -1, 0]
        track_y = [0, 0, 1, 3, 5, 6, 6, 3, 0]
        ax_map.plot(track_x, track_y, color="blue", linewidth=2, label="Racing Line")
        ax_map.scatter([4], [3], color="red", s=100, label="Marked Incident (โค้ง 3)")
        ax_map.set_title("GPS Racing Line & Marked Points")
        ax_map.axis("off")
        ax_map.legend(loc="upper left", fontsize=8)
        st.pyplot(fig_map)
        
    st.write("✂️ **Time Trimming & Lap Splitter (ตัดแต่งรอบและเลือกช่วงวิเคราะห์):**")
    st.slider("เลือกช่วงเวลาตารางข้อมูล (Trim Window)", 0, 100, (10, 90))
    st.button("📌 ยืนยันมาร์กจุดเหตุการณ์และลิงก์ข้อมูลเข้ากับสเปกเครื่องปัจจุบัน")

st.markdown("---")

# --- GLOBAL ACTION BUTTONS ---
st.markdown("### 💾 GLOBAL SYSTEM ACTIONS")
act1, act2, act3, act4 = st.columns(4)
with act1:
    st.button("📥 ส่งออก JSON")
with act2:
    st.button("📥 ส่งออก CSV")
with act3:
    st.button("📤 โอนค่าเข้ากล่อง ECU")
with act4:
    st.button("🔄 ซิงก์คลาวด์ทีม")
