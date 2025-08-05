---
title: frozenheader1.md
original_path: WinForms_Docs/99_Uncategorized/frozenheader1.md
created_at: 2025-08-05
---








  





### Frozen Header {#frozen-header style="tab-stops: 0pt"}

Users can freeze the header of the grid so that headers are always visible when scrolling through a grid with a large number of rows or columns.

Use Case Scenarios

This feature enables users to view headers even while scrolling through the grid.

 

{border="0"}

Figure 15: OLAP Grid with FreezeColumnHeaders and FreezeRowHeaders enabled

 

Properties

Table 6: OlapGrid Properties Table


  ----------------------------------------------- ----------------------------------------------------------------- ------------- -----------
  Property                                        Description                                                       Type          Data Type
  FreezeColumnHeaders[]   To freeze/unfreeze the column headers[]   Server side   bool
  FreezeRowHeaders[]      To freeze/unfreeze the row headers[]      Server side   bool
  ----------------------------------------------- ----------------------------------------------------------------- ------------- -----------


 

 

Sample Link

Follow the steps given below to view a sample of this feature.

1    Open the **Syncfusion Dashboard**.

2    Click **Business Intelligence**.

3    Click the **ASP.NET** drop-down list, and select **Explore Samples**.

4    Navigate to **OlapGrid.Web** \> **Samples** \> **3.5** \> **Scrolling** \> **Frozen Headers Demo**.

[] 

Adding Frozen Header to an Application

The frozen header can be added to an application by using the following code:

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [\<][Syncfusion][:][OlapGrid][ [ID][=\"OlapGridControl1\"] [runat][=\"server\"] [Height][=\"300\"] [Width][=\"800\"] [FreezeRowHeaders][=\"true\"] [FreezeColumnHeaders][=\"true\"] [/\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

