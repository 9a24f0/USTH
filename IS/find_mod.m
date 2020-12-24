function find_mod(a, N)
  i = 1;
  while (mod(a*i, N) != 1)
    i++;
  endwhile
  i
endfunction
