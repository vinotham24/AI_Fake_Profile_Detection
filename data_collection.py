import pandas as pd
import numpy as np

# Generate synthetic data for fake profile detection
np.random.seed(42)
n_samples = 1000

# Features
account_age = np.random.randint(1, 365*5, n_samples)  # days
post_count = np.random.randint(0, 1000, n_samples)
friend_count = np.random.randint(0, 5000, n_samples)
link_ratio = np.random.uniform(0, 1, n_samples)
duplicate_posts = np.random.randint(0, 100, n_samples)
average_likes = np.random.uniform(0, 1000, n_samples)
comment_ratio = np.random.uniform(0, 1, n_samples)

# Label: 1 for fake, 0 for real
# Fake profiles: low account_age, high post_count, low friend_count, high link_ratio, etc.
label = []
for i in range(n_samples):
    score = 0
    if account_age[i] < 30: score += 1
    if post_count[i] > 500: score += 1
    if friend_count[i] < 50: score += 1
    if link_ratio[i] > 0.5: score += 1
    if duplicate_posts[i] > 20: score += 1
    if average_likes[i] < 10: score += 1
    if comment_ratio[i] < 0.1: score += 1
    label.append(1 if score >= 4 else 0)

# Create DataFrame
data = pd.DataFrame({
    'account_age': account_age,
    'post_count': post_count,
    'friend_count': friend_count,
    'link_ratio': link_ratio,
    'duplicate_posts': duplicate_posts,
    'average_likes': average_likes,
    'comment_ratio': comment_ratio,
    'label': label
})

# Save to CSV
data.to_csv('data/synthetic_data.csv', index=False)
print("Synthetic data generated and saved to data/synthetic_data.csv")