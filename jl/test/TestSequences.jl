#!/usr/bin/env julia

"""
Tests for the [`Sequences`](@ref) common module.
"""
module TestSequences

include(joinpath("..", "src", "Sequences.jl"))

using Test

@testset "Sequences" begin
    @testset "Fibonacci" begin
        @test first(Sequences.Fibonacci()) == 1
        @test first(Sequences.Fibonacci(UInt8)) == 1
        @test typeof(first(Sequences.Fibonacci(UInt8))) == UInt8
        @test first(Sequences.Fibonacci(BigInt)) == 1
        @test typeof(first(Sequences.Fibonacci(BigInt))) == BigInt

        fib_seq = [1, 2, 3, 5, 8, 13]
        for (i, n) in enumerate(Sequences.Fibonacci())
            if i > length(fib_seq)
                break
            end
            @test n == fib_seq[i]
        end

        for (i, n) in enumerate(Sequences.Fibonacci(BigInt))
            if i <= length(fib_seq)
                @test n == fib_seq[i]
            elseif i == 13
                @test n == 377
            elseif i == 37
                @test n == 39088169
            elseif i == 170
                @test (
                    n == parse(BigInt, "244006547798191185585064349218729154")
                )
            elseif i > 170
                break
            end
        end
    end


    @testset "arithmetic_series" begin
        @test Sequences.arithmetic_series(1, 4) == 10
        @test Sequences.arithmetic_series(2, 6, -1) == -3
        @test Sequences.arithmetic_series(3, 5, 4) == 55
        @test Sequences.arithmetic_series(4, 1) == 4
        @test Sequences.arithmetic_series(4, 1, 1) == 4
        @test Sequences.arithmetic_series(4, 1, 2) == 4
        @test Sequences.arithmetic_series(1, 2, -1) == 1
        @test Sequences.arithmetic_series(19, 5, 4) == 135
        @test Sequences.arithmetic_series(7, 8, -3) == -28
        @test Sequences.arithmetic_series(-14, 8, 3) == -28
    end

    @testset "fibonacci" begin
        @test Sequences.fibonacci(0) == 1
        @test Sequences.fibonacci(1) == 1
        @test Sequences.fibonacci(2) == 2
        @test Sequences.fibonacci(3) == 3
        @test Sequences.fibonacci(4) == 5
        @test Sequences.fibonacci(5) == 8
        @test Sequences.fibonacci(6) == 13
        @test Sequences.fibonacci(13) == 377
        @test Sequences.fibonacci(37) == 39088169
        @test (
            Sequences.fibonacci(BigInt, 200)
                == parse(BigInt, "453973694165307953197296969697410619233826")
        )
    end

    @testset "sum_of_squares" begin
        @test Sequences.sum_of_squares(0) == 0
        @test Sequences.sum_of_squares(1) == 1
        @test Sequences.sum_of_squares(2) == 5
        @test Sequences.sum_of_squares(3) == 14
        @test Sequences.sum_of_squares(4) == 30
        @test Sequences.sum_of_squares(5) == 55
        @test Sequences.sum_of_squares(6) == 91
        @test Sequences.sum_of_squares(7) == 140
        @test Sequences.sum_of_squares(401) == 21574201
        @test Sequences.sum_of_squares(34594) == 13800661997045
    end

    @testset "triangular" begin
        tri_nums = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120]
        for (i, n) in enumerate(tri_nums)
            @test Sequences.triangular(i) == n
        end
        @test Sequences.triangular(292) == 42778
        @test Sequences.triangular(38483) == 740489886
        @test Sequences.triangular(4946666) == 12234754731111
    end
end

end
