/*******************************************************
 * Copyright (C) 2015 Hui Peng <peng124@purdue.edu>
 *
 * This file is part of {project}.
 *
 * {project} can not be copied and/or distributed without
 * the express permission of Hui Peng
 *******************************************************/

// http://david.wragg.org/blog/2014/02/c-tail-calls-1.html

int ackermann(int m, int n) {
  if (m == 0)
    return n + 1;
  if (n == 0)
    return ackermann(m - 1, 1);
  return ackermann(m - 1, ackermann(m, n - 1));
}


int factorial(int i) {
  if (i == 0)
    return 1;
  return i * factorial(i - 1);
}

int test_func(int i, int j) {
  if (i > 2 || i < 0)
    return 0;
  if (i == 0)
    return factorial(j);
  return ackermann(0, j);
}
