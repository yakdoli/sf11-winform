---
title: ispmt.md
original_path: WinForms_Docs/99_Uncategorized/ispmt.md
created_at: 2025-08-05
---








  









### ISPMT {#ispmt style="tab-stops: 0pt"}

 

Calculates the interest paid during a specific period of an investment.

 

**Syntax**

 

**ISPMT(rate, per, nper, pv)**

 

where:

**rate** is the interest rate for the investment.

**per** is the period for which, you want to find the interest and must be between 1 and nper.

**nper** is the total number of payment periods for the investment.

**pv** is the present value of the investment. For a loan, pv is the loan amount.

 

**Remarks**

 

[·      ]Make sure that you are consistent about the units you use for specifying rate and nper. If you make monthly payments on a four-year loan at an annual interest rate of 12 percent, use 12%/12 for rate and 4\*12 for nper. If you make annual payments on the same loan, use 12% for rate and 4 for nper.

 

[]{#related-topics}

