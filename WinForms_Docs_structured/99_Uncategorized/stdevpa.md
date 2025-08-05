---
title: stdevpa.md
original_path: WinForms_Docs/99_Uncategorized/stdevpa.md
created_at: 2025-08-05
---








  









### STDEVPA {#stdevpa style="tab-stops: 0pt"}

 

Calculates the standard deviation based on the entire population given as arguments, including text and logical values.

 

**Syntax**

 

**STDEVPA(value1, value2, \...)**

 

where:

**value1, value2, \...** are values corresponding to a population. You can also use a single array or a reference to an array instead of arguments separated by commas.

 

Remarks

 

[·      ]Arguments that contain True evaluate as 1; arguments that contain text or False evaluate as 0 (zero).

[·      ]STDEVPA uses the following formula:

[] 

{border="0"}

 

where:

**x-bar** is the sample mean AVERAGE(value1,value2,...).

**n** is the sample size.

[]{#p199} 

[]{#related-topics}

