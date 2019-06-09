#include <iostream>
#include <ctime>
#include <cstdlib>
using namespace std;

int main(){
  srand(time(0));
  int i=0;
  while (i<6){
    cout << rand() << endl;
    cout << RAND_MAX ;
    ++i;
  }
}
