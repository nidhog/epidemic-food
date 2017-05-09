"""This file contains the food store representation
"""
import settings


class FoodStore(object):
    """FoodStore class
    Manages Adding and retrieving elements from the food store
    Note: This is the basic case for stage 1
    """
    def __init__(self, food_store={}, word_space=settings.default_word_space):
        """Initializes the instance of the FoodStore class

        :param food_store: (optional) initial dictionary of foods
        in the store, keys are the binary vector representations and
        items are the string objects representing the food
        :param word_space: (optional) word space as a list of
        string objects, if no entry is given the list is
        initialized by the default settings
        """
        if (isinstance(food_store, dict)) and (isinstance(word_space, list)):
            self.food_store = food_store
            self.word_space = word_space
            self.word_space_length = len(self.word_space)
        else:
            raise TypeError

    def __str__(self):
        """Computes a string representation of the FoodStore

        :return s: string representation
        """
        s = "[>] Store Content\n"
        s += "-"*40+"\n"
        for food_vector in self.food_store.keys():
            s += "\t"+str(food_vector)+'- '+('{0:0'+str(self.word_space_length)+'b}').format(food_vector)+":\n"
            for food in self.food_store[food_vector]:
                s += "\t\t"+str(food)+"\n"
        s += "-"*40+"\n"
        return s

    def get_food_vector(self, food_string):
        pass

    def store(self, food_list):
        pass

    def retrieve_food_list_by_string(self, food_string):
        pass

    def retrieve_food_list_by_index(self, index):
        pass

    def retrieve_food_store(self):
        pass

    def reset(self):
        """Resets the food store to an empty dictionary
        """
        self.food_store = {}

    def scalar_product(self, vector_a, vector_b):
        pass

    def handle_query(self, query_string):
        pass


