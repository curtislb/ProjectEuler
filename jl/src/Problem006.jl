#!/usr/bin/env julia

"""
# Problem 6: Sum square differences

The sum of the squares of the first ten natural numbers is,

    1² + 2² + ... + 10² = 385

The square of the sum of the first ten natural numbers is,

    (1 + 2 + ... + 10)² = 55² = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first `n` natural
numbers and the square of the sum.
"""
module Problem006

include("Sequences.jl")

"""
    solve(; n::Integer = 100)

Returns the solution for [`Problem006`](@ref) with the given parameters.
"""
function solve(; n::Integer = 100)
    return Sequences.triangular(n)^2 - Sequences.sum_of_squares(n)
end

end
