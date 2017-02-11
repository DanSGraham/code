	.file	"p1.c"
	.text
	.globl	fcn2
	.type	fcn2, @function
fcn2:
.LFB24:
	.cfi_startproc
	leal	(%rdi,%rsi), %eax
	ret
	.cfi_endproc
.LFE24:
	.size	fcn2, .-fcn2
	.globl	fcn1
	.type	fcn1, @function
fcn1:
.LFB25:
	.cfi_startproc
	addl	%esi, %edi
	addl	%r9d, %r8d
	leal	(%r8,%rdi), %eax
	addl	%esi, %edx
	imull	%edx, %eax
	addl	%edi, %eax
	subl	%ecx, %eax
	ret
	.cfi_endproc
.LFE25:
	.size	fcn1, .-fcn1
	.globl	main
	.type	main, @function
main:
.LFB26:
	.cfi_startproc
	movl	$261, %eax
	ret
	.cfi_endproc
.LFE26:
	.size	main, .-main
	.ident	"GCC: (Ubuntu 4.9.2-10ubuntu13) 4.9.2"
	.section	.note.GNU-stack,"",@progbits
