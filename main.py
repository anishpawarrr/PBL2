import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title='PICT🆙', page_icon='bi bi-arrow-up', layout='centered', initial_sidebar_state='expanded')

h = 'Home'
sea = 'Search'
set = 'Settings'
abtus = 'About Us'
opt = option_menu(menu_title='PICTup', options=[h, sea, set, abtus], default_index=0, menu_icon='bi bi-box-arrow-up',
                      icons=['bi bi-house', 'bi bi-search', 'bi bi-gear-wide-connected', 'bi bi-info'], orientation= 'horizontal')
# sb = st.sidebar.selectbox(label='Sidebar', options=['1','2','3'], index=0, )



with st.sidebar as sb0:
    opt = option_menu(menu_title='PICTup', options=[h, sea, set, abtus], default_index=0, menu_icon='bi bi-box-arrow-up',
                      icons=['bi bi-house', 'bi bi-search', 'bi bi-gear-wide-connected', 'bi bi-info'], )

if opt == h:
    st.write('Home screen')
elif opt == sea:
    st.write('Search')
elif opt == set:
    st.write('Settings')
elif opt == abtus:
    st.write('About Us')