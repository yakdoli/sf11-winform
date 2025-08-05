---
title: npv.md
original_path: WinForms_Docs/99_Uncategorized/npv.md
created_at: 2025-08-05
---








  









### NPV {#npv style="tab-stops: 0pt"}

 

Calculates the net present value of an investment by using a discount rate and a series of future payments (negative values) and income (positive values).

 

**Syntax**

 

**NPV(rate, value1, value2, \...)**

 

**where**:

**rate** is the rate of discount over the length of one period.

**value1, value2, \...** are arguments representing the payments and income. Value1, value2, \... must be equally spaced in time and occur at the end of each period. NPV uses the order of value1, value2, \... to interpret the order of cash flows. Be sure to enter your payment and income values in the correct sequence.

 

**Remarks**

 

[·      ]The NPV investment begins one period before the date of the value1 cash flow and ends with the last cash flow in the list. The NPV calculation is based on future cash flows. If your first cash flow occurs at the beginning of the first period, the first value must be added to the NPV result, not included in the value arguments.

[·      ]If n is the number of cash flows in the list of values, the formula for NPV is:

[] 

{border="0"} 

[]{#p162} 

[]{#related-topics}

