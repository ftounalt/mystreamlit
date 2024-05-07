import streamlit as st
import pickle
svm=pickle.load(open('gb_model.pkl','rb'))

def classify(num):
    if num==1:
        return 'leave'
    elif num ==0:
        return 'not leave'
    else:
        return 'nothing'
    
def main():
    st.title("Streamlit Tutorial")
    html_temp = """
    <div style="background-color:teal ;padding:10px">
    <h2 style="color:white;text-align:center;">leave or not Classification</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    sl = st.selectbox('Select you education', [i for i in range(3)])
    s2 = st.text_input('What is the joining year', value='0')
    s3 = st.selectbox('Select the city', [i for i in range(3)])
    s4 = st.selectbox('Select the PaymentTier', [ i for i in range(3)])
    s5 = st.text_input('age', value='0')
    s6 = st.selectbox('gender', [i for i in range(2)])
    s7 = st.selectbox('EverBenched', [i for i in range(2)])
    s8 = st.text_input('ExperienceInCurrentDomain', value='0')
    inputs=[[sl,s2,s3,s4,s5,s6,s7,s8]]
    if st.button('Classify'):
        st.success(classify(svm.predict(inputs)))


if __name__=='__main__':
    main()