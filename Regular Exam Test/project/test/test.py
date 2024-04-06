from project.social_media import SocialMedia
from unittest import TestCase, main


class TestSocialMedia(TestCase):
    def setUp(self):
        self.sm = SocialMedia('Ivan', 'Instagram', 100, 'image')

    def test_correct_init(self):
        self.assertEqual("Ivan", self.sm._username, )
        self.assertEqual('Instagram', self.sm.platform)
        self.assertEqual(100, self.sm.followers)
        self.assertEqual('image', self.sm._content_type)
        self.assertEqual([], self.sm._posts)

    def test_followers__setter_negative_number_raise_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.sm.followers = -1

        self.assertEqual("Followers cannot be negative.", str(ex.exception))

    def test_validate_and_set_platform__wrong_platform_raise_value_error(self):
        allowed_platforms = ['Instagram', 'YouTube', 'Twitter']
        with self.assertRaises(ValueError) as ex:
            self.sm.platform = 'X'

        self.assertEqual(f'Platform should be one of {allowed_platforms}', str(ex.exception))

    def test_create_post_return_string(self):
        result = self.sm.create_post('image')

        self.assertEqual(f"New image post created by Ivan on Instagram.", result)
        self.assertEqual([{'comments': [], 'content': 'image', 'likes': 0}], self.sm._posts)

    def test_like_post_less_than_10_likes(self):
        self.sm.create_post('content')

        result = self.sm.like_post(0)

        self.assertEqual("Post liked by Ivan.", result)

    def test_like_post_exactly_10_likes(self):
        self.sm.create_post('content2')

        for i in range(10):
            self.sm.like_post(0)

        result = self.sm.like_post(0)

        self.assertEqual("Post has reached the maximum number of likes.", result)

    def test_like_post_wrong_index(self):
        self.sm.create_post('content2')

        result = self.sm.like_post(-1)

        self.assertEqual("Invalid post index.", result)

    def test_comment_on_post_len_less_than_10(self):
        self.sm.create_post('content2')

        result = self.sm.comment_on_post(0, 'content')

        self.assertEqual("Comment should be more than 10 characters.", result)

    def test_comment_on_post_len_equal_to_10(self):
        self.sm.create_post('content2')

        result = self.sm.comment_on_post(0, 'content is')

        self.assertEqual("Comment should be more than 10 characters.", result)

    def test_comment_on_post_success(self):
        self.sm.create_post('content2')

        result = self.sm.comment_on_post(0, 'content is more than 10 chars')
        result2 = [{'comments': [{'comment': 'content is more than 10 chars', 'user': 'Ivan'}],
                    'content': 'content2', 'likes': 0}]

        self.assertEqual("Comment added by Ivan on the post.", result)
        self.assertEqual(self.sm._posts, result2)


if __name__ == '__main__':
    main()
