#!/usr/bin/env julia

"""
Provides functions for producing and operating on numerical sequences.
"""
module Sequences

"""
    arithmetic_series(a::Integer, n::Integer, d::Integer = 1)

Returns the sum of the arithmetic sequence with parameters `a`, `n`, `d`.

# Arguments
- `a`: The first term in the sequence
- `n`: The total number of terms in the sequence
- `d`: The difference between two consecutive terms in the sequence

# Preconditions:
- `n ≥ 0`

# Examples
```jldoctest
julia> arithmetic_series(1, 4)
10

julia> arithmetic_series(2, 6, -1)
-3

julia> arithmetic_series(3, 5, 4)
55
```
"""
function arithmetic_series(a::Integer, n::Integer, d::Integer = 1)
    return n * (2a + (n - 1)d) ÷ 2
end

end
