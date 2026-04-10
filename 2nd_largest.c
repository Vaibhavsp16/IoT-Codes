#include <stdio.h>
int main(){
    int n;
    scanf("%d",&n);
    int a[n], *p[n];
    for(int i=0;i<n;i++){
        scanf("%d",&a[i]);
        p[i]=&a[i];
    }
    int max=*p[0], min=*p[0];
    for(int i=1;i<n;i++){
        if(*p[i]>max) max=*p[i];
        if(*p[i]<min) min=*p[i];
    }
    printf("%d", max-min);
    return 0;
}