#!/usr/bin/env julia

"""
# Problem 3: Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number `n`?
"""
module Problem003

include("Primes.jl")

"""
    solve(; n::Integer = 600851475143)

Returns the solution for [`Problem003`](@ref) with the given parameters.

## Preconditions
- `n ≥ 2`
"""
function solve(; n::Integer = 600851475143)
    return last(Primes.prime_factorization(n))[1]
end

end
