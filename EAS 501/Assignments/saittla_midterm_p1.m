function [a, n] = saittla_midterm_p1(fdf, a0, x, y, tol)
%SAITTLA_MIDTERM_P1 Computes converged coefficients and number of iterations for convergence
%
% Inputs:
%   fdf -  An external function which returns the residual vector and Jacobian matrix.
%   a0 - The initial guess at the coefficients, stored as a column vector.
%   x - values as column vector.
%   y - values of column vector.
%   tol - Tolerance to solve to.
%
% Outputs:
%   a - A column array the same length as a0 with the converged coefficients.
%   n - The number of iterations it took to converge

    a = a0;
    maximumIterations = 100;
    nestedIterations = 10;
    [r, J] = fdf(a, x, y);
    prevNorm = norm(r);

    % Iteration loop
    for n = 1: maximumIterations
        alpha=1;   % Damping factor full step 
        [r, J] = fdf(a, x, y);
        
        % Solving for delta
        delta = -J\r;
        
        % Checking for convergence
        if norm(delta) < tol
            return;
        end
        
        % Nested damped iteration
        for j = 1:nestedIterations
            ak = a + alpha * delta;
            [rk, ~] = fdf(ak, x, y);
            newNorm = norm(rk);
            
            if newNorm < prevNorm
                a = ak;
                prevNorm = newNorm;
                break; % Stopping iterations if current norm is smaller than previous norm
            else
                alpha = alpha / 2; % Reducing the step size by half
            end
        end
        
        if j == nestedIterations
            a = ak; % Accepting the last step regardless of norm
        end
    end
    
    % Reaches this line for non-convergence
    error('The algorithm did not converge within the maximum number of iterations.');
end %saittla_midterm_p1