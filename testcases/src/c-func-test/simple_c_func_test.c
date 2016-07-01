/*******************************************************
 * Copyright (C) 2015 Hui Peng <peng124@purdue.edu>
 *
 * This file is part of {project}.
 *
 * {project} can not be copied and/or distributed without
 * the express permission of Hui Peng
 *******************************************************/
#include <stdio.h>

int func_0_args() {
  int a = 1, b = 1, c = 0;

  while (c < 10) {
    a = a + b;
    b = a + b;
  }

  return a;
}

int func_1_args(int a) {
  int i = 0;
  int ret = 0;

  while (i <= a) {
    ret += i;
  }

  return ret;
}

int func_2_args(int a, int b) {
  return a + b;
}

int func_3_args(int a, int b, int c) {
  return a + b + c;
}

int func_4_args(int a, int b, int c, int d) {
  return a + b + c + d;
}

int func_5_args(int a, int b, int c, int d, int e) {
  return a + b + c + d + e;
}


int func_6_args(int a, int b, int c, int d, int e, int f) {
  return a + b + c + d + e + f;
}

int func_7_args(int a, int b, int c, int d, int e, int f, int g) {
  return a + b + c + d + e + f + g;
}

int func_8_args(int a, int b, int c, int d, int e, int f, int g, int h) {
  return a + b + c + d + e + f + g + h;
}

int func_9_args(int a, int b, int c, int d, int e, int f, int g, int h, int i) {
  return a + b + c + d + e + f + g  + h + i;
}

int main(int argc, char *argv[])
{
  int a = func_0_args();
  int b = func_1_args(1);
  int c = func_2_args(1, 2);
  int d = func_3_args(1, 2, 3);
  int e = func_4_args(1, 2, 3, 4);
  int f = func_5_args(1, 2, 3, 4, 5);
  int g = func_6_args(1, 2, 3, 4, 5, 6);
  int h = func_7_args(1, 2, 3, 4, 5, 6, 7);
  int i = func_8_args(1, 2, 3, 4, 5, 6, 7, 8);
  int j = func_9_args(1, 2, 3, 4, 5, 6, 7, 8, 9);

  return 0;
}
