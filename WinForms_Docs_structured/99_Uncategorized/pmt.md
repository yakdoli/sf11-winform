---
title: pmt.md
original_path: WinForms_Docs/99_Uncategorized/pmt.md
created_at: 2025-08-05
---








  









### PMT {#pmt style="tab-stops: 0pt"}

 

Calculates the payment for a loan based on constant payments and a constant interest rate.

 

**Syntax**

 

**PMT(rate, nper, pv, fv, type)**

 

where:

**rate** is the interest rate for the loan.

**nper** is the total number of payments for the loan.

**pv** is the present value or the total amount that a series of future payments is worth now; also known as the principal.

**fv** is the future value or a cash balance you want to attain after the last payment is made. If fv is omitted, it is assumed to be 0 (zero), that is, the future value of a loan is 0.

**type** is the number 0 (zero) or 1 and indicates when payments are due. If type equals:

[·      ]0 - payments are due at the end of the period

[·      ]1 - payments are due at the beginning of the period

[] 

Remarks[ ]

[] 

[·      ]The payment returned by PMT includes principal and interest but no taxes, reserve payments or fees sometimes associated with loans.

[·      ]Make sure that you are consistent about the units you use for specifying rate and nper. If you make monthly payments on a four-year loan at an annual interest rate of 12 percent, use 12%/12 for rate and 4\*12 for nper. If you make annual payments on the same loan, use 12 percent for rate and 4 for nper.

[]{#p169} 

[]{#related-topics}

