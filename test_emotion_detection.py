from EmotionDetection.emotion_detection import emotion_detector

tests = [
    ("I am glad this happened", "joy"),
    ("I am really mad about this", "anger"),
    ("I feel disgusted just hearing about this", "disgust"),
    ("I am so sad about this", "sadness"),
    ("I am really afraid that this will happen", "fear")
]

for statement, expected in tests:
    result = emotion_detector(statement)
    dominant = result.get("dominant_emotion")
    print(f"Statement: {statement}")
    print(f"Detected: {dominant}, Expected: {expected}")
    print("Test Passed ✅" if dominant == expected else "Test Failed ❌")
    print("-" * 40)
