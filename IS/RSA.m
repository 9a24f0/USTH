function RSA (p, q, key, text)
  phi = (p - 1) * (q - 1);
  N = p * q;
  which_key = input("e or d?\n", "s");
  which_text = input("C or M?\n", "s");
  
  if (which_text == "M")
    M = text;
    if (which_key == "e")
      e = key;
      d = 1;
      while (mod(d*e, phi) != 1) d++; endwhile
      C = ModExp(M, e, N);
    endif
    if (which_key == "d")
      d = key;
      e = 1;
      while (mod(d*e, phi) != 1) e++; endwhile
      C = ModExp(M, e, N);
    endif
  endif
  
  if (which_text == "C")
    C = text;
    if (which_key == "e")
      e = key;
      d = 1;
      while (mod(d*e, phi) != 1) d++; endwhile
      M = ModExp(M, d, N);
    endif
    if (which_key == "d")
      d = key;
      e = 1;
      while (mod(d*e, phi) != 1) e++; endwhile
      M = ModExp(M, d, N);
    endif
  endif
  
  printf("-------------------\n");
  printf("Public key: (%d, %d)\n", N, e);
  printf("Private key: %d\n", d);
  printf("Plain text: %d\n", M);
  printf("Cipher text: %d\n", C);
  
endfunction