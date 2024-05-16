function [num] = saittla_pp7(A, i, j, len)
%SAITTLA_PP7 Computes the number of paths of a given length or less between two nodes
%
% Inputs:
%   A - Adjacency matrix of the graph
%   i - Index of the departure node
%   j - Index of the arrival node
%   len - Maximum length of paths to be considered
%
% Outputs:
%   num - Total number of paths of length len or less from node i to node j

    num = 0;

    for k = 1:len
        next_state = A^k;
        num = num + next_state(i, j);
    end
end %saittla_pp7