import json
import streamlit as st

r"$\textsf{\Large This program alllows to see the genes responsible for the specific property}$"
uploaded_file = st.file_uploader(r"$\textsf{\normalsize Choose a file}$")
if uploaded_file is not None:
    data=json.load(uploaded_file)
    'Choose data to view:'
    left_column, middle_column, right_column =st.columns(3)
    with left_column:
        option = st.selectbox(
            'Data collection:',
             list(data.keys()))
    with middle_column:
        option2= st.selectbox(
            'Gene Function Category:',
             list(data.get(option).keys()))
    
    if option2=='Not in uniprot':
        'Genes that are not avalible in the uniprot library for this organism: ',
        st.write(data.get(option).get('Not in uniprot'))
    else:
        with right_column:
            option3= st.selectbox(
                'Detailed Annotations:',
                 list(data.get(option).get(option2).keys()))
        'Genes responsible for this property: '
        i=1
        for line in data.get(option).get(option2).get(option3):
            st.write(str(i),'.',line)
            i+=1