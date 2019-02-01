from unittest import TestCase
from besttravel import BestTravel, InvalidInput, check_distance


class BestTravelTest(TestCase):
	def setUp(self):
		self.besttravel = BestTravel()

	# def test_when_distance_limit_negative_raise_InvalidInput(self):
	# 	with self.assertRaises(InvalidInput):
	# 		self.besttravel.choose_best_sum(-1, 2, (3,4,5))

	# def test_when_distance_limit_invalid_raise_InvalidInput(self):
	# 	with self.assertRaises(InvalidInput):
	# 		self.besttravel.choose_best_sum('A', 2, (3,4,5))

	# def test_when_town_number_0_raise_InvalidInput(self):
	# 	with self.assertRaises(InvalidInput):
	# 		self.besttravel.choose_best_sum(6, 0, (3,4,5))

	# def test_when_town_number_invalid_raise_InvalidInput(self):
	# 	with self.assertRaises(InvalidInput):
	# 		self.besttravel.choose_best_sum(6, None, (3,4,5))


	# def test_when_list_of_distances_invalid_raise_InvalidInput(self):
	# 	with self.assertRaises(InvalidInput):
	# 		self.besttravel.choose_best_sum(6, 2, 'A')

	# def test_when_list_of_distances_empty_raise_InvalidInput(self):
	# 	with self.assertRaises(InvalidInput):
	# 		self.besttravel.choose_best_sum(6, 2, ())

	# def test_when_list_of_distances_less_than_tn_raise_InvalidInput(self):
	# 	with self.assertRaises(InvalidInput):
	# 		self.besttravel.choose_best_sum(6, 2, (3))

	# def test_when_1_town_return_Max(self):
	# 	tested_data = [(25, 1, [5], 5), (25, 1, [6], 6), (25, 1, [6, 20], 20), (25, 1, [6, 20, 26], 20)]
	# 	for (distance_limit, number_of_towns, list_of_distances, expected) in tested_data:
	# 		print('dl {} nt {} lod {} expected {}'.format(distance_limit, number_of_towns, list_of_distances, expected))
	# 		result = self.besttravel.choose_best_sum(distance_limit, number_of_towns, list_of_distances)
	# 		self.assertEqual(result, expected)

	# def test_when_2_towns_return_Max(self):
	# 	tested_data = [(25, 2, [5, 15], 20), (25, 2, [5, 15, 16], 21), (25, 2, [16, 5, 15], 21), (25, 2, [20, 2, 9], 22), (25, 2, [20, 2, 9, 8, 25], 22)]
	# 	for (distance_limit, number_of_towns, list_of_distances, expected) in tested_data:
	# 		print('dl {} nt {} lod {} expected {}'.format(distance_limit, number_of_towns, list_of_distances, expected))
	# 		result = self.besttravel.choose_best_sum(distance_limit, number_of_towns, list_of_distances)
	# 		self.assertEqual(result, expected)

	def test_3_towns(self):
		tested_data = [
			# (163, 3, [50, 55, 56, 57, 58], 163), 
			# (50, 3, [2, 3, 4, 5, 6, 7, 8, 9, 10], 27), 
			(50, 3, [5, 15, 16, 4, 10, 51, 40, 19], 50),
			(50, 5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 53, 46, 35, 4, 8, ], 50)

			]
		for (distance_limit, number_of_towns, list_of_distances, expected) in tested_data:
			print('dl {} nt {} lod {} expected {}'.format(distance_limit, number_of_towns, list_of_distances, expected))
			result = self.besttravel.choose_best_sum(distance_limit, number_of_towns, list_of_distances)
			self.assertEqual(result, expected)


class CheckDistanceTest(TestCase):
	def test_when_distance_invalid_raise_InvalidInput(self):
		with self.assertRaises(InvalidInput):
			check_distance('A')

	def test_when_distance_negative_raise_InvalidInput(self):
		with self.assertRaises(InvalidInput):
			check_distance(-1)			