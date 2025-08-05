---
title: supporttohidefieldsinpivotschemadesigner.md
original_path: WinForms_Docs/99_Uncategorized/supporttohidefieldsinpivotschemadesigner.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}





  






    


### Support to Hide Fields in PivotSchemaDesigner {#support-to-hide-fields-in-pivotschemadesigner style="tab-stops: 0pt"}

The user can customize the PivotTable field list in PivotSchemaDesigner. The user can hide the unnecessary fields from the PivotSchemaDesigner by using the ShowDisplayFieldsOnly property.

Use Case Scenarios

This feature enables the user to load required set of items in PivotSchemaDesigner.

The following screen shot shows a PivotSchemaDesigner control with all items and required items in a pivot table field list:

[] 

{border="0"}

Figure 52 Pivot Table Field List with ShowDisplayFieldsOnly Disabled

 

{border="0"}

Figure 53 Pivot Table Field List with ShowDisplayFieldsOnly Enabled

 

Properties

Table 12: Properties Table


+-----------------------+---------------------------------------------------------------------------------------+-------------+-------------+-----------------+
| Property              | Description                                                                           | Type        | Data Type   | Reference links |
+-----------------------+---------------------------------------------------------------------------------------+-------------+-------------+-----------------+
| ShowDisplayFieldsOnly | Gets or sets the value incdicating to show only the fields that are used in PivotGrid | Dependency  | Boolean     | \-              |
|                       |                                                                                       |             |             |                 |
|                       |                                                                                       |             |             |                 |
+-----------------------+---------------------------------------------------------------------------------------+-------------+-------------+-----------------+


[] 

Sample Link

A sample is placed in the following location:

**SystemDrive\\Users\\\<user_name\>\\AppData\\Local\\Syncfusion\\EssentialStudio\\\<Version_number\>\\BI\\WPF\\PivotAnalysis.Wpf\\Product Showcase\\PivotGridDemo**

 

[]{#related-topics}

