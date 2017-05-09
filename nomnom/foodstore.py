"""This file contains the food store representation
"""
import settings
import operator


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
        """Returns the corresponding vector representation
        of a food string

        :param food_string: string representing the food
        document
        """
        food_list = food_string.strip().split()
        vector = 0b0
        shift = self.word_space_length-1
        for element in self.word_space:
            if element in food_list:
                vector += 0b1 << shift
            shift -= 1
        return vector

    def store(self, food_list):
        """Stores the food in the food store

        :param food_list: list of string objects containing
        the food to be added
        """
        for food in food_list:
            # check if food is string
            if isinstance(food, basestring):
                # add food to food store
                food_vector = self.get_food_vector(food)
                if food_vector not in self.food_store.keys():
                    self.food_store[food_vector] = []
                if food not in self.food_store[food_vector]:
                    self.food_store[food_vector].append(food)

    def retrieve_food_list_by_string(self, food_string):
        """Returns the list of food corresponding to a food string

        :param food_string: food string document
        :return: list of food corresponding to the food string
        """
        index = self.get_food_vector(food_string)
        return self.retrieve_food_list_by_index(index)

    def retrieve_food_list_by_index(self, index):
        """Returns the list of food corresponding to a binary vector index

        :param index: int corresponding to the binary representation
        of the food
        :return food_list: list of food with the given index, returns
        None if the index is not present in the food store
        """
        food_list = None
        if index in self.food_store.keys():
            food_list = self.food_store[index]
        return food_list

    def retrieve_food_store(self):
        """Retrieves the list of food

        :return food_store: dictionary containing the food documents
        indexed by their binary representation as an integer
        """
        return self.food_store

    def reset(self):
        """Resets the food store to an empty dictionary
        """
        self.food_store = {}

    def scalar_product(self, vector_a, vector_b):
        """Returns the scalar product

        :param vector_a: integer representing the first index
        :param vector_b: integer representing the second index

        :return result: scalar product of the parameters
        Note: This method can be considered static but we
        will keep it this way in case we might change the scalar
        product by a measure that depends on the food store
        """
        # calculate the bitwise product of the binary representations
        and_vector = operator.and_(vector_a, vector_b)
        # the score is equal to the number of '1' in the binary
        # representation of the and_vector
        result = bin(and_vector).count('1')
        return result

    def handle_query(self, query_string):
        """Returns the document with the highest scalar product

        :param query_string: string corresponding to the query

        :return highest_score: highest scalar product
        :return highest_scoring_index: vector representation of the document
        :return highest_scoring_document : list of string documents with the
        highest scalar product
        """
        # initialize score and results
        highest_score = 0
        highest_scoring_index = None
        highest_scoring_document = None
        query_vector = self.get_food_vector(query_string)
        for food_vector in self.food_store.keys():
            new_score = self.scalar_product(food_vector, query_vector)
            # update the food document if the score is higher
            if new_score >= highest_score:
                highest_score = new_score
                highest_scoring_index = food_vector
                highest_scoring_document = self.food_store[food_vector]
        return highest_score, highest_scoring_index, highest_scoring_document


