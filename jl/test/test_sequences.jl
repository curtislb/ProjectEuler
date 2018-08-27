#!/usr/bin/env julia

import Base.Filesystem
import Test

include(Filesystem.joinpath("..", "src", "Sequences.jl"))

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
end
