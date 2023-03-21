import streamlit as st
import pandas as pd
import re
import torch 

saved_model = torch.load('/content/drive/MyDrive/Research/ER model/banglaER')

st.title("Bangla Emotion Recognition")
st.text("A context-based approach for multilabel emotion recognition from bangla text")
st.text("")

t_input = st.empty()
comment = t_input.text_input("বাংলায় আপনার কমেন্টটি লিখুন:", placeholder="আমি বাংলাদেশকে ভালোবাসি।")
suggest_cmnt = ["এটা খুবই ভালো উদ্যোগ।", "এরা মানুষ নামের কলংক।", "তোরা ধোয়া তুলসীপাতা।"]
cols = st.columns(4)
s_btn0 = cols[0].button(suggest_cmnt[0])
s_btn1 = cols[1].button(suggest_cmnt[1])
s_btn2 = cols[2].button(suggest_cmnt[2])

if s_btn0:
	comment = t_input.text_input("বাংলায় আপনার কমেন্টটি লিখুনঃ", value=suggest_cmnt[0])
elif s_btn1:
	comment = t_input.text_input("বাংলায় আপনার কমেন্টটি লিখুনঃ", value=suggest_cmnt[1])
elif s_btn2:
	comment = t_input.text_input("বাংলায় আপনার কমেন্টটি লিখুনঃ", value=suggest_cmnt[2])

btn = st.button("সাবমিট")

emotions = ["Anger", "Contempt", "Disgust", "Enjoyment", "Sadness"]

st.text("")
st.text("")

st.markdown(
    """
    <style>
        div[data-testid="column"]
        {
            text-align: center;
        } 
    </style>
    """,unsafe_allow_html=True
)
success = """
		<p style='background-color: rgb(194, 240, 194);
		font-size: 20px;
		border-radius: 7px;
		align: center;
		line-height: 50px;
		text-align: center;'>
		✅</style></p>
		"""
error = """
		<p style='background-color: rgb(255, 204, 204);
		font-size: 20px;
		border-radius: 7px;
		align: center;
		line-height: 50px;
		text-align: center;'>
		🚫</style></p>
		"""
		

if comment != "" or btn:
	f_comment = re.sub('[^\u0980-\u09FF]',' ',str(comment)) #removing unnecessary punctuation
	f_comment = f_comment.strip()

	predictions, raw_outputs = saved_model.predict([f_comment])
	raw = raw_outputs[0]*100
	cols = st.columns(5)
	for i in range(5):
		cols[i].text(emotions[i])
		cols[i].markdown(f"![{emotions[i]} Gif](https://raw.githubusercontent.com/Shammi179/Multilabel_Bangla_ER_webapp/master/gifs/{emotions[i]}64.gif)")
		
		if predictions[0][i] or raw[i]>50:
			cols[i].markdown(success, unsafe_allow_html=True)
		else:
			cols[i].markdown(error, unsafe_allow_html=True)

st.text("")
st.text("")
st.text("")
st.text("")

st.write("Copyright © 2023 Dynamic DUO.")
