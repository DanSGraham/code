	.file	"p1.c"
	.text
	.globl	fcn2
	.type	fcn2, @function
fcn2:
.LFB0:
	.cfi_startproc
	leal	(%rdi,%rsi), %eax
	ret
	.cfi_endproc
.LFE0:
	.size	fcn2, .-fcn2
	.globl	fcn1
	.type	fcn1, @function
fcn1:
.LFB1:
	.cfi_startproc
	addl	%esi, %edi
	addl	%r9d, %r8d
	leal	(%r8,%rdi), %eax
	addl	%edx, %esi
	imull	%esi, %eax
	addl	%edi, %eax
	subl	%ecx, %eax
	ret
	.cfi_endproc
.LFE1:
	.size	fcn1, .-fcn1
	.globl	main
	.type	main, @function
main:
.LFB2:
	.cfi_startproc
	movl	$261, %eax
	ret
	.cfi_endproc
.LFE2:
	.size	main, .-main
	.ident	"GCC: (Ubuntu 4.8.4-2ubuntu1~14.04) 4.8.4"
	.section	.note.GNU-stack,"",@progbits
