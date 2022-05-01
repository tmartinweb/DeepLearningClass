import numpy as np
import os

output_filename = 'np_output.npy'


class NumpyExample:

    def __init__(self):
        self.run_example()

    def __str__(self):
        print(self)

    def run_example(self):
        # Using Numpy, create a random vector of size 15 having only Integers in the range 1-20
        # & reshape the array to 3 by 5
        my_array = np.array(np.random.randint(1, 20, 15)).reshape((3, 5))

        # Print array shape
        print(my_array.shape)

        # Replace the max in each row by 0 (using where/max)
        row_maxes = my_array.max(axis=1).reshape(-1, 1)
        max_to_zero_array = np.where(my_array == row_maxes, 0, my_array)

        try:
            if os.path.isfile(output_filename):
                os.remove(output_filename)

            with open(output_filename, 'a') as file:
                # I decided to output the 3 by 5, before and after turning the max(es) into 0
                # Also, this method changes ALL max values in each row, even duplicates, into a 0
                file.write('Original pseudorandom 3 by 5 array: \n' + str(my_array) + '\n\n')
                file.write('Array after max ~> 0: \n' + str(max_to_zero_array) + '\n\n')
                # Extract diagonal from the array, and save as .npy file format
                file.write('Diagonal of array from (0,0): ' + str(np.diagonal(max_to_zero_array)) + '\n\n')

        except IOError as e:
            print("Error outputting to file: " + e + '\n')
