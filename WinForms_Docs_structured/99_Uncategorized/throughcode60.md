---
title: throughcode60.md
original_path: WinForms_Docs/99_Uncategorized/throughcode60.md
created_at: 2025-08-05
---






#### Through Code {#through-code style="tab-stops: 0pt"}

The conditional formatting can be done through code using the OlapGrid control's **QueryCellInfo** event. The QueryCellInfo event will be fired whenever a new cell is created in the grid. In the event argument, we can access the newly created cell and format the cell based on its value. Any changes made to the cell will be reflected in the output of the OLAP grid. Refer to the following code that illustrates the conditional formatting:

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                |
| [void][ OlapGrid1_QueryCellInfo([object] sender, ][CellInfoEventArgs][ e)] |
|                                                                                                                                                                                                                                                                                                |
| [{]                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                |
| [      double][ val = 0;]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                |
| [      string][ text = e.Cell.Text;]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                |
| [      if][ ([Double].TryParse(text, [out] val))]                                                                                                            |
|                                                                                                                                                                                                                                                                                                |
| [            if][ (val \< 2000)]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                |
| [                  e.Cell.BackColor = [Color].Red;]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                |
| [}]                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                   |
| [Sub][ OlapGrid1_QueryCellInfo([ByVal] s [As] [Object], [ByVal] e [As] ][CellInfoEventArgs][)] |
|                                                                                                                                                                                                                                                                                                                                                                                                   |
| [      Dim][ val [As] [Double] = 0]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                   |
| [      [Dim] text [As] [String] = e.Cell.Text]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                   |
| [      [If] [Double].TryParse(text, val) [Then]]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [If] val \< 2000 [Then]]                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                   |
| [                  e.Cell.BackColor = Color.Red]                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [End] [If]]                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                   |
| [      [End] [If]               ]                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                   |
| [End][ [Sub]]                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                                                                                           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Sample Link

A sample demo is available in the following location:

**..\\Syncfusion\\EssentialStudio\\\<VersionNumber\>\\BI\\Web\\OlapGrid.Web\\Samples\\3.5\\Application Scenario\\Grid Formatting Demo**

 

[]{#related-topics}

