from prediction import predict_profile

def analyze_profile(profile_data):
    """
    Analyze profile and return detailed analysis.
    
    Args:
        profile_data (dict): Profile data
    
    Returns:
        dict: Analysis results
    """
    features = [
        profile_data['account_age'],
        profile_data['post_count'],
        profile_data['friend_count'],
        profile_data['link_ratio'],
        profile_data['duplicate_posts'],
        profile_data['average_likes'],
        profile_data['comment_ratio']
    ]
    
    status, confidence, risk = predict_profile(features)
    
    analysis = {
        'status': status,
        'confidence': confidence,
        'risk_level': risk,
        'features': {
            'account_age': profile_data['account_age'],
            'post_count': profile_data['post_count'],
            'friend_count': profile_data['friend_count'],
            'link_ratio': profile_data['link_ratio'],
            'duplicate_posts': profile_data['duplicate_posts'],
            'average_likes': profile_data['average_likes'],
            'comment_ratio': profile_data['comment_ratio']
        }
    }
    
    return analysis