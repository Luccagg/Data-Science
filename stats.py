from __future__ import division
from collections import Counter
import linear_algebra
import math


def mean(x):
	return sum(x)/len(x)

def median(v):
	n = len(v)
	sorted_v = sorted(v)
	midpoint = n//2

	if n % 2 == 1:
		return sorted_v[midpoint]
	else:
		lo = midpoint-1
		hi = midpoint
		return (sorted_v[lo] + sorted_v[hi])

def quantile(x, p):
	p_index = int(p*len(x))
	return sorted(x)[p_index]

def mode(x):
	counts = Counter(x)
	max_count = max(counts.values())
	return [x_i for x_i, count in counts.items()
				if count == max_count]


# Dispersion #

def data_range(x):
	return max(x) - min(x)


def de_mean(x):
	x_bar = mean(x)
	return [x_i - x_bar for x_i in x]


def variance(x):
	n = len(x)
	deviations = de_mean(x)
	return linear_algebra.sum_of_squares(deviations)/(n-1)


def standard_deviation(x):
	return math.sqrt(variance(x))



if __name__ == '__main__':
	num_friends = [1, 2, 3, 4, 5, 5]
	print(mode(num_friends))
	print(variance(num_friends))
	print(standard_deviation(num_friends))

