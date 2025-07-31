---
title: usingschedulepropertiesmodel4.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingschedulepropertiesmodel4.md
created_at: 2025-07-03
---






##### Using SchedulePropertiesModel {#using-schedulepropertiesmodel style="tab-stops: 0pt"}

The steps to customize the Change an Appointment using SchedulePropertiesModel are as follows:

[[1.   ]]{.UGHyperlink}[Create a model in the application.]{.UGHyperlink}[ ]{.UGHyperlink}

2.   Add the following code in the Index.aspx file, to create the Schedule control in **View**.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**                                                                                                                                                                                                                                               |
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

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                                                       |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                                     |
|                                                                                                                                                                                                                         |
| [              [@(] Html.Syncfusion().Schedule()([\"FlatSchedule\"] ,[\"ScheduleModel\"])] |
|                                                                                                                                                                                                                         |
| [       .BindList(columns =\>]                                                                                                                                         |
|                                                                                                                                                                                                                         |
| [       {]                                                                                                                                                             |
|                                                                                                                                                                                                                         |
| [           columns.IdField([\"AppId\"]);]                                                                                                     |
|                                                                                                                                                                                                                         |
| [           columns.SubjectField([\"Subject\"]);]                                                                                              |
|                                                                                                                                                                                                                         |
| [           columns.LocationField([\"Location\"]);]                                                                                            |
|                                                                                                                                                                                                                         |
| [           columns.StartTimeField([\"StartTime\"]);]                                                                                          |
|                                                                                                                                                                                                                         |
| [           columns.EndTimeField([\"EndTime\"]);]                                                                                              |
|                                                                                                                                                                                                                         |
| [           columns.DescriptionField([\"Descrip\"]);]                                                                                          |
|                                                                                                                                                                                                                         |
| [           columns.OwnerField([\"Resource\"]);]                                                                                               |
|                                                                                                                                                                                                                         |
| [       })[)]]                                                                                                                             |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

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

5.   Use **AllowEdit** property to change an appointment through AppointmentDoubleClick Event. Create context-menu item and set the contextMenuItems property to change an appointment through context-menu.

6.   Pass this **SchedulePropertiesModel** from **Controller** to **View** using **ViewData** class as shown below.

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
| [ContextMenuItem][ editApp = [new] [ContextMenuItem]() ]                            |
|                                                                                                                                                                                                                                            |
| [{ ]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                            |
| [MenuID = [\"UpdateAppointment\"], ]                                                                                                                                  |
|                                                                                                                                                                                                                                            |
| [MenuName = [\"Update Appointment\"], ]                                                                                                                               |
|                                                                                                                                                                                                                                            |
| [CommandName = [ContextCommandNames].OpenAppointment ]                                                                                                                |
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
| **[                scheduleModel.AllowEdit = [true];]**                                                                                                                  |
|                                                                                                                                                                                                                                            |
| **[scheduleModel.ContextMenuItems = [new] [List]\<[ContextMenuItem]\>() { editApp };]**                                  |
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

7.   Create a post method for **Index** action and bind the data source to Schedule, as shown in the code displayed below.

[[]]{.MsoIntenseEmphasis} 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                                                                                                                 |
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
| [            model.SetCurrentCultureInfo();]                                                                                                                                                         |
|                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                   |
| [            [// Update existing apppointment]]                                                                                                                                |
|                                                                                                                                                                                                                                                   |
| [            [if] (args.CurrentAction == [\"Edit\"])]                                                                                                   |
|                                                                                                                                                                                                                                                   |
| [            {]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                   |
| [                [var] filterData = db.AppointmentTables.Where(c =\> c.AppId == [Convert].ToInt32(args.AppID));]                                        |
|                                                                                                                                                                                                                                                   |
| [                [if] (filterData.Count() \> 0)]                                                                                                                                |
|                                                                                                                                                                                                                                                   |
| [                {]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                   |
| [                    [DateTime] startTime = [Convert].ToDateTime(args.StartTime);]                                                                   |
|                                                                                                                                                                                                                                                   |
| [                    [DateTime] endTime = [Convert].ToDateTime(args.EndTime);]                                                                       |
|                                                                                                                                                                                                                                                   |
| [                    [AppointmentTable] appoint = db.AppointmentTables.Single(A =\> A.AppId == [Convert].ToInt32(args.AppID));]                      |
|                                                                                                                                                                                                                                                   |
| [                    appoint.StartTime = startTime;]                                                                                                                                                 |
|                                                                                                                                                                                                                                                   |
| [                    appoint.EndTime = endTime;]                                                                                                                                                     |
|                                                                                                                                                                                                                                                   |
| [                    appoint.Subject = args.Subject;]                                                                                                                                                |
|                                                                                                                                                                                                                                                   |
| [                    appoint.Location = args.Location;]                                                                                                                                              |
|                                                                                                                                                                                                                                                   |
| [                    appoint.Descrip = args.Description;]                                                                                                                                            |
|                                                                                                                                                                                                                                                   |
| [                    appoint.Resource = args.Owner;]                                                                                                                                                 |
|                                                                                                                                                                                                                                                   |
| [                }]                                                                                                                                                                                  |
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

8.   Run the application. The Schedule's appointment window will appear as shown below when the following actions happen to change an appointment.

a.       Double-click any appointment**.**

b.       Right-click an appointment and click Open Appointment.

[] 

{border="0"}

[] 

Figure 109: Appointment Dialog with Existing Appointment Details

[] 

9.   In the **Subject** box, change an appointment's subject.

10.  In the **Location** box, change the location.

11.  Change the appointment timings - start date, start time, end date and end time.

12.  In the **Description** box, change a description.

13.  On the **Appointment** dialog toolbar, click **Save** & **Close**.

[] 

[]{#related-topics}

