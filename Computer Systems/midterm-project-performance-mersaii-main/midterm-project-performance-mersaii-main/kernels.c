#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "defs.h"
/******************************************************
 * PINWHEEL KERNEL
 *
 * Your different versions of the pinwheel kernel go here
 ******************************************************/

/*
 * naive_pinwheel - The naive baseline version of pinwheel
 */
char naive_pinwheel_descr[] = "naive_pinwheel: baseline implementation";
void naive_pinwheel(pixel *src, pixel *dest)
{
  int i, j;

  for (i = 0; i < src->dim; i++)
    for (j = 0; j < src->dim; j++)
    {
      /* Check whether we're in the diamond region */
      if ((fabs(i + 0.5 - src->dim / 2) + fabs(j + 0.5 - src->dim / 2)) < src->dim / 2)
      {
        /* In diamond region, so rotate and grayscale */
        int s_idx = RIDX(i, j, src->dim);
        int d_idx = RIDX(src->dim - j - 1, i, src->dim);
        dest[d_idx].red = ((int)src[s_idx].red + src[s_idx].green + src[s_idx].blue) / 3;
        dest[d_idx].green = ((int)src[s_idx].red + src[s_idx].green + src[s_idx].blue) / 3;
        dest[d_idx].blue = ((int)src[s_idx].red + src[s_idx].green + src[s_idx].blue) / 3;
      }
      else
      {
        /* Not in diamond region, so keep the same */
        int s_idx = RIDX(i, j, src->dim);
        int d_idx = RIDX(i, j, src->dim);
        dest[d_idx] = src[s_idx];
      }
    }
}

/*
 * pinwheel - Your current working version of pinwheel
 * IMPORTANT: This is the version you will be graded on
 */

// Define the block size
#define BLOCK_SIZE 16

char pinwheel_descr[] = "pinwheel: Current working version";
void pinwheel(pixel *src, pixel *dest)
{
    int dim = src->dim;
    int half_dim = dim / 2;
    double half_half_dim = 0.5 - half_dim;
    // Process the image in blocks
    for (int bi = 0; bi < dim; bi += BLOCK_SIZE) {
        for (int j = 0; j < dim; j += 8) {
            // Process each block
            for (int i = bi; i < fmin(bi + BLOCK_SIZE, dim); i++) {
                // for (int j = bj; j < fmin(bj + BLOCK_SIZE, dim); j+=16) {
                    int s_idx1 = RIDX(i, j, dim);
                    int s_idx2 = s_idx1 + 1;
                    int s_idx3 = s_idx2 + 1;
                    int s_idx4 = s_idx3 + 1;
                    int s_idx5 = s_idx4 + 1;
                    int s_idx6 = s_idx5 + 1;
                    int s_idx7 = s_idx6 + 1;
                    int s_idx8 = s_idx7 + 1;

                    int d_idx1 = RIDX(dim - j - 1, i, dim);
                    int d_idx2 = d_idx1 - dim;
                    int d_idx3 = d_idx2 - dim;
                    int d_idx4 = d_idx3 - dim;
                    int d_idx5 = d_idx4 - dim;
                    int d_idx6 = d_idx5 - dim;
                    int d_idx7 = d_idx6 - dim;
                    int d_idx8 = d_idx7 - dim;
                    
                    // Process first pixel
                    if ((fabs(i + half_half_dim) + fabs(j + half_half_dim)) < half_dim) {
                        int avail_dest1 = ((int)src[s_idx1].red + src[s_idx1].green + src[s_idx1].blue) / 3;
                        dest[d_idx1].red = avail_dest1;
                        dest[d_idx1].green = avail_dest1;
                        dest[d_idx1].blue = avail_dest1;
                    } else {
                        d_idx1 = s_idx1;
                        dest[d_idx1] = src[s_idx1];
                    }
                    // Process second pixel
                    if ((fabs(i + half_half_dim) + fabs(j + half_half_dim + 1)) < half_dim) {
                        int avail_dest2 = ((int)src[s_idx2].red + src[s_idx2].green + src[s_idx2].blue) / 3;
                        dest[d_idx2].red = avail_dest2;
                        dest[d_idx2].green = avail_dest2;
                        dest[d_idx2].blue = avail_dest2;
                    } else {
                        d_idx2 = s_idx2;
                        dest[d_idx2] = src[s_idx2];
                    }
                                        
                    // Process third pixel
                    if ((fabs(i + half_half_dim) + fabs(j + half_half_dim + 2)) < half_dim) {
                        int avail_dest3 = ((int)src[s_idx3].red + src[s_idx3].green + src[s_idx3].blue) / 3;
                        dest[d_idx3].red = avail_dest3;
                        dest[d_idx3].green = avail_dest3;
                        dest[d_idx3].blue = avail_dest3;
                    } else {
                        d_idx3 = s_idx3;
                        dest[d_idx3] = src[s_idx3];
                    }                    
                    
                    // Process fourth pixel
                    if ((fabs(i + half_half_dim) + fabs(j + half_half_dim + 3)) < half_dim) {
                        int avail_dest4 = ((int)src[s_idx4].red + src[s_idx4].green + src[s_idx4].blue) / 3;
                        dest[d_idx4].red = avail_dest4;
                        dest[d_idx4].green = avail_dest4;
                        dest[d_idx4].blue = avail_dest4;
                    } else {
                        d_idx4 = s_idx4;
                        dest[d_idx4] = src[s_idx4];
                    }                    
                    
                    // Process fifth pixel
                    if ((fabs(i + half_half_dim) + fabs(j + half_half_dim + 4)) < half_dim) {
                        int avail_dest5 = ((int)src[s_idx5].red + src[s_idx5].green + src[s_idx5].blue) / 3;
                        dest[d_idx5].red = avail_dest5;
                        dest[d_idx5].green = avail_dest5;
                        dest[d_idx5].blue = avail_dest5;
                    } else {
                        d_idx5 = s_idx5;
                        dest[d_idx5] = src[s_idx5];
                    }                    
                    
                    // Process sixth pixel
                    if ((fabs(i + half_half_dim) + fabs(j + half_half_dim + 5)) < half_dim) {
                        int avail_dest6 = ((int)src[s_idx6].red + src[s_idx6].green + src[s_idx6].blue) / 3;
                        dest[d_idx6].red = avail_dest6;
                        dest[d_idx6].green = avail_dest6;
                        dest[d_idx6].blue = avail_dest6;
                    } else {
                        d_idx6 = s_idx6;
                        dest[d_idx6] = src[s_idx6];
                    } 
                    
                    // Process seventh pixel
                    if ((fabs(i + half_half_dim) + fabs(j + half_half_dim + 6)) < half_dim) {
                        int avail_dest7 = ((int)src[s_idx7].red + src[s_idx7].green + src[s_idx7].blue) / 3;
                        dest[d_idx7].red = avail_dest7;
                        dest[d_idx7].green = avail_dest7;
                        dest[d_idx7].blue = avail_dest7;
                    } else {
                        d_idx7 = s_idx7;
                        dest[d_idx7] = src[s_idx7];
                    }                    
                    
                    // Process eight pixel
                    if ((fabs(i + half_half_dim) + fabs(j + half_half_dim + 7)) < half_dim) {
                        int avail_dest8 = ((int)src[s_idx8].red + src[s_idx8].green + src[s_idx8].blue) / 3;
                        dest[d_idx8].red = avail_dest8;
                        dest[d_idx8].green = avail_dest8;
                        dest[d_idx8].blue = avail_dest8;
                    } else {
                        d_idx8 = s_idx8;
                        dest[d_idx8] = src[s_idx8];
                    }
                }

            }
        }
    }


/*********************************************************************
 * register_pinwheel_functions - Register all of your different versions
 *     of the pinwheel kernel with the driver by calling the
 *     add_pinwheel_function() for each test function. When you run the
 *     driver program, it will test and report the performance of each
 *     registered test function.
 *********************************************************************/

void register_pinwheel_functions()
{
  add_pinwheel_function(&naive_pinwheel, naive_pinwheel_descr);
  add_pinwheel_function(&pinwheel, pinwheel_descr);
}

/***************************************************************
 * GLOW KERNEL
 *
 * Starts with various typedefs and helper functions for the glow
 * function, and you may modify these any way you like.
 **************************************************************/

/* A struct used to compute averaged pixel value */
typedef struct
{
  int red;
  int green;
  int blue;
} pixel_sum;

/*
 * initialize_pixel_sum - Initializes all fields of sum to 0
 */
static void initialize_pixel_sum(pixel_sum *sum)
{
  sum->red = sum->green = sum->blue = 0;
}

/*
 * accumulate_sum - Accumulates field values of p in corresponding
 * fields of sum
 */
static void accumulate_weighted_sum(pixel_sum *sum, pixel p, double weight)
{
  sum->red += (int)p.red * weight;
  sum->green += (int)p.green * weight;
  sum->blue += (int)p.blue * weight;
}

/*
 * assign_sum_to_pixel - Computes averaged pixel value in current_pixel
 */
static void assign_sum_to_pixel(pixel *current_pixel, pixel_sum sum)
{
  current_pixel->red = (unsigned short)sum.red;
  current_pixel->green = (unsigned short)sum.green;
  current_pixel->blue = (unsigned short)sum.blue;
}

/*
 * weighted_combo - Returns new pixel value at (i,j)
 */
static pixel weighted_combo(int dim, int i, int j, pixel *src)
{
  int ii, jj;
  pixel_sum sum;
  pixel current_pixel;
  
  double weights[3][3] = {{0.16, 0.00, 0.16},
                          {0.00, 0.30, 0.00},
                          {0.16, 0.00, 0.16}};


  initialize_pixel_sum(&sum);
  for (ii = -1; ii < 2; ii++)
    for (jj = -1; jj < 2; jj++)
      if ((i + ii >= 0) && (j + jj >= 0) && (i + ii < dim) && (j + jj < dim))
        accumulate_weighted_sum(&sum,
                                src[RIDX(i + ii, j + jj, dim)],
                                weights[ii + 1][jj + 1]);

  assign_sum_to_pixel(&current_pixel, sum);

  return current_pixel;
}

/******************************************************
 * Your different versions of the glow kernel go here
 ******************************************************/

/*
 * naive_glow - The naive baseline version of glow
 */
char naive_glow_descr[] = "naive_glow: baseline implementation";
void naive_glow(pixel *src, pixel *dst)
{
  int i, j;

  for (i = 0; i < src->dim; i++)
    for (j = 0; j < src->dim; j++)
      dst[RIDX(i, j, src->dim)] = weighted_combo(src->dim, i, j, src);
}

static void right_side(int dim, pixel *src, pixel *dst, int jj){
  dst[jj].red = (unsigned short)((int)(src[jj].red * 0.30)  + (int)(src[jj - dim - 1].red * 0.16) + (int)(src[jj + dim - 1].red) * 0.16);
  dst[jj].green= (unsigned short)((int)(src[jj].green* 0.30)  + (int)(src[jj - dim - 1].green* 0.16) + (int)(src[jj + dim - 1].green* 0.16));
  dst[jj].blue= (unsigned short)((int)(src[jj].blue* 0.30)  + (int)(src[jj - dim - 1].blue* 0.16)  + (int)(src[jj + dim - 1].blue* 0.16));
}

static void left_side(int dim, pixel *src, pixel *dst, int jj){
  dst[jj].red = (unsigned short)((int)(src[jj].red * 0.30)  + (int)(src[jj - dim + 1].red * 0.16) + (int)(src[jj + dim + 1].red * 0.16));
  dst[jj].green= (unsigned short)((int)(src[jj].green* 0.30) + (int)(src[jj - dim + 1].green* 0.16)  + (int)(src[jj + dim + 1].green* 0.16));
  dst[jj].blue= (unsigned short)((int)(src[jj].blue* 0.30)  + (int)(src[jj - dim + 1].blue* 0.16)  + (int)(src[jj + dim + 1].blue* 0.16));
}
static void bottom_line(int dim, pixel *src, pixel *dst, int ii){
dst[ii].red   = (unsigned short)((int)(src[ii].red * 0.30) + (int)(src[ii - dim - 1].red * 0.16) + (int)(src[ii - dim + 1].red * 0.16));
dst[ii].green= (unsigned short)((int)(src[ii].green* 0.30) + (int)(src[ii - dim - 1].green * 0.16) + (int)(src[ii - dim + 1].green* 0.16)) ;
dst[ii].blue = (unsigned short)((int)(src[ii].blue* 0.30)   + (int)(src[ii - dim - 1].blue * 0.16) + (int)(src[ii - dim + 1].blue* 0.16));
}

static void top_line(int dim, pixel *src, pixel *dst, int ii){
  dst[ii].red = (unsigned short)((int)(src[ii].red * 0.30) + (int)(src[ii + dim - 1].red * 0.16) + (int)(src[ii + dim + 1].red * 0.16));
  dst[ii].green= (unsigned short)((int)(src[ii].green* 0.30) + (int)(src[ii + dim - 1].green* 0.16) + (int)(src[ii + dim + 1].green* 0.16));
  dst[ii].blue= (unsigned short)((int)(src[ii].blue* 0.30)  + (int)(src[ii + dim - 1].blue* 0.16) + (int)(src[ii + dim + 1].blue* 0.16));
}

char glow_descr[] = "glow: Current working version";
void glow(pixel *src, pixel *dst) {

int i, j, ij;
int dim = src->dim;
for (i = 1; i < dim ; i++) {
        for (j = 1; j < dim ; j++) {
            ij = RIDX(i, j, dim);
            dst[ij].red =(unsigned short)((int)(src[ij].red * 0.30) + (int)(src[ij - dim - 1].red * 0.16) + (int)(src[ij - dim + 1].red * 0.16) + (int)(src[ij + dim - 1].red * 0.16) + (int)(src[ij + dim + 1].red * 0.16));
            dst[ij].green =(unsigned short)((int)(src[ij].green* 0.30) + (int)(src[ij - dim - 1].green* 0.16) + (int)(src[ij - dim + 1].green* 0.16)+ (int)(src[ij + dim - 1].green* 0.16) + (int)(src[ij + dim + 1].green* 0.16));
            dst[ij].blue =(unsigned short)((int)(src[ij].blue* 0.30) + (int)(src[ij - dim - 1].blue* 0.16) + (int)(src[ij - dim + 1].blue* 0.16)+ (int)(src[ij + dim - 1].blue* 0.16) + (int)(src[ij + dim + 1].blue* 0.16));
        }
}
 for (int j = 1; j <= dim; j++) {
    top_line(dim, src, dst, j);
    bottom_line(dim, src, dst, dim * (dim - 1) + j + 1);
    left_side(dim, src, dst, j * dim + 1);
    right_side(dim, src, dst, j * dim);
     } 

// Top-left
ij = 1;
dst[ij].red   = (unsigned short)((int)((src[ij].red * 0.30) + (int)((src[dim + 2].red) * 0.16)));
dst[ij].green= (unsigned short)((int)((src[ij].green * 0.30) + (int)((src[dim + 2].green)* 0.16)));
dst[ij].blue = (unsigned short)((int)((src[ij].blue * 0.30)   +(int)((src[dim + 2].blue)* 0.16)));

//Top-right
ij = dim ;
dst[ij].red   = (unsigned short)((int)(src[ij].red* 0.30) + (int)(src[ij + dim - 1].red * 0.16 ));
dst[ij].green= (unsigned short)((int)(src[ij].green* 0.30)  + (int)(src[ij + dim - 1].green* 0.16)) ;
dst[ij].blue = (unsigned short)((int)(src[ij].blue* 0.30)  + (int)(src[ij + dim - 1].blue* 0.16) );

//Bottom-left
ij = dim*(dim-1 )+1;
dst[ij].red   = (unsigned short)((int)(src[ij].red *0.30)  + (int)(src[ij - dim + 1].red * 0.16));
dst[ij].green= (unsigned short)((int)(src[ij].green* 0.30) + (int)(src[ij - dim + 1].green * 0.16));
dst[ij].blue = (unsigned short)((int)(src[ij].blue* 0.30)  + (int)(src[ij - dim + 1].blue * 0.16));

//Bottom-right
ij = dim*dim ;
dst[ij].red   = (unsigned short)((int)(src[ij].red * 0.30)  + (int)(src[ij - dim - 1].red * 0.16));
dst[ij].green= (unsigned short)((int)(src[ij].green* 0.30) + (int)(src[ij - dim - 1].green* 0.16));
dst[ij].blue = (unsigned short)((int)(src[ij].blue* 0.30) +  (int)(src[ij - dim - 1].blue* 0.16));




}


// char glow_descr[] = "glow: Current working version";
// void glow(pixel *src, pixel *dst) {

// }




/*********************************************************************
 * register_glow_functions - Register all of your different versions
 *     of the glow kernel with the driver by calling the
 *     add_glow_function() for each test function.  When you run the
 *     driver program, it will test and report the performance of each
 *     registered test function.
 *********************************************************************/

void register_glow_functions()
{
  add_glow_function(&glow, glow_descr);
  add_glow_function(&naive_glow, naive_glow_descr);
}
