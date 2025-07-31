---
title: mirr.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\mirr.md
created_at: 2025-07-03
---








  









### MIRR {#mirr style="tab-stops: 0pt"}

 

Returns the modified internal rate of return for a series of periodic cash flows.

 

**Syntax**

 

**MIRR(values, finance_rate, reinvest_rate)**

 

where:

**values** is an array or a reference to cells that contain numbers. These numbers represent a series of payments (negative values) and income (positive values) occurring at regular periods. Values must contain at least one positive value and one negative value to calculate the modified internal rate of return.

**finance_rate** is the interest rate you pay on the money used in the cash flows.

**reinvest_rate** is the interest rate you receive on the cash flows as you reinvest them.

 

**Remarks**

 

[·      ]MIRR uses the order of values to interpret the order of cash flows. Be sure to enter your payment and income values in the sequence you want and with the correct signs (positive values for cash received, negative values for cash paid).

[·      ]If n is the number of cash flows in values, frate is the finance_rate, and rrate is the reinvest_rate, then the formula for MIRR is:

[] 

{border="0"}

 

[]{#p152} 

[]{#related-topics}

