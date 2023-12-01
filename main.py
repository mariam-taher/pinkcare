import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie
import requests


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

image = Image.open('img/WhatsApp Image 2023-11-29 at 22.55.46_e6b2883d.jpg')
st.image(image)

lottie_coding = load_lottieurl("https://lottie.host/0471f662-4f03-4638-9053-dd20f11e44b7/ZJlAP6Pfzv.json")
lottie_co = load_lottieurl("https://lottie.host/321da32f-8a90-42e3-8ac8-125f9dfe6d6e/6nypsMNbY7.json")
lottie = load_lottieurl("https://lottie.host/ebe8109c-8354-4d5e-9f2b-9e625071b162/19QYBeobeS.json")
lotti = load_lottieurl("https://lottie.host/d74582e9-dc1b-4ec0-83f4-13584c2266d8/PYx9tGLKH5.json")
with st.container():
 left_column, right_column = st.columns(2)
 with right_column:
  st.header(" من نحن")
  st.write("---")
  st.subheader("Pink Care")
  st.write("ان نكون الرائد في مجال رعاية صحة المراة في المملكة العربية السعودية")
  st.write("نحن هنا لتحقيق مستقبل صحي افضل للنساء")
 with left_column:
  st_lottie(lotti, key="c")
  

with st.container():
 left_column, right_column = st.columns(2)
 with left_column:
  st.header("رؤيتنا")
  st.write("---")
  st.write('أن نكون الرائد في مجال رعاية صحــــة المرأة في المملكة العربية السعوديــة، حيث نسعى لتحقيق مجتمع صحـــــي يتمتع بالوعي الكامل حول سرطـــــــان الثدي، ويتيح للنساء الوصول إلى فحص مبكر بشكل سهل وف ّعال، مما يحسن من فاعلية إدارة الحالات ويحقق تأثيــــرا إيجابيا على جودة حياتهن')
 with right_column:
        st_lottie(lottie_co, key="coding")
with st.container():
 left_column, right_column = st.columns(2)
 with right_column:
  st.header('رسالتنا')
  st.write("---")
  st.write("نحن هنا لتحقيق مستقبل صحــي أفضل للنساء في المملكة العربية السعودية. من خلال تطبيق َpink care ، نلتزم بتوفير وسيلة سهلة وفعالـة للفحص المبكر لسرطــان الثــــــدي وتقديم رعاية شاملة ومبتكـــــــرة.")
 with left_column:
  st_lottie(lottie, key="co")
  
 st.write("[لتحميل التطبيق >](https://pythonandvba.com)")

with st.container():
 st.write("---")
 left_column, right_column = st.columns(2)
 with left_column:
    st.header("تابعنا على")
    st.write("##")
    
    st.write("[X](https://x.com/iPinkCare?t=PfF5nv4niFazR6VlI7hMKA&s=09)")
    st.write("[instagram](https://instagram.com/i.pinkcare?igshid=NzZlODBkYWE4Ng%3D%3D&utm_source=qr)")
    st.write("[snapchat](https://www.snapchat.com/add/i.pinkcare?share_id=owDTHXv6nDM&locale=en-US)")
    st.write("[linkedin](https://www.linkedin.com/company/pinkcare/?viewAsMember=true)")    
    
 with right_column:
        st_lottie(lottie_coding, key="cod")