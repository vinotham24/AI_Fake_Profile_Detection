def extract_features(profile_data):
    """
    Extract features from profile data.
    
    Args:
        profile_data (dict): Dictionary with profile attributes
    
    Returns:
        list: List of features
    """
    features = [
        profile_data.get('account_age', 0),
        profile_data.get('post_count', 0),
        profile_data.get('friend_count', 0),
        profile_data.get('link_ratio', 0.0),
        profile_data.get('duplicate_posts', 0),
        profile_data.get('average_likes', 0.0),
        profile_data.get('comment_ratio', 0.0)
    ]
    return features