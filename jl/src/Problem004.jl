#!/usr/bin/env julia

"""
# Problem 4: Largest palindrome product

The prime factors of 13195 are 5, 7, 13 and 29.

A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two `d`-digit numbers.
"""
module Problem004

include("Digits.jl")

"""
    solve(; d::Integer = 3)

Returns the solution for [`Problem004`](@ref) with the given parameters.

## Preconditions
- `d > 0`
"""
function solve(; d::Integer = 3)
    # calculate max and min d-digit numbers
    base = convert(typeof(d), 10)
    max_factor = base^d - oneunit(d)
    min_factor = base^(d - oneunit(d))

    # search for palindromic products of d-digit numbers
    max_product = -oneunit(d)
    for n in max_factor:-oneunit(d):min_factor
        for m in n:-oneunit(d):min_factor
            product = n * m

            # stop checking products with n when we drop below max_product
            if max_product >= product
                break
            end

            # if product is a palindrome, it's the max possible for this n
            if Digits.is_palindrome(product)
                max_product = product
                break
            end
        end
    end

    return max_product
end

end
