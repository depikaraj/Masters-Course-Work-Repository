	PRESERVE8
     THUMB
     AREA	appcode, CODE, READONLY
     EXPORT __main
	 ENTRY 
__main  FUNCTION		 
	
		;This assembly pogram does enqeue for four times, followed by dequeue for two times and then enqueue until queue is full and then dequeues all
		;We can check the contents of the register while debugging during queue full and empty conditions.
        MOV r0, #-1 ; load initial value for front
		MOV r1, #-1 ; load initiaal value for rear
        MOV r2, #3 ; load intial valur for size of the circular queue after subtracting 1 size-1
		MOV r7, #0X20000000 ; start address of the queue
		MOV r4, #10 ; local variable
		SUB r6, r7, #4 ; storing the location of front 
		SUB r3, r7, #4 ; rear location
		MOV r8, #4 ;Counter variable for looping 
	
		
enqueue
	CMP r8,#0 ; If r8==0 queue is full
	BEQ dequeue
	SUB r10, r0, #1; r10 is temp variable to store front-1
	CMP r1, r10; Comparing rear with front-1
	BEQ full ; If rear=front-1 means queue is full
	CMP r0, #0; 
	BNE notfull
	CMP r1, r2
	BEQ full; If front=0 and rear=size-1 means queue is full
notfull
	CMP r0, #-1; If front==-1 make front=rear=0
	MOVEQ r0, #0 
	MOVEQ r1, #0
	MOVEQ r6, r7
	MOVEQ r3, r7
	BEQ store
	CMP r0, #0
	BEQ elsecase
	CMP r1, r2
	MOVEQ r1, #0
	MOVEQ r3, r7
	BEQ store
	BNE elsecase
full 
    MOV r12, #0x77777777;print Queue is full
	SUB r8, r8, #1
	B dequeue;goto end of enqueue function
elsecase
	ADD r1, r1, #1
	ADD r3, r3, #4
store
	MOV r12, #0x00000077 ; Just for debugging since Write permission is denied
	STR r4, [r3]
	ADD r4, r4, #10
	;ADD r3, r3, #4
	;ADD r1, r1, #1
	SUB r8, r8, #1
	B enqueue
dequeue
		CMP r8, #1
		BGT enqueue1
		CMP r0, #-1
		BEQ enqueue
		MOVEQ r12, #99 ;For dedugging if r12=99 then queue is empty
		
		;ADD r6, r6, #4 ; After dequeue increment the front pointer location by 4 
		CMP r0,r1
		MOVEQ r0,#-1
		MOVEQ r1,#-1
		BEQ zero
l
	    SUBEQ r6, r7, #4 ; Updating front location
		SUBEQ r3, r7, #4 ; Updating rear location
		CMP r0,r2
		MOVEQ r0,#0
		BEQ zero1
l1
		MOVEQ r6,r7 ;Updating front location to #20000000
		ADDNE r0, r0, #1
		MOV r9, #0
		STR r9, [r6] ;put zero in front location
		ADDNE r6, r6, #4; 
		ADD r8, r8, #1
		B dequeue
zero
		MOV r9, #0
		STR r9, [r6] ;put zero in front location
		B l
zero1
		MOV r9, #0
		STR r9, [r6] ;put zero in front location
		B l1
enqueue1
	CMP r8,#0 ; If r8==0 queue is full
	BEQ dequeue1
	SUB r10, r0, #1; r10 is temp variable to store front-1
	CMP r1, r10; Comparing rear with front-1
	BEQ full1 ; If rear=front-1 means queue is full
	CMP r0, #0; 
	BNE notfull1
	CMP r1, r2
	BEQ full1; If front=0 and rear=size-1 means queue is full
notfull1
	CMP r0, #-1; If front==-1 make front=rear=0
	MOVEQ r0, #0 
	MOVEQ r1, #0
	MOVEQ r6, r7
	MOVEQ r3, r7
	BEQ store1
	CMP r0, #0
	BEQ elsecase1
	CMP r1, r2
	MOVEQ r1, #0
	MOVEQ r3, r7
	BEQ store1
	BNE elsecase1
full1
    MOV r12, #0x77777777;print Queue is full
	SUB r8, r8, #1
	B dequeue1;goto end of enqueue function
elsecase1
	ADD r1, r1, #1
	ADD r3, r3, #4
store1
	MOV r12, #0x00000077 ; Just for debugging since Write permission is denied
	STR r4, [r3]
	ADD r4, r4, #10
	;ADD r3, r3, #4
	;ADD r1, r1, #1
	SUB r8, r8, #1
	B enqueue1
dequeue1
		CMP r8, #4
		BEQ stop
		CMP r0, #-1
		BEQ stop
		MOVEQ r12, #99 ;For dedugging if r12=99 then queue is empty
		
		;ADD r6, r6, #4 ; After dequeue increment the front pointer location by 4 
		CMP r0,r1
		MOVEQ r0,#-1
		MOVEQ r1,#-1
		BEQ zero2
l2
	    SUBEQ r6, r7, #4 ; Updating front location
		SUBEQ r3, r7, #4 ; Updating rear location
		CMP r0,r2; if front==size-1
		MOVEQ r0,#0
		BEQ zero3
l3
		MOVEQ r6,r7 ;Updating front location to #20000000
		ADDNE r0, r0, #1
		MOV r9, #0
		STR r9, [r6] ;put zero in front location
		ADDNE r6, r6, #4; 
		ADD r8, r8, #1
		B dequeue1
zero2
		MOV r9, #0
		STR r9, [r6] ;put zero in front location
		B l2
zero3
		MOV r9, #0
		STR r9, [r6] ;put zero in front location
		B l3
stop B stop ; stop program
     ENDFUNC
     END