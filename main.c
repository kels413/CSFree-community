#include <stdio.h>



int main(void)
{
    int a = 5;
    int b = 5;


    if(a == b)
        printf("equals");
    else
        printf("not equal");

    
    printf("%p", &a);
    printf("%p", &b);


    return (0);
}