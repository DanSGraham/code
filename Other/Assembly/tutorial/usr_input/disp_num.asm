section .data
    usrMsg db 'Enter a number: '    ;User Prompt
    lenUsrMsg equ $-usrMsg
    dispMsg db 'You entered: '      ;display message
    lenDispMsg equ $-dispMsg

section .bss
    num resb 5                      ;Unsure about this

section .text
    global _start

_start:
    ;Display user prompt
    mov eax, 4
    mov ebx, 1
    mov ecx, usrMsg
    mov edx, lenUsrMsg
    int 0x80
 
    ;Read and store input
    mov eax, 3
    mov ebx, 2
    mov ecx, num
    mov edx, 5                      ;5 bytes of input
    int 80h
    ;This is a fairly small buffer and not overflow protected. 
    ;How can I handle overflow? 
    
    ;Output the standard msg
    mov eax, 4
    mov ebx, 1
    mov ecx, dispMsg
    mov edx, lenDispMsg
    int 80h

    ;Output the user input
    mov eax, 4
    mov ebx, 1
    mov ecx, num
    mov edx, 5
    int 80h

    ;Exit
    mov eax, 1
    mov ebx, 0
    int 80h
