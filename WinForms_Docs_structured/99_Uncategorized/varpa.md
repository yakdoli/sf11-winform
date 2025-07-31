---
title: varpa.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\varpa.md
created_at: 2025-07-03
---








  









### VARPA {#varpa style="tab-stops: 0pt"}

[] 

Calculates variance based on the entire population. In addition to numbers and text, logical values such as True and False are also included in the calculation.

[] 

**Syntax**

**[VARPA(value1, value2, \...)]**

**[]** 

**[value1, value2, \...]**[ are arguments corresponding to a population.]

[] 

Remarks

[] 

[·      ]VARPA assumes that its arguments are the entire population. If your data represents a sample of the population, you must compute the variance using VARA.

[·      ]Arguments that contain True evaluate as 1; arguments that contain text or False evaluate as 0 (zero). If the calculation does not include text or logical values, use the VARP worksheet function instead.

[·      ]The equation for VARPA is:

[] 

{border="0"}

 

where:

**x** is the sample mean AVERAGE(value1, value2, ...).

**n** is the sample size.

[]{#p214} 

[]{#related-topics}

