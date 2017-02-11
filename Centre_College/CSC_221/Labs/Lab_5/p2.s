	.file	"p2.c"
	.text
	.globl	fcn4
	.type	fcn4, @function
fcn4:
.LFB24:
	.cfi_startproc
	testl	%edi, %edi
	js	.L4
	movl	$0, %edx
	movl	$0, %eax
.L3:
	addl	%edx, %eax
	addl	$1, %edx
	cmpl	%edx, %edi
	jge	.L3
	rep ret
.L4:
	movl	$0, %eax
	ret
	.cfi_endproc
.LFE24:
	.size	fcn4, .-fcn4
	.globl	main
	.type	main, @function
main:
.LFB25:
	.cfi_startproc
	movl	$10, %edi
	call	fcn4
	rep ret
	.cfi_endproc
.LFE25:
	.size	main, .-main
	.ident	"GCC: (Ubuntu 4.9.2-10ubuntu13) 4.9.2"
	.section	.note.GNU-stack,"",@progbits
