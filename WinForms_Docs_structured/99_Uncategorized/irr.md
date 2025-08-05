---
title: irr.md
original_path: WinForms_Docs/99_Uncategorized/irr.md
created_at: 2025-08-05
---








  









### IRR {#irr style="tab-stops: 0pt"}

 

Returns the internal rate of return for a series of cash flows represented by the numbers in values. The cash flows must occur at regular intervals such as monthly or annually.

 

**Syntax**

 

**IRR(values, guess)**

 

where:

**values** is an array or a reference to cells that contain numbers for which, you want to calculate the internal rate of return. Values must contain at least one positive value and one negative value to calculate the internal rate of return. IRR uses the order of values to interpret the order of cash flows. Be sure to enter your payment and income values in the sequence you want.

**guess** is a number that you guess is close to the result of IRR. An iterative technique is used for calculating IRR. In most cases, you do not need to provide a guess for the IRR calculation. If a guess is omitted, it is assumed to be 0.1 (10 percent).[]{#p132}

 

[]{#related-topics}

