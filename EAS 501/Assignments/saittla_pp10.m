function [result] = saittla_pp10(f)
%SAITTLA_PP10 Unit Test for an integration function similar to saittla_pp9.
%
% Inputs:
%   f - Function handle to the code intended to evaluate another function handle at a given input
%
% Outputs:
%   result - A number indicating the test outcome (-1 for error, 0 for incorrect output, +1 for correct output)

    try
        testFunc = @(x)(x^2);
        gridValues = [0 2 4 6 8];
    
        expectedValue = 168;
    
        actualValue = f(testFunc, gridValues);

        if actualValue == expectedValue
            result = +1;
        else
            result = 0;
        end
    catch
        result = -1;
    end
end %saittla_pp10