   PRESERVE8
     THUMB
     AREA     appcode, CODE, READONLY
     EXPORT __main
	 ENTRY 
__main  FUNCTION
	
a RN r0
b RN r1

	MOV a, #60
	MOV b, #12
	
gcd
	CMP a, b ;Compare the numbers if(a==b) base case, we do nothing
	BEQ stop
	SUBGT a,a,b ;If a is greater than b we do a=a-b
	SUBLE b,b,a ;IF b is greater than a we do b=b-a
	B gcd
	;ro or r1 will have the value of GCD.

stop B stop ; stop program
     ENDFUNC
     END
