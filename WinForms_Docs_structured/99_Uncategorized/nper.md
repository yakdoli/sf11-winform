---
title: nper.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\nper.md
created_at: 2025-07-03
---








  









### NPER {#nper style="tab-stops: 0pt"}

 

Returns the number of periods for an investment based on periodic, constant payments and a constant interest rate.

 

**Syntax**

 

**NPER(rate, pmt, pv, fv, type)**

 

where:

**rate** is the interest rate per period.

**pmt** is the payment made each period; it cannot change over the life of the annuity.

**pv** is the present value or the lump-sum amount that a series of future payments is worth right now.

**fv** is the future value or a cash balance that you want to attain after the last payment is made. If fv is omitted, it is assumed to be 0 (the future value of a loan, for example, is 0).

**type** is the number 0 or 1 and indicates when payments are due. If type equals:

 

[·      ]0 - payments are due at the end of the period

[·      ]1 - payments are due at the beginning of the period

 

[]{#p161} 

 

[]{#related-topics}

