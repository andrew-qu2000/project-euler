# 10001st prime
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13.
# What is the 10001st prime number?

_primes = [2]

def nth_prime(n): # one-indexed
  while len(_primes) < n:
      # start looking past the latest prime
      num = _primes[-1] + 1
      p_ind = 0
      while p_ind < len(_primes):
          # don't have to consider large primes as possible factors
          # ex: if we already know 2 isn't a factor, then any prime
          # greater than num / 2 isn't a factor
          if _primes[p_ind] > (num / _primes[p_ind]):
              break
          # if a previous prime is a factor, num is not a prime
          # increment num and restart search
          elif num % _primes[p_ind] == 0:
              num += 1
              p_ind = 0
          # move onto next prime for check
          else:
              p_ind += 1
      # none of the previous primes were factors, so this is a new prime
      _primes.append(num)
  return _primes[-1]

if __name__ == '__main__':
    print(nth_prime(10001))
