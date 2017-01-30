
set table 'Spec.dat'
plot[400:600][0:1] 'full-UV_Lbroad-10nm.dat' w l, 'full-deltaSpecNorm.dat' u 1:($2) with impulses
