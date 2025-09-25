# program name: printInt
# purpose: read an integer from stdin using scanf and print it with printf
# target: ARMv7 (32-bit), hard-float ABI

.text
.global main

main:
    # save return to OS on stack and keep 8-byte alignment for variadic calls
    SUB     sp, sp, #8
    STR     lr, [sp, #4]

    # prompt for input
    LDR     r0, =prompt
    BL      printf

    # read integer: scanf("%d", &num)
    LDR     r0, =input
    LDR     r1, =num
    BL      scanf

    # print the integer: printf("Your Number Is %d \n", num)
    LDR     r0, =format
    LDR     r1, =num
    LDR     r1, [r1, #0]
    BL      printf

    # return to the OS (status 0)
    MOV     r0, #0
    LDR     lr, [sp, #4]
    ADD     sp, sp, #8
    MOV     pc, lr

.data
    # storage for the scanned integer (word-aligned)
    num:    .word 0

    # prompt shown to the user
    prompt: .asciz "Enter A Number\n"

    # scanf format string for integer
    input:  .asciz "%d"

    # printf format string
    format: .asciz "Your Number Is %d \n"
