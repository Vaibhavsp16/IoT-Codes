#include <stdio.h>
#include <string.h>
struct hotel{
    char name[20];
    char address[30];
    int grade;
    int rooms;
    float charge;
};
void display_charge(struct hotel h[],int n,float x){
    for(int i=0;i<n;i++)
        if(h[i].charge < x)
            printf("%s\n",h[i].name);
}
void display_grade(struct hotel h[],int n,int g){
    for(int i=0;i<n;i++)
        if(h[i].grade==g)
            printf("%s\n",h[i].name);
}
int main(){
    int n;
    scanf("%d",&n);
    struct hotel h[n];
    for(int i=0;i<n;i++)
        scanf("%s%s%d%d%f",h[i].name,h[i].address,&h[i].grade,&h[i].rooms,&h[i].charge);
    float x;
    int g;
    scanf("%f%d",&x,&g);
    display_charge(h,n,x);
    display_grade(h,n,g);
    return 0;
}