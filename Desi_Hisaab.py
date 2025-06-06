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

person = st.number_input("How many person are there in this bill?",step=1, format='%d', placeholder= 'like, 1,2,3,4,....')
size  = st.number_input("How many places or  you done (in number)",step=1, format='%d', placeholder= 'like, 1,2,3,4,....')
for i in range(int(size)):
    key = st.text_input(f"Type the name of the product you spend money on (in strings) as Key".capitalize(), placeholder= 'Samsoa, Maggie, Coke, ...', key= f'item_{i}')
    value = st.number_input(f"Enter the total amount you spend on that product (integer) as Value (in Rs.)", placeholder=' Rs. 12,40,50', key= f'amount_{i}')
    if key:
        st.session_state.dict[key] = value
st.write("---")

if st.session_state.add_more:
    with st.form(key = "add_more_item"):
        key = st.text_input(f"Type the name of the product you spend money on (in strings) as Key".capitalize(), placeholder='Samsoa, Maggie, Coke, ...', key=f'new_item_{st.session_state.extra_count}')
        value = st.number_input(f"Enter the total amount you spend on that product (integer) as Value (in Rs.)", placeholder=' Rs. 12,40,50', key=f'new_amount_{st.session_state.extra_count}')
        submitted = st.form_submit_button("Add Item")
        if submitted and key:
            st.session_state.dict[key] = value
            # for key, value in st.session_state.dict.items():
            #     st.session_state.dict[key] = value
            st.session_state.extra_count += 1
    st.markdown("### Your Items")
    for key, value in st.session_state.dict.items():
        st.write(f'**{key.capitalize()}** -> _Rs. {value}_')
st.write("---")
                # st.write(f' {key} : : Rs. {value}')
                # st.session_state.sum = st.session_state.sum + value
if st.button('Finish and Split Bill'):
    st.session_state.sum = sum(st.session_state.dict.values())
    if st.session_state.sum != 0 and person >0:
        st.session_state.add_more = False
        st.write("Okay! I'm generating your bill now.")
        st.write("Your bill is generating please wait....")
        with st.spinner("Please wait...."):
            time.sleep(3)
        div = st.session_state.sum / person
        st.write("")
        st.write(f'Total Amount: Rs. {st.session_state.sum}')
        st.write(f'Each person have to pay: Rs.{div: .2f}/-per head')