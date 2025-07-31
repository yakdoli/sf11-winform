---
title: disablegroupingbyspecificfields.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\disablegroupingbyspecificfields.md
created_at: 2025-07-03
---








  









### Disable Grouping by Specific Fields {#disable-grouping-by-specific-fields style="tab-stops: 0pt"}

This feature enables the user to restrict the drop of certain pivot items that has been dragged either from PivotSchemaDesigner or within pivot grid to the grouping bar at runtime.

Use Case Scenarios

This feature enables the user to restrict grouping for any specific field at runtime.

 

{border="0"}

Figure 23 Showing Disabled Background Color and Cross Icon for Grouping Disabled Items

Properties

Table 3: Properties Table


+-----------------------------+-----------------------------------------------------------------------------------------------+-------------+-------------+------------------------------+
| Property                    | Description                                                                                   | Type        | Data Type   | Reference links              |
+-----------------------------+-----------------------------------------------------------------------------------------------+-------------+-------------+------------------------------+
| AllowRunTimeGroupByField    | Gets or sets the value to enable/disable grouping for PivotItem. The default value is true.   | CLR         | bool        | [- ] |
|                             |                                                                                               |             |             |                              |
|                             |                                                                                               |             |             |                              |
+-----------------------------+-----------------------------------------------------------------------------------------------+-------------+-------------+------------------------------+
| ShowDisabledGroupBackground | Enable/Disable Background color for the grouping disabled fields. The default value is false. | Dependency  | Bool        | [-]  |
|                             |                                                                                               |             |             |                              |
|                             |                                                                                               |             |             |                              |
+-----------------------------+-----------------------------------------------------------------------------------------------+-------------+-------------+------------------------------+


[] 

Sample Link

A sample has been provided in the following location:

***{InstalledLoction}:\\Users\\{User}AppData\\Local\\Syncfusion\\EssentialStudio\\{InstalledVersion}\\BI\\Silverlight\\PivotGrid.SL\\ProductShowcase\\GroupingBarDemo***

[][] 

More:





