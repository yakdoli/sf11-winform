---
title: usingschedulepropertiesmodel16.md
original_path: WinForms_Docs/99_Uncategorized/usingschedulepropertiesmodel16.md
created_at: 2025-08-05
---






#### Using SchedulePropertiesModel {#using-schedulepropertiesmodel style="tab-stops: 0pt"}

The steps to customize client-side events using SchedulePropertiesModel are as follows:

1.  [Create a model in the application.](http://help.syncfusion.com/ug_93/User%20Interface/ASP.NET%20MVC/Schedule/Documents/addingamodeltotheapplication.htm)

2.  Add the following code in the Index.aspx file, to create the **Schedule** control in **View**.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View]**[ ]                                                                                                                     |
|                                                                                                                                                                                                                            |
| [       [\<%][=]Html.Syncfusion().Schedule()([\"FlatSchedule\"],[\"ScheduleModel\"])] |
|                                                                                                                                                                                                                            |
| [       .BindList(columns =\>]                                                                                                                                                         |
|                                                                                                                                                                                                                            |
| [       {]                                                                                                                                                                             |
|                                                                                                                                                                                                                            |
| [           columns.IdField([\"AppId\"]);]                                                                                                                     |
|                                                                                                                                                                                                                            |
| [           columns.SubjectField([\"Subject\"]);]                                                                                                              |
|                                                                                                                                                                                                                            |
| [           columns.LocationField([\"Location\"]);]                                                                                                            |
|                                                                                                                                                                                                                            |
| [           columns.StartTimeField([\"StartTime\"]);]                                                                                                          |
|                                                                                                                                                                                                                            |
| [           columns.EndTimeField([\"EndTime\"]);]                                                                                                              |
|                                                                                                                                                                                                                            |
| [           columns.DescriptionField([\"Descrip\"]);]                                                                                                          |
|                                                                                                                                                                                                                            |
| [           columns.OwnerField([\"Resource\"]);]                                                                                                               |
|                                                                                                                                                                                                                            |
| [       })]                                                                                                                                                                            |
|                                                                                                                                                                                                                            |
| [                [%\>]]                                                                                                                                    |
|                                                                                                                                                                                                                            |
| []                                                                                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.  In the controller, add the Syncfusion.Mvc.Schedule and Syncfusion.Mvc.Shared namespaces.

[] 

+-------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                    |
|                                                                                                                         |
| [][]               |
|                                                                                                                         |
| [using][ Syncfusion.Mvc.Schedule;] |
|                                                                                                                         |
| [using][ Syncfusion.Mvc.Shared;]   |
|                                                                                                                         |
| []                                                     |
+-------------------------------------------------------------------------------------------------------------------------+

[] 

4.  Create a **SchedulePropertiesModel** in **Index** method and set **EnableClientSideEvents** property to handle client-side functions.

5.  Define client-side functions for appointment selection and cell double-click.

6.  Pass this **SchedulePropertiesModel** from Controller to View using **ViewData** class as shown below.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                                                              |
|                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                            |
|                                                                                                                                                                                                                                   |
| [        [///][ ][\<summary\>]]                                                                                               |
|                                                                                                                                                                                                                                   |
| [        [///][ It used to bind the Schedule]]                                                                                                     |
|                                                                                                                                                                                                                                   |
| [        [///][ ][\</summary\>]]                                                                                              |
|                                                                                                                                                                                                                                   |
| [        [///][ ][\<returns\>][View page, it displays the Schedule][\</returns\>]] |
|                                                                                                                                                                                                                                   |
| [        [public] [ActionResult] Index()]                                                                                                        |
|                                                                                                                                                                                                                                   |
| [        {]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                   |
| [            [var] data = [new] [NorthwindDataClassesDataContext]().AppointmentTables.Take(200);]                           |
|                                                                                                                                                                                                                                   |
| [            [SchedulePropertiesModel] scheduleModel = [new] [SchedulePropertiesModel]();]                               |
|                                                                                                                                                                                                                                   |
| [            scheduleModel.DataSource = data;]                                                                                                                                                |
|                                                                                                                                                                                                                                   |
| [            scheduleModel.Skins = [ScheduleSkins].Sandune;]                                                                                                          |
|                                                                                                                                                                                                                                   |
| [            scheduleModel.CurrentView = [ScheduleViewMode].Week;]                                                                                                    |
|                                                                                                                                                                                                                                   |
| **[            scheduleModel.EnableClientSideEvents = [true];]**[]                                                                   |
|                                                                                                                                                                                                                                   |
| **[            scheduleModel.ClientSideOnAppointmentSelection=[\"onAppointmentSelection\"];]**[]                                  |
|                                                                                                                                                                                                                                   |
| **[            scheduleModel.ClientSideOnCellDoubleClick = [\"onCellDblClick\"];]**                                                                                   |
|                                                                                                                                                                                                                                   |
| ```                                                                                                                                                                                                    |
|                         scheduleModel.ClientSideOnCellSingleClick = "onCellSingleClick";                                                                                                                                          |
| ```                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                            |
|                                                                                                                                                                                                                                   |
| [            ViewData\[[\"ScheduleModel\"]\] = scheduleModel;]                                                                                                        |
|                                                                                                                                                                                                                                   |
| [            [return] View();]                                                                                                                                           |
|                                                                                                                                                                                                                                   |
| [        }]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                   |
| []                                                                                                                                                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

7.  Create a post method for Index action and bind the data source to **Schedule**, as shown in the code displayed below in order to work with post actions.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                      |
| [        [///][ ][\<summary\>]]                                                                                                                                  |
|                                                                                                                                                                                                                                                                      |
| [        [///][ Post Requests are mapped to this method. This method invokes the HtmlActionResult]]                                                                                   |
|                                                                                                                                                                                                                                                                      |
| [        [///][ from the Schedule. Required response is generated.]]                                                                                                                  |
|                                                                                                                                                                                                                                                                      |
| [        [///][ ][\</summary\>]]                                                                                                                                 |
|                                                                                                                                                                                                                                                                      |
| [        [///][ ][\<param name=\"args\"\>][Contains post action properties ][\</param\>]]                             |
|                                                                                                                                                                                                                                                                      |
| [        [///][ ][\<returns\>]]                                                                                                                                  |
|                                                                                                                                                                                                                                                                      |
| [        [///][ HtmlActionResult which returns data displayed on the Schedule]]                                                                                                       |
|                                                                                                                                                                                                                                                                      |
| [        [///][ ][\</returns\>]][]                                                                           |
|                                                                                                                                                                                                                                                                      |
| [        \[[AcceptVerbs]([HttpVerbs].Post)\]]                                                                                                                   |
|                                                                                                                                                                                                                                                                      |
| [        [public] [ActionResult] Index([Params] args)]                                                                                     |
|                                                                                                                                                                                                                                                                      |
| [        {]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                      |
| [IEnumerable][ data = [new] [NorthwindDataClassesDataContext]().AppointmentTables.Take(200);] |
|                                                                                                                                                                                                                                                                      |
| [            [return] data.ScheduleActions\<[ScheduleHtmlActionResult]\>();]                                                                                       |
|                                                                                                                                                                                                                                                                      |
| [        }]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[JavaScript\]]**                                                                                                                                                                        |
|                                                                                                                                                                                                                                 |
| [  ][    [\<][script] [type][=\"text/javascript\"\>]] |
|                                                                                                                                                                                                                                 |
| [        [// To handle the appointment selection event]]                                                                                                          |
|                                                                                                                                                                                                                                 |
| [        [function] onAppointmentSelection(sender, args) {]                                                                                                            |
|                                                                                                                                                                                                                                 |
| [            [// sender - Schedule control details]]                                                                                                              |
|                                                                                                                                                                                                                                 |
| [            [// args - id -\> selected appointment id]]                                                                                                          |
|                                                                                                                                                                                                                                 |
| [            [// args - currentItem -\> selected appointment details]]                                                                                            |
|                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                 |
| [        [// To handle the cell double click ]]                                                                                                                   |
|                                                                                                                                                                                                                                 |
| [        [function] onCellDblClick(sender, args) {]                                                                                                                    |
|                                                                                                                                                                                                                                 |
| [            [// sender - Schedule control details]]                                                                                                              |
|                                                                                                                                                                                                                                 |
| [            [// args - selectedDate -\> selected cell\'s date]]                                                                                                  |
|                                                                                                                                                                                                                                 |
| [            [// args - selectedStartTime -\> selected cell\'s start time]]                                                                                       |
|                                                                                                                                                                                                                                 |
| [            [// args - selectedEndTime -\> selected cell\'s end time]]                                                                                           |
|                                                                                                                                                                                                                                 |
| [            [// args - selectedResourceId -\> selected cell\'s owner id]]                                                                                        |
|                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                 |
| [// To handle the cell single click ][]                                                                                               |
|                                                                                                                                                                                                                                 |
| [        [function] onCellSingleClick(sender, args) {]                                                                                                                 |
|                                                                                                                                                                                                                                 |
| [            [// sender - Schedule control details]]                                                                                                              |
|                                                                                                                                                                                                                                 |
| [            [// args - selectedDate -\> selected cell\'s date]]                                                                                                  |
|                                                                                                                                                                                                                                 |
| [            [// args - selectedStartTime -\> selected cell\'s start time]]                                                                                       |
|                                                                                                                                                                                                                                 |
| [            [// args - selectedEndTime -\> selected cell\'s end time]]                                                                                           |
|                                                                                                                                                                                                                                 |
| [            [// args - selectedResourceId -\> selected cell\'s owner id]]                                                                                        |
|                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                 |
| [    [\</][script][\>]]                                                                                                    |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

8.  Run the application. The Schedule will appear when the cell is clicked as shown below.

{border="0"}

Figure 139: Cell Single Click Event

 

Events

+------------------------------------------------------------+-----------------------------------------------------------------------------+----------------------------------------------------------------+-----------------------------------------------------------+
| **[Event ]**[] | **[Description ]**[]            | **[Arguments ]**[] | **[Type ]**[] |
+------------------------------------------------------------+-----------------------------------------------------------------------------+----------------------------------------------------------------+-----------------------------------------------------------+
| ClientSideOnCellSingleClick                                | The ClientSideOnCellSingleClick event will be fired when a cell is clicked. | selectedDate---Selected cell' date                             | Client Side                                               |
|                                                            |                                                                             |                                                                |                                                           |
|                                                            |                                                                             | selectedStartTime---Selected cell's start time.                |                                                           |
|                                                            |                                                                             |                                                                |                                                           |
|                                                            |                                                                             | selectedEndTime---Selected cell's end time.                    |                                                           |
|                                                            |                                                                             |                                                                |                                                           |
|                                                            |                                                                             | selectedResourceId---Selected cell's resource ID.              |                                                           |
+============================================================+=============================================================================+================================================================+===========================================================+

[][] 

Sample Link

Refer to steps 1.1 and 1.2 for procedural steps of the sample.[]

[]{#related-topics}

