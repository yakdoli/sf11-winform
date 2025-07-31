---
title: forecast.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\forecast.md
created_at: 2025-07-03
---








  









### FORECAST {#forecast style="tab-stops: 0pt"}

 

Calculates a future value by using existing values using a linear regression. The predicted value is a y-value for a given x-value.

 

**Syntax**

 

**FORECAST(x, known_ys, known_xs)**

 

where:

**x** is the data point for which you want to predict a value.

**known_ys** is the dependent array or range of data.

**known_xs** is the independent array or range of data.

 

**Remarks**

 

[·      ]The equation for FORECAST is:

 

**a+bx**

 

where:

{border="0"}

{border="0"}

 

**x-bar** and **y-bar** are the sample means AVERAGE(known_xs) and AVERAGE(known_ys).

 

[]{#related-topics}

