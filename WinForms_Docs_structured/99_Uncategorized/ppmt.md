---
title: ppmt.md
original_path: WinForms_Docs/99_Uncategorized/ppmt.md
created_at: 2025-08-05
---








  









### PPMT {#ppmt style="tab-stops: 0pt"}

[] 

Returns the payment on the principal for a given period, for an investment based on periodic, constant payments and a constant interest rate.

 

**Syntax**

 

**PPMT(rate, per, nper, pv, fv, type)**

 

where:

**rate**[ ]is the interest rate per period.

**per**[ ]specifies the period and must be in the range of 1 to nper.

**nper[ ]**is the total number of payment periods in an annuity.

**pv** is the present value--- the total amount that a series of future payments is worth now.

**fv** is the future value or a cash balance that you may want to attain after the last payment is made. If fv is omitted, it is assumed to be 0 (zero), that is, the future value of a loan is 0.

**type**[ ]is the number 0 or 1 and indicates when payments are due. If type equals:

[·      ]0 - Payments are due at the end of the period.

[·      ]1 - Payments are due at the beginning of the period.

[\
\
]**[]**

Remarks

[] 

[·      ]Make sure that you are consistent about the units you use for specifying rate and nper. If you make monthly payments on a four-year loan at 12 percent annual interest, use 12%/12 for rate and 4\*12 for nper. If you make annual payments on the same loan, use 12% for rate and 4 for nper.

[]{#p172} 

 

[]{#related-topics}

