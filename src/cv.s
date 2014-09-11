# as -arch x86_64 -o cv.o
# ld -e _main -arch x86_64 -o cv cv.o
.data
greet:
    .ascii "Hello, my name is Connor. If I do anything notable, it'll be listed below.\10\0"
greet_len:
    .long . - greet

.text
.globl _main
_main:
    movq $4, %rax  # SYS_write - OS X
    movq $1, %rdi  # stdout
    movq greet@GOTPCREL(%rip), %rsi
    syscall
    xorq %rax, %rax
    ret
