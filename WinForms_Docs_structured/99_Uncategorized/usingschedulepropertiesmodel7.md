---
title: usingschedulepropertiesmodel7.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingschedulepropertiesmodel7.md
created_at: 2025-07-03
---






##### Using SchedulePropertiesModel {#using-schedulepropertiesmodel style="tab-stops: 0pt"}

The steps to customize drag and drop appointment using SchedulePropertiesModel are as follows:

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
| [       })       [%\>]][]                                                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**[[]]{.MsoIntenseEmphasis}                                                 |
|                                                                                                                                                                                                              |
| [   ][ ][]                                                        |
|                                                                                                                                                                                                              |
| [   [@(] Html.Syncfusion().Schedule()([\"FlatSchedule\"] ,[\"ScheduleModel\"])] |
|                                                                                                                                                                                                              |
| [       .BindList(columns =\>]                                                                                                                              |
|                                                                                                                                                                                                              |
| [       {]                                                                                                                                                  |
|                                                                                                                                                                                                              |
| [           columns.IdField([\"AppId\"]);]                                                                                          |
|                                                                                                                                                                                                              |
| [           columns.SubjectField([\"Subject\"]);]                                                                                   |
|                                                                                                                                                                                                              |
| [           columns.LocationField([\"Location\"]);]                                                                                 |
|                                                                                                                                                                                                              |
| [           columns.StartTimeField([\"StartTime\"]);]                                                                               |
|                                                                                                                                                                                                              |
| [           columns.EndTimeField([\"EndTime\"]);]                                                                                   |
|                                                                                                                                                                                                              |
| [           columns.DescriptionField([\"Descrip\"]);]                                                                               |
|                                                                                                                                                                                                              |
| [           columns.OwnerField([\"Resource\"]);]                                                                                    |
|                                                                                                                                                                                                              |
| [       })[)]]                                                                                                                  |
|                                                                                                                                                                                                              |
| []                                                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

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

4.   Create a **SchedulePropertiesModel** in the **Index** method and set the **AllowDragAndDrop** property to enable the dragging feature.

5.   Pass this **SchedulePropertiesModel** from Controller to View using **ViewData** class as shown below.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                                                                                                          |
|                                                                                                                                                                                                                                            |
| [        [///][ ][\<summary\>]]                                                                                               |
|                                                                                                                                                                                                                                            |
| [        [///][ It used to bind the Schedule]]                                                                                                     |
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
| **[            scheduleModel.AllowDragAndDrop = [true];]**                                                                                                               |
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

6.   Create a post method for Index action and bind the data source to **Schedule**, as shown in the code displayed below.

[[]]{.MsoIntenseEmphasis} 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**[[]]{.MsoIntenseEmphasis}                                                                                        |
|                                                                                                                                                                                                                                                     |
| [  ][      [///][ ][\<summary\>]]                                            |
|                                                                                                                                                                                                                                                     |
| [        [///][ Post Requests are mapped to this method. This method invokes the HtmlActionResult]]                                                         |
|                                                                                                                                                                                                                                                     |
| [        [///][ from the Schedule. Required response is generated.]]                                                                                        |
|                                                                                                                                                                                                                                                     |
| [        [///][ ][\</summary\>]]                                                                                                       |
|                                                                                                                                                                                                                                                     |
| [        [///][ ][\<param name=\"args\"\>][Contains post action properties ][\</param\>]]   |
|                                                                                                                                                                                                                                                     |
| [        [///][ ][\<returns\>]]                                                                                                        |
|                                                                                                                                                                                                                                                     |
| [        [///][ HtmlActionResult which returns data displayed on the Schedule]]                                                                             |
|                                                                                                                                                                                                                                                     |
| [        [///][ ][\</returns\>]]                                                                                                       |
|                                                                                                                                                                                                                                                     |
| [        \[[AcceptVerbs]([HttpVerbs].Post)\]]                                                                                                          |
|                                                                                                                                                                                                                                                     |
| [        [public] [ActionResult] Index([Params] args, [SchedulePropertiesModel] model)]                   |
|                                                                                                                                                                                                                                                     |
| [        {]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                     |
| [NorthwindDataClassesDataContext][ db = [new] [NorthwindDataClassesDataContext]();]          |
|                                                                                                                                                                                                                                                     |
| [            model.SetCurrentCultureInfo();]                                                                                                                                                           |
|                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                     |
| [            [// Update existing apppointment with dragging arguments]]                                                                                                          |
|                                                                                                                                                                                                                                                     |
| [            [if] (args.CurrentAction == [\"DragDrop\"])]                                                                                                 |
|                                                                                                                                                                                                                                                     |
| [            {]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                     |
| [var][ filterData = db.AppointmentTables.Where(c =\> c.AppId == [Convert].ToInt32(args.AppID));]                     |
|                                                                                                                                                                                                                                                     |
| [                [if] (filterData.Count() \> 0)]                                                                                                                                  |
|                                                                                                                                                                                                                                                     |
| [                {]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                     |
| [                    [DateTime] startTime = [Convert].ToDateTime(args.StartTime);]                                                                     |
|                                                                                                                                                                                                                                                     |
| [                    [DateTime] endTime = [Convert].ToDateTime(args.EndTime);]                                                                         |
|                                                                                                                                                                                                                                                     |
| [     AppointmentTable][ appoint = db.AppointmentTables.Single(A =\> A.AppId ==  [Convert].ToInt32(args.AppID));] |
|                                                                                                                                                                                                                                                     |
| [                    appoint.StartTime = startTime;]                                                                                                                                                   |
|                                                                                                                                                                                                                                                     |
| [                    appoint.EndTime = endTime;]                                                                                                                                                       |
|                                                                                                                                                                                                                                                     |
| [                     appoint.Resource = args.Owner;]                                                                                                                                                  |
|                                                                                                                                                                                                                                                     |
| [                }]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                     |
| [            }]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                     |
| [            [//to reflect in database]]                                                                                                                                         |
|                                                                                                                                                                                                                                                     |
| [            db.SubmitChanges();]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                     |
| [ActionResult][ result = db.AppointmentTables.ScheduleActions\<[ScheduleHtmlActionResult]\>();]                   |
|                                                                                                                                                                                                                                                     |
| [            [return] result;]                                                                                                                                                    |
|                                                                                                                                                                                                                                                     |
| [        }]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

7.   Run the application. The schedule will appear as shown below with the dragged appointment by arrow.

{border="0"}

Figure 117: Drag and Drop Appointment

[] 

[]{#related-topics}

