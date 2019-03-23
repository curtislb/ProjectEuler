#!/usr/bin/env julia

"""
Methods for finding and identifying prime numbers.
"""
module Primes

include("Sequences.jl")

# Currently computed prime number terms (in sorted order)
_prime_sequence = Int128[2]

"""
Precomputes and stores at least the first `n` prime numbers.
"""
function _compute_primes(n::Integer)
    global _prime_sequence

    # check if first n primes have already been computed
    if n < length(_prime_sequence)
        return
    end

    if n ≤ 25
        _compute_primes_up_to(97)
    else
        # set estimate and increment values according to PNT
        approx_gap = _estimate_prime_gap(n)
        estimate = trunc(BigInt, n * approx_gap)
        increment = trunc(BigInt, approx_gap)

        # get primes up to estimate, then step forward until n are found
        _compute_primes_up_to(estimate)
        while length(_prime_sequence) < n
            estimate += increment
            _compute_primes_up_to(estimate)
        end
    end
end

"""
Precomputes and stores the prime numbers up to `n`.
"""
function _compute_primes_up_to(n::Integer)
    global _prime_sequence

    # check if primes up to n have already been computed
    prime_max = last(_prime_sequence)
    if prime_max ≥ n
        return
    end

    # prepare sieve for numbers prime_max + 1 to n
    sieve_size = n - prime_max
    sieve = repeat([true], sieve_size)

    # sift out composite numbers using previously computed primes
    prime_count = length(_prime_sequence)
    for p in _prime_sequence
        p_start = Sequences.next_multiple(p, prime_max + 1)
        for j in p_start:p:n
            sieve[j - prime_max] = false
        end
    end

    # sift out composite numbers using previously computed primes
    for i in 1:sieve_size
        if sieve[i]
            p = i + prime_max
            push!(_prime_sequence, p)
            for j in (p^2 - prime_max):p:sieve_size
                sieve[j] = false
            end
        end
    end
end

"""
Returns an estimate for the average gap between the first `n` primes.

This formula is based on a result derived from the Prime Number Theorem:
https://en.wikipedia.org/wiki/Prime_number_theorem
"""
function _estimate_prime_gap(n::Integer)
    log_n = log(n)
    loglog_n = log(log_n)
    log_n2 = log(n^2)
    loglog_n2 = log(log_n^2)
    return (
        log_n + loglog_n - 1 + (loglog_n - 2)/log_n
        - (loglog_n2 - 6loglog_n + 11)/(2log_n2) + exp(1)/log_n2
    )
end

"""
Resets the currently cached list of prime numbers.
"""
function _reset_prime_cache()
    global _prime_sequence
    _prime_sequence = Int128[2]
    return
end

"""
    prime(n::Integer)

Finds the `n`th prime number.

## Preconditions
- `n > 0`

## Examples
```jldoctest
julia> prime(1)
2

julia> prime(6)
13
```
"""
function prime(n::Integer)
    _compute_primes(n)
    global _prime_sequence
    return _prime_sequence[n]
end

"""
    prime_factorization(n::Integer)

Computes the prime factorization of the natural number `n`.

Result is a 1D array of base-exponent tuple pairs, containing each prime factor
and its power in the prime factorization of n.

## Preconditions
- `n ≥ 2`

## Examples
```jldoctest
julia> prime_factorization(UInt8(2))
1-element Array{Tuple{UInt8,UInt8},1}:
 (0x02, 0x01)

julia> prime_factorization(Int64(12))
2-element Array{Tuple{Int64,Int64},1}:
 (2, 2)
 (3, 1)

julia> prime_factorization(BigInt(600))
3-element Array{Tuple{BigInt,BigInt},1}:
 (2, 3)
 (3, 1)
 (5, 2)
```
"""
function prime_factorization(n::Integer)
    n_type = typeof(n)

    # populate array with (factor, power) pairs
    factor = 2 * oneunit(n_type)
    factorization = Array{Tuple{n_type, n_type}, 1}()
    while factor ≤ floor(n_type, sqrt(n))
        # compute power of factor in factorization
        power = zero(n_type)
        (d, r) = divrem(n, factor)
        while r == 0
            n = d
            power += 1
            (d, r) = divrem(n, factor)
        end

        # add (factor, power) pair to factorization
        if power > zero(n_type)
            push!(factorization, (factor, power))
        end

        factor += 1
    end

    # append remaining prime factor if necessary
    if n > 1
        push!(factorization, (n, 1))
    end

    return factorization
end

end
