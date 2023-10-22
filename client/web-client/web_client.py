import streamlit as st
import base64
screen = st.empty()
st.title("Hi, welcome to ScanBack")
file_ = None

file_ = st.file_uploader("Please upload a receipt")
#st.empty
screen.empty()
import time
import streamlit as st
with st.spinner('Wait for it...'):
    time.sleep(5)
st.success('Done!')
screen.empty()

items=[]
if file_ is not None:
    from ReceiptScannerNormal import ReceiptScanner
    model = ReceiptScanner()
    items = model.getReceiptItems(file_)
    
print(items)
items[1]
st.write(items)
st.write(items[1])