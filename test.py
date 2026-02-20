from prediction import predict_profile
import joblib

# Test with fake profile features
fake_features = [10, 600, 20, 0.8, 30, 5.0, 0.05]
model = joblib.load('models/fake_profile_model.pkl')
proba = model.predict_proba([fake_features])[0]
print(f"Fake features proba: {proba}")
status, confidence, risk = predict_profile(fake_features)
print(f"Status: {status}")
print(f"Confidence: {confidence:.2f}%")
print(f"Risk: {risk}")

# Test with real profile features
real_features = [365, 50, 200, 0.1, 5, 25.0, 0.2]
proba = model.predict_proba([real_features])[0]
print(f"\nReal features proba: {proba}")
status, confidence, risk = predict_profile(real_features)
print(f"Status: {status}")
print(f"Confidence: {confidence:.2f}%")
print(f"Risk: {risk}")