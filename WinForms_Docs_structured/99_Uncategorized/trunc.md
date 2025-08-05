---
title: trunc.md
original_path: WinForms_Docs/99_Uncategorized/trunc.md
created_at: 2025-08-05
---








  









### TRUNC {#trunc style="tab-stops: 0pt"}

 

Truncates a number to an integer by removing the fractional part of the number.

 

**Syntax**

 

**TRUNC(number, num_digits)**

 

where:

**number** is the number you want to truncate.

**num_digits** is a number specifying the precision of the truncation. The default value for num_digits is 0 (zero).

 

**Remarks**

 

[·      ]TRUNC and INT are similar in that both return integers. TRUNC removes the fractional part of the number. INT rounds numbers down to the nearest integer based on the value of the fractional part of the number. INT and TRUNC are different only when using negative numbers: TRUNC(-4.3) returns -4 but, INT(-4.3) returns -5 because -5 is the lower number.

[]{#p213} 

[]{#related-topics}

