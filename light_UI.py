import streamlit as st
import DL_app_main

def main():
    col1, col2, col3, swich = st.columns(4)

    with col1:
        n_1 = st.number_input(label='0_number_arm', value=1.0,key='M_1')
        st.write('Percent:', n_1)
    
    with col2:
        n_2 = st.number_input(label='1_number_arm', value=1.0,key='M_2')
        st.write('Percent:', n_2)

    with col3:
        n_3 = st.number_input(label='2_number_arm', value=1.0,key='M_3')
        st.write('Percent:', n_3)

    with swich:
        n_e = st.number_input(label='e_percent', value=1.0,key='M_e')

        if st.button('check',key='M'):
            if n_1 > 0 and n_2 > 0 and n_3 > 0 and n_e >0:

                st.write('answer:', DL_app_main.start(n_1,n_2,n_3,n_e))

if __name__ == '__main__':
    main()
