
import streamlit as st
from random import * 
User_in = []
ver1 = []
ver2 = []
ver3 = []
list = [ver1,ver2,ver3]

for i in range(5):
    ver1.append(randint(1,5))
    ver2.append(randint(1,5))
    ver3.append(randint(1,5))
User_in.append(st.slider("Frage 1 :",1,5,3))
st.write(User_in)
User_in.append(st.slider("Frage 2 :",1,5,3))
st.write(User_in)
User_in.append(st.slider("Frage 3 :",1,5,3))
st.write(User_in)

#noch anpassen 
t = 0 
best_erg = 0 
best_index = 0 
for n in list:
    erg = vergleich(User_in, list[t])
    if erg > best_erg :
        best_erg = erg
        best_index = t
    t += 1

st.write(best_erg)

