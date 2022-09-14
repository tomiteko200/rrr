
import streamlit as st

st.title('random website')
st.write('welcome to my dome')
button1=st.button('press me to start')
if button1:
    st.write('cool! you can proceed ')
like= st.checkbox('do you like my dome?')
button2=st.button('submit')
st.write(like)
if button2:
    if like:
        st.write('Thanks. like it too')
    else:
            st.write("😪,why don't you like it")
st.header('meat section')
meat =st.radio('what is your favourite meat?',('pork','beef','chicken'))
button3=st.button('submit meat')
if meat =='pork':
    st.write('very okay, the healthiest of them all')
else:
        st.write('ouch!try to start eating pork now!')
geopolitical_zone = st.selectbox('which geopolitical zone are you from?',('south-west','south-east','south-south','north-west','north-east','north-central'))
if st.button('submit geopolitical zone'):
    st.write('it is always nice being a Nigerian😊')
    st.write('continue to be patriotic ')
rest =st.multiselect('how do you rest?',('by sleeping','by watching movies','by playing games','others'))
button4=st.button('submit response')

no_of_hrs= st.slider('how many hrs do you sleep daily?',0,24)
st.button('enter')
if no_of_hrs<=6:
    st.write("No,that's not healty,increase your daily sleep time to 7 or 8hrs")
elif no_of_hrs>=9 :
    st.write("No,that's not healty,decrease your daily sleep time to 7 or 8hrs or maximum of 10hrs")
elif no_of_hrs==8 or no_of_hrs==7:
    st.write("nice, keep it up! it's healty for your health")
no_of_hr= st.slider('How many times do you eat a month?',0,150,30)
if st.button('next'):
    st.write('Answer the remaining questions')
sport_section=st.text_input('your favourite sport?')
button9=st.button('submit favourite sport')
if sport_section=='football':
    st.write('😜RONAlDO😂')
indoor_sport_section=st.text_input('your favourite indoor sport?','chess')
matric_no=st.number_input('input your matric number',2019)
st.button('press enter to submit matric number')

txt=st.text_area('''politics is a great game,
but particularly a game of numbers,
the majority wins,
and the minority loses.

''')
def run_sentiment_analysis(txt):
    st.write('Analysis DOne')
    
    

    
    
        



    

        
    




