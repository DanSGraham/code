;My first Assembly program
;By Dan

section .text
    global _start    ;declared for linker

_start:
    mov edx, len     ;message length
    mov ecx, msg     ;message to write
    mov ebx, 1       ;file descriptor (stdout)
    mov eax, 4       ;system call number (sys_write)
    int 0x80         ;call kernel

    mov eax,1        ;system call number (sys_exit)
    int 0x80         ;call kernel

section .data
msg db 'Greetings, human.', 0xa    ;string to be printed
len equ $ - msg                    ; length of the string
