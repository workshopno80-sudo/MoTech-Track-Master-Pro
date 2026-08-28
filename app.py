import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ตั้งค่าหน้าจอโปรแกรม
st.set_page_config(
    page_title="Ultimate Track-Master Pro: Clean Master Edition",
    page_icon="🏆",
    layout="wide"
)

# ==========================================
# 1. GLOBAL SYSTEM HEADER & TEAM VAULT
# ==========================================
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

# ==========================================
# 2. CENTRAL CONTROL PANEL (ตัวแปรกลางของทั้งแอป)
# ==========================================
st.markdown("### 🎛️ CENTRAL TUNING CONTROL PANEL (ปรับค่าตรงนี้ ค่าทุกหมวดจะเปลี่ยนตามอัตโนมัติ)")
c_ctrl1, c_ctrl2, c_ctrl3, c_ctrl4 = st.columns(4)
with c_ctrl1:
    piston_sz = st.slider("ขนาดลูกสูบ (มม.)", 55.0, 75.0, 67.0, 0.5)
with c_ctrl2:
    stroke_sz = st.slider("ช่วงชัก (มม.)", 50.0, 70.0, 58.8, 0.1)
with c_ctrl3:
    cam_lift = st.slider("แคมไทม์องศาพิเศษ", 240, 300, 272, 1)
with c_ctrl4:
    rider_wt = st.slider("น้ำหนักนักแข่งรวมชุด (กก.)", 50.0, 100.0, 68.0, 1.0)

# --- สูตรคำนวณกลาง (Shared Calculation Engine) ---
displacement = (np.pi * (piston_sz / 2)**2 * stroke_sz) / 1000
base_hp = 20.0 + (piston_sz - 57.0) * 0.4 + (stroke_sz - 58.8) * 0.3 + (cam_lift - 240) * 0.05
peak_torque = 14.0 + (displacement - 150) * 0.03
egt_temp = 780 + (base_hp - 20) * 2.5
fuel_per_lap = displacement * 0.0006

st.markdown("---")

# ==========================================
# 3. REAL-TIME MONITOR BAR (แสดงผลรวม)
# ==========================================
st.markdown("#### 🔴 STICKY REAL-TIME MONITOR BAR")
m1, m2, m3, m4 = st.columns(4)
m1.metric("พีคม้าปัจจุบัน (Real-Time)", f"{base_hp:.1f} HP", f"+{(base_hp - 24.8):.1f} HP")
m2.metric("แรงบิดสูงสุด", f"{peak_torque:.1f} Nm", "8,500 RPM")
m3.metric("EGT Thermal Safety", f"{egt_temp:.0f}°C", "🟢 ปลอดภัย" if egt_temp < 900 else "🔴 ร้อนเกินไป!")
m4.metric("ความจุกระบอกสูบ", f"{displacement:.1f} ซีซี", "CC Calculator")

st.markdown("---")

# ==========================================
# 4. LIVE DYNO CURVE & A/B COMPARISON
# ==========================================
st.markdown("### 📈 LIVE DYNO CURVE & A/B COMPARISON SUITE")
col_dyno_ctrl, col_dyno_view = st.columns([1, 3])

with col_dyno_ctrl:
    st.info(f"💡 **AI Dyno Analysis:** สเปกปัจจุบัน ลูก {piston_sz} มม. / ชัก {stroke_sz} มม. ความจุ {displacement:.1f}cc ให้แรงม้า {base_hp:.1f} HP เหมาะสำหรับซ้อมและแข่งในสนามพีระเซอร์กิต")
    run_dyno_btn = st.button("▶ รันเทสไดโน่สด (Live Dyno Run)")
    compare_mode = st.checkbox("เปิดโหมดเปรียบเทียบ A/B Testing", value=True)

with col_dyno_view:
    fig, ax = plt.subplots(figsize=(8, 3.2))
    rpm = np.array([4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000])
    hp_spec_a = np.array([10.2, 14.1, 18.5, 21.0, 23.5, 24.5, 24.8, 23.0, 20.0])
    hp_spec_b = hp_spec_a * (base_hp / 24.8) # ขยับตามสไลด์กลางทันที
    
    ax.plot(rpm, hp_spec_a, label="Spec A (มาตรฐานโรงงาน)", linestyle="--", color="gray", linewidth=2)
    if compare_mode:
        ax.plot(rpm, hp_spec_b, label=f"Spec B (ลูก {piston_sz} / ชัก {stroke_sz})", color="red", linewidth=2.5)
        
    ax.set_title("Live Horsepower Curve Comparison (RPM vs HP)")
    ax.set_xlabel("Engine RPM")
    ax.set_ylabel("Power (HP)")
    ax.grid(True, linestyle=":", alpha=0.6)
    ax.legend()
    st.pyplot(fig)

st.markdown("---")

# ==========================================
# 5. ALL MODULES (เชื่อมโยงค่ากลางทั้งหมด)
# ==========================================

# หมวดที่ 1
with st.expander("🛠️ หมวดหมู่ที่ 1: ENGINE CORE, WEIGHT SETUP & WEATHER DENSITY (DA)", expanded=True):
    st.subheader("ข้อมูลพื้นฐานเครื่องยนต์, น้ำหนัก และสภาพอากาศ")
    c_e1, c_e2, c_e3 = st.columns(3)
    with c_e1:
        st.metric("ขนาดลูกสูบ (ซิงก์จากค่ากลาง)", f"{piston_sz} มม.")
        st.metric("ช่วงชัก (ซิงก์จากค่ากลาง)", f"{stroke_sz} มม.")
    with c_e2:
        st.text_input("น้ำหนักรถเปล่า (กก.)", "128.0")
        st.metric("น้ำหนักนักแข่งรวมชุด", f"{rider_wt} กก.")
    with c_e3:
        st.text_input("อุณหภูมิแวดล้อม (°C)", "32.5")
        st.text_input("ความดันบรรยากาศ (hPa)", "1013")
    st.info(f"📊 **ผลการคำนวณอัตโนมัติ:** ความจุรวม **{displacement:.1f} ซีซี** | น้ำหนักรวมรถ+คน **{128.0 + rider_wt:.1f} กก.**")

# หมวดที่ 2
with st.expander("💻 หมวดหมู่ที่ 2: ECU TUNING, FUEL MAP, AFR & EGT THERMAL WARNING", expanded=False):
    st.subheader("ระบบจูนกล่อง ECU และตารางน้ำมันอัตโนมัติ")
    ecu_brand = st.selectbox("เลือกกล่องแต่งหลัก", ["API Tech Stand Alone", "Aracer RC Super2", "BRD Tuned ECU"])
    uploaded_file = st.file_uploader("📷 [AI OCR] อัปโหลดรูปตารางจูนกล่อง", type=["png", "jpg", "jpeg"])
    
    col_t1, col_t2 = st.columns(2)
    with col_t1:
        st.write("📊 **Fuel Map (% Correction ตามสเปกความจุ)**")
        fuel_data = {"TPS \\ RPM": ["20%", "60%", "100%"], "4,000": ["+0.0%", "+1.5%", "+4.0%"], "8,000": ["+2.0%", "+6.5%", f"+{10.0 + (displacement-150)*0.05:.1f}%"]}
        st.dataframe(pd.DataFrame(fuel_data))
    with col_t2:
        st.write("⚡ **Ignition Timing Map (องศาไฟ BTDC)**")
        ign_data = {"TPS \\ RPM": ["20%", "60%", "100%"], "4,000": ["18°", "22°", "10°"], "8,000": ["32°", "28°", "22°"]}
        st.dataframe(pd.DataFrame(ign_data))
    st.warning(f"⚠️ **EGT Thermal Warning:** อุณหภูมิไอเสียคาดการณ์ **{egt_temp:.0f}°C** | **AI Auto-Correction:** ปรับจูนน้ำมันชดเชยตามความจุ {displacement:.1f}cc เรียบร้อย")

# หมวดที่ 3
with st.expander("🏎️ หมวดหมู่ที่ 3: DRIVETRAIN, 6-SPEED RATIO & FUEL BURN STINT", expanded=False):
    st.subheader("ระบบส่งกำลัง 6 เกียร์ และคำนวณน้ำมันเรซยาว")
    gear_data = {
        "เกียร์": ["เกียร์ 1", "เกียร์ 2", "เกียร์ 3", "เกียร์ 4", "เกียร์ 5", "เกียร์ 6"],
        "อัตราทด": [2.833, 1.875, 1.421, 1.143, 0.955, 0.840],
        "Top Speed (กม./ชม.)": [52.0, 78.5, 104.2, 126.8, 145.0, round(150 + (base_hp * 0.4), 1)],
    }
    st.dataframe(pd.DataFrame(gear_data))
    c_f1, c_f2 = st.columns(2)
    with c_f1:
        st.text_input("สเตอร์หน้า / หลัง (ฟัน)", "14 / 43")
        st.selectbox("ยางแข่งขัน", ["Pirelli SC1 Slick (110/70-R17)", "IRC Formula S"])
    with c_f2:
        st.text_input("แผนการแข่งขัน (Race Stint)", "15 รอบสนาม")
        st.info(f"🛢️ **คำนวณน้ำมันเรซยาว ({displacement:.1f}cc):** อัตราใช้ {fuel_per_lap:.2f} ลิตร/รอบ | ต้องเติมน้ำมันลงถัง **{fuel_per_lap * 15:.1f} ลิตร** (+ สำรอง 15% = **{fuel_per_lap * 15 * 1.15:.1f} ลิตร**)")

# หมวดที่ 4
with st.expander("🔍 หมวดหมู่ที่ 4: SUSPENSION, CLICKER SUITE & GRIP & HANDLING DOCTOR", expanded=False):
    st.subheader("ระบบเซ็ตช่วงล่าง และ AI วิเคราะห์อาการรถ")
    c_s1, c_s2 = st.columns(2)
    with c_s1:
        st.write("**โช้คอัพหน้า (USD Fork)**")
        st.slider("Compression Clicker", 1, 20, 10)
        st.slider("Rebound Clicker", 1, 20, 12)
    with c_s2:
        st.write("**โช้คอัพหลัง (Monoshock)**")
        st.text_input("Spring Rate หลัง (lbs/in)", "650")
        st.slider("Compression Hi/Lo", 1, 20, 12)
    st.selectbox("เลือกอาการรถหน้างาน", ["อาการเข้าโค้งแล้วหน้าดื้อ / ไม่ยอมเลี้ยว", "เปิดคันเร่งออกจากโค้งแล้วล้อฟรี", "เบรกหนักแล้วท้ายสะบัด"])
    st.info("🤖 **AI Grip & Handling Doctor:** แนะนำให้ **เพิ่ม Preload สปริงหลังขึ้น +1 มม.** หรือ **ยกโช้คหน้าขึ้น 2 มม.** ตามน้ำหนักนักแข่งปัจจุบัน")

# หมวดที่ 5
with st.expander("⏱️ หมวดหมู่ที่ 5: TIRE LOG, PIT SAFETY CHECKLIST & MECHANIC SHEET", expanded=False):
    st.subheader("บันทึกอุณหภูมิยาง และเช็กลิสต์ความปลอดภัย")
    t_c1, t_c2 = st.columns(2)
    with t_c1:
        st.text_input("อุณหภูมิหน้ายาง (°C)", "78°C / 85°C / 80°C")
    with t_c2:
        st.text_input("แรงดันลมยาง (หน้า / หลัง บาร์)", "1.9 / 1.7")
    st.markdown("---")
    st.checkbox("☑️ ตรวจสอบความแน่นน็อตสเตอร์หน้า-หลังและคาลิปเปอร์เบรก", value=True)
    st.checkbox("☑️ ตรวจสอบระยะฟรีสายคันเร่งและการคืนตัวของลิ้นปีกผีเสื้อ", value=True)
    st.markdown("---")
    if st.button("🖨️ พิมพ์ใบงานหน้าพิท (Pit Sheet)"):
        st.success("สร้างเอกสาร Pit Sheet สำเร็จ!")

# หมวดที่ 6
with st.expander("🛰️ หมวดหมู่ที่ 6: SMARTPHONE IMU, GPS TELEMETRY & RACING LINE SUITE", expanded=False):
    st.subheader("ระบบวัดแรง G และ GPS สนามพีระเซอร์กิต")
    gps_col1, gps_col2 = st.columns(2)
    with gps_col1:
        st.success("🟢 เชื่อมต่อเซ็นเซอร์ IMU และ GPS 10Hz สำเร็จ")
        st.text_input("ค่าสูงสุด Longitudinal G", "+1.15G (Brk) / +0.82G (Acc)")
        st.text_input("ค่าสูงสุด Lateral G", "1.45 G (โค้ง 3 พีระฯ)")
    with gps_col2:
        st.info("🗺️ **สนาม:** Bira International Circuit | **รอบที่ดีที่สุด:** 1:13.5")
        fig_map, ax_map = plt.subplots(figsize=(4, 3))
        track_x = [0, 2, 4, 5, 4, 2, 0, -1, 0]
        track_y = [0, 0, 1, 3, 5, 6, 6, 3, 0]
        ax_map.plot(track_x, track_y, color="blue", linewidth=2, label="Racing Line")
        ax_map.scatter([4], [3], color="red", s=100, label="Marked Incident (โค้ง 3)")
        ax_map.axis("off")
        st.pyplot(fig_map)

st.markdown("---")

# ==========================================
# 6. GLOBAL ACTIONS
# ==========================================
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
