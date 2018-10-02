#!/usr/bin/env julia

"""
Tests for the [`Digits`](@ref) common module.
"""
module TestDigits

include(joinpath("..", "src", "Digits.jl"))

using Test

@testset "Digits" begin
    @testset "is_palindrome" begin
        @test Digits.is_palindrome(1)
        @test !Digits.is_palindrome(10)
        @test Digits.is_palindrome(11)
        @test Digits.is_palindrome(22)
        @test Digits.is_palindrome(UInt8(22))
        @test Digits.is_palindrome(Int16(22))
        @test Digits.is_palindrome(BigInt(22))
        @test Digits.is_palindrome(404)
        @test Digits.is_palindrome(18, base = 8)
        @test Digits.is_palindrome(24, base = 23)
        @test !Digits.is_palindrome(2, base = 2)
        @test !Digits.is_palindrome(146)
        @test Digits.is_palindrome(146, base = 8)
        @test !Digits.is_palindrome(1212)
        @test Digits.is_palindrome(2332)
        @test Digits.is_palindrome(72427)
        @test Digits.is_palindrome(0x72427, base = 16)
        @test Digits.is_palindrome(724427)
        @test Digits.is_palindrome(0x724427, base = 16)
        @test Digits.is_palindrome(722444227)
        @test Digits.is_palindrome(313, base = 2)
        @test !Digits.is_palindrome(513513)
        @test !Digits.is_palindrome(169803, base = 8)
        @test !Digits.is_palindrome(551133)
        @test !Digits.is_palindrome(0x551133, base = 16)
        @test !Digits.is_palindrome(5133150)
        @test !Digits.is_palindrome(5133150, base = 23)
    end
end

end
