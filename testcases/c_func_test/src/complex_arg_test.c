/*******************************************************
 * Copyright (C) 2015 Hui Peng <peng124@purdue.edu>
 *
 * This file is part of {project}.
 *
 * {project} can not be copied and/or distributed without
 * the express permission of Hui Peng
 *******************************************************/

#include <stdio.h>

struct nested {
  int e;
  int f;
  int g;
  int h;
};

struct test {
  int a;
  int b;
  int c;
  int d;
  struct nested nested;
};

int complex_arg_func(struct test test) {
  int sum = 0;

  sum += test.a;
  sum += test.b;
  sum += test.c;
  sum += test.d;
  sum += test.nested.e;
  sum += test.nested.f;
  sum += test.nested.g;
  sum += test.nested.h;

  return sum;
}


int main(int argc, char *argv[])
{
  struct test t= {1, 2, 3, 4, {5, 6, 7, 8}};

  int s = complex_arg_func(t);

  return 0;
}
