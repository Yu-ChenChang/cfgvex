# Issues

## An issue with radare2
** This is not an issue **
When radare2 opens an object file, the addresses of the functions are not from 0.
I have reported the problem to the developers([the starting VA address of object files](https://github.com/radare/radare2/issues/4525)).

It seems that in ELF, the starting addresses are encoded from 0 in each section, but r2 has mapped into one virtual memory address space.

And the addresses are not from 0.

But for function calls, there are *reloc* info, so we should be able to figure everything out.

## An issue with gcc(probably a bug) (Not a bug)
compile the (source code)[https://raw.githubusercontent.com/HexHive/mcsema/h.p/tests/src/c-func-test/indirect_call_test_2.c]

and compile it using the following command line
`gcc -m32 -O2 -c indirect_call_test_2.c -o indirect_call_test_2.o`

we can get an ELF file called `indirect_call_test_2.o`.

The issue is that:
If we get the size of function from readelf by reading the size of symbol `wrapper_0_args`,
we get 6.

    $readelf -s indirect_call_test_2.o
    ... others are skipped ...
     9: 00000000     6 FUNC    GLOBAL DEFAULT    1 wrapper_0_args
    10: 00000010    14 FUNC    GLOBAL DEFAULT    1 wrapper_1_args
    11: 00000020    22 FUNC    GLOBAL DEFAULT    1 wrapper_2_args
    12: 00000040    32 FUNC    GLOBAL DEFAULT    1 wrapper_3_args
    13: 00000060    40 FUNC    GLOBAL DEFAULT    1 wrapper_4_args
    14: 00000090    48 FUNC    GLOBAL DEFAULT    1 wrapper_5_args
    15: 000000c0    56 FUNC    GLOBAL DEFAULT    1 wrapper_6_args
    16: 00000100    64 FUNC    GLOBAL DEFAULT    1 wrapper_7_args
    17: 00000140    72 FUNC    GLOBAL DEFAULT    1 wrapper_8_args
    18: 00000190    80 FUNC    GLOBAL DEFAULT    1 wrapper_9_args

However, if we disassemble the ELF file, we can see that its size is bigger than 6:

    $objdump -d indirect_call_test_2.o
    00000000 <wrapper_0_args>:
    0:	8b 44 24 04          	mov    0x4(%esp),%eax
    4:	ff e0                	jmp    *%eax
    6:	8d 76 00             	lea    0x0(%esi),%esi
    9:	8d bc 27 00 00 00 00 	lea    0x0(%edi,%eiz,1),%edi
    .... others are skipped ...

(**Or does it mean that only the first 6 bytes belongs to the function, others are not?**)

This is the version information of my GCC

    $ gcc --version
    gcc (Ubuntu 4.9.3-5ubuntu1) 4.9.3
    Copyright (C) 2015 Free Software Foundation, Inc.
    This is free software; see the source for copying conditions.  There is NO
    warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
