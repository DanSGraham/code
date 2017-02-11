	.file	"p0.c"
	.text
	.globl	fcn0
	.type	fcn0, @function
fcn0:
.LFB24:
	.cfi_startproc
	leal	(%rdi,%rsi,2), %eax
	addl	%eax, %eax
	ret
	.cfi_endproc
.LFE24:
	.size	fcn0, .-fcn0
	.globl	main
	.type	main, @function
main:
.LFB25:
	.cfi_startproc
	movl	$3, %esi
	movl	$2, %edi
	call	fcn0
	rep ret
	.cfi_endproc
.LFE25:
	.size	main, .-main
	.ident	"GCC: (Ubuntu 4.9.2-10ubuntu13) 4.9.2"
	.section	.note.GNU-stack,"",@progbits
