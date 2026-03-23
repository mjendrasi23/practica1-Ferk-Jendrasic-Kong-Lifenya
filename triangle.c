#include <math.h>
#include <stdio.h>
int
checktriangle (int a, int b, int c)
{
int A, B, C;
if ((c < a + b) && (b < a + c) && (a < c + b))
 {
 if (a == b && a == c)
 {printf ("Equilateral triangle \n");}
 else if (a == b || b == c)
 {printf ("Isosceles triangle \n");}
 else
 {printf ("Equal-sided triangle \n");}
 }
 else
 {printf ("It is not a triangle. \n");}
return 0;
}
int
main ()
{
int a, b, c, i, n;
printf ("Number of test cases: \n");
scanf ("%d", &n);
 printf ("%d", n);
 printf ("\n");

for (i = 1; i < n + 1; i++)
 {printf ("Mark the length values of the sides of the triangle (one per line): \n");
 scanf ("%d", &a); printf ("%d,", a);
 scanf ("%d", &b); printf ("%d,", b);
 scanf ("%d", &c); printf ("%d: \n", c);
 checktriangle (a, b, c);};
return 0;
}
