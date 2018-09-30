#!/usr/bin/env julia

"""
Methods for manipulating and operating on numerical digits.
"""
module Digits

"""
    is_palindrome(n::Integer; base::Integer = 10)

Determines if the natural number `n` is a palindrome (reads the same forwards
and backwards) when written in base `base`.

## Preconditions
- `n > 0`
- `base ≥ 2`

## Examples
```jldoctest
julia> is_palindrome(1)
true

julia> is_palindrome(404)
true

julia> is_palindrome(146)
false

julia> is_palindrome(146, base = 8)
true
```
"""
function is_palindrome(n::Integer; base::Integer = 10)
    n_digits = digits(n, base = base)

    i = 1
    j = length(n_digits)
    while i < j
        if n_digits[i] != n_digits[j]
            return false
        end
        i += 1
        j -= 1
    end

    return true
end

end
