#include <stdio.h>
#include <stdlib.h>

int main(void) {

	 char m[] = "attack at dawn";
	 char m2[] = "attack at dusk";

	 //char hexc[] = "6c73d5240a948c86981bc294814d";

	 char byteCipher[] = "\x6c\x73\xd5\x24\x0a\x94\x8c\x86\x98\x1b\xc2\x94\x81\x4d";   // convert the cipher from hex strings to bytes

	 char key[14];
	 int i = 0;		// allot ints for the indecies 
	 int k = 0;
	 char byteCipherPrime[14];

	 // xor the message text with the cipher text to derive the OTP
	 for (i=0; i < 14; i++) {
		 key[i] = m[i]^byteCipher[i];
	 }

	 // this will show the bytes of the  OTP
	 for (k=0; k < 14; k++) {
		 printf(" %02x", key[k]);
	 }

	 // xor the OTP with "attack at dusk" to discover what the cipher text for 
	 // the would be under the same OTP


	 for (k=0; k < 14; k++) {
	 	byteCipherPrime[k] = m2[k]^key[k];
	 }

	 printf("\n");
	 for (k=0; k < 14; k++) {
	 	printf(" %02x\n", byteCipherPrime[k]);
	 }



}


