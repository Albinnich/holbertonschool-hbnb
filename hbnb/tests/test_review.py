import unittest
from models.review import Review

class TestReview(unittest.test):

    def add_test_review(self):
        review = Review(text="Nice host", user_id="123", place_id="456")
        self.assertIsNotNone(review.id)
        self.assertEqual(review.text, "Nice host")
        self.assertEqual(review.user_id, "123")
        self.assertEqual(review.place_id, "456")

    def test_save_method(self):
        review = Review(text="Save Test", user_id="123", place_id="456")
        old_updated_at = review.updated_at
        review.save()
        self.assertNotEqual(review.updated_at, old_updated_at)

    def test_str_method(self):
        review = Review(text="Str Test", user_id="123", place_id="456")
        self.assertIn("[Review]", str(review))
        self.assertIn(review.id, str(review))

if __name__ == '__main__':
    unittest.main()
