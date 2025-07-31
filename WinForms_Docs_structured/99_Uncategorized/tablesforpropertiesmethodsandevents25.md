---
title: tablesforpropertiesmethodsandevents25.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\tablesforpropertiesmethodsandevents25.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Tables for Properties, Methods, and Events {#tables-for-properties-methods-and-events style="tab-stops: 0pt"}

###### 1.6.2.23.2.1        Properties {#properties style="tab-stops: 0pt"}

  ------------------------------------------------ -------------------------------------------------------------------------------------------- ------------ ---------------
  **Property**                                     **Description**                                                                              **Type**     **Data Type**
  [EnableContextMenu]   Gets or sets the context menu for expander cells (row header and column header cells only)   Dependency   Boolean
  ------------------------------------------------ -------------------------------------------------------------------------------------------- ------------ ---------------

[] 

###### 1.6.2.23.2.2        Methods {#methods style="tab-stops: 0pt"}

+----------------------------------+-------------------------------------------------------------+----------------+-------------+-----------------+
| **Method**                       | **Description**                                             | **Parameters** | **Type**    | **Return Type** |
+----------------------------------+-------------------------------------------------------------+----------------+-------------+-----------------+
| ExpandRow(string)                | Expands the group for the given row UniqueText.             | string         | NA          | void            |
+----------------------------------+-------------------------------------------------------------+----------------+-------------+-----------------+
| ExpandColumn (string)            | Expands the group for the given column UniqueText.          | string         | NA          | void            |
|                                  |                                                             |                |             |                 |
|                                  |                                                             |                |             |                 |
+----------------------------------+-------------------------------------------------------------+----------------+-------------+-----------------+
| CollapseRow(string)              | Collapse the group for the given row UniqueText.            | string         | NA          | void            |
|                                  |                                                             |                |             |                 |
|                                  |                                                             |                |             |                 |
+----------------------------------+-------------------------------------------------------------+----------------+-------------+-----------------+
| CollapseColumn (string)          | Collapse the group for the given column UniqueText.         | string         | NA          | void            |
|                                  |                                                             |                |             |                 |
|                                  |                                                             |                |             |                 |
+----------------------------------+-------------------------------------------------------------+----------------+-------------+-----------------+
| ExpandRow(List\<string\>)        | Expands the group for the given list of row UniqueText.     | List\<string\> | NA          | void            |
|                                  |                                                             |                |             |                 |
|                                  |                                                             |                |             |                 |
+----------------------------------+-------------------------------------------------------------+----------------+-------------+-----------------+
| ExpandColumn (List\<string\>)    | Expands the group for the given list of column UniqueText.  | List\<string\> | NA          | void            |
|                                  |                                                             |                |             |                 |
|                                  |                                                             |                |             |                 |
+----------------------------------+-------------------------------------------------------------+----------------+-------------+-----------------+
| CollapseRow(List\<string\>)      | Collapse the group for the given list of row UniqueText.    | List\<string\> | NA          | void            |
|                                  |                                                             |                |             |                 |
|                                  |                                                             |                |             |                 |
+----------------------------------+-------------------------------------------------------------+----------------+-------------+-----------------+
| CollapseColumn (List\<string\>)  | Collapse the group for the given list of column UniqueText. | List\<string\> | NA          | void            |
|                                  |                                                             |                |             |                 |
|                                  |                                                             |                |             |                 |
+==================================+=============================================================+================+=============+=================+

[] 

###### 1.6.2.23.2.3        Events {#events style="tab-stops: 0pt"}

+-----------------+-------------------------------------------------------------------------------------------------+-----------------+-----------------+
| **Event**       | **Description**                                                                                 | **Arguments**   | **Type**        |
+-----------------+-------------------------------------------------------------------------------------------------+-----------------+-----------------+
| ExpandCollapse  | Provides enabling/disabling option for expand/collapse for a specific group (using UniqueText). | NA              | Event           |
|                 |                                                                                                 |                 |                 |
|                 |                                                                                                 |                 |                 |
+=================+=================================================================================================+=================+=================+

[] [] 

Sample Link

A sample is available in the Syncfusion WPF BI dashboard in the following location.

**PivotAnalysis** \> **GroupingBar** \> **Context Menu Demo**

{InstalledDrive}\\Users\\ {User}\\AppData\\ Local \\Syncfusion\\ EssentialStudio\\{Installed Version}\\BI\\WPF\\PivotAnalysis.Wpf\\Samples\\Grouping Bar \\Context Menu Demo

[] 

[]{#related-topics}

