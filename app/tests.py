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


class TestLastThreeView:
    def test_without_num_doesnt_set_answer(self, client):
        response = client.get(reverse('app:lastThree'))

        answer = response.context.get('answer')

        assert answer is None

    def test_lastThree_str_of_1_2_3_4_should_list_4_3_2(self, client):
        response = client.get(
            reverse('app:lastThree'),
            {'l1': '1 2 3 4'}, )

        answer = response.context.get('answer')

        assert answer == [2, 3, 4]

    def test_lastThree_str_of_12_34_1_65_should_list_65_1_34(self, client):
        response = client.get(
            reverse('app:lastThree'),
            {'l1': '12 34 1 65'}, )

        answer = response.context.get('answer')

        assert answer == [34, 1, 65]


class TestSumofListView:
    def test_without_num_doesnt_set_answer(self, client):
        response = client.get(reverse('app:sumofList'))

        answer = response.context.get('answer')

        assert answer is None

    def test_sumofList_str_of_1_2_3_4_equals_10(self, client):
        response = client.get(
            reverse('app:sumofList'),
            {'l': '1 2 3 4'}, )

        answer = response.context.get('answer')

        assert answer == 10

    def test_sumofList_str_of_22_44_10_equals_76(self, client):
        response = client.get(
            reverse('app:sumofList'),
            {'l': '22 44 10'}, )

        answer = response.context.get('answer')

        assert answer == 76


class TestSumofLongerView:
    def test_without_num_doesnt_set_answer(self, client):
        response = client.get(reverse('app:sumofLonger'))

        answer = response.context.get('answer')

        assert answer is None

    def test_sumofLonger_str_of_1_2_3_4_and_str_of_23_2_equals_10(
            self, client):
        response = client.get(
            reverse('app:sumofLonger'),
            {'L1': '1 2 3 4',
             'L2': '23 2'}, )

        answer = response.context.get('answer')

        assert answer == 10

    def test_sumofLonger_str_of_1_2__and_str_of_23_2_equals_28(self, client):
        response = client.get(
            reverse('app:sumofLonger'),
            {'L1': '1 2',
             'L2': '23 2'}, )

        answer = response.context.get('answer')

        assert answer == 28

    def test_sumofLonger_str_of_1_2__and_str_of_23_2_34_1_equals_60(
            self, client):
        response = client.get(
            reverse('app:sumofLonger'),
            {'L1': '1 2',
             'L2': '23 2 34 1'}, )

        answer = response.context.get('answer')

        assert answer == 60


class TestDifferenceFromMinimumview:
    def test_without_num_doesnt_set_answer(self, client):
        response = client.get(reverse('app:diffFromMin'))

        answer = response.context.get('answer')

        assert answer is None

    def test_diffFromMin_str_of_1_2_3_4_and_equals_0_1_2_3(self, client):
        response = client.get(
            reverse('app:diffFromMin'),
            {'l': '1 2 3 4'}, )

        answer = response.context.get('answer')

        assert answer == [0, 1, 2, 3]

    def test_diffFromMin_str_of_neg67_222_3_4_and_equals_0_155_neg64_neg63(
            self, client):
        response = client.get(
            reverse('app:diffFromMin'),
            {'l': '-67 222 3 4'}, )

        answer = response.context.get('answer')

        assert answer == [0, 289, 70, 71]


class TestHashTagsView:
    def test_without_str_doesnt_set_answer(self, client):
        response = client.get(reverse('app:hashTags'))

        answer = response.context.get('answer')

        assert answer is None

    def test_hashTags_strList_of_hashtag_Hello_and_just_world(self, client):
        response = client.get(
            reverse('app:hashTags'),
            {'Tweet': '#hello world'}, )

        answer = response.context.get('answer')

        assert answer == ['#hello']

    def test_hashTags_strList_of_hashtag_Hello_and_just_world_of_hashtagPython(
            self, client):
        response = client.get(
            reverse('app:hashTags'),
            {'Tweet': '#hello world of #python'}, )

        answer = response.context.get('answer')

        assert answer == ['#hello', '#python']


class TestMentionsView:
    def test_without_str_doesnt_set_answer(self, client):
        response = client.get(reverse('app:mentions'))

        answer = response.context.get('answer')

        assert answer is None

    def test_mentions_strList_of_mentions_Hello_and_just_world(self, client):
        response = client.get(
            reverse('app:mentions'),
            {'Mentions': '#hello world'}, )

        answer = response.context.get('answer')

        assert answer == []

    def test_Mentions_strList_of_mention_Hello_and_just_world_of_hashtagPython(
            self, client):
        response = client.get(
            reverse('app:mentions'),
            {'Mentions': '@hello world of #python'}, )

        answer = response.context.get('answer')

        assert answer == ['@hello']


class TestParseInventoryStringView:
    def test_without_str_doesnt_set_answer(self, client):
        response = client.get(reverse('app:parseInventoryString'))

        answer = response.context.get('answer')

        assert answer is None

    def test_Inventory_strList_of_pizza_7_9(self, client):
        response = client.get(
            reverse('app:parseInventoryString'),
            {'Inventory': 'pizza 7 9'}, )

        answer = response.context.get('answer')

        assert answer == ['pizza', 7, 9]

    def test_Inventory_strList_of_burrito_5_7(self, client):
        response = client.get(
            reverse('app:parseInventoryString'),
            {'Inventory': 'burrito 5 7'}, )

        answer = response.context.get('answer')

        assert answer == ['burrito', 5, 7]


class TestIsDollarStoreView:
    def test_without_str_doesnt_set_answer(self, client):
        response = client.get(reverse('app:isDollarStore'))

        answer = response.context.get('answer')

        assert answer is None

    def test_isDollarStore_for_chips_129_quantity_1_should_false(self, client):
        response = client.get(
            reverse('app:isDollarStore'),
            {'L1': 'chips,1.29,1'}, )

        answer = response.context.get('answer')

        assert answer == False

    def test_isDollarStore_for_chips_dollar_quantity_1_should_false(
            self, client):
        response = client.get(
            reverse('app:isDollarStore'),
            {'L1': 'chips,1.00,1'}, )

        answer = response.context.get('answer')

        assert answer == True


# Create your tests here.
