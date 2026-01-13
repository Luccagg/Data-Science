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


def interquartile_range(x):
	return quantile(x, 0.75) - quantile(x, 0.25)


def covariance(x, y):
	n = len(x)
	return linear_algebra.dot_product(de_mean(x), de_mean(y))/(n-1)


def correlaton(x, y):
	stdev_x = standard_deviation(x)
	stdev_y = standard_deviation(y)
	if stdev_x > 0 and stdev_y > 0:
		return covariance(x,y) / stdev_x / stdev_y
	else:
		return 0


if __name__ == '__main__':
	num_friends = [1, 2, 3, 4, 5, 5]
	daily_minutes = [3, 4, 5, 6, 10, 9]
	print(mode(num_friends))
	print(variance(num_friends))
	print(standard_deviation(num_friends))
	print(interquartile_range(num_friends))
	print(covariance(num_friends, daily_minutes))
	print(correlaton(num_friends, daily_minutes))
