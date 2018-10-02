#!/usr/bin/env julia

"""
Utilities for producing and operating on numerical sequences.
"""
module Sequences

"""
    Fibonacci([T::Type{<:Integer}])

Iterable object that returns subsequent terms of the Fibonacci sequence.

## Fields
- `T`: The integer type of each term in the sequence. Defaults to `Int`

## Examples
```julia-repl
julia> first(Fibonacci())
1

julia> first(Fibonacci(UInt8))
0x01

julia> for n in Fibonacci()
           println(n)
           if n > 10
               break
           end
       end
1
2
3
5
8
13

julia> for (i, n) in Iterators.enumerate(Fibonacci())
           println(n)
           if i == 5
               break
           end
       end
1
2
3
5
8
```

See also: [`fibonacci`](@ref)
"""
struct Fibonacci
    T::Type{<:Integer}
end
Fibonacci() = Fibonacci(Int)

function Base.iterate(
    iter::Fibonacci,
    state::Tuple{Integer, Integer} = (zero(iter.T), oneunit(iter.T))
)
    fib_old, fib_new = state
    fib_old, fib_new = fib_new, (fib_old + fib_new)
    return fib_new, (fib_old, fib_new)
end

"""
    arithmetic_series(a::Integer, n::Integer, d::Integer = 1)

Returns the sum of the arithmetic sequence with parameters `a`, `n`, `d`.

# Arguments
- `a`: The first term in the sequence
- `n`: The total number of terms in the sequence
- `d`: The difference between two consecutive terms in the sequence

# Preconditions
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

"""
    fibonacci([T::Type{<:Integer}], n::Integer)

Computes the specified term `F(n)` of the Fibonacci sequence, defined by the
relation `F(m) = F(m - 1) + F(m - 2)` with `F(0) = F(1) = 1`.

## Arguments
- `T`: The integer type of each term in the sequence. Defaults to `typeof(n)`
- `n`: Specifies the term `F(n)` in the Fibonacci sequence to return

## Preconditions
- `n ≥ 0`

## Examples
```jldoctest
julia> fibonacci(0)
1

julia> fibonacci(4)
5

julia> fibonacci(UInt8, 5)
0x08
```

See also: [`Fibonacci`](@ref)
"""
function fibonacci(n::Integer)
    return fibonacci(typeof(n), n)
end
function fibonacci(T::Type{<:Integer}, n::Integer)
    # Fibonacci iterates from F(1), so handle F(0) ourselves
    if n == 0
        return oneunit(T)
    end

    for (i, fib_num) in enumerate(Fibonacci(T))
        if i == n
            return fib_num
        end
    end

    # Fibonacci iterator should never terminate
    throw(ErrorException("iteration terminated unexpectedly"))
end

"""
    sum_of_squares(n::Integer)

Computes the sum of the squares of the first `n` natural numbers.

## Preconditions
- `n ≥ 0`

## Examples
```jldoctest
julia> sum_of_squares(1)
1

julia> sum_of_squares(0x02)
0x05

julia> sum_of_squares(4)
30
```
"""
function sum_of_squares(n::Integer)
    T = typeof(n)
    cube_term = convert(T, 2) * n^3
    square_term = convert(T, 3) * n^2
    return (cube_term + square_term + n) ÷ convert(T, 6)
end

"""
    triangular(n::Integer)

Computes the `n`th triangular number `T(n)`, with `T(1) = 1`. The resulting
value is also the sum of the first `n` natural numbers.

## Preconditions
- `n ≥ 0`

## Examples
```jldoctest
julia> triangular(1)
1

julia> triangular(0x03)
0x06

julia> triangular(4)
10
```
"""
triangular(n::Integer) = n * (n + oneunit(n)) ÷ convert(typeof(n), 2)

end
