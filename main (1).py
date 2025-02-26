import streamlit as st

st.set_page_config(page_title='trac nghiem tinh cach', page_icon=':moyai:', layout='wide')
st.title('hay chon mot con vat ma ban yeu thich')
c1, c2, c3, c4, c5 = st.columns(5)

tinhcach = {'cn mel beo': 'bạn là một con mèl bél độc lập, thích sáng tạo ₍^. .^₎⟆', 
'cn dog': 'bn là một con c̶h̶ó người trung thành, mạnk mẽ ദ്ദി(– ⌓ –)', 
'cn chim': 'bn là một cn trim dz, có tham vọng và mục tiêu cao (˶˃ ᵕ ˂˶)',
'cn cá hell': 'bn là một cn người zui zẻ, hòa đồng, thưn thịn (˶ˆᗜˆ˵)', 
'cn sutuhadong': 'bn cs một vẻ ngoài vô cùng sigma, thu hút mn (≧ ∇ ≦)'}

with c1:
  b1 = st.button('cn mèl bél')
with c2:
  b2 = st.button('cn chos')
with c3:
  b3 = st.button('cn trim')
with c4:
  b4 = st.button('cn ca hel')
with c5:
  b5 = st.button('cn su tu')

if b1:
  with st.expander('cn mèl bél'):
    st.write(tinhcach['cn mel beo'])
if b2:
  with st.expander('cn chos'):
    st.write(tinhcach['cn dog'])
if b3:
  with st.expander('cn trim'):
    st.write(tinhcach['cn chim'])
if b4:
  with st.expander('cn ca hel'):
    st.write(tinhcach['cn cá hell'])
if b5:
  with st.expander('cn su tu'):
    st.write(tinhcach['cn sutuhadong'])

with st.sidebar:
  st.title('trac nghiem tinh cach omg (✿ᴗ͈ˬᴗ͈)')
  if b1:
    st.write('bn đã chọn cn mèl!!')
  if b2:
    st.write('bn đã chọn cn dog!!')
  if b3:
    st.write('bn đã chọn cn cu!!')
  if b4:
    st.write('bn đã chọn cn cá hell!!')
  if b5:
    st.write('bn đã chọn cn su tu!!')
