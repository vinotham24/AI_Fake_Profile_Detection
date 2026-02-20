import streamlit as st
from prediction import predict_profile

st.title("🛡️ AI-Based Fake Profile Detection System")

st.markdown("""
This system analyzes social media profiles to detect fake accounts using machine learning.
Enter the profile details below and click 'Analyze Profile' to get the prediction.
""")

st.header("📝 Enter Profile Details")

col1, col2 = st.columns(2)

with col1:
    account_age = st.number_input("Account Age (days)", min_value=0, value=100)
    post_count = st.number_input("Post Count", min_value=0, value=50)
    friend_count = st.number_input("Friend Count", min_value=0, value=200)

with col2:
    link_ratio = st.slider("Link Ratio", 0.0, 1.0, value=0.1)
    duplicate_posts = st.number_input("Duplicate Posts", min_value=0, value=5)
    average_likes = st.number_input("Average Likes", min_value=0.0, value=25.0, format="%.2f")
    comment_ratio = st.slider("Comment Ratio", 0.0, 1.0, value=0.2)

if st.button("🔍 Analyze Profile"):
    features = [account_age, post_count, friend_count, link_ratio, duplicate_posts, average_likes, comment_ratio]
    status, confidence, risk = predict_profile(features)
    
    st.header("📊 Prediction Result")
    if status == "Fake Profile":
        st.error(f"🚨 {status}")
    else:
        st.success(f"✅ {status}")
    
    st.write(f"**Confidence:** {confidence:.2f}%")
    st.write(f"**Risk Level:** {risk}")
    
    # Risk level color
    if risk == "High":
        st.markdown('<p style="color:red; font-weight:bold;">High Risk</p>', unsafe_allow_html=True)
    else:
        st.markdown('<p style="color:green; font-weight:bold;">Low Risk</p>', unsafe_allow_html=True)

st.markdown("---")
st.markdown("**Note:** This is a demonstration using synthetic data. In a real application, use actual profile data.")