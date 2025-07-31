---
title: ipmt.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\ipmt.md
created_at: 2025-07-03
---








  









### IPMT {#ipmt style="tab-stops: 0pt"}

 

Returns the interest payment for a given period for an investment based on periodic, constant payments and a constant interest rate.

 

Syntax

 

IPMT(rate, per, nper, pv, fv, type)

 

where:

**rate** is the interest rate per period.

**per** is the period for which, you want to find the interest and must be in the range 1 to nper.

**nper** is the total number of payment periods in an annuity.

**pv** is the present value or the lump-sum amount that a series of future payments is worth right now.

**fv** is the future value or a cash balance that you want to attain after the last payment is made. If fv is omitted, it is assumed to be 0 (the future value of a loan, for example, is 0).

**type** is the number 0 or 1 and indicates when payments are due. If type is omitted, it is assumed to be 0. If type = 0, payments are made at the end of the period. If type is 1, payments are made at the beginning of the period.

 

**Remarks**

 

[·      ]Make sure that you are consistent about the units you use for specifying rate and nper. If you make monthly payments on a four-year loan at 12 percent annual interest, use 12%/12 for rate and 4\*12 for nper. If you make annual payments on the same loan, use 12% for rate and 4 for nper.[]{#p131}

 

[]{#related-topics}

