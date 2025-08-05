---
title: tablesforpropertiesmethodsandevents24.md
original_path: WinForms_Docs/99_Uncategorized/tablesforpropertiesmethodsandevents24.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Tables for Properties, Methods, and Events {#tables-for-properties-methods-and-events style="tab-stops: 0pt"}

###### 1.6.2.22.2.1        Properties {#properties style="tab-stops: 0pt"}

  -------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------- ---------------
  **Property**               **Description**                                                                                                                                                                                                                                                                                                  **Type**   **Data Type**
  EnableValueEditing         Gets/sets the Boolean value to enable editing in value cells                                                                                                                                                                                                                                                     **CLR**    Boolean
  EnableUpdating             Gets/sets the Boolean value to enable updating                                                                                                                                                                                                                                                                   **CLR**    Boolean
  ThrottleUpdateRate         Gets or sets a millisecond value for time between UI refreshes. Zero indicates immediate refreshes of the UI without delays. Throttling the refresh rate can minimize CPU usage. The default value is zero, but depending upon your updating rate, values of 300 to 500 milliseconds may give lower CPU usage.   **CLR**    Int
  AllowEditingOfTotalCells   Gets/sets the Boolean value to enable editing in total cells                                                                                                                                                                                                                                                     **CLR**    Boolean
  HideExpanders              Gets/sets the Boolean value to hide expanders in the header cells                                                                                                                                                                                                                                                **CLR**    Boolean
  -------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------- ---------------

 

###### 1.6.2.22.2.2        Events {#events style="tab-stops: 0pt"}

+-------------------------------------------------------------+------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+------------------------------------------------------------+
| **[Event ]** [] | **[Description ]** []                        | **[Arguments ]** []                            | **[Type ]** [] |
+-------------------------------------------------------------+------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+------------------------------------------------------------+
| ChangeValue                                                 | Triggered when changing a cell's value. Using this event we can alter the PivotCellInfo. | \<object\> oldValue, \<object \>newValue, \<int\> row1, \<int\> col1, \<PivotCellInfo \>pi | Event                                                      |
|                                                             |                                                                                          |                                                                                            |                                                            |
|                                                             |                                                                                          |                                                                                            |                                                            |
+=============================================================+==========================================================================================+============================================================================================+============================================================+

[] [] 

Sample Link

 

Updating Demo

{InstalledDrive}\\Users\\{User}\\AppData\\Local\\Syncfusion\\EssentialStudio\\{Version}\\BI\\WPF\\PivotAnalysis.Wpf\\Samples\\Interactive Features\\Updating Demo

 

Editing Demo

{InstalledDrive}\\Users\\{User}\\AppData\\Local\\Syncfusion\\EssentialStudio\\{Version}\\BI\\WPF\\PivotAnalysis.Wpf\\Samples\\Interactive Features\\Editing Demo

[] 

[]{#related-topics}

