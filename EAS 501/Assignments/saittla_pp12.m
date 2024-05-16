function [result] = saittla_pp12(f)
%SAITTLA_PP12 Tests a given function f
%
% Inputs:
%   f - Function handle to the Newton Raphson function
%
% Outputs:
%   result - A number indicating the test outcome (-1 for error, 0 for incorrect output, +1 for correct output)

    g = @(x)deal(x^2 - 4*x + 3, 2*x - 4); %returns multiple outputs
    x0 = 0.5; % Initial guess close to one of the roots (x = 1)
    eps = 1e-6; % Tolerance for convergence
    delta = 1e6; % To check divergence in this test
    itermax = 100; % Maximum number of iterations
    
    % Known correct output (root of g close to x0 is x = 1)
    expectedOutput = 1;
    
    try
        [actualOutput] = f(g, x0, eps, delta, itermax);  
        % Checking if the output is correct (within tolerance)
        if abs(actualOutput - expectedOutput) < eps
            result = +1; % Correct output
        else
            result = 0; % Incorrect output
        end
    catch ME
        % Check for a specific known error message
        if contains(ME.message, 'Divergence')
            result = 0; % Specific error related to divergence
        elseif contains(ME.message, 'Maximum iterations exceeded')
            result = 0; % Specific error related to exceeding max iterations
        else
            result = -1; % An unknown error occurred
        end
    end
end %saittla_pp12