#!/usr/bin/env julia

"""
# Problem 1: Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of `m` or `n` below `limit`.
"""
module Problem001

include("Sequences.jl")

"""
    solve(; m::Integer = 3, n::Integer = 5, limit::Integer = 1000)

Returns the solution for [`Problem001`](@ref) with the given parameters.
"""
function solve(; m::Integer = 3, n::Integer = 5, limit::Integer = 1000)
    m_sum = sum_divisible_by(m, limit)
    n_sum = sum_divisible_by(n, limit)
    lcm_sum = sum_divisible_by(lcm(m, n), limit)
    return m_sum + n_sum - lcm_sum
end

"""
    sum_divisible_by(n::Integer, limit::Integer)

Returns the sum of natural numbers below `limit` that are divisible by `n`.

## Preconditions
- `n > 0`
- `limit > 0`

## Examples
```jldoctest
julia> sum_divisible_by(3, 10)
18

julia> sum_divisible_by(5, 10)
5

julia> sum_divisible_by(5, 5)
0
```
"""
function sum_divisible_by(n::Integer, limit::Integer)
    return Sequences.arithmetic_series(n, (limit - 1) ÷ n, n)
end

end
