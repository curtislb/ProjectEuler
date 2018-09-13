#!/usr/bin/env julia

include(joinpath("..", "src", "Primes.jl"))

import Test

Test.@testset "Primes" begin
    Test.@testset "prime_factorization" begin
        Test.@test Primes.prime_factorization(2) == [(2, 1)]
        Test.@test Primes.prime_factorization(3) == [(3, 1)]
        Test.@test Primes.prime_factorization(4) == [(2, 2)]
        Test.@test Primes.prime_factorization(5) == [(5, 1)]
        Test.@test Primes.prime_factorization(6) == [(2, 1), (3, 1)]
        Test.@test Primes.prime_factorization(12) == [(2, 2), (3, 1)]
        Test.@test Primes.prime_factorization(600) == [(2, 3), (3, 1), (5, 2)]
        Test.@test Primes.prime_factorization(2903) == [(2903, 1)]
        Test.@test(
            Primes.prime_factorization(61740)
                == [(2, 2), (3, 2), (5, 1), (7, 3)]
        )
        Test.@test(
            Primes.prime_factorization(4928693)
                == [(7, 1), (11, 3), (23, 2)]
        )
        Test.@test(
            Primes.prime_factorization(169165232)
                == [(2, 4), (17, 1), (313, 1), (1987, 1)]
        )
        Test.@test(
            Primes.prime_factorization(74435892358158)
                == [(2, 1), (3, 3), (29, 1), (3049, 2), (5113, 1)]
        )
    end
end
