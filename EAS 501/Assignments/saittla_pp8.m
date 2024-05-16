function [R] = saittla_pp8(A)
%SAITTLA_PP8 Computes the Reduced Row Echelon Form of a matrix using Gaussian Elimination with Pivoting.
%
% Inputs:
%   A - Matrix for which the Reduced Row Echelon Form is to be computed.
%
% Outputs:
%   R - The Reduced Row Echelon Form (RREF) of matrix A.

    [m, n] = size(A);
    R = A;
    precision = 1e-15;
    
    for i = 1:min(m, n)
        [p, pivotRow] = max(abs(R(i:m, i)));
        pivotRow = pivotRow + i - 1;
        R([i, pivotRow], :) = R([pivotRow, i], :);
        if(p>precision)
            R(i, :) = R(i, :) / R(i, i);
            
            for j = [1:i-1, i+1:m]
                R(j, :) = R(j, :) - R(j, i) * R(i, :);
            end
        end
    end
end %saittla_pp8