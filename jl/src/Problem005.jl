#!/usr/bin/env julia

"""
# Problem 5: Smallest multiple

2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to `max_num`?
"""
module Problem005

"""
    solve(; max_num::Integer = 20)

Returns the solution for [`Problem005`](@ref) with the given parameters.

## Preconditions
- `max_num > 0`
"""
function solve(; max_num::Integer = 20)
    return lcm((1:max_num)...)
end

end
