---
title: normdist.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\normdist.md
created_at: 2025-07-03
---








  









### NORMDIST {#normdist style="tab-stops: 0pt"}

 

Returns the normal distribution for the specified mean and standard deviation.

 

**Syntax**

 

**NORMDIST(x, mean, standard_dev, cumulative)**

 

where:

**x** is the value for which, you want the distribution.

**mean** is the arithmetic mean of the distribution.

**standard_dev** is the standard deviation of the distribution.

**cumulative** is a logical value that determines the form of the function. If cumulative is True, NORMDIST returns the cumulative distribution function; if False, it returns the probability mass function.

 

**Remarks**

 

[·      ]Standard_dev must be \> 0.

[·      ]The equation for the normal density function (cumulative = False) is:

[] 

{border="0"}

[] 

[·      ]When cumulative = True, the formula is the integral from negative infinity to x of the given formula.

 

[]{#p157} 

[]{#related-topics}

