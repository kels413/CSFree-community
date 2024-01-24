#include <stdio.h>

#define CSFree main 


int CSFree(void)
{
    int num1 = 10;
    int num2 = 10;

 

    printf("%p\n", &num1);

    printf("%p\n", &num2);
    return 0;
}