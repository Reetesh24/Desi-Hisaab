import time

import streamlit as st

if "dict" not in st.session_state:
    st.session_state.dict = {}
if "" in st.session_state.dict:
    del st.session_state.dict[""]
if "sum" not in st.session_state:
    st.session_state.sum = 0
if "extra_count" not in st.session_state:
    st.session_state.extra_count = 0
if "add_more" not in st.session_state:
    st.session_state.add_more = True

st.title(":orange[Desi Hisaab]")

person = st.number_input("How many persons?",step=1, format='%d', placeholder= 'like, 1,2,3,4,....')
size  = st.number_input("How many places you spend?",step=1, format='%d', placeholder= 'like, 1,2,3,4,....')
for i in range(int(size)):
    key = st.text_input("Name of the product", placeholder= 'Samsoa, Maggie, Coke, ...', key= f'item_{i}')
    value = st.number_input("Enter Price of the product Rs.",step=1, format= "%d", placeholder=' Rs. 12,40,50', key= f'amount_{i}')
    if key:
        st.session_state.dict[key] = value
st.write("---")

if st.session_state.add_more:
    with st.form(clear_on_submit=True, key = "add_more_item"):
        key = st.text_input("Name of the product", placeholder= 'Samsoa, Maggie, Coke, ...', key=f'new_item_{st.session_state.extra_count}')
        value = st.number_input("Enter Price of the product Rs.",step=1, format= "%d", placeholder=' Rs. 12,40,50', key= f'new_amount_{st.session_state.extra_count}')
        submitted = st.form_submit_button("Add Item")
        if submitted and key:
            st.session_state.dict[key] = value
            # st.session_state.extra_count += 1
    st.markdown("### Your Items")
    for key, value in st.session_state.dict.items():
        st.write(f'**{key.capitalize()}** -> _Rs. {value}_')
st.write("---")
                # st.write(f' {key} : : Rs. {value}')
                # st.session_state.sum = st.session_state.sum + value
if st.button('Finish and Split Bill'):
    st.session_state.add_more= False
    st.session_state.sum = sum(st.session_state.dict.values())
    if st.session_state.sum != 0 and person >0:
        div = st.session_state.sum / person
        st.write("Okay Your bill is now generating")
        with st.spinner("Please Wait"):
            time.sleep(3)
        st.write(f"Your Total Amount: Rs. {st.session_state.sum}")
        st.write(f'The Splitted bill is here: Rs. {div: .2f}/- Per Head')
    else:
        st.error("Please Fill All Sections Correctly")
