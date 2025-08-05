---
title: howtoselectalltextinagridafterclickingacell.md
original_path: WinForms_Docs/04_Controls/Grid/howtoselectalltextinagridafterclickingacell.md
created_at: 2025-08-05
---








  









### How to Select All Text in a Grid After Clicking a Cell {#how-to-select-all-text-in-a-grid-after-clicking-a-cell style="tab-stops: 0pt"}

[] 

Introduction

[] 

The **ActivateCurrentCellBehavior** property controls the activation behavior as a cell becomes current by being clicked or through the cursor keys. If you want the cell text to be fully selected when a cell becomes the current cell, then use the following property.

[] 

[The following code illustrates how to set the Cell Activation behavior to SelectAll in GridControl:]

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                           |
|                                                                                                                                                                                          |
| []                                                                                                                                     |
|                                                                                                                                                                                          |
| [// Set Cell Activation behavior to \'SelectAll\'.]                                                                                    |
|                                                                                                                                                                                          |
| [this][.gridControl1.ActivateCurrentCellBehavior = GridCellActivateAction.SelectAll;] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                            |
|                                                                                                                                                                               |
| []                                                                                                                          |
|                                                                                                                                                                               |
| [\' Set Cell Activation behavior to \'SelectAll\'.]                                                                         |
|                                                                                                                                                                               |
| [Me][.Grid.ActivateCurrentCellBehavior = GridCellActivateAction.SelectAll] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[The following code illustrates how to set the Cell Activation behavior to SelectAll in GridGrouping control:]

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                          |
| [this][.gridGroupingControl1.ActivateCurrentCellBehavior = [GridCellActivateAction].SelectAll;][] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[] 


{border="0"}Note: Other options range from None (no activation at all) to ClickOnCell, DblClickOnCell or SetCurrent.


 

[]{#p638} 

 

[]{#related-topics}

