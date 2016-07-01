/*******************************************************
 * Copyright (C) 2016 Hui Peng <peng124@purdue.edu>
 *
 * This file is part of HexHive.
 *
 * The source files from HexHive can not be copied and/or
 * distributed without the express permission of Hui Peng
 *******************************************************/
#include <iostream>
using namespace std;

class Animal
{
private:
  int age;
public:
  Animal();
  virtual void info();
  void setAge(int age) {this->age = age;}
  virtual ~Animal();
};

Animal::Animal() {
  this->age = 0;
}

void Animal::info() {
  cout << "age:" << this->age << endl;
}

Animal::~Animal() { 
}

class Dog:public Animal
{
private:
  int spec;
public:
  Dog();
  void setSpec(int spec) {
    this->spec = spec;
  }

  void info();
  virtual ~Dog();
};

Dog::Dog() {
  this->spec = 0;
}

void Dog::info() {
  cout << "spec:" << spec << endl;
}

Dog::~Dog() {

}

class Cat:public Animal
{
private:
  int from;
public:
  Cat();
  void setFrom(int from) {
    this->from = from;
  }
  void info();
  virtual ~Cat();
};

Cat::Cat() {
  this->from = 0;
}

void Cat::info() {
  cout << "from:" << from << endl;
}

Cat::~Cat() {

}

class AsianCat:public Cat
{
public:
  AsianCat();
  void info();
  virtual ~AsianCat();
};

AsianCat::AsianCat() {

}

void AsianCat::info(){
  cout << "AsianCat" << endl;
}

AsianCat::~AsianCat() {

}

static Animal animal;
static Dog dog;
static Cat cat;
static AsianCat asianCat;
int main(int argc, char *argv[])
{
  animal.setAge(10);
  animal.info();

  dog.setSpec(20);
  dog.info();

  cat.setFrom(30);
  cat.info();

  asianCat.info();
  
  Animal *animals[4] = {&animal, &dog, &cat, &asianCat};
  for (int i = 0; i < 4; i++) {
    animals[i]->info();
  }

  
  return 0;
}




