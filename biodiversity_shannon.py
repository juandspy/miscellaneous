# This programme calculates Shannon index (biodiversity) of any enviroment.
# Necessary inputs are name of taxons/species and number of individuals.

# Importing necessary modules:

import random            as rd
import numpy             as np
import math
import matplotlib.pyplot as plt

# Input example:

taxons = ['cats', 'sogs', 'rats']
individuals = [80, 2, 4]
number_of_elements = [6, 60, 80]
#number_of_elements = np.linspace(20, 160, 20, dtype = 'int')
max_number_of_takes = 1000

# --------- Necessary functions (can skip) ------------

def how_many(lista, protagonist):
	# -- Arguments --
	# lista:       list of items where we want to count how many times does protagonist appears
	# protagonist: can be a number or a string

	# -- Output --
	# Returns the number of times that protagonist appears in the list

	reps = 0

	for element in lista:
		if element == protagonist:
			reps += 1
	return reps


def biodiversity(samples, taxons, number_of_elements):
	# This function returns the number of different individuals from /sample/ when taking random /number_of_elements/ individuals
	# --Arguments --
	# samples:            list of individuals
	# taxons:            
	# number_of_elements: number of elements that the function takes from the list of samples

	chosen_Data = np.random.choice(samples, number_of_elements)

	random_community = [] # List where to classificate elements from chosen_Data into different samples columns

	for counter, value in enumerate(taxons):
		random_community.append(how_many(chosen_Data, value))

	return random_community

# --------------- Main function ------------------

def shannon(taxons, individuals, number_of_elements, max_number_of_takes):
	# -- Arguments --
	# taxons:             list with taxons names in string.
	# individuals:        list of number of animals corresponding to each taxon
	# number_of_elements: list of how many elements will the programme take to calculate shannon index

	# -- Output --output
	# shannons:           list of each shannon index corresponding to each number_of_elements

	poblation             = sum(individuals)
	number_of_taxons      = len(taxons)

	samples = []

	ancho = max(number_of_elements)/2/len(number_of_elements) #plotplot

	for counter, value in enumerate(taxons):
		for i in range(individuals[counter]):
			samples.append(value)

	rd.shuffle(samples)

	# Now /samples/ is a list that contains each individual in a random position. We will add in a table the percentage and
	#  Shannon index for each number_of_elements

	for counter, value in enumerate(number_of_elements):
		
		#groups_of_shannons = np.empty(len(number_of_elements))

		probability   = []

		print('For %d random elements: ' %(value))

		number_of_takes = 0  # We'll use max_number_of_takes to calculate the index

		tuples = np.empty((max_number_of_takes,), dtype = object) # This empty list will contain tuples of random_communities. They'll be tuples in order to use np.unique to obtain number of different random_communities		
		
		while number_of_takes < max_number_of_takes:
			
			random_community = biodiversity(samples, taxons, value)

			tuples[number_of_takes] = tuple(random_community)

			number_of_takes += 1

		different_random_communities = np.unique(tuples, return_counts = True)  # different tuples witch its frecuency

		number_of_different_random_communities = len(different_random_communities[0])

		shannons = []
		adjust = 0
		for i in range(number_of_different_random_communities):
			probabilities = []
			probability_of_having_this_random_community = different_random_communities[1][i]/len(tuples)
			for j in range(number_of_taxons):
				probabilities.append(different_random_communities[0][i][j]/ poblation)

			probability.append(probabilities)

			# Each element in  percentages correspond to the probability of having that community
			# In order to calculate the Shannon index we'll use H = -\Sum pi*Log pi

			sumatory = 0
			for prob in probabilities:
				if prob != 0:
					sumatory += prob*math.log(prob)

			H = - sumatory
			print(H)
			shannons.append(H)

			plt.bar(x = value, bottom = adjust, height = probability_of_having_this_random_community, width = ancho)
			adjust += probability_of_having_this_random_community
		plt.legend(shannons)
		plt.xlabel('Number of elements')
		plt.ylabel('Probabilities')
		print('----------------------')
	return shannons
		
shannon(taxons, individuals, number_of_elements, max_number_of_takes)

plt.show()