# program name: helloWorld
# author: daniel daum
# date: 11 sep 2025
# purpose: a program to show how to print a string using the c function printf

.text 
.global main 

main: 
    # save return to OS on stack
    SUB sp, sp, #4 
    STR lr, [sp, #0] 

    # printing the message
    LDR r0, =helloWorld
    BL printf
    
    # return to the OS
    LDR lr, [sp, #0] 
    ADD sp, sp, #4 
    MOV pc, lr 
    
.data
    # stores the string to be printed
    helloWorld: .asciz "Hello World!\n"