# MISRA compliance

All MCUXpresso SDK drivers comply to MISRA 2012 rules with exceptions in [Table 1](misra_compliance.md#NEWIDTABLE).

|Exception rules

|Description

|
|-----------------|-------------|
|Directive 4.​4

|Sections of code should not be commented out.​

|
|Directive 4.​5

|Identifiers in the same namespace with overlapping visibility should be typographically unambiguous.​

|
|Directive 4.​6

|Typedefs that indicate size and signedness should be used in place of the basic numerical types.​

|
|Directive 4.​8

|If a pointer to a structure or union is never dereferenced within a translation unit, then the implementation of the object should be hidden.​

|
|Directive 4.​9

|A function should be used in preference to a function-​like macro where they are interchangeable.​

|
|Directive 4.​13

|Functions which are designed to provide operations on a resource should be called in an appropriate sequence.​

|
|Rule 1.​2

|Language extensions should not be used.​

|
|Rule 2.​3

|A project should not contain unused type declarations.​

|
|Rule 2.​4

|A project should not contain unused tag declarations.​

|
|Rule 2.​5

|A project should not contain unused macro declarations.​

|
|Rule 2.​6

|A function should not contain unused label declarations.​

|
|Rule 2.​7

|There should be no unused parameters in functions.​

|
|Rule 4.​2

|Trigraphs should not be used.​

|
|Rule 5.​1

|External identifiers shall be distinct.​

|
|Rule 5.​4

|Macro identifiers shall be distinct.​

|
|Rule 5.​9

|Identifiers that define objects or functions with internal linkage should be unique.​

|
|Rule 8.​7

|Functions and objects should not be defined with external linkage if they are referenced in only one translation unit.​

|
|Rule 8.​9

|An object should be defined at block scope if its identifier only appears in a single function.​

|
|Rule 8.​11

|When an array with external linkage is declared, its size should be explicitly specified.​

|
|Rule 8.​13

|A pointer should point to a const-​qualified type whenever possible.​

|
|Rule 10.​5

|The value of an expression should not be cast to an inappropriate essential type.​

|
|Rule 11.​4

|A conversion should not be performed between a pointer to object and an integer type.​

|
|Rule 11.​5

|A conversion should not be performed from pointer to void into pointer to object.​

|
|Rule 12.​1

|The precedence of operators within expressions should be made explicit.​

|
|Rule 12.​3

|The comma operator should not be used.​

|
|Rule 12.​4

|Evaluation of constant expressions should not lead to unsigned integer wrap-​around.​

|
|Rule 13.​3

|A full expression containing an increment \(++\) or decrement \(–\) operator should have no other potential side effects other than that caused by the increment or decrement operator.​

|
|Rule 15.​4

|There should be no more than one break or go to statement used to terminate any iteration statement.​

|
|Rule 17.​5

|The function argument corresponding to a parameter declared to have an array type shall have an appropriate number of elements.​

|
|Rule 17.​8

|A function parameter should not be modified.​

|
|Rule 19.​2

|The union keyword should not be used.​

|
|Rule 20.​1

|\#include directives should only be preceded by preprocessor directives or comments.​

|
|Rule 20.​10

|The \# and \#\# preprocessor operators should not be used.​

|
|Rule 21.​1

|\#define and \#undef shall not be used on a reserved identifier or reserved macro name.​

|
|Rule 21.​2

|A reserved identifier or macro name shall not be declared.​

|
|Rule 21.​12

|The exception handling features of <fenv.​h\> should not be used.​

|

