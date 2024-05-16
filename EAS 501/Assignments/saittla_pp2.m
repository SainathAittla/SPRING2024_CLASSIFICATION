function [f] = saittla_pp2(n)
%SAITTLA_PP2 Computes the factorial of a whole number using a for-loop.
%
% Inputs:
%   n - Whole number for which factorial needs to be computed.
%
% Outputs:
%   f - Factorial of the input integer.

    if n < 0 || (n - floor(n)) ~= 0
        error('Input must be a whole number');
    end

    f = 1;

    for i = 1:n
        f = f * i;
    end
end %saittla_pp2