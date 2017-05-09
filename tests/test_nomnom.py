"""This file contains the basic tests for the nomnom module
"""
import unittest
from test_settings import test_nomnom_settings as settings
# adding nomnom path to PYTHONPATH
import sys, os
nomnom_path = os.path.dirname(os.getcwd())
sys.path.append(nomnom_path)
from nomnom import foodstore


class BasicTest(unittest.TestCase):
    def test_instantiation(self):
        fs = foodstore.FoodStore()

    def test_instantiation_wrong(self):
        with self.assertRaises(TypeError):
            fs = foodstore.FoodStore([])

    def test_reset(self):
        fs = foodstore.FoodStore(settings['food_init_dict'])
        fs.reset()
        self.assertEqual(fs.food_store, {})

    def test_get_food_vector(self):
        """The transformation into a binary vector works properly
        """
        fs = foodstore.FoodStore(word_space=settings['word_space'])
        fs.reset()
        for food_vector, food_string in settings['food_vector_map'].iteritems():
            self.assertEqual(fs.get_food_vector(food_string), food_vector)

    def test_store(self):
        fs = foodstore.FoodStore(word_space=settings['word_space'])
        fs.reset()
        fs.store(settings['food_list'])
        self.assertEqual(fs.food_store, settings['food_list_store'])

    def test_storage_outlier(self):
        """Elements of the provided food list that are not
        string objects are skipped
        """
        fs = foodstore.FoodStore(word_space=settings['word_space'])
        fs.reset()
        fs.store(settings['food_list_outlier'])
        self.assertEqual(fs.food_store, settings['food_list_store'])

    def test_retrieve(self):
        """Retrieving the food store is working properly
        """
        fs = foodstore.FoodStore(word_space=settings['word_space'])
        fs.reset()
        fs.store(settings['food_list'])
        self.assertEqual(fs.retrieve_food_store(), settings['food_list_store'])

    def test_retrieve_by_index(self):
        """Retrieving a food list by index is working properly
        """
        fs = foodstore.FoodStore(word_space=settings['word_space'])
        fs.reset()
        fs.store(settings['food_list'])
        for index in settings['food_list_store']:
            self.assertEqual(fs.retrieve_food_list_by_index(index), settings['food_list_store'][index])

    def test_storage_not_in_word_space(self):
        """Food that is not in the word space is indexed by 0
        """
        fs = foodstore.FoodStore(word_space=settings['word_space'])
        fs.reset()
        fs.store(settings['food_not_in_word_space'])
        self.assertEqual(fs.retrieve_food_list_by_index(0), settings['food_not_in_word_space'])

    def test_storage_same_food(self):
        """Storing the same food keeps the same
        previous food store
        """
        fs = foodstore.FoodStore(word_space=settings['word_space'])
        fs.reset()
        fs.store(settings['food_list'])
        # store previously stored food documents
        fs.store(settings['food_list'][2:])
        print fs
        self.assertEqual(fs.retrieve_food_store(), settings['food_list_store'])

    def test_storage_same_binary_vector_similar(self):
        """Storing the two types of food that have the
        same binary vector stores both of them in a list
        indexed by the same binary vector representation
        """
        fs = foodstore.FoodStore(word_space=settings['word_space'])
        fs.reset()
        fs.store(settings['similar_foods'])
        self.assertEqual(fs.retrieve_food_list_by_string(settings['similar_foods'][0]),
                         fs.retrieve_food_list_by_string(settings['similar_foods'][1]))

    def test_storage_same_binary_vector_dissimilar(self):
        """Storing the two types of food where one has
        one more word that is not present in the word
        space is considered the same as storing similar
        food documents
        """
        fs = foodstore.FoodStore(word_space=settings['word_space'])
        fs.reset()
        fs.store(settings['similar_foods'])
        self.assertEqual(fs.retrieve_food_list_by_string(settings['similar_foods'][0]),
                         fs.retrieve_food_list_by_string(settings['similar_foods'][2]))

    def test_scalar_product(self):
        """Calculating the scalar product works properly
        """
        fs = foodstore.FoodStore(word_space=settings['word_space'])
        fs.reset()
        for vectors, result in settings['scalar_product_results'].iteritems():
            self.assertEqual(fs.scalar_product(vectors[0], vectors[1]), result)

    def test_handle_query(self):
        """Queries return the expected results
        """
        fs = foodstore.FoodStore(word_space=settings['word_space'])
        fs.reset()
        fs.store(settings['food_list'])
        for query, result in settings['query_results'].iteritems():
            self.assertEqual(fs.handle_query(query), result)

    def test_handle_query_empty_food_store(self):
        """Queries work properly if the food store is empty
        """
        fs = foodstore.FoodStore(word_space=settings['word_space'])
        fs.reset()
        for query in settings['query_results'].keys():
            self.assertEqual(fs.handle_query(query), settings['empty_query_result'])


if __name__ == '__main__':
    unittest.main()


