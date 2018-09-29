#!/usr/bin/env julia

using ArgParse
using Base.Iterators
using Printf

function main()
    args = parse_arguments()
    answers = load_answers()
    prob_strs = select_problems(answers, args["prob_nums"], args["skip"])
    pass_count = 0
    for prob_str in prob_strs
        if test_problem(answers, prob_str)
            pass_count += 1
        end
    end
    println("-"^40)
    println("Solutions passed $(pass_count)/$(length(prob_strs)) tests")
end

"Parses script arguments from the command line and returns them as a `Dict`."
function parse_arguments()
    settings = ArgParseSettings()
    @add_arg_table settings begin
        "-s", "--skip"
            help = "test all *except* the following problems"
            action = :store_true
        "prob_nums"
            help = "number of a specific problem to be tested"
            arg_type = Int
            nargs = '*'
            metavar = "prob_num"
    end
    return parse_args(settings)
end

"Reads problem numbers and answers from `stdin` and returns them as a `Dict`."
function load_answers()
    answers = Dict{String, Int}()
    for line in eachline()
        prob_num, answer = split(line)
        answers[prob_num] = parse(Int, answer)
    end
    return answers
end

"Returns a list of strings representing the problem numbers to be tested."
function select_problems(
    answers::Dict{String, Int},
    prob_nums::Array{Int, 1},
    should_skip::Bool
)
    if isempty(prob_nums)
        prob_strs = collect(keys(answers))
    elseif should_skip
        skip_set = Set(prob_nums)
        prob_strs = String[]
        for prob_str in keys(answers)
            if parse(Int, prob_str) ∉ skip_set
                push!(prob_strs, prob_str)
            end
        end
    else
        prob_strs = map(prob_nums) do prob_num
            @sprintf "%03d" prob_num
        end
    end
    return sort(prob_strs)
end

"Tests a specific problem. Returns `true` on success or `false` on failure."
function test_problem(answers::Dict{String, Int}, prob_str::String)
    if !haskey(answers, prob_str)
        println(stderr, "Problem $prob_str: no answer in input file")
        return false
    end

    print("Testing Problem $prob_str...")
    flush(stdout)

    try_or_fail(prob_str, "no file found for this problem") do
        include(joinpath("..", "src", "Problem$(prob_str).jl"))
    end || return false

    try_or_fail(prob_str, "solution failed with an error", show_error = true) do
        solve_expr = Meta.parse("Problem$(prob_str).solve()")
        (answer, time_sec) = @timed eval(solve_expr)
        correct = answers[prob_str]
        @assert (answer == correct) "expected $correct, but got $answer"
        @printf "PASSED (%6.2f s)\n" time_sec
    end || return false

    return true
end

"Runs `f` or prints an error. Returns `true` on success or `false` on failure."
function try_or_fail(
    f::Function,
    prob_str::String,
    error_msg::String;
    show_error::Bool = false
)
    try
        f()
        return true
    catch e
        println("FAILED")
        println(stderr, "Problem $prob_str: $error_msg")
        if (show_error)
            showerror(stderr, e)
            println(stderr)
            print_trace(stacktrace(catch_backtrace()))
        end
        return false
    end
end

"Prints a stack trace to `stderr` in a human-readable format."
function print_trace(trace::StackTraces.StackTrace)
    for (index, frame) in enumerate(trace)
        println(stderr, " [$index] $frame")
    end
end

main()
