function [f] = saittla_pp3(n)
%SAITTLA_PP3 Computes the factorial of a whole number using a while-loop
%
% Inputs:
%   n - Whole number for which factorial needs to be computed
%
% Outputs:
%   f - Factorial of the input integer

    if n < 0 || (n - floor(n)) ~= 0
        error('Input must be a whole number');
    end

    f = 1;
    
    i = 1;
    while i <= n
        f = f * i;
        i = i + 1;
    end
end %saittla_pp3