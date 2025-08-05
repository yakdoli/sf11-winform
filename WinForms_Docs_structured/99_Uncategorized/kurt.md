---
title: kurt.md
original_path: WinForms_Docs/99_Uncategorized/kurt.md
created_at: 2025-08-05
---








  









### KURT {#kurt style="tab-stops: 0pt"}

 

Returns the kurtosis of a data set. Kurtosis characterizes the relative peakedness or flatness of a distribution compared with the normal distribution. Positive kurtosis indicates a relatively peaked distribution. Negative kurtosis indicates a relatively flat distribution.

 

**Syntax**

**\
KURT(number1, number2, \...)**

 

where:

**number1, number2, \...** are arguments for which you want to calculate kurtosis. You can also use a single array or a reference to an array instead of arguments separated by commas.

 

**Remarks**

 

[·      ]The arguments must be either numbers or names, arrays or references that contain numbers.

[·      ]If an array or reference argument contains text, logical values or empty cells, those values are ignored; however, cells with the value zero are included.

[·      ]If there are fewer than four data points or if the standard deviation of the sample equals zero, KURT returns the #DIV/0! error value.

[·      ]Kurtosis is defined as:

[] 

{border="0"}

 

where:

**s** is the sample standard deviation.

 

[]{#p136} 

 

[]{#related-topics}

