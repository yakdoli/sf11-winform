---
title: themes2.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\themes2.md
created_at: 2025-07-03
---








  









## Themes {#themes style="tab-stops: 0pt"}

Essential BI OLAP Chart for Silverlight supports a set of predefined themes, which can be applied to customize the Chart control.

Use Case Scenarios

Users can customize the look and feel of Charts by using themes. A theme can be selected from the 54 available themes and the users can define their customized styles.


 

{border="0"}Note:

If a default style is overridden by any customized style, the overridden style of the element will remain the same even if the theme is changed.


{border="0"}

 

Figure 40: Sample Themes

Specifying a Theme for an OlapChart in an Application

 

OlapChart for Silverlight supports 54 default themes. The users can select a particular theme by using the ChartVisualStyle property.

 Applying a Theme

 

To apply a theme to an OlapChart:

1.   Create an instance of **OlapChart**.

2.   Set the **ChartVisualStyle** property, as shown in the following code snippets.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\<][sfchart][:][OlapChart][ ChartVisualStyle][=\"GreenBlend\"/\>][] |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                     |
|                                                                                                                                                                                      |
| **[]**                                                                                                                                           |
|                                                                                                                                                                                      |
| [OlapChart][ olapChart1 = [new] [OlapChart]();] |
|                                                                                                                                                                                      |
| [this][.olapChart1.ChartVisualStyle = [ChartStyles].GreenBlend;]        |
|                                                                                                                                                                                      |
|                                                                                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                              |
| **[]**                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                              |
| [Dim][ olapChart1 [As] ][OlapChart][ = [New] ][OlapChart][()] |
|                                                                                                                                                                                                                                                                                                                                                                              |
| [Me][.olapChart1.ChartVisualStyle = ][ChartStyles][.GreenBlend]                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Create an **OlapReport**, as shown in the following code snippets.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                              |
|                                                                                                                                                                               |
| **[]**                                                                                                                                    |
|                                                                                                                                                                               |
| [private][ [OlapReport] SimpleDimensions()]                      |
|                                                                                                                                                                               |
| [{\                                                                                                                                                                           |
|       [OlapReport] olapReport = [new] [OlapReport]();\                                                   |
|       olapReport.CurrentCubeName = [\"Adventure Works\"];\                                                                                            |
|  \                                                                                                                                                                            |
|       [DimensionElement] dimensionElementColumn = [new] [DimensionElement]();\                           |
|            \                                                                                                                                                                  |
|       [//// Specifying the Name of the Dimension.]\                                                                                                     |
|       dimensionElementColumn.Name = [\"Customer\"];\                                                                                                  |
|  \                                                                                                                                                                            |
|       dimensionElementColumn.HierarchyName = [\"Customer Geography\"];\                                                                               |
|  \                                                                                                                                                                            |
|       dimensionElementColumn.AddLevel([\"Customer Geography\"], [\"Country\"]);\                                              |
|  \                                                                                                                                                                            |
|  \                                                                                                                                                                            |
|       [MeasureElements] measureElementColumn = [new] [MeasureElements]();\                               |
|       measureElementColumn.Elements.Add([new] [MeasureElement] { Name = [\"Internet Sales Amount\"] });\ |
|  \                                                                                                                                                                            |
|       [DimensionElement] dimensionElementRow = [new] [DimensionElement]();\                              |
|       [//// Specifying the Name of the Dimension.]\                                                                                                     |
|       dimensionElementRow.Name = [\"Date\"];\                                                                                                         |
|       dimensionElementRow.AddLevel([\"Fiscal\"], [\"Fiscal Year\"]);\                                                         |
|  \                                                                                                                                                                            |
|       [//// Adding the MeasureElement.]\                                                                                                                |
|       olapReport.CategoricalElements.Add([new] [Item] { ElementValue = measureElementColumn });\                                 |
|  \                                                                                                                                                                            |
|       [//// Adding the ColumnMembers.]\                                                                                                                 |
|       olapReport.CategoricalElements.Add([new] [Item] { ElementValue = dimensionElementColumn });\                               |
|             \                                                                                                                                                                 |
|       [//// Adding the RowMembers.]\                                                                                                                    |
|       olapReport.SeriesElements.Add([new] [Item] { ElementValue = dimensionElementRow });\                                       |
|  \                                                                                                                                                                            |
|       [return] olapReport;\                                                                                                                              |
| }]                                                                                                                                        |
|                                                                                                                                                                               |
|                                                                                                                                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [Private][ [Function] SimpleDimensions() [As] ][OlapReport][]                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [      [Dim] olapReport [As] OlapReport = [New] ][OlapReport][()]                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [      olapReport.CurrentCubeName = ][\"Adventure Works\"][]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [      [Dim] dimensionElementColumn [As] ][DimensionElement][ = [New] ][DimensionElement][()] |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [      [\' Specifying the Name of the Dimension.]]                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [      dimensionElementColumn.Name = ][\"Customer\"][]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [      dimensionElementColumn.HierarchyName = ][\"Customer Geography\"][]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [      dimensionElementColumn.AddLevel(][\"Customer Geography\"][, ][\"Country\"][)]                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [      [Dim] measureElementColumn [As] ][MeasureElements][ = [New] ][MeasureElements][()]     |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [      measureElementColumn.Elements.Add([New] MeasureElement [With] {.Name = ][\"Internet Sales Amount\"][})]                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [      [Dim] dimensionElementRow [As] ][DimensionElement][ = [New] ][DimensionElement][()]    |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [      [\' Specifying the Name of the Dimension.]]                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [      dimensionElementRow.Name = ][\"Date\"][]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [      dimensionElementRow.AddLevel(][\"Fiscal\"][,][ \"Fiscal Year\"][)]                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [      [\' Adding the MeasureElement.]]                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [      olapReport.CategoricalElements.Add([New] Item [With] {.ElementValue = measureElementColumn})]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [      [\' Adding the ColumnMembers.]]                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [      olapReport.CategoricalElements.Add([New] Item [With] {.ElementValue = dimensionElementColumn})]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [      [\' Adding the RowMembers.]]                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [      olapReport.SeriesElements.Add([New] Item [With] {.ElementValue = dimensionElementRow})]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [      [Return] olapReport]                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [End][ [Function]]                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Add the **OlapReport** to **OlapDataManager**, and bind the report to the **OlapChart** control.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                      |
|                                                                                                                                                                       |
|                                                                                                                                                                       |
|                                                                                                                                                                       |
| [      [this].olapDataManager.SetCurrentReport(][SimpleDimensions][());\ |
|       [this].olapChart1.OlapDataManager = olapDataManager;]                                                  |
|                                                                                                                                                                       |
|                                                                                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                           |
|                                                                                                                            |
| []                                                                        |
|                                                                                                                            |
| [      [Me].olapDataManager.SetCurrentReport(SimpleDimensions())] |
|                                                                                                                            |
| [      [Me].olapChart1.OlapDataManager = olapDataManager]         |
|                                                                                                                            |
|                                                                                                                            |
+----------------------------------------------------------------------------------------------------------------------------+

[] 

See Also:

For more information on how to create a simple working sample of an OlapChart refer:

[]{.UGHyperlink}

[] 

The following screen shot shows the GreenBlend theme applied to an OlapChart for Silverlight:

[] 

{border="0"}

 

Figure 41: GreenBlend Theme Applied to OlapChart

[]{#_Sample_Link}Sample Link

Chart Appearance Sample

To access a Chart Appearance sample:

1.   Open the Syncfusion Dashboard.

2.   Click **Business Intelligence**.

3.   Click the Silverlight drop-down list, and then select **Explore Samples**.

4.   Navigate to **Syncfusion.OlapChart.Silverlight.Samples** -\> **Syncfusion.OlapChart.Silverlight.Samples** -\> **Samples** -\> **AppearanceDemo**.

[] 

[]{#related-topics}

