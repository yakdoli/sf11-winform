---
title: stdevp.md
original_path: WinForms_Docs/99_Uncategorized/stdevp.md
created_at: 2025-08-05
---








  









### STDEVP {#stdevp style="tab-stops: 0pt"}

 

Calculates standard deviation based on the entire population given as arguments.

 

**Syntax**

 

**STDEVP(number1, number2, \...)**

 

where:

**number1, number2, \...** are 1 to 30 number arguments corresponding to a population. You can also use a single array or a reference to an array instead of arguments separated by commas.

 

Remarks

 

[·      ]STDEVP assumes that its arguments are the entire population. If your data represents a sample of the population, then compute the standard deviation using STDEV.

[·      ]STDEVP uses the following formula:

[] 

{border="0"}

 

where:

**x** is the sample mean AVERAGE(number1,number2,...).

**n** is the sample size.

 

[]{#p198} 

[]{#related-topics}

