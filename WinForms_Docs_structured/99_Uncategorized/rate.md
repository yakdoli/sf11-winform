---
title: rate.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\rate.md
created_at: 2025-07-03
---








  









### RATE {#rate style="tab-stops: 0pt"}

 

Returns the interest rate per period of an annuity. RATE is calculated by iteration and may not converge to a unique solution.

 

**Syntax**

 

**RATE(nper, pmt, pv, fv, type, guess)**

 

where:

**nper** is the total number of payment periods in an annuity.

**pmt** is the payment made for each period and cannot change over the life of the annuity. Typically, pmt includes  the principal and interest but, no other fees or taxes. If pmt is omitted, you must include the fv argument.

**pv** is the present value--- the total amount that a series of future payments is worth now.

**fv** is the future value or a cash balance that you want to attain after the last payment is made. If fv is omitted, it is assumed to be 0 (the future value of a loan, for example, is 0).

**type** is the number 0 or 1 and indicates when payments are due. If type equals:

[·      ]0 - Payments are due at the end of the period.

[·      ]1 - Payments are due at the beginning of the period.

**guess** is your guess for what the rate will be. If you omit guess, it is assumed to be 10 percent. If RATE does not converge, try different values for guess. RATE usually converges if guess is between 0 and 1.

 

[]{#related-topics}

