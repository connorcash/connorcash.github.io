# to build and link on OS X:
# as -arch x86_64 -o cv.o cv.s
# ld -arch x86_64 -lSystem -o cv cv.o

.cstring
greet:
    .ascii "Hello, my name is Connor. I love reversing!\n\n"

.text
.globl _main
_main:
    subq $8, %rsp
    leaq greet(%rip), %rdi
    call _printf
    addq $8, %rsp
    ret
