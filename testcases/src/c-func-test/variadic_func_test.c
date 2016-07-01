/*******************************************************
 * Copyright (C) 2015 Hui Peng <peng124@purdue.edu>
 *
 * This file is part of {project}.
 *
 * {project} can not be copied and/or distributed without
 * the express permission of Hui Peng
 *******************************************************/
#include <stdarg.h>
#include <stdio.h>

int variadic_sum(int count, ...) {
  va_list ap;
  int i, sum;

  va_start (ap, count);         /* Initialize the argument list. */

  sum = 0;
  for (i = 0; i < count; i++)
    sum += va_arg (ap, int);    /* Get the next argument value. */

  va_end (ap);                  /* Clean up. */

  return sum;
}

int main(int argc, char *argv[])
{
  int s = variadic_sum(10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
  return 0;
}

