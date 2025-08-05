---
title: usingschedulepropertiesmodel17.md
original_path: WinForms_Docs/99_Uncategorized/usingschedulepropertiesmodel17.md
created_at: 2025-08-05
---






#### Using SchedulePropertiesModel {#using-schedulepropertiesmodel style="tab-stops: 0pt"}

The steps to customize context menu using SchedulePropertiesModel are as follows:

1.   [Create a model in the application]{.UGHyperlink}[.][ ]

2.   Add the following code in the Index.aspx file, to create the Schedule control in **View**.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**[[]]{.MsoIntenseEmphasis}                                                                                                    |
|                                                                                                                                                                                                                                                               |
| [       [\<%][=]Html.Syncfusion().Schedule()([\"FlatSchedule\"],[\"ScheduleModel\"])[]] |
|                                                                                                                                                                                                                                                               |
| [       .BindList(columns =\>]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                               |
| [       {]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                               |
| [           columns.IdField([\"AppId\"]);]                                                                                                                                               |
|                                                                                                                                                                                                                                                               |
| [           columns.SubjectField([\"Subject\"]);]                                                                                                                                        |
|                                                                                                                                                                                                                                                               |
| [           columns.LocationField([\"Location\"]);]                                                                                                                                      |
|                                                                                                                                                                                                                                                               |
| [           columns.StartTimeField([\"StartTime\"]);]                                                                                                                                    |
|                                                                                                                                                                                                                                                               |
| [           columns.EndTimeField([\"EndTime\"]);]                                                                                                                                        |
|                                                                                                                                                                                                                                                               |
| [           columns.DescriptionField([\"Descrip\"]);]                                                                                                                                    |
|                                                                                                                                                                                                                                                               |
| [           columns.OwnerField([\"Resource\"]);]                                                                                                                                         |
|                                                                                                                                                                                                                                                               |
| [       })]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                               |
| [      [%\>]]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**[[]]{.MsoIntenseEmphasis}                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                         |
| [       ][@(][ Html.Syncfusion().Schedule()([\"FlatSchedule\"],[\"ScheduleModel\"])] |
|                                                                                                                                                                                                                                                                                                         |
| [       .BindList(columns =\>]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                         |
| [       {]                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                         |
| [           columns.IdField([\"AppId\"]);]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                         |
| [           columns.SubjectField([\"Subject\"]);]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                         |
| [           columns.LocationField([\"Location\"]);]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                         |
| [           columns.StartTimeField([\"StartTime\"]);]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                         |
| [           columns.EndTimeField([\"EndTime\"]);]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                         |
| [           columns.DescriptionField([\"Descrip\"]);]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                         |
| [           columns.OwnerField([\"Resource\"]);]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                         |
| [       })[)]]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   In Controller, add the Syncfusion.Mvc.Schedule, Syncfusion.Mvc.Shared namespaces.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**[[]]{.MsoIntenseEmphasis} |
|                                                                                                                                                              |
| [using][ Syncfusion.Mvc.Schedule;]                    |
|                                                                                                                                                              |
| [using][ Syncfusion.Mvc.Shared;]                      |
|                                                                                                                                                              |
| []                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Create a **SchedulePropertiesModel** in the **Index** method and set **ContextMenuItems** property to show Context menu on appointment and Schedule cell.

5.   Pass this **SchedulePropertiesModel** from Controller to View using **ViewData** class as shown  below.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                               |
| [        [///][ ][\<summary\>]]                                                                                                                                  |
|                                                                                                                                                                                                                                                                               |
| [        [///][ It is used to bind the Schedule]]                                                                                                                                     |
|                                                                                                                                                                                                                                                                               |
| [        [///][ ][\</summary\>]]                                                                                                                                 |
|                                                                                                                                                                                                                                                                               |
| [        [///][ ][\<returns\>][View page, it displays the Schedule][\</returns\>]]                                    |
|                                                                                                                                                                                                                                                                               |
| [        [public] [ActionResult] Index()]                                                                                                                                           |
|                                                                                                                                                                                                                                                                               |
| [        {]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                               |
| [            [var] data = [new] [NorthwindDataClassesDataContext]().AppointmentTables.Take(200);]                                                              |
|                                                                                                                                                                                                                                                                               |
| [            [SchedulePropertiesModel] schduleModel = [new] [SchedulePropertiesModel]();]                                                                   |
|                                                                                                                                                                                                                                                                               |
| [            ScheduleModel.DataSource = data;]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                               |
| [            [// Creating context menu items]]                                                                                                                                                             |
|                                                                                                                                                                                                                                                                               |
| [            [ContextMenuItem] newapp = [new] [ContextMenuItem]() ]                                                                                         |
|                                                                                                                                                                                                                                                                               |
| [{ ]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                               |
| [MenuID = [\"NewAppointment\"], ]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                               |
| [MenuName = [\"New Appointment\"], ]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                               |
| [CommandName = [ContextCommandNames].NewAppointment ]                                                                                                                                                    |
|                                                                                                                                                                                                                                                                               |
| [};]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                               |
| [            [ContextMenuItem] recurMnu = [new] [ContextMenuItem]() ]                                                                                       |
|                                                                                                                                                                                                                                                                               |
| [{ ]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                               |
| [MenuID = [\"RecurAppointment\"], ]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                               |
| [MenuName = [\"Recur Appointment\"], ]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                               |
| [CommandName = [ContextCommandNames].NewRecurringAppointment ]                                                                                                                                           |
|                                                                                                                                                                                                                                                                               |
| [};]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                               |
| [            [ContextMenuItem] todayMnu = [new] [ContextMenuItem]() ]                                                                                       |
|                                                                                                                                                                                                                                                                               |
| [{ ]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                               |
| [MenuID = [\"todayMnu\"], ]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                               |
| [MenuName = [\"Go to Today \"], ]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                               |
| [CommandName = [ContextCommandNames].GoToToday ]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                               |
| [};]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                               |
| [            [ContextMenuItem] openMnu = [new] [ContextMenuItem]() ]                                                                                        |
|                                                                                                                                                                                                                                                                               |
| [{ ]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                               |
| [MenuID = [\"OpenAppointment\"], ]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                               |
| [MenuName = [\"Open Appointment\"], ]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                               |
| [CommandName = [ContextCommandNames].OpenAppointment ]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                               |
| [};]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                               |
| [            [ContextMenuItem] quickMnu = [new] [ContextMenuItem]() ]                                                                                       |
|                                                                                                                                                                                                                                                                               |
| [{ ]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                               |
| [MenuID = [\"PrintAppointment\"], ]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                               |
| [MenuName = [\"Print Appointment\"], ]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                               |
| [CommandName = [ContextCommandNames].QuickPrint ]                                                                                                                                                        |
|                                                                                                                                                                                                                                                                               |
| [};]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                               |
| [            [ContextMenuItem] delMnu = [new] [ContextMenuItem]() ]                                                                                         |
|                                                                                                                                                                                                                                                                               |
| [{ ]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                               |
| [MenuID = [\"DeleteAppointment\"], ]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                               |
| [MenuName = [\"Remove Appointment\"], ]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                               |
| [CommandName = [ContextCommandNames].DeleteAppointment ]                                                                                                                                                 |
|                                                                                                                                                                                                                                                                               |
| [};]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                               |
| [            [ContextMenuItem] menuItem1 = [new] [ContextMenuItem]() ]                                                                                      |
|                                                                                                                                                                                                                                                                               |
| [{ ]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                               |
| [MenuID = [\"MenuItem1\"], ]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                               |
| [MenuName = [\"Menu Item1\"], ]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                               |
| [CommandName = [ContextCommandNames].UserDefined ]                                                                                                                                                       |
|                                                                                                                                                                                                                                                                               |
| [};]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                               |
| [            [ContextMenuItem] menuItem2 = [new] [ContextMenuItem]() ]                                                                                      |
|                                                                                                                                                                                                                                                                               |
| [{ ]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                               |
| [MenuID = [\"MenuItem2\"], ]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                               |
| [MenuName = [\"Menu Item2\"], ]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                               |
| [CommandName = [ContextCommandNames].UserDefined ]                                                                                                                                                       |
|                                                                                                                                                                                                                                                                               |
| [};]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                               |
| [            [//Adding context menu items into Schedule model class]]                                                                                                                                      |
|                                                                                                                                                                                                                                                                               |
| **[scheduleModel.ContextMenuItems = [new] [List]\<[ContextMenuItem]\>() { newapp, recurMnu, todayMnu, openMnu, quickMnu, delMnu, menuItem1, menuItem2 };]** |
|                                                                                                                                                                                                                                                                               |
| [scheduleModel.Skins = [ScheduleSkins].Sandune;]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                               |
| [                scheduleModel.CurrentView = [ScheduleViewMode].Day;]                                                                                                                                    |
|                                                                                                                                                                                                                                                                               |
| [                ViewData\[[\"ScheduleModel\"]\] = ScheduleModel;]                                                                                                                                       |
|                                                                                                                                                                                                                                                                               |
| [                [return] View();]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                               |
| [        }]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

6.   Create a post method for **Index** action and bind the data source to **Schedule**, as shown in the code displayed below.

[[]]{.MsoIntenseEmphasis} 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**[[]]{.MsoIntenseEmphasis}                                                                                         |
|                                                                                                                                                                                                                                                      |
| [        [///][ ][\<summary\>]]                                                                                                         |
|                                                                                                                                                                                                                                                      |
| [        [///][ Post Requests are mapped to this method. This method invokes the HtmlActionResult]]                                                          |
|                                                                                                                                                                                                                                                      |
| [        [///][ from the Schedule. Required response is generated.]]                                                                                         |
|                                                                                                                                                                                                                                                      |
| [        [///][ ][\</summary\>]]                                                                                                        |
|                                                                                                                                                                                                                                                      |
| [        [///][ ][\<param name=\"args\"\>][Contains post action properties ][\</param\>]]    |
|                                                                                                                                                                                                                                                      |
| [        [///][ ][\<returns\>]]                                                                                                         |
|                                                                                                                                                                                                                                                      |
| [        [///][ HtmlActionResult which returns data displayed on the Schedule]]                                                                              |
|                                                                                                                                                                                                                                                      |
| [        [///][ ][\</returns\>]]                                                                                                        |
|                                                                                                                                                                                                                                                      |
| [        \[[AcceptVerbs]([HttpVerbs].Post)\]]                                                                                                           |
|                                                                                                                                                                                                                                                      |
| [        [public] [ActionResult] Index([Params] args)]                                                                             |
|                                                                                                                                                                                                                                                      |
| [        {]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                      |
| [IEnumerable][ data = [new] [NorthwindDataClassesDataContext]().AppointmentTables.Take(200);] |
|                                                                                                                                                                                                                                                      |
| [                [return] data.ScheduleActions\<[ScheduleHtmlActionResult]\>();]                                                                           |
|                                                                                                                                                                                                                                                      |
| [        }]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[[]]{.MsoIntenseEmphasis} 

7.   Run the application. The Schedule will appear as shown in the following screenshot with the default Context menu items and custom Context menu items when right-clicked on the appointment.

[] 

{border="0"}

Figure 142: Appointment Context-Menu

[] 

8.   The Schedule will appear as shown in the following screenshot with the default Context menu items and custom Context menu items when right-clicked on the cell.

{border="0"}

Figure 143: Cell Context-Menu

[] 

[]{#related-topics}

