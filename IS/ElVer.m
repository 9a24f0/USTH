function ElVer(x, a, b, d, p, r, s)
  t = mod(ModExp(b, r, p) * ModExp(r, s, p), p)
  if (t == ModExp(a, x, p))
    printf("Valid\n");
    else printf("Invalid\n");
  endif
endfunction
