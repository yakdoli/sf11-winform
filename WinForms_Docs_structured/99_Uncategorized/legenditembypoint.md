---
title: legenditembypoint.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\legenditembypoint.md
created_at: 2025-07-03
---








  









### LegendItem By Point {#legenditem-by-point style="tab-stops: 0pt"}

**  **

Get LegendItem By Point

 

The **Legend.GetItemBy** method will let you get the reference to a legend item at a specific point. Implementing the below code sample, will display a tooltip with legend item name, on which the user mouse hover.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                      |
| **[]**                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                      |
| [private][ [ToolTip] toolTip2;]                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                      |
| [this][.chartControl1.Legend.MouseHover += [new] [MouseEventHandler](lgnd_MouseHover);]                                                                               |
|                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                      |
| [void][ lgnd_MouseHover([object] sender, [EventArgs] e)]                                                                                                              |
|                                                                                                                                                                                                                                                                                                      |
| [{]                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                      |
| [    [Point] p1 = [this].chartControl1.Legend.PointToClient([new] [Point]([Control].MousePosition.X, [Control].MousePosition.Y));] |
|                                                                                                                                                                                                                                                                                                      |
| [    [ChartLegendItem] item = chartControl1.Legend.GetItemBy(p1);]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                      |
| [    [if] (item != [null])]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                      |
| [        [this].toolTip2.Show(item.Text, [this].chartControl1.Legend, p1.X + 10, p1.Y + 20, 3000);]                                                                                                                    |
|                                                                                                                                                                                                                                                                                                      |
| [}]                                                                                                                                                                                                                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB][.NET][\]]**                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                 |
| **[]**                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                 |
| [private][ toolTip2 [As] [ToolTip]]                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                 |
| [AddHandler][ [Me].chartControl1.Legend.MouseHover, [AddressOf] lgnd_MouseHover]                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                 |
| [Private][ [Sub] lgnd_MouseHover([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)]                    |
|                                                                                                                                                                                                                                                                                                                                 |
| [    [\' Get the item at the specified location..]]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                 |
| [    [Dim] p1 [As] Point = [Me.]chartControl1.Legend.PointToClient([New] [Point]([Control].MousePosition.X, [Control].MousePosition.Y))] |
|                                                                                                                                                                                                                                                                                                                                 |
| [Dim][ item [As] Chart[LegendItem = ]chartControl1.Legend.GetItemBy(p1)[ ]   ]                                                                                            |
|                                                                                                                                                                                                                                                                                                                                 |
| [If][ item [IsNot] [Nothing] [Then]]                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                 |
| [        [Me.]toolTip2.Show(item.Text, [this].chartControl1.Legend, p1.X + 10, p1.Y + 20, 3000)]                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                 |
| [    [End] [If]]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                 |
| [End][ [Sub]]                                                                                                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

 

Figure 362: Legend Item Identified using GetItemBy Method

[]{#p265} 

[]{#related-topics}

