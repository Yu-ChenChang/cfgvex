/*******************************************************
 * Copyright (C) 2016 Hui Peng <peng124@purdue.edu>
 *
 * This file is part of project.
 *
 * The source files from project can not be copied and/or
 * distributed without the express permission of Hui Peng
 *******************************************************/
#include <iostream>
#include <climits>

using namespace std;

int divide(int a, int b) {
  int ret;
  try {
    if (b == 0)
      throw 1000;
    ret = a/b;
  } catch (int e) {
    ret = INT_MAX;
  }

  return ret;
}

int main () {
  int ret = divide(100, 0);
  cout << "divide(100, 0) = " << ret << endl;
  return 0;
}
