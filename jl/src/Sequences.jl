#!/usr/bin/env julia

"""
Provides utilities for producing and operating on numerical sequences.
"""
module Sequences

"""
    Fibonacci()
    Fibonacci(int_t::Type{<:Integer})

Iterable object that returns subsequent terms of the Fibonacci sequence.

## Fields
- `int_t`: The integer type of each term in the sequence. Defaults to `Int`

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
    int_t::Type{<:Integer}
end
Fibonacci() = Fibonacci(Int)

function Base.iterate(
    iter::Fibonacci,
    state::Tuple{Integer, Integer} = (zero(iter.int_t), oneunit(iter.int_t))
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
    fibonacci(n::Integer, int_type::Type{<:Integer} = Int)

Computes the specified term `F(n)` of the Fibonacci sequence, defined by the
relation `F(m) = F(m - 1) + F(m - 2)` with `F(0) = F(1) = 1`.

## Arguments
- `n`: Specifies the term `F(n)` in the Fibonacci sequence to return
- `int_type`: The integer type of each term in the sequence

## Preconditions
- `n ≥ 0`

## Examples
```jldoctest
julia> fibonacci(0)
1

julia> fibonacci(4)
5

julia> fibonacci(5, UInt8)
0x08
```

See also: [`Fibonacci`](@ref)
"""
function fibonacci(n::Integer, int_type::Type{<:Integer} = Int)
    # Fibonacci iterates from F(1), so handle F(0) ourselves
    if n == 0
        return oneunit(n)
    end

    for (i, fib_num) in Iterators.enumerate(Fibonacci(int_type))
        if i == n
            return fib_num
        end
    end

    # Fibonacci iterator should never terminate
    throw(ErrorException("iteration terminated unexpectedly"))
end

end