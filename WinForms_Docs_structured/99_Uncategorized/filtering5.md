---
title: filtering5.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\filtering5.md
created_at: 2025-07-03
---






#### Filtering {#filtering style="tab-stops: 0pt"}

AJAX Grid allows you to restrict the display of records using a mechanism called filters. A filter facilitates the extraction of a subset of records that meet certain criteria. Filters can be applied to one or more columns. This is very useful when dealing with large data sets. The following figure gives you a basic idea of the appearance of the filter bar in the AJAX grid.

The AJAX Grid exposes the following properties to enable and control the filtering feature.

 

+--------------------------+---------------------------------------------------------------------------------------------------------------+----------------------+------------------------+--------------------------+
| **Property**             | **Description**                                                                                               | **Type of property** | **Value It Accepts**   | **Dependencies**         |
+--------------------------+---------------------------------------------------------------------------------------------------------------+----------------------+------------------------+--------------------------+
| AllowFilter              | Enables the filtering feature. Default value is False.                                                        | Boolean              | True                   | NA                       |
|                          |                                                                                                               |                      |                        |                          |
|                          |                                                                                                               |                      | False                  |                          |
|                          |                                                                                                               |                      |                        |                          |
|                          |                                                                                                               |                      | Default value is False |                          |
|                          |                                                                                                               |                      |                        |                          |
|                          |                                                                                                               |                      |                        |                          |
+--------------------------+---------------------------------------------------------------------------------------------------------------+----------------------+------------------------+--------------------------+
| ShowFilterBar            | This property specifies whether the filter bar will be displayed in the grid or not.                          | Boolean              | True                   | Dependent on AllowFilter |
|                          |                                                                                                               |                      |                        |                          |
|                          |                                                                                                               |                      | False                  |                          |
|                          |                                                                                                               |                      |                        |                          |
|                          |                                                                                                               |                      | Default value is True  |                          |
|                          |                                                                                                               |                      |                        |                          |
|                          |                                                                                                               |                      |                        |                          |
+--------------------------+---------------------------------------------------------------------------------------------------------------+----------------------+------------------------+--------------------------+
| AllowActiveFilteringMode | This property specifies whether the filter data will be rendered immediately or after pressing the ENTER key. | Boolean              | True                   | Dependent on AllowFilter |
|                          |                                                                                                               |                      |                        |                          |
|                          |                                                                                                               |                      | False                  |                          |
|                          |                                                                                                               |                      |                        |                          |
|                          |                                                                                                               |                      | Default value is True  |                          |
|                          |                                                                                                               |                      |                        |                          |
|                          |                                                                                                               |                      |                        |                          |
+--------------------------+---------------------------------------------------------------------------------------------------------------+----------------------+------------------------+--------------------------+
| ShowFilterStatusMessage  | This property specifies whether the status message will be displayed in the grid or not.                      | Boolean              | True                   | Dependent on AllowFilter |
|                          |                                                                                                               |                      |                        |                          |
|                          |                                                                                                               |                      | False                  |                          |
|                          |                                                                                                               |                      |                        |                          |
|                          |                                                                                                               |                      | Default value is True  |                          |
|                          |                                                                                                               |                      |                        |                          |
|                          |                                                                                                               |                      |                        |                          |
+--------------------------+---------------------------------------------------------------------------------------------------------------+----------------------+------------------------+--------------------------+
| FilterStatusBarWidth     | This property is used to set the filter status bar width in the grid.                                         | Int                  | +ve Integers           | Dependent on AllowFilter |
|                          |                                                                                                               |                      |                        |                          |
|                          |                                                                                                               |                      |                        |                          |
+==========================+===============================================================================================================+======================+========================+==========================+

 

Server Mode

In server mode, filtering will be done by enabling the property **AllowFilter** and setting the **AllowActiveFilteringMode** property to specify whether filtered data will be rendered on pressing ENTER or immediately, the **ShowFilterBar** property to specify the whether the filter bar will be displayed in the grid or not, the **ShowFilterStatusMessage** property  to set whether the status message will be displayed in the grid or not, and the **FilterStatusBarWidth** property to set the width of the filter status bar as per requirement.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**[]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [\<][Syncfusion][:][GridGroupingControl][ [ID][=\"GridGroupingControl1\"] [runat][=\"server\"] [AjaxAutoformat][=\"Midnight\" ][EnableCallbacks][=\"false\"] [ShowGroupDropArea][=\"false\"]  [EnableAjaxMode][=\"true\"] [\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [\<][TableDescriptor][  [AllowFilter][=\"true\"]  [\>\</][TableDescriptor][\>]]                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [\<][TopLevelGroupOptions][  [AllowActiveFilteringMode][=\"true\"] [ShowFilterBar][=\"true\"] [FilterStatusBarWidth][=\"550\"] [ShowFilterStatusMessage][=\"true\"] [/\>]]                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [\</][Syncfusion][:][GridGroupingControl][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                          |
|                                                                                                                                                                                                 |
| [this][.GridGroupingControl1.TableDescriptor.AllowFilter = [true];]                   |
|                                                                                                                                                                                                 |
| [this][.GridGroupingControl1.TopLevelGroupOptions.ShowFilterBar = [true];]            |
|                                                                                                                                                                                                 |
| [this][.GridGroupingControl1.TopLevelGroupOptions.ShowFilterStatusMessage = [true];]  |
|                                                                                                                                                                                                 |
| [this][.GridGroupingControl1.TopLevelGroupOptions.FilterStatusBarWidth = 550;]                             |
|                                                                                                                                                                                                 |
| [this][.GridGroupingControl1.TopLevelGroupOptions.AllowActiveFilteringMode = [true];] |
|                                                                                                                                                                                                 |
| []                                                                                                                                                          |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**[]                                                                                                       |
|                                                                                                                                                                                              |
| [Me][.GridGroupingControl1.TableDescriptor.AllowFilter = [True]]                   |
|                                                                                                                                                                                              |
| [Me][.GridGroupingControl1.TopLevelGroupOptions.ShowFilterBar = [True]]            |
|                                                                                                                                                                                              |
| [Me][.GridGroupingControl1.TopLevelGroupOptions.ShowFilterStatusMessage = [True]]  |
|                                                                                                                                                                                              |
| [Me][.GridGroupingControl1.TopLevelGroupOptions.FilterStatusBarWidth = 550]                             |
|                                                                                                                                                                                              |
| [Me][.GridGroupingControl1.TopLevelGroupOptions.AllowActiveFilteringMode = [True]] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

The following figure is obtained using the code snippet above.

 

{border="0"}

Figure 137: Filtering

[]{#related-topics}

