section .text
	global _start

_start:
	mov eax, 4           
	mov ebx, 1            
	mov ecx, msg        
	mov edx, leng   	                     
	int 80h
	mov eax, 1            
	mov ebx, 0            
	int 80h

section .data
	msg: db 'This is my first assm code !', 10
	leng: equ $-msg
