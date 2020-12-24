function i = Inv(x, p)
  i = 1;
  while (mod(x * i, p) != 1) i++; endwhile
  return
endfunction
