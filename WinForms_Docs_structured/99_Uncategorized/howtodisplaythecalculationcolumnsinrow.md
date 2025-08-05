---
title: howtodisplaythecalculationcolumnsinrow.md
original_path: WinForms_Docs/99_Uncategorized/howtodisplaythecalculationcolumnsinrow.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}





  






   


## How to Display the Calculation Columns in Row? {#how-to-display-the-calculation-columns-in-row style="tab-stops: 0pt"}

By default, calculation values are displayed in columns, However it can be displayed in row by setting the following property of Grid to false.

+---------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                        |
|                                                                                                                                       |
| []                                                                                  |
|                                                                                                                                       |
| [// Display Calculation values in Row] [\                                           |
| [this].pivotGrid1.ShowCalculationsAsColumns = [false];] |
|                                                                                                                                       |
| []                                                                                                |
+---------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                   |
|                                                                                                                                                                  |
| []                                                                                                             |
|                                                                                                                                                                  |
| [\' Display Calculation values in Row] []                                  |
|                                                                                                                                                                  |
| [Me] [.pivotGrid1.ShowCalculationsAsColumns = [False]] |
|                                                                                                                                                                  |
| []                                                                                                                           |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#related-topics}

