int add(int a, int b, int c=4);


int add(int a, int b, int c) {
  return a + b + c;
}


int main () {
  int a = add(1, 2);

  int b = add(1, 2, 3);
}
