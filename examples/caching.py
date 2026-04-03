from contextlib import contextmanager
import time
import streamlit as st

@contextmanager
def display_load_time():
    start_time = time.time()

    try:
        yield
    finally:
        elapsed = time.time() - start_time
        st.caption(f"Page loaded in {elapsed:.2f} seconds")

@st.cache_data
def slow_thing():
    time.sleep(2)  # Simulate a slow operation

with display_load_time():
    # Simulate a long-running operation
    slow_thing()

    st.markdown("# This page is cached")
    st.write("This page simulates a long-running operation, but it will be cached for faster loading on subsequent visits.")
    