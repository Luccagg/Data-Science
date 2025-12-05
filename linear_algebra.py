import math
# Math of vectors

def vector_add(v, w):
	return [i + j for i, j in zip(v, w)]

def vector_subtract(v, w):
	return [i - j for i, j in zip(v, w)]

def vector_summation(vectors):
	# receive an array of vectors and add one by one
	result = vectors[0]
	for vector in vectors[1:]:
		result = vector_add(result, vector)
	return result

def scalar_multiplication(k, v):
	# k is a real number and v is a vector
	return [k*i for i in v]

def vector_mean(vectors):
	return scalar_multiplication(1/len(vectors), vector_summation(vectors))

def dot_product(v, w):
	# v_1 * w_1 + ... + v_n * w_n
	return sum(i*j for i, j in zip(v, w))

def sum_of_squares(v):
	return dot_product(v, v)

def magnitude(v):
	return math.sqrt(sum_of_squares(v))

def squared_distance(v, w):
	return sum_of_squares(vector_subtract(v, w))

def distance(v, w):
	return magnitude(vector_subtract(v, w))


if __name__ == '__main__':
	# canonical vectors for R^2 to test the implementations
	v = [1, 0] 
	w = [0, 1]
	# just to test
	print(vector_add(v, w))
	print(vector_subtract(v, w))
	print(vector_summation([v, w]))
	print(scalar_multiplication(2, v))
	print(vector_mean([v, w]))
	print(dot_product(v, w))
	print(sum_of_squares(v))
	print(magnitude(v))
	print(squared_distance(v, w))
	print(distance(v, w))