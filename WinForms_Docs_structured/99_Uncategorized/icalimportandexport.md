---
title: icalimportandexport.md
original_path: WinForms_Docs/99_Uncategorized/icalimportandexport.md
created_at: 2025-08-05
---








  









## ICal Import and Export {#ical-import-and-export style="tab-stops: 0pt"}

Appointments can be exported from and imported to Schedule, in an internet calendar file (\*.ics) format using this feature.[ ]This way the portability of appointments is enhanced.

The following figure gives you an overview of imported appointments in Schedule:

{border="0"}

Figure 144: Schedule with ICal import and export

The following figures give you a basic idea of the appearance of the output of the feature.

{border="0"}

Figure 145: Import Appointment

 

{border="0"}

Figure 146: Appointment Export

Use Case Scenarios

This feature allows you to share your appointments by enabling you to import and export appointment files.

You can also import appointments on loading Schedule.

 

[]{#_Constructors_for_PDF}Properties

 

+----------------------+------------------------------------------------------------------+---------------------------------------------+----------------------------------------------------+---------------------------------------------------------+
| **Property**         | **Description**                                                  | **Type of property**                        | **Value it accepts**                               | **Dependencies**                                        |
+----------------------+------------------------------------------------------------------+---------------------------------------------+----------------------------------------------------+---------------------------------------------------------+
| ShowImport           | This property is used to show the import icon in Schedule        | bool                                        | True                                               | NA                                                      |
|                      |                                                                  |                                             |                                                    |                                                         |
|                      |                                                                  |                                             | False                                              |                                                         |
+----------------------+------------------------------------------------------------------+---------------------------------------------+----------------------------------------------------+---------------------------------------------------------+
| ShowExport           | This property is used to show the export icon in Schedule        | bool                                        | True                                               | NA                                                      |
|                      |                                                                  |                                             |                                                    |                                                         |
|                      |                                                                  |                                             | False                                              |                                                         |
+----------------------+------------------------------------------------------------------+---------------------------------------------+----------------------------------------------------+---------------------------------------------------------+
| ImportFile           | This property is used to get the file name to import on load.    | string                                      | File name                                          | NA                                                      |
+----------------------+------------------------------------------------------------------+---------------------------------------------+----------------------------------------------------+---------------------------------------------------------+
| ImportedAppointments | This property returns the List of Imported schedule appointments | List\<ScheduleAppointment\>  (i.e. AppList) | Function with argument List\<ScheduleAppointment\> | Depends on the Controller method---                     |
|                      |                                                                  |                                             |                                                    |                                                         |
|                      |                                                                  |                                             |                                                    | The AppList returns its values to the Controller method |
+----------------------+------------------------------------------------------------------+---------------------------------------------+----------------------------------------------------+---------------------------------------------------------+

 

 

Methods

 


  **Name of the method**       **Parameters of the method**   **Return type**   **Descriptions**
  ---------------------------- ------------------------------ ----------------- -------------------------------------------------------------------------
  ScheduleImportActions\<T\>   Import FileName                ActionResult      This method Import all appointment from the given file name
  ScheduleExportActions\<T\>   Export FileName                ActionResult      This method Export all appointment from the schedule to given file name


 

 

Events

 

  --------------- ------------------------------------------------------ --------------- ---------------------
  **Name**        **Description**                                        **Arguments**   **Reference Links**
  ActionBegin     This event is triggered when an action begins.         Events          NA
  ActionSuccess   This event is triggered on the success of an action.   Events          NA
  --------------- ------------------------------------------------------ --------------- ---------------------

 

More:







