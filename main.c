#include <stdio.h>



int main(void)
{
    int a = 5;
    int b = 5;


    if(a == b)
        printf("equals\n");
    else
        printf("not equal\n");

    
    printf("%p\n", &a);
    printf("%p\n", &b);


    return (0);
}