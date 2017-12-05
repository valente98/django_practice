from django.test import TestCase
from django.urls import reverse


class TestAddView(TestCase):
    def test_without_nums_doesnt_set_answer(self):
        response = self.client.get(reverse('app:add'))

        answer = response.context.get('answer')

        self.assertIsNone(answer)

    def test_add_two_two_equals_four(self):
        response = self.client.get(
            reverse('app:add'),
            {'num1': 2,
             'num2': 2}, )

        answer = response.context.get('answer')

        self.assertEqual(answer, 4)

    def test_add_four_negthree_equals_one(self):
        response = self.client.get(
            reverse('app:add'),
            {'num1': 4,
             'num2': -3}, )

        answer = response.context.get('answer')

        self.assertEqual(answer, 1)


class TestDoubleView(TestCase):
    def test_without_num_doesnt_set_answer(self):
        response = self.client.get(reverse('app:double'))

        answer = response.context.get('answer')

        self.assertIsNone(answer)


# Create your tests here.
