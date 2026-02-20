# AI-Based Fake Profile Detection System

## Overview

This project implements an AI-based system to detect fake social media profiles using machine learning. The system analyzes various profile attributes to classify profiles as real or fake.

## Features

- **Profile Behavior Analysis**: Detects abnormal activities and suspicious behavior patterns.
- **Post Frequency Analysis**: Identifies spam-like posting patterns.
- **Friends/Followers Analysis**: Analyzes friend and follower ratios to detect fake accounts.
- **AI Classification**: Uses Random Forest algorithm for classification.
- **User Interface**: Streamlit-based web interface for easy interaction.
- **Confidence Scoring**: Provides prediction confidence percentage.
- **Risk Assessment**: Categorizes profiles as High or Low risk.

## Technologies Used

- **Python**: Core programming language
- **Scikit-learn**: Machine learning library
- **Pandas & NumPy**: Data manipulation
- **Streamlit**: Web UI framework
- **NLTK**: Natural language processing (for future text analysis)
- **Matplotlib & Seaborn**: Data visualization

## Dataset Attributes

- `account_age`: Age of the account in days
- `post_count`: Number of posts
- `friend_count`: Number of friends/followers
- `link_ratio`: Ratio of posts containing links
- `duplicate_posts`: Number of duplicate posts
- `average_likes`: Average likes per post
- `comment_ratio`: Ratio of posts with comments

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Generate synthetic data:
   ```bash
   python data_collection.py
   ```
4. Train the model:
   ```bash
   python model_training.py
   ```
5. Run the application:
   ```bash
   streamlit run ui.py
   ```

## Usage

1. Start the Streamlit app
2. Enter profile details in the input fields
3. Click "Analyze Profile"
4. View the prediction results including status, confidence, and risk level

## Project Structure

```
├── data/
│   └── synthetic_data.csv          # Synthetic dataset
├── models/
│   └── fake_profile_model.pkl      # Trained model
├── data_collection.py              # Data generation script
├── feature_extraction.py           # Feature extraction utilities
├── model_training.py               # Model training script
├── prediction.py                   # Prediction functions
├── profile_analysis.py             # Profile analysis logic
├── report_generation.py            # Report generation
├── ui.py                           # Streamlit user interface
├── utils.py                        # Utility functions
├── requirements.txt                # Python dependencies
└── README.md                       # This file
```

## Machine Learning Model

The system uses a Random Forest classifier trained on synthetic data. The model achieves approximately 96% accuracy on test data.

## Future Enhancements

- Real-time social media API integration
- Deep learning models for better accuracy
- Image-based fake profile detection
- Advanced NLP for post content analysis
- Bot detection algorithms
- Browser extension support

## Limitations

- Accuracy depends on quality and quantity of training data
- Cannot access private profile data
- Requires regular model updates for evolving fake profile patterns

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## License

This project is open source and available under the MIT License.