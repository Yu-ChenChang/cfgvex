/*******************************************************
 * Copyright (C) 2015 Hui Peng <peng124@purdue.edu>
 *
 * This file is part of {project}.
 *
 * {project} can not be copied and/or distributed without
 * the express permission of Hui Peng
 *******************************************************/
#include <stdio.h>
#include <string.h>

// bubble sorting algo
void mysort(void *base, int num, int size, int (*compare)(const void *, const void *))
{
  char buf[size];
  int i,j;

  for (i = 0; i < num; i++) {
    for (j = 1; j < num - i; j++) {
      if (compare(base + (j-1) * size, base + j * size) > 0) {
        // do the swap by memcpy
        memcpy(buf, base + (j-1) * size, size);
        memcpy(base + (j-1) * size, base + j * size, size);
        memcpy(base + j * size, buf, size);
      }
    }
  }
}

int int_cmp(const void *a, const void *b) {
  if (*(int *)a > *(int *)b)
    return 1;
  return 0;
}

int float_cmp(const void *a, const void *b) {
  if (*(float *)a > *(float *)b)
    return 1;
  return 0;
}

#define ARR_SIZE 10
int main(void) {
  int i;
  int int_array[] = {9, 8, 7, 6, 5, 4, 3, 2, 1, 0};
  float float_array[] = {9.0, 8.0, 7.0, 6.0, 5.0, 4.0, 3.0, 2.0, 1.0, 0.0};

  mysort(int_array, ARR_SIZE, sizeof(int), int_cmp);
  mysort(float_array, ARR_SIZE, sizeof(float), float_cmp);

  for (i = 0; i < ARR_SIZE; i++) {
    printf("%d ", int_array[i]);
  }
  printf("\n");

  for (i = 0; i < ARR_SIZE; i++) {
    printf("%f ", float_array[i]);
  }
  printf("\n");

  return 0;
}
