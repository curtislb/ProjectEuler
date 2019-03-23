#!/usr/bin/env julia

"""
# Problem 7: 10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the `n`th prime number?
"""
module Problem007

include("Primes.jl")

"""
    solve(; n::Integer = 10001)

Returns the solution for [`Problem007`](@ref) with the given parameters.
"""
function solve(; n::Integer = 10001)
    return Primes.prime(n)
end

end
