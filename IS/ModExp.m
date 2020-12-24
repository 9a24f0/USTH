function r = ModExp (x, e, m)
  r = x;
  i = 1;
  bin = [];
  while (e > 0)
    if (mod(e, 2) == 0)
      bin(i) = 0;
      e = e/2;
    else 
      bin(i) = 1;
      e = (e-1)/2;
  endif
    i++;
  endwhile
  
  i--;
  while (i > 1)
    r = mod((r * r), m);
    --i;
    if (bin(i) == 1)
      r = mod((r*x), m);
    endif
  endwhile
  return;
endfunction
