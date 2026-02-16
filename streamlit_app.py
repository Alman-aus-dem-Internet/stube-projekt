from numpy import *
import streamlit as st
from random import * 
User_in = []
ver1 = ["A"]
ver2 = ["B"]
ver3 = ["C"]
list = [ver1,ver2,ver3]

for i in range(3):
        ver1.append(randint(1,5))
        ver2.append(randint(1,5))
        ver3.append(randint(1,5))

list_without_first = [i[1:] for i in list]
st.write(list)
st.write(list_without_first)

User_in.append(st.slider("Frage 1 :",1,5,3))
st.write(User_in)
User_in.append(st.slider("Frage 2 :",1,5,3))
st.write(User_in)
User_in.append(st.slider("Frage 3 :",1,5,3))
st.write(User_in)

def vergleich(a,b):
    a = array(a,dtype=float)
    b = array(b,dtype=float)
    test = dot(a,b)
    # Step 2: Compute the magnitudes of the vectors
    magnitude_A = linalg.norm(a)
    magnitude_B = linalg.norm(b)
    # Step 3: Calculate cosine similaritycosine_similarity = test2 / (magnitude_A * magnitude_C)
    cos_similarity = test / (magnitude_A * magnitude_B)
    return cos_similarity

#noch anpassen 
t = 0 
best_erg = 0 
best_index = 0 
for n in list:
    erg = vergleich(User_in, list_without_first[t])
    if erg > best_erg :
        best_erg = erg
        best_index = t
    t += 1

st.write(best_erg)
st.write(best_index)
st.write(list[best_index][0])

