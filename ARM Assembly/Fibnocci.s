   PRESERVE8
     THUMB
     AREA     appcode, CODE, READONLY
     EXPORT __main
	 ENTRY 
__main  FUNCTION
;Fibonacci series --> 0,1,1,2,3,5,8,13 (First 5 terms)
;First two numbers are given by default
;Lets start by storing the numbers from the loaction pointed by R3
;In the end we can observe the value of r4 to be 13
	MOV R0, #0
	MOV R1, #1
	MOV R2, #5 ;Display first five fib numbers
	MOV R3, #0X20000000
	STR R0, [R3] ;Store '0'
	ADD R3, #0X4 ;Increment the address
	STR R1, [R3] ;Store '1'
	ADD R3, #0X4 ;Increment
	
fib CMP R2, #0 ;Loop for 5 times 
	ADD R4, R0, R1 ;(0+1=1) R4-->temp reg
	MOV R0, R1 ;Take control to the next element 
	MOV R1, R4
	STR R4, [R4]
	ADD R3, #0X4
	SUBGT R2, R2, #1 ;Decrement counter by 1
	BGT fib

stop B stop ; stop program
     ENDFUNC
     END