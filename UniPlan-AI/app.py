
import streamlit as st
from pathlib import Path
from html import escape

# ==================================================
# تنظیمات اصلی
# ==================================================
st.set_page_config(
    page_title="UniPlan AI | Sky",
    page_icon="☁️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

BASE_DIR = Path(__file__).parent
ASSETS_DIR = BASE_DIR / "assets"
SKY_IMAGE = ASSETS_DIR / "sky.png"
SKY_STATES = ASSETS_DIR / "sky_states.png"

# ==================================================
# طراحی سایت
# ==================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;500;600;700;800&display=swap');

:root {
    --blue: #079cff;
    --navy: #03112d;
}

html, body, [class*="css"], [data-testid="stAppViewContainer"] {
    font-family: 'Vazirmatn', Tahoma, sans-serif !important;
}

.stApp {
    background:
        radial-gradient(ellipse at 5% 5%, #092d70 0%, transparent 32%),
        radial-gradient(ellipse at 95% 90%, #10255b 0%, transparent 30%),
        linear-gradient(140deg, #010819, #041633 55%, #020a1d);
    color: #f1f7ff;
}

header[data-testid="stHeader"] {
    background: transparent;
}

#MainMenu, footer {
    visibility: hidden;
}

.block-container {
    max-width: 1800px;
    padding: 1rem 1.2rem 1.5rem;
}

.brand {
    text-align: center;
    padding: 16px 8px;
    border: 1px solid #078dff;
    border-radius: 22px;
    background: linear-gradient(160deg, #061d4b, #020b20);
    box-shadow: 0 0 24px #007bff20;
    margin-bottom: 14px;
}

.brand-title {
    color: #ffffff;
    font-size: clamp(32px, 3.2vw, 52px);
    font-weight: 800;
    text-shadow: 0 0 20px #148bff;
}

.brand-sub {
    color: #a6dcff;
    font-size: 13px;
    line-height: 2;
}

.panel {
    border: 1px solid #078dff;
    border-radius: 20px;
    background: linear-gradient(145deg, #061c43f5, #020c22f5);
    padding: 15px;
    margin-bottom: 14px;
    box-shadow: 0 0 18px #007bff12;
}

.panel-title {
    color: #eaf6ff;
    font-size: 17px;
    font-weight: 800;
    padding-bottom: 10px;
    border-bottom: 1px solid #1459a0;
    margin-bottom: 10px;
}

.small {
    color: #b8d3f2;
    font-size: 12px;
    line-height: 2;
}

.stat {
    background: #061a3c;
    border: 1px solid #124e91;
    border-radius: 13px;
    padding: 10px;
    margin: 8px 0;
    color: #e7f4ff;
    line-height: 2;
    overflow-wrap: anywhere;
}

.chat-header {
    border: 1px solid #078dff;
    border-radius: 20px;
    background: linear-gradient(100deg, #09245b, #04132e);
    padding: 13px 18px;
    margin-bottom: 12px;
}

.chat-title {
    font-size: 22px;
    font-weight: 800;
    color: white;
}

.online {
    color: #43e3ad;
    font-size: 12px;
}

.message {
    border: 1px solid #087fff;
    background: linear-gradient(140deg, #083b91, #062762);
    border-radius: 18px 18px 18px 5px;
    padding: 13px 15px;
    margin: 10px 0;
    color: #ffffff;
    line-height: 2.1;
    overflow-wrap: anywhere;
    white-space: pre-wrap;
}

.user-message {
    border: 1px solid #087fff;
    background: linear-gradient(120deg, #0755b8, #073579);
    border-radius: 18px 18px 5px 18px;
    padding: 12px 15px;
    margin: 10px 0 10px 12%;
    color: #ffffff;
    line-height: 2;
    overflow-wrap: anywhere;
    white-space: pre-wrap;
}

.stButton > button {
    background: linear-gradient(110deg, #063b91, #0755b8);
    color: white;
    border: 1px solid #078dff;
    border-radius: 12px;
    min-height: 42px;
    font-family: 'Vazirmatn', Tahoma, sans-serif;
    transition: .2s;
}

.stButton > button:hover {
    border-color: #7ce7ff;
    box-shadow: 0 0 15px #078dff70;
    color: white;
}

.stTextInput input,
.stNumberInput input,
.stTextArea textarea {
    background: #ffffff !important;
    color: #000000 !important;
    -webkit-text-fill-color: #000000 !important;
    caret-color: #000000 !important;
    border: 1px solid #078dff !important;
    border-radius: 12px !important;
    font-family: Tahoma, sans-serif !important;
}

.stTextInput input::placeholder,
.stTextArea textarea::placeholder {
    color: #555555 !important;
    -webkit-text-fill-color: #555555 !important;
    opacity: 1 !important;
}

[data-testid="stChatInput"] {
    background: #ffffff !important;
    border: 1px solid #078dff !important;
    border-radius: 16px !important;
}

[data-testid="stChatInput"] textarea {
    background: #ffffff !important;
    color: #000000 !important;
    -webkit-text-fill-color: #000000 !important;
    caret-color: #000000 !important;
    font-family: Tahoma, sans-serif !important;
}

[data-testid="stChatInput"] textarea::placeholder {
    color: #555555 !important;
    -webkit-text-fill-color: #555555 !important;
    opacity: 1 !important;
}

[data-testid="stFileUploader"] {
    background: #041632;
    border: 1px dashed #078dff;
    border-radius: 14px;
    padding: 8px;
}

[data-testid="stFileUploader"] section {
    background: transparent;
}

[data-testid="stFileUploader"] small {
    color: #dcecff !important;
}

[data-baseweb="select"] {
    background: #ffffff !important;
    border-radius: 10px !important;
}

[data-baseweb="select"] * {
    color: #000000 !important;
}

hr {
    border-color: #123e75;
}

@media (max-width: 800px) {
    .block-container {
        padding: .5rem;
    }
    .user-message {
        margin-left: 3%;
    }
}
</style>
""", unsafe_allow_html=True)

# ==================================================
# پیام خوشامدگویی
# ==================================================
WELCOME = (
    "Uniplan AI سلام! خوش امدی به \n "
    "من اسکای هستم دستیار هوشمند انتخاب واحدت\n"
    "برای شروع سال ورودت به دانشگاه رو بنویس "
    "(مثلا 1403 یا 1404)"
)


def new_student():
    return {
        "سال ورود": "ثبت نشده",
        "رشته": "ثبت نشده",
        "گرایش": "ثبت نشده",
        "معدل کل": "ثبت نشده",
        "مشروطی": "ثبت نشده",
        "درس‌های گذرانده": [],
        "درس‌های مردودی": [],
        "درس‌های انتخاب‌شده": []
    }


if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": WELCOME}
    ]

if "student" not in st.session_state:
    st.session_state.student = new_student()

if "uploads" not in st.session_state:
    st.session_state.uploads = []

if "show_form" not in st.session_state:
    st.session_state.show_form = False

# ==================================================
# توابع کمکی
# ==================================================
def add_message(role, content):
    st.session_state.messages.append({
        "role": role,
        "content": content
    })


def normalize_digits(value):
    table = str.maketrans(
        "۰۱۲۳۴۵۶۷۸۹٠١٢٣٤٥٦٧٨٩",
        "01234567890123456789"
    )
    return value.translate(table)


def split_courses(value):
    return [
        item.strip()
        for item in value.replace("،", ",").split(",")
        if item.strip()
    ]


def process_user_message(text):
    text = text.strip()
    if not text:
        return

    add_message("user", text)
    student = st.session_state.student
    normalized = normalize_digits(text)

    if student["سال ورود"] == "ثبت نشده":
        if "1403" in normalized:
            student["سال ورود"] = "۱۴۰۳"
            reply = "سال ورود ۱۴۰۳ ثبت شد. رشته تحصیلی‌ات چیه؟"
        elif "1404" in normalized:
            student["سال ورود"] = "۱۴۰۴"
            reply = "سال ورود ۱۴۰۴ ثبت شد. رشته تحصیلی‌ات چیه؟"
        elif "1405" in normalized:
            student["سال ورود"] = "۱۴۰۵"
            reply = "سال ورود ۱۴۰۵ ثبت شد. رشته تحصیلی‌ات چیه؟"
        else:
            reply = (
                "لطفاً سال ورودت رو مشخص کن؛ مثلاً ۱۴۰۳ یا ۱۴۰۴."
            )

    elif student["رشته"] == "ثبت نشده":
        student["رشته"] = text
        if "برق" in text:
            reply = (
                "رشته مهندسی برق ثبت شد. لطفاً گرایش دقیق خودت رو هم "
                "بنویس؛ مثلاً قدرت، الکترونیک، مخابرات یا کنترل."
            )
        else:
            reply = (
                "رشته ثبت شد. حالا اطلاعات درس‌های گذرانده و مردودی "
                "رو وارد کن یا از فرم اطلاعات دانشجو استفاده کن."
            )

    elif "نمی‌دانم" in text or "نمیدانم" in text:
        reply = (
            "اشکالی نداره. می‌تونیم بعداً گرایش رو از روی مدارک رسمی "
            "بررسی کنیم. برای ادامه، اطلاعات درس‌هات رو وارد کن."
        )

    else:
        reply = (
            "پیامت دریافت شد. برای بررسی دقیق انتخاب واحد، "
            "به کارنامه، چارت رسمی متناسب با سال ورود و فهرست "
            "درس‌های ارائه‌شده در همین ترم نیاز داریم. "
            "بدون این مدارک، پیش‌نیازها یا خطاها رو قطعی اعلام نمی‌کنم."
        )

    add_message("assistant", reply)


# ==================================================
# صفحه اصلی
# ==================================================
left, center, right = st.columns(
    [0.92, 2.2, 0.92],
    gap="small"
)

# -------------------- ستون چپ --------------------
with left:
    st.markdown("""
    <div class="brand">
        <div class="brand-title">Sky</div>
        <div style="font-size:21px;color:#8bdcff;font-weight:700">
            UniPlan AI
        </div>
        <div class="brand-sub">
            دستیار هوشمند برنامه‌ریزی<br>
            دانشگاه آزاد اسلامی
        </div>
    </div>
    """, unsafe_allow_html=True)

    if SKY_IMAGE.exists():
        st.image(str(SKY_IMAGE), use_container_width=True)
    else:
        st.markdown("""
        <div class="panel" style="text-align:center">
            <div style="font-size:55px">🤖</div>
            <div class="small">
                تصویر اصلی را در assets/sky.png قرار بده.
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="panel">
      <div class="panel-title">امکانات UniPlan</div>
      <div class="stat">📚 تحلیل چارت درسی</div>
      <div class="stat">☑️ بررسی پیش‌نیازها</div>
      <div class="stat">🔎 پیشنهاد واحد مناسب</div>
      <div class="stat">⚠️ شناسایی خطاها</div>
      <div class="small">
      نتایج نهایی به مدارک رسمی و اطلاعات دانشجو وابسته‌اند.
      </div>
    </div>
    """, unsafe_allow_html=True)

# -------------------- ستون وسط: چت --------------------
with center:
    st.markdown("""
    <div class="chat-header">
      <div class="chat-title">UniPlan AI</div>
      <div class="online">● آنلاین · دستیار انتخاب واحد Sky</div>
    </div>
    """, unsafe_allow_html=True)

    chat_area = st.container(height=440, border=True)

    with chat_area:
        for msg in st.session_state.messages:
            safe_content = escape(msg["content"])
            formatted = safe_content.replace("\n", "<br>")

            if msg["role"] == "assistant":
                st.markdown(
                    f'<div class="message">Sky<br>{formatted}</div>',
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    f'<div class="user-message">{formatted}</div>',
                    unsafe_allow_html=True
                )

    prompt = st.chat_input("پیامت رو اینجا بنویس...")

    if prompt:
        process_user_message(prompt)
        st.rerun()

    st.markdown("##### 📎 ارسال مدارک")

    uploaded_files = st.file_uploader(
        "کارنامه، چارت درسی یا فهرست انتخاب واحد",
        type=["pdf", "png", "jpg", "jpeg"],
        accept_multiple_files=True,
        key="document_uploader"
    )

    if st.button("📥 ثبت فایل‌های ارسال‌شده", use_container_width=True):
        if uploaded_files:
            known = {
                (item["name"], item["size"])
                for item in st.session_state.uploads
            }

            for file in uploaded_files:
                key = (file.name, file.size)
                if key not in known:
                    st.session_state.uploads.append({
                        "name": file.name,
                        "size": file.size,
                        "type": file.type,
                        "data": file.getvalue()
                    })
                    known.add(key)

            add_message(
                "assistant",
                "فایل‌ها دریافت شدند. در این نسخه دریافت فایل فعال است؛ "
                "اما استخراج خودکار متن از تصویر یا PDF اسکن‌شده هنوز "
                "فعال نیست. برای بررسی معتبر باید محتوای مدارک استخراج "
                "و با چارت رسمی تطبیق داده شود."
            )
            st.rerun()
        else:
            st.warning("ابتدا یک فایل انتخاب کن.")

    if st.session_state.uploads:
        with st.expander("📂 فایل‌های دریافت‌شده"):
            for file in st.session_state.uploads:
                st.write(
                    f"{file['name']} — {file['size']:,} بایت"
                )

    col_a, col_b = st.columns(2)

    with col_a:
        if st.button("📝 ورود اطلاعات دانشجو", use_container_width=True):
            st.session_state.show_form = True

    with col_b:
        if st.button("🔄 شروع گفت‌وگوی جدید", use_container_width=True):
            st.session_state.messages = [
                {"role": "assistant", "content": WELCOME}
            ]
            st.session_state.student = new_student()
            st.session_state.uploads = []
            st.session_state.show_form = False
            st.rerun()

    if st.session_state.show_form:
        with st.expander("اطلاعات تکمیلی دانشجو", expanded=True):
            with st.form("student_form"):
                year = st.selectbox(
                    "سال ورود",
                    ["۱۴۰۳", "۱۴۰۴", "۱۴۰۵", "سایر"]
                )
                major = st.text_input("رشته تحصیلی")
                specialization = st.text_input(
                    "گرایش (در صورت وجود)"
                )
                gpa = st.number_input(
                    "معدل کل",
                    min_value=0.0,
                    max_value=20.0,
                    value=0.0,
                    step=0.25
                )
                probation = st.selectbox(
                    "وضعیت مشروطی",
                    ["خیر", "بله", "نامشخص"]
                )
                passed = st.text_area(
                    "درس‌های گذرانده‌شده",
                    placeholder="نام درس‌ها را با ویرگول جدا کن"
                )
                failed = st.text_area(
                    "درس‌های مردودی یا ناتمام"
                )
                selected = st.text_area(
                    "درس‌های انتخاب‌شده این ترم"
                )

                submitted = st.form_submit_button(
                    "ذخیره اطلاعات",
                    use_container_width=True
                )

                if submitted:
                    student = st.session_state.student
                    student.update({
                        "سال ورود": year,
                        "رشته": major.strip() or "ثبت نشده",
                        "گرایش": specialization.strip() or "ثبت نشده",
                        "معدل کل": gpa if gpa > 0 else "ثبت نشده",
                        "مشروطی": probation,
                        "درس‌های گذرانده": split_courses(passed),
                        "درس‌های مردودی": split_courses(failed),
                        "درس‌های انتخاب‌شده": split_courses(selected)
                    })

                    add_message(
                        "assistant",
                        "اطلاعات دانشجو ذخیره شد. برای بررسی واقعی، "
                        "چارت رسمی و فهرست درس‌های ارائه‌شده این ترم "
                        "هم باید در دسترس باشند."
                    )
                    st.session_state.show_form = False
                    st.rerun()

# -------------------- ستون راست: داشبورد --------------------
with right:
    st.markdown("""
    <div class="panel">
      <div class="panel-title">👤 اطلاعات دانشجو</div>
    """, unsafe_allow_html=True)

    student = st.session_state.student

    for label, key in [
        ("🎓 رشته", "رشته"),
        ("📅 سال ورود", "سال ورود"),
        ("📊 معدل کل", "معدل کل"),
        ("💙 وضعیت مشروطی", "مشروطی")
    ]:
        st.markdown(
            f'<div class="stat"><span class="small">{label}</span><br>'
            f'<b>{escape(str(student[key]))}</b></div>',
            unsafe_allow_html=True
        )

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class="panel">
      <div class="panel-title">📋 وضعیت اطلاعات درسی</div>
    """, unsafe_allow_html=True)

    st.markdown(
        f'<div class="stat">🟢 درس‌های گذرانده: '
        f'{len(student["درس‌های گذرانده"])}</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        f'<div class="stat">🔴 درس‌های مردودی: '
        f'{len(student["درس‌های مردودی"])}</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        f'<div class="stat">🔵 درس‌های انتخاب‌شده: '
        f'{len(student["درس‌های انتخاب‌شده"])}</div>',
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class="panel">
      <div class="panel-title">⚙️ امکانات</div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("📚 تحلیل چارت درسی", use_container_width=True):
        add_message(
            "assistant",
            "برای تحلیل چارت، فایل رسمی و قابل‌استناد رشته، "
            "واحد دانشگاهی و سال ورودت لازم است. "
            "هنوز تطبیق خودکار با سند رسمی فعال نیست."
        )
        st.rerun()

    if st.button("⚠️ بررسی اشکالات انتخاب واحد", use_container_width=True):
        if not student["درس‌های انتخاب‌شده"]:
            st.warning("ابتدا درس‌های انتخاب‌شده این ترم را وارد کن.")
        else:
            st.info(
                "فهرست درس‌ها ثبت شده، اما بدون چارت رسمی، "
                "پیش‌نیازها و فهرست ارائه‌شده این ترم نمی‌توان "
                "خطاها را قطعی اعلام کرد."
            )

    st.markdown("""
    <div class="small" style="text-align:center;padding:10px">
      همیشه همراهت هستم<br>
      <b style="font-size:20px;color:#6dcaff">Sky</b>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<hr>
<div style="text-align:center;color:#9bb9df;font-size:12px">
UniPlan AI | دستیار هوشمند برنامه‌ریزی درسی
</div>
""", unsafe_allow_html=True)


