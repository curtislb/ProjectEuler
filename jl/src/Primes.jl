#!/usr/bin/env julia

"""
Provides functions for finding and identifying prime numbers.
"""
module Primes

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
    while factor <= floor(n_type, sqrt(n))
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
