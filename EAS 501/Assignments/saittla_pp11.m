function [x] = saittla_pp11(g, x0, eps, delta, itermax)
%SAITTLA_PP11 Computes the root of given function using Newton-Raphson method.
%
% Inputs:
%   g - Function handle that returns a function at x and its derivative at x
%   x0 - Initial guess of the root
%   eps - Convergence criteria
%   delta - Divergence Criteria
%   itermax - Maximum iterations
%
% Outputs:
%   x - Predicted root after convergence
    
    x = x0;
    
    % Loop until the maximum number of iterations is reached
    for i = 1:itermax
        [f, fx] = g(x);
        
        x_pred = x - f/fx;

        %Checking for convergence
        if abs(x_pred - x) < eps
            x = x_pred;
            return;
        end
        
        % Checking for divergence
        if abs(x_pred - x) > delta
            error('Divergence');
        end
        
        x = x_pred;
    end
    
    % This line is reached when the maximum number of iterations are exceeded
    error('Maximum iterations exceeded');
end %saittla_pp11