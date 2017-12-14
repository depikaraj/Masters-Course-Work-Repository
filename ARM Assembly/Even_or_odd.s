   PRESERVE8
     THUMB
     AREA     appcode, CODE, READONLY
     EXPORT __main
	 ENTRY 
__main  FUNCTION
;Check if a number id even or odd using modulus operator
;UDIV r0,r1,r2 ---> r0=r1/r2 
;MLS  r0,r0,r2,r1 ----> r0=r1-r0*r2
input RN r0
two RN r1

	MOV input, #7
	MOV two, #2 
	UDIV r2, input, two
	MLS r2, r2, two, input ;Modulus
	CMP r2, #0
	ITE EQ
	MOVEQ r3, #0 ;If r3=0 then number is even
	MOVNE r3, #1 ;If r3=1 then number is odd

stop B stop ; stop program
     ENDFUNC
     END