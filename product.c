#include <stdio.h>
#include <string.h>
struct product{
    int id;
    char name[20];
    float price;
};
int main(){
    int n;
    scanf("%d",&n);
    struct product p[n], temp;
    for(int i=0;i<n;i++)
        scanf("%d%s%f",&p[i].id,p[i].name,&p[i].price);
    for(int i=0;i<n-1;i++){
        for(int j=i+1;j<n;j++){
            if(p[i].price > p[j].price){
                temp=p[i];
                p[i]=p[j];
                p[j]=temp;
            }
        }
    }
    for(int i=0;i<n;i++)
        printf("%d %s %.2f\n",p[i].id,p[i].name,p[i].price);
    return 0;
}