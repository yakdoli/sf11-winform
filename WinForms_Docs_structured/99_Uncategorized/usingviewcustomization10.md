---
title: usingviewcustomization10.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingviewcustomization10.md
created_at: 2025-07-03
---






##### Using View customization {#using-view-customization style="tab-stops: 0pt"}

The steps to customize recurring appointment using View Customization are as follows:

1.   Create a model in the application.[ ]

2.   Create a strongly typed view.[]

3.   In **View**, you can use  **Model** property in **DataSource** in order to bind the data source and bind the database fields into the corresponding **Schedule** fields.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**                                                                                                                                                                     |
|                                                                                                                                                                                                                                     |
| [    [\<%][=]Html.Syncfusion().Schedule()([\"FlatSchedule\"])][] |
|                                                                                                                                                                                                                                     |
| [       .DataSource(([IEnumerable])Model)]                                                                                                                     |
|                                                                                                                                                                                                                                     |
| [       .BindList(columns =\>]                                                                                                                                                         |
|                                                                                                                                                                                                                                     |
| [       {]                                                                                                                                                                             |
|                                                                                                                                                                                                                                     |
| [           columns.IdField([\"AppId\"]);]                                                                                                                     |
|                                                                                                                                                                                                                                     |
| [           columns.SubjectField([\"Subject\"]);]                                                                                                              |
|                                                                                                                                                                                                                                     |
| [           columns.LocationField([\"Location\"]);]                                                                                                            |
|                                                                                                                                                                                                                                     |
| [           columns.StartTimeField([\"StartTime\"]);]                                                                                                          |
|                                                                                                                                                                                                                                     |
| [           columns.EndTimeField([\"EndTime\"]);]                                                                                                              |
|                                                                                                                                                                                                                                     |
| [           columns.DescriptionField([\"Descrip\"]);]                                                                                                          |
|                                                                                                                                                                                                                                     |
| [           columns.OwnerField([\"Resource\"]);]                                                                                                               |
|                                                                                                                                                                                                                                     |
| [           columns.RecurrenceField([\"Recurrence\"]);]                                                                                                        |
|                                                                                                                                                                                                                                     |
| [           columns.RecurrenceTypeField([\"RecurFrequency\"]);]                                                                                                |
|                                                                                                                                                                                                                                     |
| [           columns.RecurrenceTypeCountField([\"RecurInterval\"]);]                                                                                            |
|                                                                                                                                                                                                                                     |
| [       })]                                                                                                                                                                            |
|                                                                                                                                                                                                                                     |
| [    [%\>]]                                                                                                                                                |
|                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                              |
|                                                                                                                                                                |
| [  [@(] Html.Syncfusion().Schedule()([\"FlatSchedule\"])] |
|                                                                                                                                                                |
| [       .DataSource(([IEnumerable])Model)]                                            |
|                                                                                                                                                                |
| [       .BindList(columns =\>]                                                                                |
|                                                                                                                                                                |
| [       {]                                                                                                    |
|                                                                                                                                                                |
| [           columns.IdField([\"AppId\"]);]                                            |
|                                                                                                                                                                |
| [           columns.SubjectField([\"Subject\"]);]                                     |
|                                                                                                                                                                |
| [           columns.LocationField([\"Location\"]);]                                   |
|                                                                                                                                                                |
| [           columns.StartTimeField([\"StartTime\"]);]                                 |
|                                                                                                                                                                |
| [           columns.EndTimeField([\"EndTime\"]);]                                     |
|                                                                                                                                                                |
| [           columns.DescriptionField([\"Descrip\"]);]                                 |
|                                                                                                                                                                |
| [           columns.OwnerField([\"Resource\"]);]                                      |
|                                                                                                                                                                |
| [           columns.RecurrenceField([\"Recurrence\"]);]                               |
|                                                                                                                                                                |
| [           columns.RecurrenceTypeField([\"RecurFrequency\"]);]                       |
|                                                                                                                                                                |
| [           columns.RecurrenceTypeCountField([\"RecurInterval\"]);]                   |
|                                                                                                                                                                |
| [       })[)]]                                                                    |
|                                                                                                                                                                |
| []                                                                                                            |
|                                                                                                                                                                |
| []                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

4.   Set the **AllowRecurrence()** method to create/update recurring appointment.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**                                                                                                                                         |
|                                                                                                                                                                                                         |
| [    [\<%][=]Html.Syncfusion().Schedule()([\"FlatSchedule\"])]                    |
|                                                                                                                                                                                                         |
| [       .DataSource(([IEnumerable])Model)]                                                                                         |
|                                                                                                                                                                                                         |
| [       .BindList(columns =\>]                                                                                                                             |
|                                                                                                                                                                                                         |
| [       {]                                                                                                                                                 |
|                                                                                                                                                                                                         |
| [           columns.IdField([\"AppId\"]);]                                                                                         |
|                                                                                                                                                                                                         |
| [           columns.SubjectField([\"Subject\"]);]                                                                                  |
|                                                                                                                                                                                                         |
| [           columns.LocationField([\"Location\"]);]                                                                                |
|                                                                                                                                                                                                         |
| [           columns.StartTimeField([\"StartTime\"]);]                                                                              |
|                                                                                                                                                                                                         |
| [           columns.EndTimeField([\"EndTime\"]);]                                                                                  |
|                                                                                                                                                                                                         |
| [           columns.DescriptionField([\"Descrip\"]);]                                                                              |
|                                                                                                                                                                                                         |
| [           columns.OwnerField([\"Resource\"]);]                                                                                   |
|                                                                                                                                                                                                         |
| [           columns.RecurrenceField([\"Recurrence\"]);]                                                                            |
|                                                                                                                                                                                                         |
| [           columns.RecurrenceTypeField([\"RecurFrequency\"]);]                                                                    |
|                                                                                                                                                                                                         |
| [           columns.RecurrenceTypeCountField([\"RecurInterval\"]);]                                                                |
|                                                                                                                                                                                                         |
| []                                                                                                                                                         |
|                                                                                                                                                                                                         |
| [       })]                                                                                                                                                |
|                                                                                                                                                                                                         |
| [       .CurrentView([ScheduleViewMode].Week)    ]                                                                                 |
|                                                                                                                                                                                                         |
| [       .Skins([ScheduleSkins].Sandune)]                                                                                           |
|                                                                                                                                                                                                         |
| [       .AllowAddNew([true])]                                                                                                         |
|                                                                                                                                                                                                         |
| [       .AllowEdit([true])]                                                                                                           |
|                                                                                                                                                                                                         |
| **[       .][ ][AllowRecurrence ([true])]** |
|                                                                                                                                                                                                         |
| [    [%\>]]                                                                                                                    |
|                                                                                                                                                                                                         |
| []                                                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                 |
|                                                                                                                                                                   |
| [     [@(] Html.Syncfusion().Schedule()([\"FlatSchedule\"])] |
|                                                                                                                                                                   |
| [       .DataSource(([IEnumerable])Model)]                                               |
|                                                                                                                                                                   |
| [       .BindList(columns =\>]                                                                                   |
|                                                                                                                                                                   |
| [       {]                                                                                                       |
|                                                                                                                                                                   |
| [           columns.IdField([\"AppId\"]);]                                               |
|                                                                                                                                                                   |
| [           columns.SubjectField([\"Subject\"]);]                                        |
|                                                                                                                                                                   |
| [           columns.LocationField([\"Location\"]);]                                      |
|                                                                                                                                                                   |
| [           columns.StartTimeField([\"StartTime\"]);]                                    |
|                                                                                                                                                                   |
| [           columns.EndTimeField([\"EndTime\"]);]                                        |
|                                                                                                                                                                   |
| [           columns.DescriptionField([\"Descrip\"]);]                                    |
|                                                                                                                                                                   |
| [           columns.OwnerField([\"Resource\"]);]                                         |
|                                                                                                                                                                   |
| [           columns.RecurrenceField([\"Recurrence\"]);]                                  |
|                                                                                                                                                                   |
| [           columns.RecurrenceTypeField([\"RecurFrequency\"]);]                          |
|                                                                                                                                                                   |
| [           columns.RecurrenceTypeCountField([\"RecurInterval\"]);]                      |
|                                                                                                                                                                   |
| []                                                                                                               |
|                                                                                                                                                                   |
| [       })]                                                                                                      |
|                                                                                                                                                                   |
| [       .CurrentView([ScheduleViewMode].Week)    ]                                       |
|                                                                                                                                                                   |
| [       .Skins([ScheduleSkins].Sandune)]                                                 |
|                                                                                                                                                                   |
| [       .AllowAddNew([true])]                                                               |
|                                                                                                                                                                   |
| [       .AllowEdit([true])]                                                                 |
|                                                                                                                                                                   |
| [       . AllowRecurrence ([true])]                                                         |
|                                                                                                                                                                   |
| [       [)]]                                                                         |
|                                                                                                                                                                   |
| []                                                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   In **Controller**, add the Syncfusion.Mvc.Schedule, Syncfusion.Mvc.Shared namespaces.

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

6.   Set its data source and render the view.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**[[]]{.MsoIntenseEmphasis}                                                                               |
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
| [            [return] View(data);]                                                                                                                                       |
|                                                                                                                                                                                                                                            |
| [        }]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

7.   Create a post method for Index action and bind the data source to Schedule, as shown in the code displayed below.

[[]]{.MsoIntenseEmphasis} 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**[[]]{.MsoIntenseEmphasis}                                                                                      |
|                                                                                                                                                                                                                                                   |
| [  ][       [///][ ][\<summary\>]]                                         |
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
| [           [// Create New appointment with Recurrence and insert into database]]                                                                                              |
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
| **[                    Recurrence = [Convert].ToByte(args.Recurrence),]**                                                                                                    |
|                                                                                                                                                                                                                                                   |
| **[                    RecurFrequency = args.RecurrenceType,]**                                                                                                                                      |
|                                                                                                                                                                                                                                                   |
| **[                    RecurInterval = [Convert].ToInt32(args.RecurrenceTypeCount)]**                                                                                        |
|                                                                                                                                                                                                                                                   |
| [                };]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                   |
| [                db.AppointmentTables.InsertOnSubmit(appoint);]                                                                                                                                      |
|                                                                                                                                                                                                                                                   |
| [            }]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                   |
| [            [// Update existing apppointment with Recurrence]]                                                                                                                |
|                                                                                                                                                                                                                                                   |
| [            [else] [if] (args.CurrentAction == [\"Edit\"])]                                                                       |
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
| [                    appoint.EndTime = endTime;]                                                                                                                                                     |
|                                                                                                                                                                                                                                                   |
| [                    appoint.Subject = args.Subject;]                                                                                                                                                |
|                                                                                                                                                                                                                                                   |
| [                    appoint.Location = args.Location;]                                                                                                                                              |
|                                                                                                                                                                                                                                                   |
| [                    appoint.Descrip = args.Description;]                                                                                                                                            |
|                                                                                                                                                                                                                                                   |
| [                    appoint.Resource = args.Owner;]                                                                                                                                                 |
|                                                                                                                                                                                                                                                   |
| **[                    appoint.Recurrence = [Convert].ToByte(args.Recurrence);]**                                                                                            |
|                                                                                                                                                                                                                                                   |
| **[                    appoint.RecurFrequency = args.RecurrenceType;]**                                                                                                                              |
|                                                                                                                                                                                                                                                   |
| **[                    appoint.RecurInterval = [Convert].ToInt32(args.RecurrenceTypeCount);]**                                                                               |
|                                                                                                                                                                                                                                                   |
| [                }]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                   |
| [            }]                                                                                                                                                                                      |
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

8.   Run the application. The Schedule's recurrence window will appear as shown below.

[] 

{border="0"}

[] 

Figure 122: Recurrence Dialog

[] 

[]{#related-topics}

