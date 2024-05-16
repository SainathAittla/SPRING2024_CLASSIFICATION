function [r, J] = saittla_midterm_p2(af, x, y)
%SAITTLA_MIDTERM_P2 Computes the Jacobian and residual vectors of given function at x and y.
%
% Inputs:
%   af -  The coefficient list.
%   x - The x-locations.
%   y - The y-locations.
%
% Outputs:
%   r - The residual vector.
%   J - The Jacobian matrix.

    a1 = af(1);
    a2 = af(2);
    a3 = af(3);
    
    prediction = a1 ./ (1 + exp(a2 + a3.*x));
    
    % Calculating the residual vector
    r = prediction - y;
    
    % Initialize the Jacobian matrix with zeros.
    J = zeros(length(x), length(af));
    
    % Derivative with respect to a1
    J(:, 1) = 1 ./ (1 + exp(a2 + a3.*x));
    % Derivative with respect to a2
    nonLinearTerm = exp(a2 + a3.*x);
    J(:, 2) = -(a1 .* nonLinearTerm) ./ ((1 + nonLinearTerm).^2);
    
    % Derivative with respect to a3
    J(:, 3) = -(a1 .* nonLinearTerm .* x) ./ ((1 + nonLinearTerm).^2);     
end %saittla_midterm_p2