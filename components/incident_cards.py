import streamlit as st
import html


def render_info_card(
    title,
    value,
    border_color="#4682B4"
):

    safe_title = html.escape(str(title))
    safe_value = html.escape(str(value))
    safe_border = html.escape(str(border_color))

    card_html = f"""
<div style="
    padding:1rem;
    border-radius:12px;
    border-left:5px solid {safe_border};
    background-color:rgba(255,255,255,0.03);
    margin-bottom:1rem;
">

<h4 style="
    margin-top:0;
    margin-bottom:0.5rem;
">
    {safe_title}
</h4>

<div style="
    font-size:1rem;
    line-height:1.6;
    white-space:pre-wrap;
    word-break:break-word;
">
    {safe_value}
</div>

</div>
"""

    st.markdown(
        card_html,
        unsafe_allow_html=True
    )