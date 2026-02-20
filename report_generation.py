import pandas as pd

def generate_report(analysis):
    """
    Generate a text report from analysis.
    
    Args:
        analysis (dict): Analysis results
    
    Returns:
        str: Report text
    """
    report = f"""
Profile Analysis Report
=======================

Status: {analysis['status']}
Confidence: {analysis['confidence']:.2f}%
Risk Level: {analysis['risk_level']}

Profile Features:
- Account Age: {analysis['features']['account_age']} days
- Post Count: {analysis['features']['post_count']}
- Friend Count: {analysis['features']['friend_count']}
- Link Ratio: {analysis['features']['link_ratio']:.2f}
- Duplicate Posts: {analysis['features']['duplicate_posts']}
- Average Likes: {analysis['features']['average_likes']:.2f}
- Comment Ratio: {analysis['features']['comment_ratio']:.2f}

Conclusion: {'This profile shows signs of being fake. Exercise caution.' if analysis['status'] == 'Fake Profile' else 'This profile appears to be legitimate.'}
"""
    return report