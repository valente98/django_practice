from django.urls import reverse


class TestAddView:
    def test_without_nums_doesnt_set_answer(self, client):
        response = client.get(reverse('app:add'))

        answer = response.context.get('answer')

        assert answer is None

    def test_add_two_two_equals_four(self, client):
        response = client.get(
            reverse('app:add'),
            {'num1': 2,
             'num2': 2}, )

        answer = response.context.get('answer')

        assert answer == 4

    def test_add_four_negthree_equals_one(self, client):
        response = client.get(
            reverse('app:add'),
            {'num1': 4,
             'num2': -3}, )

        answer = response.context.get('answer')

        assert answer == 1


class TestDoubleView:
    def test_without_num_doesnt_set_answer(self, client):
        response = client.get(reverse('app:double'))

        answer = response.context.get('answer')

        assert answer is None

    def test_double_two_equals_four(self, client):
        response = client.get(
            reverse('app:double'),
            {'num': 2}, )

        answer = response.context.get('answer')

        assert answer == 4

    def test_double_neg4_equals_negeight(self, client):
        response = client.get(
            reverse('app:double'),
            {'num': -4}, )

        answer = response.context.get('answer')

        assert answer == -8


class TestmultThreeView:
    def test_test_without_num_doesnt_set_answer(self, client):
        response = client.get(reverse('app:multThree'))

        answer = response.context.get('answer')

        assert answer is None

    def test_multThre_three_four_eight_equals_ninetysix(self, client):
        response = client.get(
            reverse('app:multThree'),
            {'num1': 3,
             'num2': 4,
             'num3': 8}, )

        answer = response.context.get('answer')

        assert answer == 96

    def test_multThre_seven_one_two_equals_fourteen(self, client):
        response = client.get(
            reverse('app:multThree'),
            {'num1': 7,
             'num2': 1,
             'num3': 2}, )

        answer = response.context.get('answer')

        assert answer == 14


class TestEarningView:
    def test_test_without_num_doesnt_set_answer(self, client):
        response = client.get(reverse('app:earning'))

        answer = response.context.get('answer')

        assert answer is None

    def test_earning_seven_one_two_equals_oneHudredThirtyFive(self, client):
        response = client.get(
            reverse('app:earning'),
            {'seat1': 7,
             'seat2': 1,
             'seat3': 2}, )

        answer = response.context.get('answer')

        assert answer == 135

    def test_earning_one_five_ten_equals_oneHundredSixtyFive(self, client):
        response = client.get(
            reverse('app:earning'),
            {'seat1': 1,
             'seat2': 5,
             'seat3': 10}, )

        answer = response.context.get('answer')

        assert answer == 165


class TestBothTrueview:
    def test_without_truth_doesnt_set_answer(self, client):
        response = client.get(reverse('app:bothTrue'))

        answer = response.context.get('answer')

        assert answer == False

    def test_bothTrue_true_false_equals_false(self, client):
        response = client.get(
            reverse('app:bothTrue'),
            {'bool1': True,
             'bool2': False}, )

        answer = response.context.get('answer')

        assert answer == False

    def test_bothTrue_true_true_equals_true(self, client):
        response = client.get(
            reverse('app:bothTrue'),
            {'bool1': True,
             'bool2': True}, )

        answer = response.context.get('answer')

        assert answer == True

    def test_bothTrue_false_false_equals_false(self, client):
        response = client.get(
            reverse('app:bothTrue'),
            {'bool1': False,
             'bool2': False}, )

        answer = response.context.get('answer')

        assert answer == False


class TestWalkorDriveview:
    def test_without_num_and_bool_doesnt_set_answer(self, client):
        response = client.get(reverse('app:WalkorDrive'))

        answer = response.context.get('answer')

        assert answer is None

    def test_WalkorDrive_three_miles_Goodweather_should_drive(self, client):
        response = client.get(
            reverse('app:WalkorDrive'),
            {'miles': 3,
             'Weather': True}, )

        answer = response.context.get('answer')

        assert answer == 'You should drive'

    def test_WalkorDrive_pointtTwo_miles_Goodweather_should_walk(self, client):
        response = client.get(
            reverse('app:WalkorDrive'),
            {'miles': .2,
             'Weather': True}, )

        answer = response.context.get('answer')

        assert answer == 'You should walk'


class TestHowPopulatedView:
    def test_without_num_doesnt_set_answer(self, client):
        response = client.get(reverse('app:howPopulated'))

        answer = response.context.get('answer')

        assert answer is None

    def test_HowPopulated_100_poulation_1_landArea_Equals_sparsely_populated(
            self, client):
        response = client.get(
            reverse('app:howPopulated'),
            {'Population': 100,
             'LandArea': 1}, )

        answer = response.context.get('answer')

        assert answer == 'Sparsely Populated'

    def test_HowPopulated_200_poulation_1_landArea_Equals_sparsely_populated(
            self, client):
        response = client.get(
            reverse('app:howPopulated'),
            {'Population': 200,
             'LandArea': 1}, )

        answer = response.context.get('answer')

        assert answer == 'Densely Populated'


class TestGoldStarView:
    def test_without_num_doesnt_set_answer(self, client):
        response = client.get(reverse('app:goldStar'))

        answer = response.context.get('answer')

        assert answer is None

    def test_goldStar_999_point_should_equal_one_star(self, client):
        response = client.get(
            reverse('app:goldStar'),
            {'Points': 999}, )

        answer = response.context.get('answer')

        assert answer == '*'

    def test_goldStar_2000_point_should_equal_2_star(self, client):
        response = client.get(
            reverse('app:goldStar'),
            {'Points': 2000}, )

        answer = response.context.get('answer')

        assert answer == '**'

    def test_goldStar_6799_point_should_equal_3_star(self, client):
        response = client.get(
            reverse('app:goldStar'),
            {'Points': 6799}, )

        answer = response.context.get('answer')

        assert answer == '***'

    def test_goldStar_8765_point_should_equal_4_star(self, client):
        response = client.get(
            reverse('app:goldStar'),
            {'Points': 8765}, )

        answer = response.context.get('answer')

        assert answer == '****'

    def test_goldStar_20000_point_should_equal_5_star(self, client):
        response = client.get(
            reverse('app:goldStar'),
            {'Points': 20000}, )

        answer = response.context.get('answer')

        assert answer == '*****'


class TestHowManyPointsView:
    def test_howManyPoints_touchDown_equals_6(self, client):
        response = client.get(
            reverse('app:howManyPoints'),
            {'scoringAction': 'td'}, )

        answer = response.context.get('answer')

        assert answer == '6'

    def test_howManyPoints_extraKick_equals_1(self, client):
        response = client.get(
            reverse('app:howManyPoints'),
            {'scoringAction': 'ek'}, )

        answer = response.context.get('answer')

        assert answer == '1'

    def test_howManyPoints_extraConvertion_equals_6(self, client):
        response = client.get(
            reverse('app:howManyPoints'),
            {'scoringAction': 'ec'}, )

        answer = response.context.get('answer')

        assert answer == '2'

    def test_howManyPoints_fieldGoal_equals_1(self, client):
        response = client.get(
            reverse('app:howManyPoints'),
            {'scoringAction': 'fg'}, )

        answer = response.context.get('answer')

        assert answer == '3'

    def test_howManyPoints_touchDown_equals_6(self, client):
        response = client.get(
            reverse('app:howManyPoints'),
            {'scoringAction': 'sa'}, )

        answer = response.context.get('answer')

        assert answer == '2'


# Create your tests here.
