---
title: confidence.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\confidence.md
created_at: 2025-07-03
---








  









### CONFIDENCE {#confidence style="tab-stops: 0pt"}

 

Returns a value that you can use to construct a confidence interval about a population mean. The confidence interval is a range of values. In your sample, mean x is at the center of this range and the range is x ± CONFIDENCE. For example, if x is the sample mean of delivery times for products ordered through the mail, x ± CONFIDENCE is a range of population means.

[] 

Syntax

[] 

[CONFIDENCE(alpha, standard_dev,size)]

[] 

where:

**alpha** is the significance level used to compute the confidence level. The confidence level equals 100\*(1 - alpha)%, or in other words, an alpha of 0.05 indicates a 95 percent confidence level.

**standard_dev**[ ]is the population standard deviation for the data range and is assumed to be known.

**size** is the sample size.

 

**Remarks**

[] 

[·      ]All arguments must be non-numeric.

[·      ]Alpha must be \> 0 and \< 1.

[·      ]Standard_dev must be \> 0.

[·      ]Size must be \>= 1.

 

[]{#p93} 

[]{#related-topics}

