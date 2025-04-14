import re
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Password Strength Analyzer", 
    page_icon="🔒",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# [CSS and initial HTML setup remains identical...]

# Main container
st.markdown("<div class='main-container'>", unsafe_allow_html=True)

# Title and description
st.markdown("<h1>🔒 Password Strength Analyzer</h1>", unsafe_allow_html=True)
st.markdown(
    "<p class='description'>Check how secure your password is and get instant feedback for improvement</p>", 
    unsafe_allow_html=True
)

# Password input
password = st.text_input(
    "Enter your password", 
    type="password", 
    placeholder="Type your password here...",
    help="We don't store your password. It's checked locally in your browser."
)

if password:
    # Password requirements configuration
    requirements = [
        {'text': 'Minimum 8 characters', 'check': lambda p: len(p) >= 8},
        {'text': 'Contains uppercase letter (A-Z)', 'check': lambda p: re.search(r'[A-Z]', p) is not None},
        {'text': 'Contains lowercase letter (a-z)', 'check': lambda p: re.search(r'[a-z]', p) is not None},
        {'text': 'Contains digit (0-9)', 'check': lambda p: re.search(r'\d', p) is not None},
        {'text': 'Contains special character (!@#$%^&*)', 'check': lambda p: re.search(r'[!@#$%^&*]', p) is not None},
        {'text': 'No common patterns', 'check': lambda p: not re.search(r'password|1234|qwerty|abc123', p, re.IGNORECASE)}
    ]

    # Check requirements
    met_requirements = [req['check'](password) for req in requirements]
    score = sum(met_requirements)
    total_requirements = len(requirements)
    strength_percent = (score / total_requirements) * 100

    # Determine strength parameters
    if score <= 2:
        color = '#ef4444'  # Red
        strength_label = 'Weak'
        feedback = "Your password is vulnerable. Consider adding more complexity."
    elif score <= 4:
        color = '#f59e0b'  # Orange
        strength_label = 'Moderate'
        feedback = "Your password needs improvement for better security."
    else:
        color = '#10b981'  # Green
        strength_label = 'Strong'
        feedback = "Your password is highly secure! Well done!"

    # Strength indicator bar
    st.markdown(f"""
    <div class="strength-indicator">
        <div class="strength-bar" style="width: {strength_percent}%; background-color: {color};"></div>
    </div>
    """, unsafe_allow_html=True)

    # Requirements checklist
    st.markdown("<div class='requirement-list'>", unsafe_allow_html=True)
    for i, req in enumerate(requirements):
        icon = '✔' if met_requirements[i] else '✖'
        status_class = 'valid' if met_requirements[i] else 'invalid'
        st.markdown(f"""
        <div class="requirement-item">
            <span class="requirement-icon {status_class}">{icon}</span>
            <span>{req['text']}</span>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Feedback card
    st.markdown(f"""
    <div class="result-card" style="border-left-color: {color};">
        <strong>{strength_label}:</strong> {feedback}
    </div>
    """, unsafe_allow_html=True)

# Security footer
st.markdown(
    "<p class='footer'>🔒 Your password is processed locally and never stored</p>", 
    unsafe_allow_html=True
)

# Close main container
st.markdown("</div>", unsafe_allow_html=True)
