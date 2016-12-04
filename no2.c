#include <stdio.h>
static long n = 10;

int main ( int argc, char **argv ) {
  long long sum = 0;
  long long r = 0;
  long long p1 = 1;
  long long p2 = 2;

  while(r < n-3) {
      if (r % 2 == 0) {
          sum += r;
      }
      r = p1 + p2;
      p1 = p2;
      p2 = r;
  }

  printf("%lld\n", sum);
}
