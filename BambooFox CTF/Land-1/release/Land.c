#include "Land.h"

//----do not modify above----
int findx1(int x1, int x2, long long total) {
	if (x2 - x1 == 1) {
		if (area(x1, 0, 1000000000, 1000000000) == total)
			return x1;
		else
		  return x2;
	}
	int mid = (x1 + x2) / 2;
	long long area1 = area(mid, 0, 1000000000, 1000000000);
	if (area1 == total)
		return findx1(mid, x2, total);
	else
		return findx1(x1, mid, total);
}
int findx2(int x1, int x2, long long total) {
	if (x2 - x1 == 1) {
		if (area(0, 0, x2, 1000000000) == total)
			return x2;
		else
		  return x1;
	}
	int mid = (x1 + x2) / 2;
	long long area1 = area(0, 0, mid, 1000000000);
	if (area1 == total)
		return findx2(x1, mid, total);
	else
		return findx2(mid, x2, total);
}
int findy1(int x1, int x2, long long total) {
	if (x2 - x1 == 1) {
		if (area(0, x1, 1000000000, 1000000000) == total)
			return x1;
		else
		  return x2;
	}
	int mid = (x1 + x2) / 2;
	long long area1 = area(0, mid, 1000000000, 1000000000);
	if (area1 == total)
		return findy1(mid, x2, total);
	else
		return findy1(x1, mid, total);
}
int findy2(int x1, int x2, long long total) {
	if (x2 - x1 == 1) {
		if (area(0, 0, 1000000000, x2) == total)
			return x2;
		else
		  return x1;
	}
	int mid = (x1 + x2) / 2;
	long long area1 = area(0, 0, 1000000000, mid);
	if (area1 == total)
		return findy2(x1, mid, total);
	else
		return findy2(mid, x2, total);
}
rectangle find_rectangle(int subtask){
	rectangle answer;
	int x1=0;
	int x2=1000000000;
	int y1=0;
	int y2=1000000000;
	long long total = area(x1, y1, x2, y2);
	x1 = findx1(x1, x2, total);
	x2 = findx2(0, x2, total);
	y1 = findy1(y1, y2, total);
	y2 = findy2(0, y2, total);
	answer.a=x1,answer.b=y1,answer.c=x2,answer.d=y2;
	return answer;
}

//----do not modify below----

#ifndef EVAL
const int _MAX_C = 1000000000;
const int _MAX_NUM_QUERY = 128;
int _count=0,_a,_b,_c,_d;
int _valid(int x){
	if(x<0||x>_MAX_C) return 0;
	return 1;
}
int _max(int a,int b){
	if(a>b) return a;
	return b;
}
int _min(int a,int b){
	if(a<b) return a;
	return b;
}
void _input(int *x){
	scanf("%d",x);
}
void _wrong_answer(const char *MSG) {
	printf("Wrong Answer: %s\n", MSG);
	exit(0);
}
void _Accepted(const int c){
	printf("Accepted: %d\n",c);
}

long long area(int x1, int y1, int x2, int y2){
	++_count;
	if(_count>_MAX_NUM_QUERY)
		_wrong_answer("too many queries");
	if(!_valid(x1)||!_valid(x2)||!_valid(y1)||!_valid(y2))
		_wrong_answer("invalid query1");
	if(!(x1<x2&&y1<y2))
		_wrong_answer("invalid query2");
	int ml=_max(x1,_a),mr=_min(x2,_c);
	int md=_max(y1,_b),mu=_min(y2,_d);
	if(ml>=mr||md>=mu) return 0;
	return (long long)(mr-ml)*(long long)(mu-md);
}

int main() {
	int t,mx=0,subtask=0;
	rectangle tmp;
	_input(&t),_input(&subtask);
	while(t--){
		_count=0;
		_input(&_a),_input(&_b),_input(&_c),_input(&_d);
		tmp=find_rectangle(subtask);
		if(tmp.a!=_a||tmp.b!=_b||tmp.c!=_c||tmp.d!=_d)
			_wrong_answer("incorrect place");
		else
			mx=_max(mx,_count);
	}
	_Accepted(mx);
}
#endif
