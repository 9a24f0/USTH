i = 1;
while (i < 1000)
  if (ModExp(3, i, 17) == 15) 
    print(i);
    i++;
  endif
endwhile
