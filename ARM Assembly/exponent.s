	 AREA     appcode, CODE, READONLY
     EXPORT __main
	 ENTRY 

;Program to calculate pow(e,x) 
;enable FP for Cortex M4 during project creation.
; VMOV	Floating-point Move Register
; VCMP	Compare two floating-point registers etct

__main  FUNCTION	
x SN 1 ; exponent of e stored in R1
result SN 3;result of calculation store in R3
count SN 5;counter variable
n SN 4 ;  no. of iterations
one SN 6 
temp SN 2 ; intermediate variable

	VMOV.F32 x,#3 ; Evaluate e^3
	VMOV.F32 n,#10 ; Sum upto 10 terms according to Taylor Series
	VMOV.F32 one,#1
	VMOV.F32 temp,#1
	VMOV.F32 count,#1
	VMOV.F32 result,#1
	
	
loop
	VCMP.F32 n,count;
	VMRS.F32 APSR_nzcv,FPSCR;To analyse FPSR
	BEQ stop
	VMUL.F32 temp,temp,x;temp = temp*x/i
	VDIV.F32 temp,temp,count
	VADD.F32 result,result,temp; result += temp
	VADD.F32 count,count,one;increase loop counter
	B loop
    
stop B stop ; stop program
     ENDFUNC
     END