# -*- coding: latin-1 -*-

r"""
Module fibonacci.py (February 29, 2016)

Several implementation of Fibonacci numbers computation.

Fibonacci numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377...

.. math::
  F_0 = 0

  F_1 = 1

  F_{n+2} = F_{n+1} + F_n   \qquad\forall n\ integer

https://oeis.org/A000045

Lucas numbers: 2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, 199, 322, 521, 843...

.. math::
  L_0 = 2

  L_1 = 1

  L_{n+2} = L_{n+1} + L_n   \qquad\forall n\ integer

https://oeis.org/A000032

See

* **Mathematical** relations:
  *Fibonacci numbers - several relations to implement good algorithms*
  https://bitbucket.org/OPiMedia/severalgos/src/master/Fibonacci/math/Fibonacci.pdf

* Complete **C++ and Python sources** on **Bitbucket**
  https://bitbucket.org/OPiMedia/severalgos/src/master/Fibonacci/

* The **C++ HTML online documentation**
  http://www.opimedia.be/DS/online-documentations/severalgos/Fibonacci-cpp/html/


Complexity informations in each function
considers that operations on large numbers
are in constant time and constant space (which is obviously false). ::

| Implementations              | Time O(n)     | Space O(n)
| -----------------------------+---------------+-----------
| fibonacci_pair               | lg(n) + cache | 1 + chache
| fibonacci_pair__iter_lg      | lg(n)         | 1
| fibonacci_pair__rec_lg       | lg(n)         | lg(n)
| fibonacci__iter_lg_optimized | lg(n)         | 1
| fibonacci__iter_lg           | lg(n)         | 1
| fibonacci__iter_n            | n             | 1
| fibonacci__rec_memoized_n    | n + cache     | n + cache
| fibonacci_pair__rec_n        | n             | n
| fibonacci__rec_exp           | 2^n           | n
| -----------------------------+---------------+-----------
| fibonacci_pair_with          | lg(n/k)       | 1
|                              | 1             |
|                              | lg(n)         |
| -----------------------------+---------------+-----------
| fibonacci_pow2               | n             | 1
| fibonacci_pow2_pair          | n             | 1

Benchmark from C++ implementations of this functions:
|benchmark|

.. |benchmark| image:: _static/benchmark_Debian_gcc4_7_2_64bits.svg

Piece of severalgos.
https://bitbucket.org/OPiMedia/severalgos

GPLv3 --- Copyright (C) 2015, 2016 Olivier Pirson
http://www.opimedia.be/
"""


import collections
import sys


#
# Functions
############
def fibonacci(n):
    """
    Return :math:`F_n`.

    | Time O(n):  lg(n) + size of cache
    | Space O(n): 1 + size of cache

    :param n: int >= 0

    :return: int >= 0 (maybe long if Python 2)
    """
    return fibonacci_pair(n)[1]


def fibonacci_int(n):
    """
    Return :math:`F_n` forall n integer.

    :math:`F_{-n} = -(-1)^n F_n`

    | Time O(n):  lg(n)
    | Space O(n): 1

    :param n: n int

    :return n: int (maybe long if Python 2)
    """
    assert isinstance(n, int), type(n)

    return (fibonacci(n) if n >= 0
            else (fibonacci(-n) if -n & 1 != 0  # odd
                  else -fibonacci(-n)))


def fibonacci_int_generator(n=0):
    """
    Return a generator
    that yields :math:`F_n, F_{n+1}, F_{n+2},F_{n+3}, ...` for n integer.

    Initialization:
      | Time O(n):  lg(n)
      | Space O(n): 1

    Next:
      | Time O(n):  1
      | Space O(n): 1

    :param n: int

    :return: int (maybe long if Python 2)
    """
    assert isinstance(n, int), type(n)

    f_n_1, f_n = fibonacci_int_pair(n)

    while True:
        yield f_n

        f_n_1, f_n = f_n, f_n + f_n_1


def fibonacci_int_pair(n):
    """
    Return :math:`(F_{n-1}, F_n)` forall n integer.

    | Time O(n):  lg(n)
    | Space O(n): 1

    :param n: int

    :return: (int, int) (maybe long if Python 2)
    """
    assert isinstance(n, int), type(n)

    if n >= 0:
        return fibonacci_pair(n)
    else:
        n = -n
        f_n, f_n_p1 = fibonacci_pair(n + 1)

        return ((f_n_p1, -f_n) if n & 1 == 0  # even
                else (-f_n_p1, f_n))


def fibonacci_pair(n):
    """
    Return :math:`(F_{n-1}, F_n)`.

    Same algorithm as `fibonacci_pair__rec_lg()` with memoization.

    | Time O(n):  lg(n) + size of cache
    | Space O(n): 1 + size of cache

    :warning: Side effects: set or move results to the top of cache.

    :param n: int >= 0

    :return: (int >= 0, int >= 0) (maybe long if Python 2)
    """
    f_n_1 = __fibonacci_memo_get(n - 1)
    f_n = __fibonacci_memo_get(n)

    if (f_n is None) or (f_n_1 is None):  # not already in cache
        if n != 0:
            f_k_1, f_k = fibonacci_pair(n >> 1)  # F_{k-1}, F_k with k = n/2
            sqr_f_k = f_k**2

            if n & 1 == 0:  # even
                new_f_n_1 = sqr_f_k + f_k_1**2
                new_f_n = ((f_k*f_k_1) << 1) + sqr_f_k
            else:           # odd
                new_f_n_1 = ((f_k*f_k_1) << 1) + sqr_f_k
                new_f_n = (f_k + f_k_1)**2 + sqr_f_k
        else:
            new_f_n_1 = 1
            new_f_n = 0

        if (f_n_1 is None) and ((n - 1) not in __fibonacci_memo):
            __fibonacci_memo_set(n - 1, new_f_n_1)

        if (f_n is None) and (n not in __fibonacci_memo):
            __fibonacci_memo_set(n, new_f_n)

        return (new_f_n_1, new_f_n)
    else:                                 # both in cache
        return (f_n_1, f_n)


def fibonacci_pair_with(k, f_k_1, f_k, n):
    """
    Return :math:`(F_{n-1}, F_n)`
    with help (if possible) of :math:`(F_{k-1}, F_k)`.

    Algorithm:
    Double k while < n, with relations:

    .. math::
      F_{2k-1} = F^2_k + F^2_{k-1}

      F_{2k}   = 2 F_k F_{k-1} + F^2_k

    Next, with relations:

    .. math::
      F_{n-1} = F_k F_{n-k} + F_{k-1} F_{n-k-1}

      F_n     = F_k F_{n-k+1} + F_{k-1} F_{n-k}

    | Time O(n): lg(n/k) if 0 < k < n,
    |            1       if k == n,
    |            lg(n)   if k > n or k = 0
    | Space O(n): 1

    :param k: int >= 0
    :param f_k_1: int >= 0 (or long if Python 2)
    :param f_k: int >= 0 (or long if Python 2)
    :param n: int >= 0

    :return: (int >= 0, int >= 0) (maybe long if Python 2)
    """
    assert isinstance(k, int), type(k)
    assert k >= 0, k

    assert isinstance(f_k_1, int) or isinstance(f_k_1, long), type(f_k_1)
    assert f_k_1 >= 0, f_k_1

    assert isinstance(f_k, int) or isinstance(f_k, long), type(f_k)
    assert f_k >= 0, f_k

    assert (f_k_1, f_k) == fibonacci_pair(k)

    assert isinstance(n, int), type(n)
    assert n >= 0, n

    if (k == 0) or (k > n):
        return fibonacci_pair(n)

    k <<= 1  # k <- k*2
    while k < n:
        sqr_f_k = f_k**2
        f_k = ((f_k*f_k_1) << 1) + sqr_f_k  # F_k
        f_k_1 = sqr_f_k + f_k_1**2          # F_{k-1}

        k <<= 1  # k <- k*2

    k >>= 1  # k <- k/2

    if k < n:
        i = n - k  # i = n - k >= 1
        if i == 1:
            return f_k, f_k + f_k_1
        else:
            f_i_1, f_i = fibonacci_pair(i)  # F_{n-k-1}, F_{n-k}

            return (f_k*f_i + f_k_1*f_i_1, f_k*(f_i + f_i_1) + f_k_1*f_i)

    return (f_k_1, f_k)


def fibonacci_pow2(n):
    """
    Return :math:`F_{2^n}`.

    | Time O(n):  n
    | Space O(n): 1

    :param n: int >= 0

    :return: int >= 0 (maybe long if Python 2)
    """
    return fibonacci_pow2_pair(n)[1]


def fibonacci_pow2_pair(n):
    """
    Return :math:`(F_{2^n - 1}, F_{2^n})`.

    Algorithm:
    Compute successively:

    .. math::
      F_0, F_1, F_3, F_7, F_15, F_31, F_63, ..., F_{2^n - 1}

      F_1, F_2, F_4, F_8, F_16, F_32, F_64, ..., F_{2^n}

    With relations:

    .. math::
      F_{2^{i+1} - 1} = F^2_{2^i} + F^2_{2^i - 1}

      F_{2^{i+1}}     = 2 F_{2^i} F_{2^i - 1} + F^2_{2^i}

    | Time O(n):  n
    | Space O(n): 1

    :param n: int >= 0

    :return: (int >= 0, int >= 0) (maybe long if Python 2)
    """
    assert isinstance(n, int), type(n)
    assert n >= 0, n

    f_2i_1 = 0  # F_{2^i - 1}
    f_2i = 1    # F_{2^i}

    for _ in range(n):
        sqr_f_2i = f_2i**2
        f_2i = ((f_2i*f_2i_1) << 1) + sqr_f_2i  # F_{2^{i+1}}
        f_2i_1 = sqr_f_2i + f_2i_1**2           # F_{2^{i+1} - 1}

    return (f_2i_1, f_2i)


def lucas_int(n):
    """
    Return :math:`L_n` forall n integer.

    | Time O(n):  lg(n)
    | Space O(n): 1

    :param n: n int

    :return n: int (maybe long if Python 2)
    """
    assert isinstance(n, int), type(n)

    f_n_1, f_n = fibonacci_int_pair(n)

    return (f_n_1 << 1) + f_n


def lucas_int_pair(n):
    """
    Return :math:`(L_{n-1}, L_n)` forall n integer.

    | Time O(n):  lg(n)
    | Space O(n): 1

    :param n: int

    :return: (int, int) (maybe long if Python 2)
    """
    assert isinstance(n, int), type(n)

    f_n_2, f_n_1 = fibonacci_int_pair(n - 1)

    return ((f_n_2 << 1) + f_n_1,
            f_n_1*3 + f_n_2)


#
# Other (worse) implementations
###############################
def fibonacci__iter_lg(n):
    """
    Return :math:`F_n`.

    Algorithm:
    Compute successively:

    .. math::
      F_0, F_1, F_3, F_7, F_15, F_31, F_63, ..., F_{2^{lg(n)+1} - 1}

      F_1, F_2, F_4, F_8, F_16, F_32, F_64, ..., F_{2^{lg(n)+1}}

    With relations:

    .. math::
      F_{2^{i+1} - 1} = F^2_{2^i} + F^2_{2^i - 1}

      F_{2^{i+1}}     = 2 F_{2^i} F_{2^i - 1} + F^2_{2^i}

    For each ith bit of n equal to 1, add the corresponding F_{2^i}
    with relations:

    .. math::
      F_{k + 2^i - 1} = F_k F_{2^i} + F_{k-1} F_{2^i - 1}

      F_{k + 2^i}     = F_k F_{2^i} + F_{k-1} F_{2^i} + F_k F_{2^i - 1}

    | Time O(n):  lg(n)
    | Space O(n): 1

    :param n: int >= 0

    :return: int >= 0 (maybe long if Python 2)
    """
    assert isinstance(n, int), type(n)
    assert n >= 0, n

    if n != 0:
        # k = 0
        f_k_1 = 1  # F_{k-1}
        f_k = 0    # F_k

        # i = 0
        f_2i_1 = 0  # F_{2^i - 1}
        f_2i = 1    # F_{2^i}

        while True:
            if n & 1 != 0:  # ith bit of initial n is 1
                t = f_k*f_2i
                f_k = t + f_k_1*f_2i + f_k*f_2i_1  # F_{k + 2^i}
                f_k_1 = t + f_k_1*f_2i_1           # F_{k + 2^i - 1}
                # k <- k + 2^i = k + 10...0

                if n == 1:  # inv: k = initial n
                    return f_k

            t = f_2i**2
            f_2i = ((f_2i*f_2i_1) << 1) + t  # F_{2^{i+1}}
            f_2i_1 = t + f_2i_1**2           # F_{2^{i+1} - 1}
            # ++i

            n >>= 1  # n <- n/2
    else:
        return 0


def fibonacci__iter_lg_optimized(n):
    """
    Return :math:`F_n`.

    Algorithm:
    Compute successively:

    .. math::
      F_0, F_1, F_3, F_7, F_15, F_31, F_63, ..., F_{2^{lg(n)+1} - 1}

      F_1, F_2, F_4, F_8, F_16, F_32, F_64, ..., F_{2^{lg(n)+1}}

    With relations:

    .. math::
      F_{2^{i+1} - 1} = F^2_{2^i} + F^2_{2^i - 1}

      F_{2^{i+1}}     = 2 F_{2^i} F_{2^i - 1} + F^2_{2^i}

    For each ith bit of n equal to 1, add the corresponding F_{2^i}
    with relations:

    .. math::
      F_{k + 2^i - 1} = F_k F_{2^i} + F_{k-1} F_{2^i - 1}

      F_{k + 2^i}     = F_k F_{2^i} + F_{k-1} F_{2^i} + F_k F_{2^i - 1}

    Process before the first consecutive bits equals to 0...0 or 1...1.

    | Time O(n):  lg(n)
    | Space O(n): 1

    :param n: int >= 0

    :return: int >= 0 (maybe long if Python 2)
    """
    assert isinstance(n, int), type(n)
    assert n >= 0, n

    # k = 0
    f_k_1 = 1  # F_{k-1}
    f_k = 0    # F_k

    # i = 0
    f_2i_1 = 0  # F_{2^i - 1}
    f_2i = 1    # F_{2^i}

    odd = bool(n & 1)  # n is odd, its first bit is 1

    # First consecutive bits equals to 0...0 or 1...1
    while (((n & 1) != 0) is odd) and (n != 0):  # same bit as first_bit
        t = f_2i**2
        f_2i = ((f_2i*f_2i_1) << 1) + t  # F_{2^{i+1}}
        f_2i_1 = t + f_2i_1**2           # F_{2^{i+1} - 1}
        # ++i

        n >>= 1  # n <- n/2

    if odd:       # (i + 1) first consecutive bits equals to 01...1
        f_k_1 = f_2i - f_2i_1  # F_{2^i - 2}
        f_k = f_2i_1           # F_{2^i - 1}
    elif n != 0:  # (i + 1) first consecutive bits equals to 10...0
        f_k_1 = f_2i_1  # F_{2^i - 1}
        f_k = f_2i      # F_{2^i}

    # Remaining bits
    n >>= 1  # n <- n/2
    while n != 0:
        t = f_2i**2
        f_2i = ((f_2i*f_2i_1) << 1) + t  # F_{2^{i+1}}
        f_2i_1 = t + f_2i_1**2           # F_{2^{i+1} - 1}
        # ++i

        if n & 1 != 0:  # ith bit of initial n is 1
            t = f_k*f_2i
            f_k = t + f_k_1*f_2i + f_k*f_2i_1  # F_{k + 2^i}
            f_k_1 = t + f_k_1*f_2i_1           # F_{k + 2^i - 1}
            # k <- k + 2^i = k + 10...0

        n >>= 1  # n <- n/2

    # inv: k = initial n

    return f_k


def fibonacci__iter_n(n):
    """
    Return :math:`F_n`.

    Algorithm:
    Simple iteration
    with usage of the recursive definition :math:`F_{n+2} = F_{n+1} + F_n`.

    | Time O(n):  n
    | Space O(n): 1

    :param n: int >= 0

    :return: int >= 0 (maybe long if Python 2)
    """
    assert isinstance(n, int), type(n)
    assert n >= 0, n

    f_k_1 = 1  # F_{k-1}
    f_k = 0    # F_k

    for n in range(n):
        f_k_1, f_k = f_k, f_k + f_k_1

    return f_k


def fibonacci__rec_exp(n):
    """
    Return :math:`F_n`.

    From a certain n, recursion fails.

    Algorithm:
    Simple usage of the recursive definition :math:`F_{n+2} = F_{n+1} + F_n`
    (twice calls on each step).

    | Time O(n):  2^n
    | Space O(n): n

    :param n: int >= 0

    :return: int >= 0 (maybe long if Python 2)
    """
    assert isinstance(n, int), type(n)
    assert n >= 0, n

    return (n if n <= 1
            else fibonacci__rec_exp(n - 1) + fibonacci__rec_exp(n - 2))


def fibonacci__rec_memoized_n(n):
    """
    Return :math:`F_n`.

    From a certain n, recursion fails.

    Algorithm:
    Simple usage of the recursive definition :math:`F_{n+2} = F_{n+1} + F_n`
    with memoization.

    | Time O(n):  n + size of cache
    | Space O(n): n + size of cache

    :warning: Side effects: set or move result to the top of cache.

    :param n: int >= 0

    :return: int >= 0 (maybe long if Python 2)
    """
    assert isinstance(n, int), type(n)
    assert n >= 0, n

    f_n = __fibonacci_memo_get(n)

    if f_n is None:  # not already in cache
        if n <= 1:
            f_n = n
        else:
            f_n = (fibonacci__rec_memoized_n(n - 1)
                   + fibonacci__rec_memoized_n(n - 2))

        __fibonacci_memo_set(n, f_n)

    return f_n


def fibonacci_memoization_reinit(max_size=1000):
    """
    Clear the cache used by `fibonacci__rec_memoized_n()`
    and set its maximum size to `max_size`.

    :param max_size: int >= 2
    """
    assert isinstance(max_size, int), type(max_size)
    assert max_size >= 2, max_size

    global __fibonacci_memo
    global __fibonacci_memo_max_size

    __fibonacci_memo = collections.OrderedDict()
    __fibonacci_memo_max_size = max_size


def fibonacci_pair__iter_lg(n):
    """
    Return :math:`(F_{n-1}, F_n)`.

    Algorithm:
    Iterate on each bit of n, with relations:

    .. math::
      F_{2n-1} = F^2_n + F^2_{n-1}

      F_{2n}   = 2 F_n F_{n-1} + F^2_n

      F_{2n+1} = (F_n + F_{n-1})^2 + F^2_n

    | Time O(n):  lg(n)
    | Space O(n): 1

    :param n: int >= 0

    :return: (int >= 0, int >= 0) (maybe long if Python 2)
    """
    assert isinstance(n, int), type(n)
    assert n >= 0, n

    f_k_1 = 1
    f_k = 0

    pow2 = 1 << n.bit_length()

    while pow2 > 1:
        sqr_f_k = f_k**2

        pow2 >>= 1
        if n & pow2 == 0:  # bit 0
            f_k = ((f_k*f_k_1) << 1) + sqr_f_k
            f_k_1 = sqr_f_k + f_k_1**2
            # k <- k*2
        else:              # bit 1
            t = f_k_1
            f_k_1 = ((f_k*t) << 1) + sqr_f_k
            f_k = (f_k + t)**2 + sqr_f_k
            # k <- k*2 + 1

    return (f_k_1, f_k)


def fibonacci_pair__rec_lg(n):
    """
    Return :math:`(F_{n-1}, F_n)`.

    Algorithm:
    Recursive call with relations:

    .. math::
      F_{2n-1} = F^2_n + F^2_{n-1}

      F_{2n}   = 2 F_n F_{n-1} + F^2_n

      F_{2n+1} = (F_n + F_{n-1})^2 + F^2_n

    | Time O(n):  lg(n)
    | Space O(n): lg(n)

    :param n: int >= 0

    :return: (int >= 0, int >= 0) (maybe long if Python 2)
    """
    assert isinstance(n, int), type(n)
    assert n >= 0, n

    if n != 0:
        f_k_1, f_k = fibonacci_pair__rec_lg(n >> 1)  # F_{k-1},F_k with k = n/2
        sqr_f_k = f_k**2

        return ((sqr_f_k + f_k_1**2,
                 ((f_k*f_k_1) << 1) + sqr_f_k) if n & 1 == 0  # even
                else (((f_k*f_k_1) << 1) + sqr_f_k,
                      (f_k + f_k_1)**2 + sqr_f_k))
    else:
        return (1, 0)


def fibonacci_pair__rec_n(n):
    """
    Return :math:`(F_{n-1}, F_n)`.

    From a certain n, recursion fails.

    Algorithm:
    Simple usage of the recursive definition :math:`F_{n+2} = F_{n+1} + F_n`
    (but only one call on each step).

    | Time O(n):  n
    | Space O(n): n

    :param n: int >= 0

    :return: (int >= 0, int >= 0) (maybe long if Python 2)
    """
    assert isinstance(n, int), type(n)
    assert n >= 0, n

    if n != 0:
        f_k_2, f_k_1 = fibonacci_pair__rec_n(n - 1)  # F_{k-2}, F_{k-1}

        return (f_k_1, f_k_1 + f_k_2)
    else:
        return (1, 0)


#
# Private functions
###################
if sys.version_info[:2] >= (3, 2):
    def __fibonacci_memo_get(n):
        """
        If :math:`F_n` is in cache,
        then return :math:`F_n` taken from cache and move it to the top of cache,
        else return None.

        :warning: Side effects: move result to the top of cache.

        :param n: int >= -1

        :return: None or (int >= 0) (maybe long if Python 2)
        """
        assert isinstance(n, int), type(n)
        assert n >= -1, n

        assert len(__fibonacci_memo) <= __fibonacci_memo_max_size

        f_n = __fibonacci_memo.get(n)

        if f_n is not None:
            __fibonacci_memo.move_to_end(n)

        return f_n
else:
    def __fibonacci_memo_get(n):
        assert isinstance(n, int), type(n)
        assert n >= -1, n

        assert len(__fibonacci_memo) <= __fibonacci_memo_max_size

        f_n = __fibonacci_memo.get(n)

        if f_n is not None:
            f_n = __fibonacci_memo.pop(n)
            __fibonacci_memo[n] = f_n

        return f_n


def __fibonacci_memo_set(n, f_n):
    """
    Set `n`: `f_n` to the top of cache.

    :warning: Side effects: set result to the top of cache
                            and maybe kill oldest value.

    :param n: int >= -1
    :param f_n: int >= 0 (maybe long if Python 2)
    """
    assert isinstance(n, int), type(n)
    assert n >= -1, n

    assert isinstance(f_n, int) or isinstance(f_n, long), type(f_n)
    assert f_n >= 0, f_n

    assert len(__fibonacci_memo) <= __fibonacci_memo_max_size
    assert n not in __fibonacci_memo, (n, __fibonacci_memo[n])

    if len(__fibonacci_memo) == __fibonacci_memo_max_size:  # remove oldest
        __fibonacci_memo.popitem(False)

    __fibonacci_memo[n] = f_n


#
# Private global variables
##########################
__fibonacci_memo = None
"""
Cache used by `fibonacci__rec_memoized_n()`.
"""


__fibonacci_memo_max_size = None
"""
Maximum size of cache used by `fibonacci__rec_memoized_n()`.
"""


#
# Init
######
fibonacci_memoization_reinit()
