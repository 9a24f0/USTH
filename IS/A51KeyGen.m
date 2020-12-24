function A51KeyGen (x, y, z, n)
  s = zeros(1, n);
  for i = 1:n
    %% find keystream bits
    s(i) = xor(x(19), y(22), z(23));
    
    %% find majority
    m = xor((x(9)&&y(11)), (x(9)&&z(11)), (y(11)&&z(11)));
    if (x(9) == m)
      x = shift(x, 1);
      x(1) = xor(x(19), x(18), x(15), x(14));
    endif
    if (y(11) == m)
      y = shift(y, 1);
      y(1) = xor(y(22), y(21));
    endif
    if (z(11) == m)
      z = shift(z, 1);
      z(1) = xor(z(23), z(22), z(21), z(8));
    endif
  end
  s
  x
  y
  z
endfunction