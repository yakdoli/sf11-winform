---
title: members1.md
original_path: WinForms_Docs/99_Uncategorized/members1.md
created_at: 2025-08-05
---








  









## Members {#members style="TEXT-ALIGN: justify; tab-stops: 0pt"}

**[Properties]**

Table 4: Properties Table**[]**


  ---------------------------- ----------------------------------------------------------------------------------------- --------------------- ----------------------------
  **Property**                 **Description**                                                                           **Type**              **Data Type**
  DataSources                  Gets a collection of data sources used by the report.                                      -                    ReportDataSourceCollection
  CurrentPage                  Gets or sets the current page                                                             Dependency Property   Int
  ShowPrintButton              Gets or sets a value that indicates whether **Print** button is visible on the toolbar.   Dependency Property   Bool
  ShowRefreshButton            Gets or sets a value that indicates whether the **Refresh** button is visible.            Dependency Property   Bool
  ShowToolBar                  Gets or sets a value that indicates whether the toolbar is visible on the control.        Dependency Property   Bool
  ShowZoomControl              Gets or sets a value that indicates whether the **Zoom** list box is visible.             Dependency Property   Bool
  ViewMode                     Gets or sets a value that indicates whether it is Normal or Print View                    Dependency Property   Enum
  ShowPageNavigationControls   Get or set a value that indicates whether the Show navigationcontrols is visible          Dependency Property   Bool
  ---------------------------- ----------------------------------------------------------------------------------------- --------------------- ----------------------------


 

**[Methods]**

Table 5: Methods Table**[]**


+-----------------+-------------------------------------------------------+------------------------------+-------------------------------+
| **Method**      | **Description**                                       | **Parameters**               | **Return Type**               |
+-----------------+-------------------------------------------------------+------------------------------+-------------------------------+
| RefreshReport   | Causes the local report to be rendered with new data. | [ ]- | Void                          |
+-----------------+-------------------------------------------------------+------------------------------+-------------------------------+
| GetParameters   | Get the necessary parameters for the report           | \-                           | ReportParameterInfoCollection |
|                 |                                                       |                              |                               |
|                 |                                                       |                              |                               |
+-----------------+-------------------------------------------------------+------------------------------+-------------------------------+
| GetTotalPage    | Gets the total pages of the report                    | \-                           | int                           |
|                 |                                                       |                              |                               |
|                 |                                                       |                              |                               |
+-----------------+-------------------------------------------------------+------------------------------+-------------------------------+
| GetDataSetNames | Get the dataset names from the local report           | \-                           | IList\<string\>               |
|                 |                                                       |                              |                               |
|                 |                                                       |                              |                               |
+-----------------+-------------------------------------------------------+------------------------------+-------------------------------+
| LoadReport      | Loads the local report for processing                 | Stream                       | void                          |
|                 |                                                       |                              |                               |
|                 |                                                       |                              |                               |
|                 |                                                       |                              |                               |
|                 |                                                       |                              |                               |
+-----------------+-------------------------------------------------------+------------------------------+-------------------------------+
| Print           | Displays the **Print** dialog box.                    | \-                           | Void                          |
|                 |                                                       |                              |                               |
|                 |                                                       |                              |                               |
+-----------------+-------------------------------------------------------+------------------------------+-------------------------------+
| ShowNormalView  | Displays the Normal view of the report                | \-                           | Void                          |
|                 |                                                       |                              |                               |
|                 |                                                       |                              |                               |
+-----------------+-------------------------------------------------------+------------------------------+-------------------------------+
| SetParameters   | Set the necessary parameters for the report           | ReportParameter\[\]          | Void                          |
|                 |                                                       |                              |                               |
|                 |                                                       |                              |                               |
+=================+=======================================================+==============================+===============================+


**[]** 

**[Events]**

Table 6: Events Table**[]**


+-----------------------------------+---------------------------------------------------------------------------------+
| **Event**                         | **Description**                                                                 |
+-----------------------------------+---------------------------------------------------------------------------------+
| ViewModeChanged                   | The event is triggered when the view is changed to normal and print view        |
|                                   |                                                                                 |
|                                   |                                                                                 |
+-----------------------------------+---------------------------------------------------------------------------------+
| ViewButtonClick                   | The event is triggered when the view button is clicked                          |
|                                   |                                                                                 |
|                                   |                                                                                 |
+-----------------------------------+---------------------------------------------------------------------------------+
| SubreportProcessing               | The event will be triggered if the report is RDLC and contains with sub report. |
|                                   |                                                                                 |
|                                   |                                                                                 |
+===================================+=================================================================================+


[]{#related-topics}

