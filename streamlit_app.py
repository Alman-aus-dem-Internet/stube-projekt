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

User_in.append(st.slider("Wie gerne arbeite ich in einem Labor?",1,5,3))
User_in.append(st.slider("Wie gerne arbeite ich in einem Museum?",1,5,3))
User_in.append(st.slider("Ich arbeite gerne mit Kindern",1,5,3))
User_in.append(st.slider("Ich arbeite gerne mit Menschen",1,5,3))
User_in.append(st.slider("Ich arbeite gerne mit Tieren",1,5,3))
User_in.append(st.slider("Ich mag es kreativ zu sein",1,5,3))
User_in.append(st.slider("Ich spreche gerne andere Sprachen",1,5,3))
User_in.append(st.slider("Ich mag es lange in der Natur zu sein",1,5,3))
User_in.append(st.slider("Ich arbeite gerne mit Computern",1,5,3))
User_in.append(st.slider("Ich mag es mit Zahlen zu arbeiten",1,5,3))
User_in.append(st.slider("Ich arbeite gerne allein",1,5,3))
User_in.append(st.slider("Ich mag Routine",1,5,3))
User_in.append(st.slider("Ich löse gerne Probleme",1,5,3))
User_in.append(st.slider("Ich verfasse gerne Texte",1,5,3))
User_in.append(st.slider("Ich mag es mit meinen Händen zu arbeiten",1,5,3))
User_in.append(st.slider("Ich mag es mich körperlich zu betätigen",1,5,3))
User_in.append(st.slider("Ich mag es vor Leuten zu sprechen",1,5,3))
User_in.append(st.slider("Ich mag es Verantwortung zu übernehmen",1,5,3))
User_in.append(st.slider("Mir ist es wichtig Menschen oder Tieren zu helfen (biologisch)",1,5,3))
User_in.append(st.slider("Ich mag es neue Themen zu erfahren",1,5,3))
User_in.append(st.slider("Ich arbeite gerne Experimente durchzuführen",1,5,3))
User_in.append(st.slider("Ich setze mich gerne mit theoretischen Fragen auseinander",1,5,3))
User_in.append(st.slider("Ich setze gerne meine eigenen Ideen um",1,5,3))
User_in.append(st.slider("Ich beschäftige mich gerne mit Kunst, Musik oder Literatur",1,5,3))
User_in.append(st.slider("Ich lese gerne wissenschaftliche Texte",1,5,3))
User_in.append(st.slider("Ich diskutiere gerne",1,5,3))
User_in.append(st.slider("Ich setze mich gerne mit anderen Kulturen auseinander",1,5,3))
User_in.append(st.slider("Ich beschäftige mich gerne mit Geschichte",1,5,3))
User_in.append(st.slider("Ich koordiniere oder sortiere gerne",1,5,3))
User_in.append(st.slider("Ich arbeite gerne von verschiedenen Orten",1,5,3))
User_in.append(st.slider("Ich gehe/würde gerne oft auf Arbeitsreisen gehen",1,5,3))

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
st.write(list[best_index])

