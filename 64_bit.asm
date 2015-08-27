section .text
	global _start

_start:
	mov rax, 1           
	mov rdi, 1            
	mov rsi, msg      
	mov rdx, leng   	                     
	syscall
	mov rax, 60            
	mov rdi, 0            
	syscall

section .data
	msg: db 'This is my first assm code !', 10
	leng: equ $-msg
