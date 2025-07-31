---
title: ceiling.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\ceiling.md
created_at: 2025-07-03
---








  









### CEILING {#ceiling style="tab-stops: 0pt"}

 

Returns number rounded up, away from zero, to the nearest multiple of significance. For example, if you want to avoid using pennies in your prices and your product is priced at \$4.82, use the formula =CEILING(4.82,0.05) to round prices up to the nearest nickel.

 

Syntax

[] 

CEILING(number, significance)

 

where:

**number**[ ]is the value you want to round off.

**significance** is the multiple to which you want to round.

 

**Remarks**

 

[·      ]Both values must be numeric.

[·      ]Regardless of the sign of a number, a value is rounded up when adjusted away from zero. If the number is an exact multiple of significance, no rounding occurs.

 

[]{#p87} 

[]{#related-topics}

