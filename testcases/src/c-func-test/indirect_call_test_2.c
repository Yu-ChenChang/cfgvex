/*******************************************************
 * Copyright (C) 2015 Hui Peng <peng124@purdue.edu>
 *
 * This file is part of {project}.
 *
 * {project} can not be copied and/or distributed without
 * the express permission of Hui Peng
 *******************************************************/

int wrapper_0_args(int (*fc)()) {
  int ret = fc();
  return ret;
}

int wrapper_1_args(int (*fc)(int), int a) {
  int ret = fc(a);
  return ret;
}

int wrapper_2_args(int (*fc)(int, int), int a, int b) {
  int ret = fc(a, b);
  return ret;
}

int wrapper_3_args(int (*fc)(int, int, int), int a, int b, int c) {
  int ret = fc(a, b, c);
  return ret;
}

int wrapper_4_args(int (*fc)(int, int, int, int), int a, int b, int c, int d) {
  int ret = fc(a, b, c, d);
  return ret;
}

int wrapper_5_args(int (*fc)(int, int, int, int, int), int a, int b, int c, int d, int e) {
  int ret = fc(a, b, c, d, e);
  return ret;
}

int wrapper_6_args(int (*fc)(int, int, int, int, int, int), int a, int b, int c, int d, int e, int f) {
  int ret = fc(a, b, c, d, e, f);
  return ret;
}

int wrapper_7_args(int (*fc)(int, int, int, int, int, int, int), int a, int b, int c, int d, int e, int f, int g) {
  int ret = fc(a, b, c, d, e, f, g);
  return ret;
}

int wrapper_8_args(int (*fc)(int, int, int, int, int, int, int, int), int a, int b, int c, int d, int e, int f, int g, int h) {
  int ret = fc(a, b, c, d, e, f, g, h);
  return ret;
}

int wrapper_9_args(int (*fc)(int, int, int, int, int, int, int, int, int), int a, int b, int c, int d, int e, int f, int g, int h, int i) {
  int ret = fc(a, b, c, d, e, f, g, h, i);
  return ret;
}
