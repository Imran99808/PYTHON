#include<stdio.h>
#include<string.h>
int main()
{
    char a[100], b[100];
    gets(a);
    strcpy(b,a);
    puts(strrev(b));
    if (strcmp(a,b)==0){
    printf("Yes");
    }
    else{
    printf("No");
    }
    return 0;
}