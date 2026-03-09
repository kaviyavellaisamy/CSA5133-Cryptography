#include <stdio.h>
#include <string.h>

int main() {
char text[100];
char k1, k2, k3;
int choice, i;

printf("1. Encrypt\n2. Decrypt\nEnter choice: ");
scanf("%d",&choice);
getchar();

printf("Enter text: ");
fgets(text,100,stdin);

printf("Enter Key1: ");
scanf(" %c",&k1);
printf("Enter Key2: ");
scanf(" %c",&k2);
printf("Enter Key3: ");
scanf(" %c",&k3);

if(choice==1) {   // Encryption
    for(i=0;i<strlen(text);i++)
        text[i]=text[i]^k1^k2^k3;
    printf("Encrypted Text: %s",text);
}
else if(choice==2) {  // Decryption
    for(i=0;i<strlen(text);i++)
        text[i]=text[i]^k3^k2^k1;
    printf("Decrypted Text: %s",text);
}
else
    printf("Invalid choice");

return 0;

}

