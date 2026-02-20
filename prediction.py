import joblib

def predict_profile(features):
    """
    Predict if a profile is fake or real based on features.
    
    Args:
        features (list): [account_age, post_count, friend_count, link_ratio, duplicate_posts, average_likes, comment_ratio]
    
    Returns:
        tuple: (status, confidence, risk_level)
    """
    model = joblib.load('models/fake_profile_model.pkl')
    proba = model.predict_proba([features])[0]
    prediction = 1 if proba[1] > 0.05 else 0  # Lower threshold for fake detection
    confidence = max(proba) * 100
    status = "Fake Profile" if prediction == 1 else "Real Profile"
    risk_level = "High" if prediction == 1 else "Low"
    return status, confidence, risk_level