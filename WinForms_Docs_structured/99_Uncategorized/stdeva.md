---
title: stdeva.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\stdeva.md
created_at: 2025-07-03
---








  









### STDEVA {#stdeva style="tab-stops: 0pt"}

 

Estimates standard deviation based on a sample. The standard deviation is a measure of how widely values are dispersed from the average value (the mean). Text and logical values such as True and False are also included in the calculation.

 

**Syntax**

 

**STDEVA(value1, value2 , \...)**

 

where:

**value1, value2, \...** are values corresponding to a sample of a population. You can also use a single array or a reference to an array instead of arguments separated by commas.

 

**Remarks**

 

[·      ]Arguments that contain True evaluate as 1; arguments that contain text or False evaluate as 0 (zero).

[·      ]STDEVA uses the following formula:

[] 

{border="0"}

 

where:

**x-bar** is the sample mean AVERAGE(value1,value2,...).

**n** is the sample size.

 

[]{#related-topics}

