import streamlit as st


def render_info_card(
    title,
    value,
    border_color="#4682B4"
):

    st.markdown(
        f"""
<div style="
padding: 1rem;
border-radius: 12px;
border-left: 5px solid {border_color};
background-color: rgba(255,255,255,0.03);
margin-bottom: 1rem;
">

<h4 style="margin-bottom:0.5rem;">
{title}
</h4>

<p style="
font-size:1rem;
margin-bottom:0;
">
{value}
</p>

</div>
""",
        unsafe_allow_html=True
    )