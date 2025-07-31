---
title: unhidecolumnbydoubleclickingdisabled.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\unhidecolumnbydoubleclickingdisabled.md
created_at: 2025-07-03
---






##### Unhide Column by Double-Clicking Disabled {#unhide-column-by-double-clicking-disabled style="tab-stops: 0pt"}

Essential Grid has changed the unhide column operation to emulate the behavior found in Microsoft Excel. Previously, hidden columns could be shown by double-clicking a row. This behavior has been disabled so that applications created using Essential Grid will be similar to the hide/unhide behavior found in Microsoft Excel.

 

 

Properties

 

*[Table ][2][: Property Table]*


  ---------------------- --------------------------------------------------------------------------------- ---------- --------------- ---------------------
  **Property**           **Description**                                                                   **Type**   **Data Type**   **Reference links**
  UnHideColsOnDblClick   Indicates whether to allow unhide the hidden columns when double click the row.   Property   Boolean         N/A.
  ---------------------- --------------------------------------------------------------------------------- ---------- --------------- ---------------------


[] 

Sample Link

A demo of this feature is available in the following location:

***..\\..\\AppData\\Local\\Syncfusion\\EssentialStudio\\{Installed Version}\\Windows\\Grid.Windows\\Samples\\2.0\\Grid Layout\\Hide Rows and Columns Demo***

**** 

**** 

Disabling Unhide Column by Double-Clicking

To disable unhide column by double- clicking, set the *UnHideColsOnDblClick* property to true. By default this is set to true.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                              |
|                                                                                                                                                                               |
| [     //Disables unhide column when ][double clicking as found in Excel.] |
|                                                                                                                                                                               |
| [            [this].gridControl1.UnHideColsOnDblClick = [true];]                                |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                              |
|                                                                                                                                                                                                                             |
| [     \'Disables unhide column when double clicking as found in Excel.]                                                                                                   |
|                                                                                                                                                                                                                             |
| [            ][Me][.gridControl1.UnHideColsOnDblClick = [True]] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

**[]** 

 

 

[]{#related-topics}

