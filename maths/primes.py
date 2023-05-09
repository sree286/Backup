from math import log,ceil
def get_primes(limit):
	nums = [True]*(limit+1)
	nums[0] = nums[1] = False
	for i,is_prime in enumerate(nums):
		if is_prime:
			yield i
			for q in range(i*i,limit+1,i):
				nums[q] = False
def upper_bound(n):
	if n<6:
		return 100
	return ceil(n*(log(n)+log(log(n))))
def get_n_primes(n):
	primes = list(get_primes(upper_bound(n)))
	return primes
def get_factors(num):
	primes = get_n_primes(num/2)
	for k in primes:
		if num%k==0:
			yield k
def max_factor(num):
	factors = list(get_factors(num))
	return max(factors)
print(max_factor(10**7))