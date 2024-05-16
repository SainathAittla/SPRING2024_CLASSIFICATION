function [v] = saittla_pp4(f, x)
%SAITTLA_PP4 Evaluates the anonymous function f at scalar x
%
% Inputs:
%   f - Anonymous function
%   x - Scalar value at which to evaluate the function f
%
% Outputs:
%   v - Result of evaluating f at x

    if ~isa(f, 'function_handle')
        error('Input f must be a proper anonymous function');
    end

    v = f(x);
end %saittla_pp4
