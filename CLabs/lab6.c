#include <stdio.h>
#include <math.h>
#define NROWS 6
#define NCOLS 8

int main(void)
{
   /*  Declare and initialize variables.  */
   int row, col;
   double t[NROWS][NCOLS], top, right, left, bottom, tolerance, update, check, max_update=0.0;

   /*  Prompt user to enter initial temperatures and tolerance.  */
   //printf("Enter initial temperatures (top, right, bottom, left): ");
   scanf("%lf %lf %lf %lf",&top,&right,&bottom,&left);
   //printf("Enter tolerance for equilibrium (>0): ");
   scanf("%lf",&tolerance);

   /*  Initialize grid.  */
   for (row=1; row<NROWS-1; row++)
   {
      for (col=1; col<NCOLS-1; col++)
         t[row][col] = 0.0;
      t[row][0] = left;
      t[row][NCOLS-1] = right;
   }
   for (col=0; col<NCOLS; col++)
   {
      t[0][col] = top;
      t[NROWS-1][col] = bottom;
   }

   /*  Update the grid across the rows.  */
   do
   {
      /*  Initialize the maximum update this iteration to zero */
      max_update = 0.0;

      /*  Interior rows */
      for (row=1; row<NROWS-1; row++)
      {
         for(col=1; col<NCOLS-1; col++)
         {
            update = (t[row][col+1] + t[row][col-1] + t[row-1][col] + t[row+1][col])/4;
            check = update - t[row][col];
            if (check > max_update)
               max_update = check;
            t[row][col] = update;
         }
      }
   } while(max_update > tolerance);

   printf("Equilibrium values: \n");
   for (row=1; row<NROWS-1; row++)
   {
      for (col=1; col<NCOLS-1; col++)
         printf(" %.3f ",t[row][col]);
      printf("\n");
   }

   /*  Exit program.  */
   return 0;
}
