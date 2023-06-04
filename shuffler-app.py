import streamlit as st
import pandas as pd
import time
import random



headers = st.container()
model_training = st.container() 

with headers:
    st.title('Card Shuffler',)
    st.subheader("""A card-shuffling app for your card-shuffling needs.🃏""")
    st.markdown("""Have you ever played a board game via Teams and realised that the cards you
    have to shuffle are in a very inconvenient pdf file? This app is exactly what you need.""" , unsafe_allow_html=False)
    st.markdown("""Instructions:✨""", unsafe_allow_html=False)
    st.markdown("""**1.** Use the slider to select the number of cards you have.""", unsafe_allow_html=False)
    st.markdown("""**2.** Click on **Shuffle & Draw** to receive your card.""", unsafe_allow_html=False)


    number_of_cards = st.slider('# of cards', 1, 12, 1)
    card_list = [i for i in range(1,number_of_cards + 1)]
    
    if st.button('Shuffle & Draw'):
        st.write("Shuffling...")
        time.sleep(0.5)
        st.write(f"""This is your card 🃏""")
        time.sleep(0.5)
        st.title(f"{random.choice(card_list)}")
        time.sleep(0.5)
        if st.button('Reset'):
            st.write('')
    else:
        st.write('')