"""Test settings can be defined here
"""
test_nomnom_settings = {
                        # example food list to initialize the food store
                        'food_init_dict': {0:  'banana',
                                           1: 'chocolate'},
                        # food list to be stored
                        'food_list':      ['banana', 'chocolate cake', 'hot chocolate', 'chocolate milk'],
                        'food_list_outlier':      ['banana', 'chocolate cake', 'hot chocolate', 'chocolate milk', 12],
                        # the space of words considered in the tests
                        'word_space':     ['hot', 'cold', 'chocolate', 'milk', 'cake', 'banana', 'orange'],
                        # maps binary representation and corresponding food
                        'food_vector_map':{0b10:'banana',
                                           0b110:'banana cake',
                                           0b110:'cake banana',
                                           0b110:'banana cream cake',
                                           0b1010000:'hot chocolate'},
                        # food with words that are not in the word space
                        'food_not_in_word_space': ['vanilla cupcake', 'apple juice', 'coconut oil'],
                        # expected food store result
                        'food_list_store': {0b10:       ['banana'],
                                            0b10100:    ['chocolate cake'],
                                            0b1010000:  ['hot chocolate'],
                                            0b11000:    ['chocolate milk']},
                        # food documents that have a similar index
                        'similar_foods': ['milk chocolate', 'chocolate milk', 'milk chocolate drink'],
                        # maps two numbers and their expected resulting product
                        'scalar_product_results': {(0, 0b1111): 0,
                                                (0b1001, 0b0110): 0,
                                                (0b1010, 0b0101): 0,
                                                (0b1001, 0b1000): 1,
                                                (0b1111, 0b1111): 4},
                        # maps queries and expected results
                        'query_results': {'hot chocolate': (2, 0b1010000, ['hot chocolate']),
                                          'chocolate hot': (2, 0b1010000, ['hot chocolate']),
                                          'banana smoothie': (1, 0b10, ['banana']),
                                          'banana cake': (1, 0b10100, ['chocolate cake'])},
                        # result of querying an empty food store
                        'empty_query_result': (0, None, None)
                        }
