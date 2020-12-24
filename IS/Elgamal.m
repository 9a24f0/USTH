function ElSig(a, p, d, x, k_E)
  printf("Parameters: (alpha, beta, p, d, x, k_E)\n");
  b = ModExp(a, d, p);
  r = ModExp(a, k_E, p)
  s = mod((x-d*r)*Inv(k_E, p-1), p-1);
  t = mod(ModExp(b, r, p) * ModExp(r, s, p), p);
  
  printf("-------------------\n");
  printf("Public key: (%d, %d, %d)\n", p, a, b);
  printf("Private key: %d\n", d);
  printf("Signature: (%d, %d)\n", r, s);
endfunction
