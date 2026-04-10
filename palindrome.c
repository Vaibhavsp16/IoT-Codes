#include <stdio.h>
int rev(int n,int r){
    if(n==0) return r;
    return rev(n/10, r*10 + n%10);
}
int main(){
    int n;
    scanf("%d",&n);
    if(n==rev(n,0)) printf("Palindrome");
    else printf("Not Palindrome");
    return 0;
}