function [val] = saittla_pp9(f, x)
%SAITTLA_PP9 Integrates a function over a set of grid locations using the midpoint rule
%
% Inputs:
%   f - Function handle to the function to be integrated
%   x - Vector containing the grid locations
%
% Outputs:
%   val - The integral of the function f over the grid locations defined by x

    if iscolumn(x)
        x = x';
    end
    val = 0;
    for i = 1:length(x)-1
        midpoint = (x(i) + x(i+1)) / 2;
        height = f(midpoint);
        width = x(i+1) - x(i);
        val = val + width*height;
    end
end %saittla_pp9