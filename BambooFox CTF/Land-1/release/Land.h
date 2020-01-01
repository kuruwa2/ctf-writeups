#ifndef _LAND_H_
#define _LAND_H_
#include <stdio.h>
#include <stdlib.h>

typedef struct rectangle{
	int a,b,c,d;
}rectangle;

rectangle find_rectangle();

long long area(int x1, int y1, int x2, int y2);

#endif
