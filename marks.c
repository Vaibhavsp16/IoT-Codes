#include <stdio.h>
struct student{
    int m1,m2,m3,total;
};
int main(){
    struct student s;
    scanf("%d%d%d",&s.m1,&s.m2,&s.m3);
    s.total = s.m1 + s.m2 + s.m3;
    if(s.total>=150) printf("Pass %d",s.total);
    else printf("Fail %d",s.total);
    return 0;
}