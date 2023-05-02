import streamlit as st
import tensorflow as tf
from PIL import Image

#inuktitut_translator=tf.saved_model.load('translator_inuktitut')


st.set_page_config(
    page_title='Translation',
    layout='centered'
)

image = Image.open('Aingailogo.png')
new_image = image.resize((850, 450))
    
add_selectbox = st.sidebar.image(new_image,caption=" ")
st.sidebar.title("About US / ᐅᕙᒍᑦ ᒥᒃᓵᓄᑦ") 
st.sidebar.write("AingA.I. is a 100% Indigenous company dedicated to preserving the Inuktitut language by providing language tools for use by all age groups.")
st.sidebar.write('ᓯᕗᓪᓕᖅ ᐱᔨᑦᑎᕋᐅᑎᒋᔭᕗᑦ ᑎᑎᕋᖅᓯᒪᕗᑦ ᑎᑎᕋᖅᓯᒪᓪᓗᑎᒃ ᐅᖃᐅᓯᖅᑕᑦ ᑐᑭᓕᐅᖅᑕᐅᓯᒪᔪᑦ ᐃᓄᒃᑎᑐᑦ ᐊᒻᒪ ᖃᓪᓗᓈᑐᑦ. ᓴᓇᕐᕈᑎᒃᑲᓐᓃᑦ ᓴᖅᑭᓛᓕᖅᑐᑦ.')
st.sidebar.write("Every day life, cultural activities, education, work, and for leisure.")
st.sidebar.write("The first service we provide is text to text language translation between Inuktitut and English. Additional tools are coming soon.")
st.sidebar.write('ᖃᐅᑕᒫᑦ ᐃᓅᓯᖅ, ᐃᓕᖅᑯᓯᑐᖃᓕᕆᓂᖅ, ᐃᓕᓐᓂᐊᕐᓂᖅ, ᐃᖅᑲᓇᐃᔭᕐᓂᖅ, ᐊᒻᒪ ᓴᐃᓕᓂᖅ.')

st.title('Aing A.I.                \t ᐊᐃᖓᐃ')

selected=st.selectbox('Please Select',('English to Inuktitut', 'Inuktitut to English'))
st.write(str(selected))

if selected=='English to Inuktitut':

    st.markdown('### '+'English / ᖃᓪᓗᓈᖅ') 
    eng_text=st.text_area('')
    st.markdown('### '+'Inuktitut / ᐃᓄᒃᑎᑐᑦ')
    inuktitut_box=st.empty()
    inuktitut_box.text_area(label='hello',label_visibility='hidden')
    translate_button=st.button('Translate')

    if translate_button:
        out='ᕼᐊᓘ ᖃᐅᔨᓴᖅᑕᕗᑦ'
        
        inuktitut_box.text_area(label='hello',value=out,label_visibility='hidden')
else:
    st.markdown('### '+'Inuktitut / ᐃᓄᒃᑎᑐᑦ')
    inuktitut_text=st.text_area('')
    st.markdown('### '+'English / ᖃᓪᓗᓈᖅ') 
    english_box=st.empty()
    english_box.text_area(label='hello',label_visibility='hidden')
    translate_button=st.button('Translate')


    # if translate_button:
    #     out='Hello'
    #     result=inuktitut_translator.translate([inuktitut_text])
    #     result=result[0].numpy().decode()
    #     english_box.text_area(label='hello',value=result,label_visibility='hidden')

