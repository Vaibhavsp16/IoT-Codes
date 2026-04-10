#include <stdio.h>
struct book{
    char title[30];
    char author[30];
    float price;
};
void calc(struct book b,float d){
    float final = b.price - (b.price * d / 100);
    printf("%.2f",final);
}
int main(){
    struct book b;
    float d;
    scanf("%s%s%f",&b.title,b.author,&b.price);
    scanf("%f",&d);
    calc(b,d);
    return 0;
}