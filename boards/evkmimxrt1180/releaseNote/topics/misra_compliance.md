# MISRA compliance {#GUID-4021200A-89CC-48DE-AD64-EC041A3F6FDA}

All MCUXpresso SDK drivers comply to MISRA 2012 rules with exceptions in [Table 1](misra_compliance.md#TABLE_MISRA).

<table id="TABLE_MISRA"><thead><tr><th>

Exception rules

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Directive 4.4

</td><td>

Sections of code should not be commented out.

</td></tr><tr><td>

Directive 4.5

</td><td>

Identifiers in the same name space with overlapping visibility should be typographically unambiguous.

</td></tr><tr><td>

Directive 4.6

</td><td>

Typedefs that indicate size and signedness should be used in place of the basic numerical types.

</td></tr><tr><td>

Directive 4.8

</td><td>

If a pointer to a structure or union is never dereferenced within a translation unit, then the implementation of the object should be hidden.

</td></tr><tr><td>

Directive 4.9

</td><td>

A function should be used in preference to a function-like macro where they are interchangeable.

</td></tr><tr><td>

Directive 4.13

</td><td>

Functions which are designed to provide operations on a resource should be called in an appropriate sequence.

</td></tr><tr><td>

Rule 1.2

</td><td>

Language extensions should not be used.

</td></tr><tr><td>

Rule 2.3

</td><td>

A project should not contain unused type declarations.

</td></tr><tr><td>

Rule 2.4

</td><td>

A project should not contain unused tag declarations.

</td></tr><tr><td>

Rule 2.5

</td><td>

A project should not contain unused macro declarations.

</td></tr><tr><td>

Rule 2.6

</td><td>

A function should not contain unused label declarations.

</td></tr><tr><td>

Rule 2.7

</td><td>

There should be no unused parameters in functions.

</td></tr><tr><td>

Rule 4.2

</td><td>

Trigraphs should not be used.

</td></tr><tr><td>

Rule 5.1

</td><td>

External identifiers shall be distinct.

</td></tr><tr><td>

Rule 5.4

</td><td>

Macro identifiers shall be distinct.

</td></tr><tr><td>

Rule 5.9

</td><td>

Identifiers that define objects or functions with internal linkage should be unique.

</td></tr><tr><td>

Rule 8.7

</td><td>

Functions and objects should not be defined with external linkage if they are referenced in only one translation unit.

</td></tr><tr><td>

Rule 8.9

</td><td>

An object should be defined at block scope if its identifier only appears in a single function.

</td></tr><tr><td>

Rule 8.11

</td><td>

When an array with external linkage is declared, its size should be explicitly specified.

</td></tr><tr><td>

Rule 8.13

</td><td>

A pointer should point to a const-qualified type whenever possible.

</td></tr><tr><td>

Rule 10.5

</td><td>

The value of an expression should not be cast to an inappropriate essential type.

</td></tr><tr><td>

Rule 11.4

</td><td>

A conversion should not be performed between a pointer to object and an integer type.

</td></tr><tr><td>

Rule 11.5

</td><td>

A conversion should not be performed from pointer to void into pointer to object.

</td></tr><tr><td>

Rule 12.1

</td><td>

The precedence of operators within expressions should be made explicit.

</td></tr><tr><td>

Rule 12.3

</td><td>

The comma operator should not be used.

</td></tr><tr><td>

Rule 12.4

</td><td>

Evaluation of constant expressions should not lead to unsigned integer wrap-around.

</td></tr><tr><td>

Rule 13.3

</td><td>

A full expression containing an increment \(++\) or decrement \(–\) operator should have no other potential side effects other than that caused by the increment or decrement operator.

</td></tr><tr><td>

Rule 15.4

</td><td>

There should be no more than one break or go to statement used to terminate any iteration statement.

</td></tr><tr><td>

Rule 17.5

</td><td>

The function argument corresponding to a parameter declared to have an array type shall have an appropriate number of elements.

</td></tr><tr><td>

Rule 17.8

</td><td>

A function parameter should not be modified.

</td></tr><tr><td>

Rule 19.2

</td><td>

The union keyword should not be used.

</td></tr><tr><td>

Rule 19.2

</td><td>

The union keyword should not be used.

</td></tr><tr><td>

Rule 20.10

</td><td>

The \# and \#\# preprocessor operators should not be used.

</td></tr><tr><td>

Rule 21.1

</td><td>

\#define and \#undef shall not be used on a reserved identifier or reserved macro name.

</td></tr><tr><td>

Rule 21.2

</td><td>

A reserved identifier or macro name shall not be declared.

</td></tr><tr><td>

Rule 21.12

</td><td>

The exception handling features of &lt;fenv.h&gt; should not be used.

</td></tr></tbody>
</table>