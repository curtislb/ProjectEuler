#!/usr/bin/env julia

include(joinpath("..", "src", "Sequences.jl"))

import Test

Test.@testset "Sequences" begin
    Test.@testset "arithmetic_series" begin
        Test.@test Sequences.arithmetic_series(1, 4) == 10
        Test.@test Sequences.arithmetic_series(2, 6, -1) == -3
        Test.@test Sequences.arithmetic_series(3, 5, 4) == 55
        Test.@test Sequences.arithmetic_series(4, 1) == 4
        Test.@test Sequences.arithmetic_series(4, 1, 1) == 4
        Test.@test Sequences.arithmetic_series(4, 1, 2) == 4
        Test.@test Sequences.arithmetic_series(1, 2, -1) == 1
        Test.@test Sequences.arithmetic_series(19, 5, 4) == 135
        Test.@test Sequences.arithmetic_series(7, 8, -3) == -28
        Test.@test Sequences.arithmetic_series(-14, 8, 3) == -28
    end

    Test.@testset "fibonacci" begin
        Test.@test Sequences.fibonacci(0) == 1
        Test.@test Sequences.fibonacci(1) == 1
        Test.@test Sequences.fibonacci(2) == 2
        Test.@test Sequences.fibonacci(3) == 3
        Test.@test Sequences.fibonacci(4) == 5
        Test.@test Sequences.fibonacci(5) == 8
        Test.@test Sequences.fibonacci(6) == 13
        Test.@test Sequences.fibonacci(13) == 377
        Test.@test Sequences.fibonacci(37) == 39088169
        Test.@test (
            Sequences.fibonacci(200, BigInt)
                == parse(BigInt, "453973694165307953197296969697410619233826")
        )
    end

    Test.@testset "Fibonacci" begin
        Test.@test first(Sequences.Fibonacci()) == 1
        Test.@test first(Sequences.Fibonacci(UInt8)) == 1
        Test.@test typeof(first(Sequences.Fibonacci(UInt8))) == UInt8
        Test.@test first(Sequences.Fibonacci(BigInt)) == 1
        Test.@test typeof(first(Sequences.Fibonacci(BigInt))) == BigInt

        fib_seq = [1, 2, 3, 5, 8, 13]
        for (i, n) in enumerate(Sequences.Fibonacci())
            if i > length(fib_seq)
                break
            end
            Test.@test n == fib_seq[i]
        end

        for (i, n) in Iterators.enumerate(Sequences.Fibonacci(BigInt))
            if i <= length(fib_seq)
                Test.@test n == fib_seq[i]
            elseif i == 13
                Test.@test n == 377
            elseif i == 37
                Test.@test n == 39088169
            elseif i == 170
                Test.@test (
                    n == parse(BigInt, "244006547798191185585064349218729154")
                )
            elseif i > 170
                break
            end
        end
    end
end
