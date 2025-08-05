---
title: howtoalignthesummarycellsinthegridgroupingcontrol.md
original_path: WinForms_Docs/04_Controls/Grid/howtoalignthesummarycellsinthegridgroupingcontrol.md
created_at: 2025-08-05
---






#### How to align the summary cells in the GridGroupingControl {#how-to-align-the-summary-cells-in-the-gridgroupingcontrol style="tab-stops: 0pt"}

[] 

You can align the summary cells of the GridGroupingControl by making use of the **Horizontal Alignment** property, as shown below.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [GridSummaryColumnDescriptor][ sumCol1 = [new] [GridSummaryColumnDescriptor]([\"sumCol1\"], SummaryType.DoubleAggregate, [\"Col1\"], [\"{Sum}\"]);] |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [sumCol1.Appearance.AnyCell.HorizontalAlignment = GridHorizontalAlignment.Right;]                                                                                                                                                                                                                                            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                    |
| [Dim][ sumCol1 [As] [New] GridSummaryColumnDescriptor([\"sumCol1\"], SummaryType.DoubleAggregate, [\"Col1\"], [\"{Sum}\"])] |
|                                                                                                                                                                                                                                                                                                                                    |
| [sumCol1.Appearance.AnyCell.HorizontalAlignment = GridHorizontalAlignment.Right ]                                                                                                                                                                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p665} 

 

[]{#related-topics}

