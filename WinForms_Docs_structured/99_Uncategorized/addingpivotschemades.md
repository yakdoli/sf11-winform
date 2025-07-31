---
title: addingpivotschemades.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\addingpivotschemades.md
created_at: 2025-07-03
---








  





### Adding Pivot Schema Designer to an Application {#adding-pivot-schema-designer-to-an-application style="TEXT-ALIGN: justify; tab-stops: 0pt"}

The following steps illustrate the implementation of the pivot schema designer in an application.

1.  Create a Silverlight application and add **PivotGridControl** and **PivotSchemaDesigner** to it.

2.  Set the **PivotControl** property of **PivotSchemaDesigner** to the **PivotGridControl** object created via the designer. The following code snippet shows the implementation of the **PivotSchemaDesigner**.

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [\<][pivotSchemaDesigner][:][PivotSchemaDesigner][ Name][=\"Designer\"][ PivotControl][=\"{][Binding][ ElementName][=pivotGrid1 }\" ][ ] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                         |
|                                                                                                                                                                          |
| [this][.pivotSchemaDesigner.PivotControl = [this].pivotGrid1;] |
|                                                                                                                                                                          |
|                                                                                                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.  Bind the **PivotCalculations**, **PivotRows**, and **PivotColumns** to the **PivotGridControl** and run the application.

The following images illustrate remarkable functionalities of the pivot schema designer with the PivotGrid control.

{border="0"}

Figure 39: Pivot Schema Designer with PivotGrid Control

 

{border="0"}

Figure 40: Pivot Schema Designer showing Pivot Computation Info Dialog

 

{border="0"}

Figure 41: Pivot Schema Designer showing Pop-up Filter Window

[]{#related-topics}

