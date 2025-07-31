---
title: usingschedulepropertiesmodel5.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingschedulepropertiesmodel5.md
created_at: 2025-07-03
---






##### Using SchedulePropertiesModel {#using-schedulepropertiesmodel style="tab-stops: 0pt"}

The steps to customize delete an appointment using SchedulePropertiesModel are as follows:

1.   [Create a model in the application]{.UGHyperlink}[.][ ]

2.   Add the following code in the Index.aspx file, to create the Schedule control in **View**.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**[[]]{.MsoIntenseEmphasis}                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                               |
| [   ][    [\<%][=]Html.Syncfusion().Schedule()([\"FlatSchedule\"] ,[\"ScheduleModel\"])[]] |
|                                                                                                                                                                                                                                                                                                               |
| [       .BindList(columns =\>]                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                               |
| [       {]                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                               |
| [           columns.IdField([\"AppId\"]);]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                               |
| [           columns.SubjectField([\"Subject\"]);]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                               |
| [           columns.LocationField([\"Location\"]);]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                               |
| [           columns.StartTimeField([\"StartTime\"]);]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                               |
| [           columns.EndTimeField([\"EndTime\"]);]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                               |
| [           columns.DescriptionField([\"Descrip\"]);]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                               |
| [           columns.OwnerField([\"Resource\"]);]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                               |
| [       })]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                               |
| [       [%\>]][]                                                                                                                                                                        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**[[]]{.MsoIntenseEmphasis}                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                         |
| [   ][    ][@(][ Html.Syncfusion().Schedule()([\"FlatSchedule\"] ,[\"ScheduleModel\"])] |
|                                                                                                                                                                                                                                                                                                                                                         |
| [       .BindList(columns =\>]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                         |
| [       {]                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                         |
| [           columns.IdField([\"AppId\"]);]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                         |
| [           columns.SubjectField([\"Subject\"]);]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                         |
| [           columns.LocationField([\"Location\"]);]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                         |
| [           columns.StartTimeField([\"StartTime\"]);]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                         |
| [           columns.EndTimeField([\"EndTime\"]);]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                         |
| [           columns.DescriptionField([\"Descrip\"]);]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                         |
| [           columns.OwnerField([\"Resource\"]);]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                         |
| [       })[)]]                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

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

4.   Create a **SchedulePropertiesModel** in the **Index** method.

5.   Use **AllowDelete** property to delete an appointment through **AppointmentDoubleClick** Event.

6.   Create context-menu item and set the **contextMenuItems** property to delete an appointment through Context-menu.

7.   Pass this **SchedulePropertiesModel** from **Controller** to **View** using **ViewData** classes given below.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                                                                                                          |
|                                                                                                                                                                                                                                            |
| [        [///][ ][\<summary\>]]                                                                                               |
|                                                                                                                                                                                                                                            |
| [        [///][ It is used to bind the Schedule]]                                                                                                  |
|                                                                                                                                                                                                                                            |
| [        [///][ ][\</summary\>]]                                                                                              |
|                                                                                                                                                                                                                                            |
| [        [///][ ][\<returns\>][View page, it displays the Schedule][\</returns\>]] |
|                                                                                                                                                                                                                                            |
| [        [public] [ActionResult] Index()]                                                                                                        |
|                                                                                                                                                                                                                                            |
| [        {]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                            |
| [ContextMenuItem][ deleteApp = [new] [ContextMenuItem]() ]                          |
|                                                                                                                                                                                                                                            |
| [{ ]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                            |
| [MenuID = [\"DeleteAppointment\"], ]                                                                                                                                  |
|                                                                                                                                                                                                                                            |
| [MenuName = [\"Delete Appointment\"], ]                                                                                                                               |
|                                                                                                                                                                                                                                            |
| [CommandName = [ContextCommandNames].DeleteAppointment ]                                                                                                              |
|                                                                                                                                                                                                                                            |
| [};]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                            |
| [                [var] data = [new] [NorthwindDataClassesDataContext]().AppointmentTables.Take(200);]                       |
|                                                                                                                                                                                                                                            |
| [                [SchedulePropertiesModel] scheduleModel = [new] [SchedulePropertiesModel]();]                           |
|                                                                                                                                                                                                                                            |
| [                scheduleModel.DataSource = data;]                                                                                                                                            |
|                                                                                                                                                                                                                                            |
| [                 scheduleModel.Skins = [ScheduleSkins].Sandune;]                                                                                                     |
|                                                                                                                                                                                                                                            |
| **[                scheduleModel.AllowDelete = [true];]**                                                                                                                |
|                                                                                                                                                                                                                                            |
| **[scheduleModel.ContextMenuItems = [new] [List]\<[ContextMenuItem]\>() { deleteApp };]**                                |
|                                                                                                                                                                                                                                            |
| [                ViewData\[[\"ScheduleModel\"]\] = scheduleModel;]                                                                                                    |
|                                                                                                                                                                                                                                            |
| [                [return] View();]                                                                                                                                       |
|                                                                                                                                                                                                                                            |
| [        }]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

8.   Create a post method for Index action and bind the data source to Schedule, as shown in the code displayed below.

[[]]{.MsoIntenseEmphasis} 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**[[]]{.MsoIntenseEmphasis}                                                                                      |
|                                                                                                                                                                                                                                                   |
| [  ][      [///][ ][\<summary\>]]                                          |
|                                                                                                                                                                                                                                                   |
| [        [///][ Post Requests are mapped to this method. This method invokes the HtmlActionResult]]                                                       |
|                                                                                                                                                                                                                                                   |
| [        [///][ from the Schedule. Required response is generated.]]                                                                                      |
|                                                                                                                                                                                                                                                   |
| [        [///][ ][\</summary\>]]                                                                                                     |
|                                                                                                                                                                                                                                                   |
| [        [///][ ][\<param name=\"args\"\>][Contains post action properties ][\</param\>]] |
|                                                                                                                                                                                                                                                   |
| [        [///][ ][\<returns\>]]                                                                                                      |
|                                                                                                                                                                                                                                                   |
| [        [///][ HtmlActionResult which returns data displayed on the Schedule]]                                                                           |
|                                                                                                                                                                                                                                                   |
| [        [///][ ][\</returns\>]]                                                                                                     |
|                                                                                                                                                                                                                                                   |
| [        \[[AcceptVerbs]([HttpVerbs].Post)\]]                                                                                                        |
|                                                                                                                                                                                                                                                   |
| [        [public] [ActionResult] Index([Params] args)]                                                                          |
|                                                                                                                                                                                                                                                   |
| [        {]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                   |
| [NorthwindDataClassesDataContext][ db = [new] [NorthwindDataClassesDataContext]();]        |
|                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                   |
| [            [// Select the particular appointment with args.AppID and delete it]]                                                                                             |
|                                                                                                                                                                                                                                                   |
| [            [if] (args.CurrentAction == [\"Delete\"])]                                                                                                 |
|                                                                                                                                                                                                                                                   |
| [            {]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                   |
| [                [AppointmentTable] app = db.AppointmentTables.Where(c =\> c.AppId == [Convert].ToInt32(args.AppID)).FirstOrDefault();]              |
|                                                                                                                                                                                                                                                   |
| [                [if] (app != [null]) db.AppointmentTables.DeleteOnSubmit(app);]                                                                           |
|                                                                                                                                                                                                                                                   |
| [            }]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                   |
| [            [//to reflect in database]]                                                                                                                                       |
|                                                                                                                                                                                                                                                   |
| [            db.SubmitChanges();]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                   |
| [            [ActionResult] result = db.AppointmentTables.ScheduleActions\<[ScheduleHtmlActionResult]\>();]                                          |
|                                                                                                                                                                                                                                                   |
| [            [return] result;]                                                                                                                                                  |
|                                                                                                                                                                                                                                                   |
| [        }]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

9.   Run the application. The Schedule's appointment window will appear as shown below when double-clicking any appointment**.**

[] 

{border="0"}

Figure 112: Appointment dialog when double click an appointment

[] 

10.  On the **Appointment dialog** toolbar, click **Delete** OR

Right-click an appointment and click **Delete Appointment.** The confirmation dialog will appear as shown below.

[] 

{border="0"}

[] 

Figure 113: Appointment dialog with confirmation alert

[] 

11.  On the confirmation dialog, click **OK**.

[] 

[]{#related-topics}

