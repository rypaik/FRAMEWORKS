import streamlit as st



# Build a Counter
st.title('Counter Example without Session state')
st.text('The Counter resets to 0 - after the button is pressed, streamlit loops back to top')

count = 0

increment = st.button('Increment')
if increment:
    count += 1

st.write('Count = ', count)


# Initialization
import streamlit as st

# Check if 'key' already exists in session_state
# If not, then initialize it
if 'key' not in st.session_state:
    st.session_state['key'] = 'value'

# Session State also supports the attribute based syntax
if 'key' not in st.session_state:
    st.session_state.key = 'value'



# READS AND UPDATES
import streamlit as st

if 'key' not in st.session_state:
    st.session_state['key'] = 'value'

# Reads
st.write(st.session_state.key)

# Outputs: value

# UPDATES

if 'key' not in st.session_state:
    st.session_state['key'] = 'value'

# Updates
st.session_state.key = 'value2'     # Attribute API
st.session_state['key'] = 'value2'  # Dictionary like API

st.write(st.session_state)
st.session_state


# Streamlit Counter 
st.text("Counter with States")

import streamlit as st

st.title('Counter Example')
if 'count' not in st.session_state:
    st.session_state.count = 0

increment = st.button('Increment')
if increment:
    st.session_state.count += 1

st.write('Count = ', st.session_state.count)



# Session State and Callbacks
import streamlit as st

st.title('Counter Example using Callbacks')
if 'count' not in st.session_state:
    st.session_state.count = 0

def increment_counter():
    st.session_state.count += 1

st.button('Increment', on_click=increment_counter)

st.write('Count = ', st.session_state.count)


# Session State with Callbacks using args and kwargs
st.text("Session State Example - Callbacks and args")
import streamlit as st

st.title('Counter Example using Callbacks')
if 'count' not in st.session_state:
    st.session_state.count = 0

def increment_counter():
    st.session_state.count += 1

st.button('Increment', on_click=increment_counter)

st.write('Count = ', st.session_state.count)




# Session State with Callbacks using args and kwargs
st.text("Session State Example - Callbacks and kwargs")
import streamlit as st

st.title('Counter Example using Callbacks with kwargs')
if 'count' not in st.session_state:
    st.session_state.count = 0

def increment_counter(increment_value=0):
    st.session_state.count += increment_value

def decrement_counter(decrement_value=0):
    st.session_state.count -= decrement_value

st.button('Increment', on_click=increment_counter,
    kwargs=dict(increment_value=5))

st.button('Decrement', on_click=decrement_counter,
    kwargs=dict(decrement_value=1))

st.write('Count = ', st.session_state.count)
