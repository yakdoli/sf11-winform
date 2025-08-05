---
title: addingtooltiptoanapplication2.md
original_path: WinForms_Docs/99_Uncategorized/addingtooltiptoanapplication2.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Adding ToolTip to an Application {#adding-tooltip-to-an-application style="tab-stops: 0pt"}

To show the ToolTip in the PivotGrid control you need to set the PivotGrid control's **TooltipEnabled** property to **true**. This is the master property which controls all the styles of the ToolTip property. The following code explains its usage.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                            |
|                                                                                                                                                                                             |
| [//Enable Tooltip for PivotGridControl]                                                                                 |
|                                                                                                                                                                                             |
| [this] [.pivotGrid1.ToolTipEnabled = [true];] |
|                                                                                                                                                                                             |
|                                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                         |
|                                                                                                                                                                                          |
| [//Enable Tooltip for PivotGridControl]                                                                              |
|                                                                                                                                                                                          |
| [Me] [.pivotGrid1.ToolTipEnabled = [True]] |
|                                                                                                                                                                                          |
|                                                                                                                                                                                          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

You can set the appearance of ToolTips with respect to their styles. Each style has its own **ToolTipEnabled** property. These properties help to set the appearance individually for each style. The following code explains its implementation.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                  |
|                                                                                                                                                                                                                   |
| [//Enable Tooltip for RowHeaderCellStyle] []                                            |
|                                                                                                                                                                                                                   |
| [this] [.pivotGrid1.RowHeaderCellStyle.ToolTipEnabled = [true];]    |
|                                                                                                                                                                                                                   |
| [//Enable Tooltip for ColumnHeaderCellStyle] []                                         |
|                                                                                                                                                                                                                   |
| [this] [.pivotGrid1.ColumnHeaderCellStyle.ToolTipEnabled = [true];] |
|                                                                                                                                                                                                                   |
| [//Enable Tooltip for ValueCellStyle] []                                                |
|                                                                                                                                                                                                                   |
| [this] [.pivotGrid1.ValueCellStyle.ToolTipEnabled = [true];]        |
|                                                                                                                                                                                                                   |
| [//Enable Tooltip for SummaryHeaderStyle] []                                            |
|                                                                                                                                                                                                                   |
| [this] [.pivotGrid1.SummaryHeaderStyle.ToolTipEnabled = [true];]    |
|                                                                                                                                                                                                                   |
| [//Enable Tooltip for SummaryCellStyle] []                                              |
|                                                                                                                                                                                                                   |
| [this] [.pivotGrid1.SummaryCellStyle.ToolTipEnabled = [true];]      |
|                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                               |
|                                                                                                                                                                                                                |
| [//Enable Tooltip for RowHeaderCellStyle] []                                         |
|                                                                                                                                                                                                                |
| [Me] [.pivotGrid1.RowHeaderCellStyle.ToolTipEnabled = [True]]    |
|                                                                                                                                                                                                                |
| [//Enable Tooltip for ColumnHeaderCellStyle] []                                      |
|                                                                                                                                                                                                                |
| [Me] [.pivotGrid1.ColumnHeaderCellStyle.ToolTipEnabled = [True]] |
|                                                                                                                                                                                                                |
| [//Enable Tooltip for ValueCellStyle] []                                             |
|                                                                                                                                                                                                                |
| [Me] [.pivotGrid1.ValueCellStyle.ToolTipEnabled = [True]]        |
|                                                                                                                                                                                                                |
| [//Enable Tooltip for SummaryHeaderStyle] []                                         |
|                                                                                                                                                                                                                |
| [Me] [.pivotGrid1.SummaryHeaderStyle.ToolTipEnabled = [True]]    |
|                                                                                                                                                                                                                |
| [//Enable Tooltip for SummaryCellStyle] []                                           |
|                                                                                                                                                                                                                |
| [Me] [.pivotGrid1.SummaryCellStyle.ToolTipEnabled = [True]]      |
|                                                                                                                                                                                                                |
|                                                                                                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 39: Default ToolTip (Visual Style: Office2007Blue)

 

{border="0"}

Figure 40: ToolTip Shown at Column

{border="0"}

Figure 41: ToolTip Shown at Row

 

Custom data templates can be set to the PivotGrid control's ToolTip. To do so, you need to write a data template and bind the style's **Tag** property and set the key to the PivotGrid control's **CustomToolTipTemplateKey** property. The following code explains its implementation.

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                   |
| [//Set the Custom DataTemplate for PivotGridControl's Tooltip]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                   |
| [this] [.pivotGrid1.CustomToolTipTemplateKey = \"[CustomTemplateTooltip]\";] [] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                           |
|                                                                                                                                                                                                                            |
| [//Set the Custom DataTemplate for PivotGridControl's Tooltip]                                                                                         |
|                                                                                                                                                                                                                            |
| [Me] [.pivotGrid1.CustomToolTipTemplateKey = \"[CustomTemplateTooltip]\"] |
|                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

{border="0"}

Figure 42: Custom ToolTip (Custom DataTemplate)

 

You can set the data template of ToolTip with respect to its styles. Each style has its own **CustomToolTipTemplateKey** property. These properties help to set the appearance individually for each style. The following code explains its implementation.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                               |
| [//Set the Custom DataTemplate for ColumnHeaderCellStyle Tooltip]                                                                                                                                         |
|                                                                                                                                                                                                                                                                               |
| [this] [.pivotGrid1.ColumnHeaderCellStyle.CustomToolTipTemplateKey = [\"ColumnTemplateTooltip\"];]                           |
|                                                                                                                                                                                                                                                                               |
| [//Set the Custom DataTemplate for RowHeaderCellStyle Tooltip]                                                                                                                                            |
|                                                                                                                                                                                                                                                                               |
| [this] [.pivotGrid1.RowHeaderCellStyle.CustomToolTipTemplateKey = [\"RowTemplateTooltip\"];]                                 |
|                                                                                                                                                                                                                                                                               |
| [//Set the Custom DataTemplate for ] [  [ValueCellStyle Tooltip]]                                                             |
|                                                                                                                                                                                                                                                                               |
| [this] [.pivotGrid1.ValueCellStyle.CustomToolTipTemplateKey = [\"ValueTemplateTooltip\"];]                                   |
|                                                                                                                                                                                                                                                                               |
| [//Set the Custom DataTemplate for ] [  [SummaryHeaderStyle Tooltip]]                                                         |
|                                                                                                                                                                                                                                                                               |
| [this] [.pivotGrid1.SummaryHeaderStyle.CustomToolTipTemplateKey = [\"SummaryHeaderTemplateTooltip\"];]                       |
|                                                                                                                                                                                                                                                                               |
| [//Set the Custom DataTemplate for SummaryCellStyle Tooltip] []                                                                                     |
|                                                                                                                                                                                                                                                                               |
| [this] [.pivotGrid1.SummaryCellStyle.CustomToolTipTemplateKey = [\"SummaryCellTemplateTooltip\"];[]] |
|                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                      |
| [//Set the Custom DataTemplate for ColumnHeaderCellStyle Tooltip]                                                                                                                |
|                                                                                                                                                                                                                                                      |
| [Me] [.pivotGrid1.ColumnHeaderCellStyle.CustomToolTipTemplateKey = [\"ColumnTemplateTooltip\"]]     |
|                                                                                                                                                                                                                                                      |
| [//Set the Custom DataTemplate for RowHeaderCellStyle Tooltip]                                                                                                                   |
|                                                                                                                                                                                                                                                      |
| [Me] [.pivotGrid1.RowHeaderCellStyle.CustomToolTipTemplateKey = [\"RowTemplateTooltip\"]]           |
|                                                                                                                                                                                                                                                      |
| [//Set the Custom DataTemplate for ] [  [ValueCellStyle Tooltip]]                                    |
|                                                                                                                                                                                                                                                      |
| [Me] [.pivotGrid1.ValueCellStyle.CustomToolTipTemplateKey = [\"ValueTemplateTooltip\"]]             |
|                                                                                                                                                                                                                                                      |
| [//Set the Custom DataTemplate for ] [  [SummaryHeaderStyle Tooltip]]                                |
|                                                                                                                                                                                                                                                      |
| [Me] [.pivotGrid1.SummaryHeaderStyle.CustomToolTipTemplateKey = [\"SummaryHeaderTemplateTooltip\"]] |
|                                                                                                                                                                                                                                                      |
| [//Set the Custom DataTemplate for SummaryCellStyle Tooltip] []                                                            |
|                                                                                                                                                                                                                                                      |
| [Me] [.pivotGrid1.SummaryCellStyle.CustomToolTipTemplateKey = [\"SummaryCellTemplateTooltip\"]]     |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 43: Custom DataTemplate for ColumnHeaderCellStyle

[]{#related-topics}

