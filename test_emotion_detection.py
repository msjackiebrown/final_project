from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector_joy(self):
        result = emotion_detector("I am glad this happened")
        dominant_emotion = max(result, key=result.get)
        self.assertEqual(dominant_emotion, 'joy')

    def test_emotion_detector_anger(self):
        result = emotion_detector("I am really mad about this")
        dominant_emotion = max(result, key=result.get)
        self.assertEqual(dominant_emotion, 'anger')

    def test_emotion_detector_disgust(self):
        result = emotion_detector("I feel disgusted just hearing about this")
        dominant_emotion = max(result, key=result.get)
        self.assertEqual(dominant_emotion, 'disgust')

    def test_emotion_detector_sadness(self):
        result = emotion_detector("I am so sad about this")
        dominant_emotion = max(result, key=result.get)
        self.assertEqual(dominant_emotion, 'sadness')

    def test_emotion_detector_fear(self):
        result = emotion_detector("I am really afraid that this will happen")
        dominant_emotion = max(result, key=result.get)
        self.assertEqual(dominant_emotion, 'fear')

if __name__ == "__main__":
    unittest.main()