---
title: pv.md
original_path: WinForms_Docs/99_Uncategorized/pv.md
created_at: 2025-08-05
---








  









### PV {#pv style="tab-stops: 0pt"}

 

Returns the present value of an investment. The present value is the total amount that a series of future payments is worth now.

 

**Syntax**

 

**PV(rate, nper, pmt, fv, type)**

 

where:

**rate** is the interest rate per period. For example, if you obtain an automobile loan at a 10% annual interest rate and make monthly payments, your interest rate per month is 10%/12 or 0.83%. You would enter 10%/12 or 0.83% or 0.0083, into the formula as the rate.

**nper** is the total number of payment periods in an annuity. For example, if you get a four-year car loan and make monthly payments, your loan has 4\*12 (or 48) periods. You would enter 48 into the formula for nper.

**pmt** is the payment made for each period and cannot change over the life of the annuity. Typically, pmt includes principal and interest but, no other fees or taxes. For example, the monthly payments on a \$10,000, four-year car loan at 12 percent are \$263.33. You will have to enter -263.33 into the formula as the pmt. If pmt is omitted, you must include the fv argument.

**fv** is the future value or a cash balance that you want to attain after the last payment is made. If fv is omitted, it is assumed to be 0 (the future value of a loan, for example, is 0). For example, if you want to save \$50,000 to pay for a special project in 18 years, then \$50,000 is the future value. You could then make a conservative guess at an interest rate and determine how much you must save each month. If fv is omitted, you must include the pmt argument.

**type** is the number 0 or 1 and indicates when payments are due. If type equals:

[·      ]0 - Payments are due at the end of the period.

[·      ]1 - Payments are due at the beginning of the period.

[\
]Remarks[ ]

[] 

[·      ]Make sure that you are consistent about the units you use for specifying rate and nper. If you make monthly payments on a four-year loan at 12 percent annual interest, use 12%/12 for rate and 4\*12 for nper. If you make annual payments on the same loan, use 12% for rate and 4 for nper.

[·      ]In annuity functions, the cash you pay out such as a deposit to savings is represented by a negative number; the cash you receive such as a dividend check is represented by a positive number.

[·      ]One financial argument is solved for in terms of the others. If rate is not 0, then,

[] 

{border="0"}

 

If rate is 0:

 

**(pmt \* nper) + pv + fv = 0**

 

[]{#related-topics}

