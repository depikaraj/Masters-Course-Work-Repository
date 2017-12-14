   PRESERVE8
     THUMB
     AREA     appcode, CODE, READONLY
     EXPORT __main
	 ENTRY 
__main  FUNCTION
	
a RN r0
b RN r1
c RN r2
	MOV a, #3
	MOV b, #4
	MOV c, #5
	CMP a, b ;Compare first two numbers if(a>b)
	BGT b1   ;If greater branch to b1
	BLE b2	 ;If lesser branch to b2
b1
	CMP a,c ;Compare a and c if(a>c)
	ITE GT
	MOVGT r3,a  ;a is the greatest
	MOVLE r3,c  ;c is the greatest
	B stop
b2
	CMP b,c ;Compare b and c if(b>c)
	ITE GT
	MOVGT r3,b ;b is the greatest
	MOVLE r3,c ;c is the greatest
	B stop

stop B stop ; stop program
     ENDFUNC
     END