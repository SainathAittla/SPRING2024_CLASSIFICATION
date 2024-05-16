function [l, v] = saittla_pp14(A, v0, tol, itermax)
%SAITTLA_PP14 Calculates dominant eigenvector and eigenvalue using Rayleigh-Quotient iteration
%
% Inputs:
%   A - Matrix whose dominant eigenvalue and eigenvector are to be found
%   v0 - Initial vector guess
%   tol - Tolerance for convergence
%   itermax - Maximum number of iterations
%
% Outputs:
%   l - Dominant eigenvalue
%   v - Corresponding eigenvector

    % Normalize the initial vector v0
    v = v0 / norm(v0);
    % Compute initial Rayleigh quotient as the eigenvalue estimate
    l = dot(v, A * v);

    % Main iteration loop
    for i = 1:itermax

        % Normalize w to get the next eigenvector estimate
        v = A * v;
        v = v / norm(v);

        % Update the eigenvalue estimate using the Rayleigh quotient
        l_old = l;
        l = dot(v, A * v);

        % Check convergence
        if abs((l - l_old) / l) < tol
            return;
        end
    end

    % This line is reached if maximum iterations are exceeded
    error('Maximum number of iterations exceeded');
end %saittla_pp14