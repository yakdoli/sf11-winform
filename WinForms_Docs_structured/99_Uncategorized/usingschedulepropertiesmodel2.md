---
title: usingschedulepropertiesmodel2.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingschedulepropertiesmodel2.md
created_at: 2025-07-03
---






##### Using SchedulePropertiesModel {#using-schedulepropertiesmodel style="tab-stops: 0pt"}

The steps to customize the Create New Appointment using SchedulePropertiesModel are as follows:

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
| [       [%\>]]                                                                                                                                                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**[[]]{.MsoIntenseEmphasis}                                                    |
|                                                                                                                                                                                                                 |
| [][]                                                                                                              |
|                                                                                                                                                                                                                 |
| [      [@(] Html.Syncfusion().Schedule()([\"FlatSchedule\"] ,[\"ScheduleModel\"])] |
|                                                                                                                                                                                                                 |
| [       .BindList(columns =\>]                                                                                                                                 |
|                                                                                                                                                                                                                 |
| [       {]                                                                                                                                                     |
|                                                                                                                                                                                                                 |
| [           columns.IdField([\"AppId\"]);]                                                                                             |
|                                                                                                                                                                                                                 |
| [           columns.SubjectField([\"Subject\"]);]                                                                                      |
|                                                                                                                                                                                                                 |
| [           columns.LocationField([\"Location\"]);]                                                                                    |
|                                                                                                                                                                                                                 |
| [           columns.StartTimeField([\"StartTime\"]);]                                                                                  |
|                                                                                                                                                                                                                 |
| [           columns.EndTimeField([\"EndTime\"]);]                                                                                      |
|                                                                                                                                                                                                                 |
| [           columns.DescriptionField([\"Descrip\"]);]                                                                                  |
|                                                                                                                                                                                                                 |
| [           columns.OwnerField([\"Resource\"]);]                                                                                       |
|                                                                                                                                                                                                                 |
| [       })[)]]                                                                                                                     |
|                                                                                                                                                                                                                 |
| []                                                                                                                                                             |
|                                                                                                                                                                                                                 |
| []                                                                                                                                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   In Controller, add the Syncfusion.Mvc.Schedule, Syncfusion.Mvc.Shared namespaces.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**[[]]{.MsoIntenseEmphasis} |
|                                                                                                                                                              |
| [using][ Syncfusion.Mvc.Schedule;]                    |
|                                                                                                                                                              |
| [using][ Syncfusion.Mvc.Shared;]                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Create a **SchedulePropertiesModel** in the**Index** method. Use **AllowAddNew** property to create a new appointment through **CellDoubleClick** Event. Create context-menu item and set the **contextMenuItems** property to create a new appointment through context-menu. Pass this **SchedulePropertiesModel** from **Controller** to **View** using **ViewData** class as given below.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| [        [///][ ][\<summary\>]]                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| [        [///][ It is used to bind the Schedule]]                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| [        [///][ ][\</summary\>]]                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| [        [///][ ][\<returns\>][View page, it displays the Schedule][\</returns\>]]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| [        [public] [ActionResult] Index()]                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| [        {]                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| [ContextMenuItem][ newapp = [new] [ContextMenuItem]() { MenuID = [\"NewAppointment\"], MenuName = [\"New Appointment\"], CommandName = [ContextCommandNames].NewAppointment };] |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| [                [var] data = [new] [NorthwindDataClassesDataContext]().AppointmentTables.Take(200);]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| [                [SchedulePropertiesModel] scheduleModel = [new] [SchedulePropertiesModel]();]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| [                scheduleModel.DataSource = data;]                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| [                 scheduleModel.Skins = [ScheduleSkins].Sandune;]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| **[                scheduleModel.AllowAddNew = [true];]**                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| **[scheduleModel.ContextMenuItems = [new] [List]\<[ContextMenuItem]\>() { newapp };]**                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| [                ViewData\[[\"ScheduleModel\"]\] = scheduleModel;]                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| [                [return] View();]                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| [        }]                                                                                                                                                                                                                                                                                                                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   Create a post method for Index action and bind the data source to **Schedule**, as shown in the code displayed below:

[] 

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
| [        [public] [ActionResult] Index([Params] args, [SchedulePropertiesModel] model)]                 |
|                                                                                                                                                                                                                                                   |
| [        {]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                   |
| [NorthwindDataClassesDataContext][ db = [new] [NorthwindDataClassesDataContext]();]        |
|                                                                                                                                                                                                                                                   |
| [int][ intMax = db.AppointmentTables.ToList().Count \> 0 ? db.AppointmentTables.ToList().Max(p =\> p.AppId) : 1;]                          |
|                                                                                                                                                                                                                                                   |
| [            model.SetCurrentCultureInfo();]                                                                                                                                                         |
|                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                   |
| [            [// Create a New appointment and insert into the database]]                                                                                                       |
|                                                                                                                                                                                                                                                   |
| [            [if] (args.CurrentAction == [\"Save\"])]                                                                                                   |
|                                                                                                                                                                                                                                                   |
| [            {]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                   |
| [                [DateTime] startTime = [Convert].ToDateTime(args.StartTime);]                                                                       |
|                                                                                                                                                                                                                                                   |
| [                [DateTime] endTime = [Convert].ToDateTime(args.EndTime);]                                                                           |
|                                                                                                                                                                                                                                                   |
| [                [AppointmentTable] appoint = [new] [AppointmentTable]()]                                                       |
|                                                                                                                                                                                                                                                   |
| [                {]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                   |
| [                    AppId = intMax + 1,]                                                                                                                                                            |
|                                                                                                                                                                                                                                                   |
| [                    StartTime = startTime,]                                                                                                                                                         |
|                                                                                                                                                                                                                                                   |
| [                    EndTime = endTime,]                                                                                                                                                             |
|                                                                                                                                                                                                                                                   |
| [                    Subject = args.Subject,]                                                                                                                                                        |
|                                                                                                                                                                                                                                                   |
| [                    Location = args.Location,]                                                                                                                                                      |
|                                                                                                                                                                                                                                                   |
| [                    Descrip = args.Description,]                                                                                                                                                    |
|                                                                                                                                                                                                                                                   |
| [                    Resource = args.Owner,]                                                                                                                                                         |
|                                                                                                                                                                                                                                                   |
| [                };]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                   |
| [                db.AppointmentTables.InsertOnSubmit(appoint);]                                                                                                                                      |
|                                                                                                                                                                                                                                                   |
| [            }]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                   |
| [                [//to reflect in database]]                                                                                                                                   |
|                                                                                                                                                                                                                                                   |
| [                db.SubmitChanges();]                                                                                                                                                                |
|                                                                                                                                                                                                                                                   |
| [ActionResult][ result = db.AppointmentTables.ScheduleActions\<[ScheduleHtmlActionResult]\>();]                 |
|                                                                                                                                                                                                                                                   |
| [                [return] result;]                                                                                                                                              |
|                                                                                                                                                                                                                                                   |
| [        }]                                                                                                                                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

6.   Run the application. The Schedule's appointment window will appear as shown below when the following actions happen to create a new appointment.

a.       Double-click any Schedule cell.

b.       Right-click a Schedule cell and click New Appointment.

[] 

{border="0"}

[] 

Figure 105: Add Appointment Dialog

[] 

7.   In the **Subject** box, type an appointment's subject.

8.   In the **Location** box, type the location.

9.   Select the appointment timings - start date, start time, end date and end time.

10.  In the **Description** box, type a description.

11.  On the **Appointment** dialog toolbar, click **Save & Close**.

[] 

[]{#related-topics}

