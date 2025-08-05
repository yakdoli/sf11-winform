---
title: maxa.md
original_path: WinForms_Docs/99_Uncategorized/maxa.md
created_at: 2025-08-05
---








  









### MAXA {#maxa style="tab-stops: 0pt"}

 

Returns the largest value in a list of arguments. Text and logical values such as True and False are compared as well as numbers.

 

**Syntax**

 

**MAXA(value1, value2, \...)**

 

where:

**value1, value2, \...** are values for which you want to find the largest value.

 

**Remarks**

 

[·      ]You can specify arguments that are numbers, empty cells, logical values or text representations of numbers. Arguments that are error values cause errors. If the calculation does not include text or logical values, use the MAX worksheet function instead.

[·      ]If an argument is an array or reference, only values in that array or reference are used. Empty cells and text values in the array or reference are ignored.

[·      ]Arguments that contain True evaluate as 1; arguments that contain text or False evaluate as 0 (zero).

[·      ]If the arguments contain no values, MAXA returns 0 (zero).

[]{#p146} 

[]{#related-topics}

