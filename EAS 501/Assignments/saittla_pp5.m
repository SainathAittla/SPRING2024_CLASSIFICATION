function [result] = saittla_pp5(f)
%SAITTLA_PP5 Tests a given function for evaluating function handles
%
% Inputs:
%   f - Function handle to the code intended to evaluate another function handle at a given input
%
% Outputs:
%   result - A number indicating the test outcome (-1 for error, 0 for incorrect output, +1 for correct output)

    testFunc = @(x)(x^2);
    testValue = 2;
    expectedOutput = 4;

    try
        output = f(testFunc, testValue);

        if output == expectedOutput
            result = +1;
        else
            result = 0;
        end
    catch
        result = -1;
    end
end %saittla_pp5
