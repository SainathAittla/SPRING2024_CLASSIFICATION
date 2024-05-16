function [f, fx] = functionhandle_p11(x)
    % Define the function value at x
    f = x^2 - 4*x + 3;
    
    % Define the derivative of the function at x
    fx = 2*x - 4;
end
