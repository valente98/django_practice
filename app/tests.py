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

    def test_double_two_equals_four(self):
        response = self.client.get(
            reverse('app:double'),
            {'num1': 2}, )

        answer = response.context.get('answer')

        self.assertEqual(answer, 4)

    def test_double_neg4_equals_negeight(self):
        response = self.client.get(
            reverse('app:double'),
            {'num1': -4}, )

        answer = response.context.get('answer')

        self.assertEqual(answer, -8)


class TestmultThreeView(TestCase):
    def test_test_without_num_doesnt_set_answer(self):
        response = self.client.get(reverse('app:multThree'))

        answer = response.context.get('answer')

        self.assertIsNone(answer)

    def test_multThre_three_four_eight_equals_ninetysix(self):
        response = self.client.get(
            reverse('app:multThree'),
            {'num1': 3,
             'num2': 4,
             'num3': 8}, )

        answer = response.context.get('answer')

        self.assertEqual(answer, 96)

    def test_multThre_seven_one_two_equals_fourteen(self):
        response = self.client.get(
            reverse('app:multThree'),
            {'num1': 7,
             'num2': 1,
             'num3': 2}, )

        answer = response.context.get('answer')

        self.assertEqual(answer, 14)


class TestEarningView(TestCase):
    def test_test_without_num_doesnt_set_answer(self):
        response = self.client.get(reverse('app:earning'))

        answer = response.context.get('answer')

        self.assertIsNone(answer)

    def test_earning_seven_one_two_equals_oneHudredThirtyFive(self):
        response = self.client.get(
            reverse('app:earning'),
            {'num1': 7,
             'num2': 1,
             'num3': 2}, )

        answer = response.context.get('answer')

        self.assertEqual(answer, 135)

    def test_earning_one_five_ten_equals_oneHundredSixtyFive(self):
        response = self.client.get(
            reverse('app:earning'),
            {'num1': 1,
             'num2': 5,
             'num3': 10}, )

        answer = response.context.get('answer')

        self.assertEqual(answer, 165)


# Create your tests here.
