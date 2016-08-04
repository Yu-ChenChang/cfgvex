/*******************************************************
 * Copyright (C) 2015 Hui Peng <peng124@purdue.edu>
 *
 * This file is part of {project}.
 *
 * {project} can not be copied and/or distributed without
 * the express permission of Hui Peng
 *******************************************************/
#include <stdio.h>

int func_int_int_args(int a, int b) {
	return a + b;
}

int func_int_char_intptr_args(int a, char b, int* c) {
	char t2 = b;
	int* t3 = c;
	return a;
}

int main(int argc, char *argv[])
{
  int a = func_int_int_args(1,2);
  int b = func_int_char_intptr_args(1,'x',&a);

  return 0;
}
