---
title: symbolcustomization2.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\symbolcustomization2.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}





  






    


### Symbol Customization {#symbol-customization style="tab-stops: 0pt"}

 Symbols rendered in the series data points can be customized by using this property


+----------------------+--------------------------------------------------------------------------------------------------------------------+------------------+--------------------+-----------------------------------+
| ChartLegend Property | Description                                                                                                        | Type of Property | Value it accepts   | Dependencies                      |
+----------------------+--------------------------------------------------------------------------------------------------------------------+------------------+--------------------+-----------------------------------+
| Visible              | Gets or sets if the Symbol is visible or not.                                                                      | bool             | True               | NA                                |
|                      |                                                                                                                    |                  |                    |                                   |
|                      |                                                                                                                    |                  | False              |                                   |
+----------------------+--------------------------------------------------------------------------------------------------------------------+------------------+--------------------+-----------------------------------+
| Shape                | Gets or sets the shape of the Symbol.                                                                              | SymbolShape      | SymbolShape.Circle | Visible---                        |
|                      |                                                                                                                    |                  |                    |                                   |
|                      |                                                                                                                    |                  | SymbolShape.Cross  | Only applies if Symbol is visible |
|                      |                                                                                                                    |                  |                    |                                   |
|                      |                                                                                                                    |                  | .                  |                                   |
|                      |                                                                                                                    |                  |                    |                                   |
|                      |                                                                                                                    |                  | .                  |                                   |
|                      |                                                                                                                    |                  |                    |                                   |
|                      |                                                                                                                    |                  | .                  |                                   |
|                      |                                                                                                                    |                  |                    |                                   |
|                      |                                                                                                                    |                  | SymbolShape.Wedge  |                                   |
+----------------------+--------------------------------------------------------------------------------------------------------------------+------------------+--------------------+-----------------------------------+
| Size                 | Gets or sets the size of symbol                                                                                    | Size             | SizeObject         | Visible---                        |
|                      |                                                                                                                    |                  |                    |                                   |
|                      |                                                                                                                    |                  |                    | Only applies if Symbol is visible |
+----------------------+--------------------------------------------------------------------------------------------------------------------+------------------+--------------------+-----------------------------------+
| Style                | Gets or sets the style of the Symbol which include the border, interior, line cap, line join, opacity, and shadow. | Style            | StyleObject        | Visible---                        |
|                      |                                                                                                                    |                  |                    |                                   |
|                      |                                                                                                                    |                  |                    | Only applies if Symbol is visible |
+----------------------+--------------------------------------------------------------------------------------------------------------------+------------------+--------------------+-----------------------------------+


 

Chart with legend can be created through two ways:

[·      ]Builder

[·      ]ChartModel

 

More:







