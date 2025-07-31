---
title: querybasestyles1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\querybasestyles1.md
created_at: 2025-07-03
---






#### QueryBaseStyles[]{#p218} {#querybasestyles style="tab-stops: 0pt"}

This event is used to provide base styles for desired grid cells. It receives an argument of type GridQueryBaseStylesEventArgs that contains the following parameters.

 


  ------------ -----------------------------------------------------------------------
  Property     Description
  BaseStyles   Holds a list of base styles applicable for current cell co-ordinates.
  Cell         Represent the cell co-ordinates.
  Style        Gives cell style information.
  ------------ -----------------------------------------------------------------------


 

Example

 

This event can be triggered using the following code:

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                                        |
|                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                            |
|                                                                                                                                                                                                                                   |
| [this][.grid.QueryBaseStyles += [new] [GridQueryBaseStylesEventHandler](grid_QueryBaseStyles);] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Event Handler

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                               |
|                                                                                                                                                                                          |
| []                                                                                                                                                   |
|                                                                                                                                                                                          |
| [void][ grid_QueryBaseStyles([object] sender, GridQueryBaseStylesEventArgs e)] |
|                                                                                                                                                                                          |
| [{]                                                                                                                                                  |
|                                                                                                                                                                                          |
| [    [if] (ColumnRowIndex.Text != [\"\"])]                                                              |
|                                                                                                                                                                                          |
| [    {]                                                                                                                                              |
|                                                                                                                                                                                          |
| [       [if] (e.Cell.RowIndex == 3)]                                                                                            |
|                                                                                                                                                                                          |
| [       {]                                                                                                                                           |
|                                                                                                                                                                                          |
| [                    ]                                                                                                                               |
|                                                                                                                                                                                          |
| [         e.BaseStyles.Add([new] GridStyleInfo() { Background = [new] SolidColorBrush(Colors.Maroon) });]  |
|                                                                                                                                                                                          |
| [       }]                                                                                                                                           |
|                                                                                                                                                                                          |
| [       [if] (e.Cell.ColumnIndex == 3)]                                                                                         |
|                                                                                                                                                                                          |
| [       {]                                                                                                                                           |
|                                                                                                                                                                                          |
| [         e.BaseStyles.Add([new] GridStyleInfo() { Background = [new] SolidColorBrush(Colors.Orange) });]  |
|                                                                                                                                                                                          |
| [       }]                                                                                                                                           |
|                                                                                                                                                                                          |
| []                                                                                                                                                   |
|                                                                                                                                                                                          |
| [    }]                                                                                                                                              |
|                                                                                                                                                                                          |
| [}]                                                                                                                                                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Output

 

The following output is generated using the code above.

 

{border="0"}

Figure 96: QueryBaseStyles

 

 

 

[]{#related-topics}

