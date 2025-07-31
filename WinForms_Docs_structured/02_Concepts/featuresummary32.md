---
title: featuresummary32.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\featuresummary32.md
created_at: 2025-07-03
---








  









## Feature Summary {#feature-summary style="tab-stops: 0pt"}

 

The features of Essential Calculate are listed below.

 

[·      ]Essential Calculate comes with a function library of more than 150 entries and supports cross sheet references.

[·      ]It can be used in conjunction with Essential XlsIO to fully load, manipulate and compute Excel spreadsheets without depending on Excel.

[·      ]Essential Calculate does not depend on Microsoft Excel and thus enables you to perform calculations independent of Excel.

[·      ]You can add extensive calculation support to your own business objects in both Windows Forms and ASP.NET applications.

[·      ]Easily set up forms that have calculation dependencies among various controls.

[·      ]With Essential Calculate, you can set properties that will indicate that you want formula dependencies to be tracked so that the values are automatically updated when a dependent value changes. Or you can turn off the overhead of tracking dependencies and have formulas calculated from scratch when you need a particular formula value.

[·      ]Essential Calculate can be used in manual mode or automatic mode.

[·      ]The manual mode works when you explicitly request for a value. At that point, the calculation is done from scratch to obtain the computed value. So, if your formula depends on several other values in the form, and when you request the computed value, the other values will be retrieved and used to compute the requested formula.

[·      ]In automatic mode, Essential Calculate maintains a dependency list. Hence, when a value is changed, any formula that depends on it, is recalculated at that particular point. When you request for a formula value, the formula value is not computed from scratch; instead it is retrieved from where Essential Calculate stores computed values.

[]{#p18} 

[]{#related-topics}

