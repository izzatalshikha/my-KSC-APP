import streamlit as st
import google.generativeai as genai

# إعداد الصفحة وتصميمها
st.set_page_config(page_title="تطبيق ذكاء اصطناعي", page_icon="🚀", layout="centered")

# تنسيق CSS بسيط لتحسين المظهر
st.markdown("""
    <style>
    .main { text-align: right; direction: rtl; }
    div.stButton > button:first-child { background-color: #4CAF50; color: white; }
    </style>
    """, unsafe_allow_html=True)

# إعداد مفتاح API (قم بوضعه هنا أو اجعل المستخدم يدخله)
# ملاحظة أمنية: في التطبيقات الحقيقية نستخدم "Secrets" بدلاً من كتابة الكود هنا
API_KEY = "AIzaSyCBmsKSlI47kFrQKkQcmErY10DqV4ebJ1w" 

try:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')

    st.title("🤖 مشروعي على أرض الواقع")
    st.write("مرحباً بك! اكتب سؤالك أدناه وسيقوم النموذج بالرد عليك فوراً.")

    # منطقة الإدخال
    user_input = st.text_input("بماذا يمكنني مساعدتك؟", placeholder="اكتب سؤالك هنا...")

    if st.button("إرسال"):
        if user_input:
            with st.spinner('جاري التحليل واستخراج الإجابة...'):
                response = model.generate_content(user_input)
                st.subheader("النتيجة:")
                st.success(response.text)
        else:
            st.warning("من فضلك اكتب سؤالاً أولاً.")

except Exception as e:
    st.error(f"حدث خطأ في الاتصال: {e}")

st.divider()
st.caption("تم التطوير باستخدام Google Gemini API و Streamlit")