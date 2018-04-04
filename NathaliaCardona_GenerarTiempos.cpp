#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
//Se declaran las funciones y se especifica el tipo de funcion
int fibonacci(int N);
double get_time(int N);
//se crea la clase main
int main(){
  int N=35;
  for(int i=0;i<=N;i++){
    //retorna el N y el tiempo que le tomo calcular ese termino
    cout << i << " " << get_time(i) << endl;
  }

  return 0;
}
//Calcula el numero N de la serie de fibonacci y lo retorna
int fibonacci(int N){
  //se evaluan los dos casos base
  if(N=0){
    return 0;
  }
  if(N=1){
    return 1;
  }
  else{
    return fibonacci(N-1)+fibonacci(N-2);
  }
}
//calcula la cantidad de segundos que le toma calcular el termino n de fibonacci
double get_time(int N){
  //se inicia el cronometro
  clock_t t;
  t = clock();
  // SOME CODE THAT TAKES TIME
  //corre la funcion y cuando termina lo para y retorna el tiempo
  fibonacci(N);
  t = clock() - t;
  float time = ((float)t)/CLOCKS_PER_SEC;
  return time;
}
