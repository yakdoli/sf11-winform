---
title: usingschedulepropertiesmodel9.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingschedulepropertiesmodel9.md
created_at: 2025-07-03
---






##### Using SchedulePropertiesModel {#using-schedulepropertiesmodel style="tab-stops: 0pt"}

The steps to customize reminders for an appointment using SchedulePropertiesModel are as follows:

1.   Create a model in the application.[ ]

2.   Add the following code in the Index.aspx file, to create the **Schedule** control in **View**.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**[[]]{.MsoIntenseEmphasis}                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                              |
| [   ][    [\<%][=]Html.Syncfusion().Schedule()([\"FlatSchedule\"],[\"ScheduleModel\"])[]] |
|                                                                                                                                                                                                                                                                                                              |
| [       .BindList(columns =\>]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                              |
| [       {]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                              |
| [           columns.IdField([\"AppId\"]);]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                              |
| [           columns.SubjectField([\"Subject\"]);]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                              |
| [           columns.LocationField([\"Location\"]);]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                              |
| [           columns.StartTimeField([\"StartTime\"]);]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                              |
| [           columns.EndTimeField([\"EndTime\"]);]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                              |
| [           columns.DescriptionField([\"Descrip\"]);]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                              |
| [           columns.OwnerField([\"Resource\"]);]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                              |
| [           columns.ReminderField([\"Reminder\"]);]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                              |
| [       })]                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                              |
| [        [%\>]]                                                                                                                                                                                                                     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**[[]]{.MsoIntenseEmphasis}                                                     |
|                                                                                                                                                                                                                  |
| [][]                                                                                                               |
|                                                                                                                                                                                                                  |
| [        [@(] Html.Syncfusion().Schedule()([\"FlatSchedule\"],[\"ScheduleModel\"])] |
|                                                                                                                                                                                                                  |
| [       .BindList(columns =\>]                                                                                                                                  |
|                                                                                                                                                                                                                  |
| [       {]                                                                                                                                                      |
|                                                                                                                                                                                                                  |
| [           columns.IdField([\"AppId\"]);]                                                                                              |
|                                                                                                                                                                                                                  |
| [           columns.SubjectField([\"Subject\"]);]                                                                                       |
|                                                                                                                                                                                                                  |
| [           columns.LocationField([\"Location\"]);]                                                                                     |
|                                                                                                                                                                                                                  |
| [           columns.StartTimeField([\"StartTime\"]);]                                                                                   |
|                                                                                                                                                                                                                  |
| [           columns.EndTimeField([\"EndTime\"]);]                                                                                       |
|                                                                                                                                                                                                                  |
| [           columns.DescriptionField([\"Descrip\"]);]                                                                                   |
|                                                                                                                                                                                                                  |
| [           columns.OwnerField([\"Resource\"]);]                                                                                        |
|                                                                                                                                                                                                                  |
| [           columns.ReminderField([\"Reminder\"]);]                                                                                     |
|                                                                                                                                                                                                                  |
| [       })[)]]                                                                                                                      |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                              |
|                                                                                                                                                                                                                  |
| []                                                                                                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

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

4.   Create a **SchedulePropertiesModel** in **Index** method and set the **AllowReminder** property to create/update appointment with reminders.

5.   Pass this **SchedulePropertiesModel** from the **Controller** to **View** using **ViewData** class as shown below.

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
| [            [var] data = [new] [NorthwindDataClassesDataContext]().AppointmentTables.Take(200);]                           |
|                                                                                                                                                                                                                                            |
| [            [SchedulePropertiesModel] scheduleModel = [new] [SchedulePropertiesModel]();]                               |
|                                                                                                                                                                                                                                            |
| [            scheduleModel.DataSource = data;]                                                                                                                                                |
|                                                                                                                                                                                                                                            |
| [            scheduleModel.Skins = [ScheduleSkins].Sandune;]                                                                                                          |
|                                                                                                                                                                                                                                            |
| [            scheduleModel.CurrentView = [ScheduleViewMode].Week;]                                                                                                    |
|                                                                                                                                                                                                                                            |
| [            scheduleModel.AllowAddNew = [true];]                                                                                                                        |
|                                                                                                                                                                                                                                            |
| [            scheduleModel.AllowEdit = [true];]                                                                                                                          |
|                                                                                                                                                                                                                                            |
| **[            scheduleModel.AllowReminder = [true];]**                                                                                                                  |
|                                                                                                                                                                                                                                            |
| [            ViewData\[[\"ScheduleModel\"]\] = scheduleModel;]                                                                                                        |
|                                                                                                                                                                                                                                            |
| [            [return] View();]                                                                                                                                           |
|                                                                                                                                                                                                                                            |
| [        }]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

6.   Create a post method for Index action and bind the data source to Schedule, as shown in the code displayed below.

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
| [           [// Create New appointment with Reminder and insert into database]]                                                                                                |
|                                                                                                                                                                                                                                                   |
| [            [if] (args.CurrentAction == [\"Save\"])]                                                                                                   |
|                                                                                                                                                                                                                                                   |
| [            {]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                   |
| [                [DateTime] startTime = [Convert].ToDateTime(args.StartTime);]                                                                       |
|                                                                                                                                                                                                                                                   |
| [                [DateTime] endTime = [Convert].ToDateTime(args.EndTime);]                                                                           |
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
| **[                    Reminder = [Convert].ToInt32(args.Reminder)]**                                                                                                        |
|                                                                                                                                                                                                                                                   |
| [                };]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                   |
| [                db.AppointmentTables.InsertOnSubmit(appoint);]                                                                                                                                      |
|                                                                                                                                                                                                                                                   |
| [            }]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                   |
| [            [// Update existing apppointment with Reminder]]                                                                                                                  |
|                                                                                                                                                                                                                                                   |
| [            [else] [if] (args.CurrentAction == [\"Edit\"])]                                                                       |
|                                                                                                                                                                                                                                                   |
| [            {]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                   |
| [var][ filterData = db.AppointmentTables.Where(c =\> c.AppId == [Convert].ToInt32(args.AppID));]                   |
|                                                                                                                                                                                                                                                   |
| [                [if] (filterData.Count() \> 0)]                                                                                                                                |
|                                                                                                                                                                                                                                                   |
| [                {]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                   |
| [                    [DateTime] startTime = [Convert].ToDateTime(args.StartTime);]                                                                   |
|                                                                                                                                                                                                                                                   |
| [                    [DateTime] endTime = [Convert].ToDateTime(args.EndTime);]                                                                       |
|                                                                                                                                                                                                                                                   |
| [     [AppointmentTable] appoint = db.AppointmentTables.Single(A =\> A.AppId == [Convert].ToInt32(args.AppID));]                                     |
|                                                                                                                                                                                                                                                   |
| [                    appoint.StartTime = startTime;]                                                                                                                                                 |
|                                                                                                                                                                                                                                                   |
| [                    appoint.EndTime = endTime;]                                                                                                                                                     |
|                                                                                                                                                                                                                                                   |
| [                    appoint.Subject = args.Subject;]                                                                                                                                                |
|                                                                                                                                                                                                                                                   |
| [                    appoint.Location = args.Location;]                                                                                                                                              |
|                                                                                                                                                                                                                                                   |
| [                    appoint.Descrip = args.Description;]                                                                                                                                            |
|                                                                                                                                                                                                                                                   |
| [                    appoint.Resource = args.Owner;]                                                                                                                                                 |
|                                                                                                                                                                                                                                                   |
| **[                    appoint.Reminder = [Convert].ToInt32(args.Reminder);]**                                                                                               |
|                                                                                                                                                                                                                                                   |
| [                }]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                   |
| [            }]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                   |
| [            [//to reflect in database]]                                                                                                                                       |
|                                                                                                                                                                                                                                                   |
| [            db.SubmitChanges();]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                   |
| [ActionResult][ result = db.AppointmentTables.ScheduleActions\<[ScheduleHtmlActionResult]\>();]                 |
|                                                                                                                                                                                                                                                   |
| [            [return] result;]                                                                                                                                                  |
|                                                                                                                                                                                                                                                   |
| [        }]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[[]]{.MsoIntenseEmphasis} 

7.   Run the application. The Schedule's reminder dialog will appear as shown below.

[] 

{border="0"}

[] 

Figure 121: Reminder Dialog

[] 

[]{#related-topics}

