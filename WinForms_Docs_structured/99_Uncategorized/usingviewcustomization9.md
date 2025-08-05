---
title: usingviewcustomization9.md
original_path: WinForms_Docs/99_Uncategorized/usingviewcustomization9.md
created_at: 2025-08-05
---






##### Using View Customization {#using-view-customization style="tab-stops: 0pt"}

The steps to customize reminder for an appointment using View Customization are as follows:

1.   [Create a model in the application]{.UGHyperlink}[.][ ]

2.   [Create a strongly typed view]{.UGHyperlink}[.][]

3.   In **View**, you can use its **Model** property in **DataSource** in order to bind the data source and bind the  database fields into the corresponding Schedule fields.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**                                                                                                                      |
|                                                                                                                                                                                      |
| [    [\<%][=]Html.Syncfusion().Schedule()([\"FlatSchedule\"])] |
|                                                                                                                                                                                      |
| [       .DataSource(([IEnumerable])Model)]                                                                      |
|                                                                                                                                                                                      |
| [       .BindList(columns =\>]                                                                                                          |
|                                                                                                                                                                                      |
| [       {]                                                                                                                              |
|                                                                                                                                                                                      |
| [           columns.IdField([\"AppId\"]);]                                                                      |
|                                                                                                                                                                                      |
| [           columns.SubjectField([\"Subject\"]);]                                                               |
|                                                                                                                                                                                      |
| [           columns.LocationField([\"Location\"]);]                                                             |
|                                                                                                                                                                                      |
| [           columns.StartTimeField([\"StartTime\"]);]                                                           |
|                                                                                                                                                                                      |
| [           columns.EndTimeField([\"EndTime\"]);]                                                               |
|                                                                                                                                                                                      |
| [           columns.DescriptionField([\"Descrip\"]);]                                                           |
|                                                                                                                                                                                      |
| [           columns.OwnerField([\"Resource\"]);]                                                                |
|                                                                                                                                                                                      |
| [           columns.ReminderField([\"Reminder\"]);]                                                             |
|                                                                                                                                                                                      |
| [       })]                                                                                                                             |
|                                                                                                                                                                                      |
| [    [%\>]]                                                                                                 |
|                                                                                                                                                                                      |
| []                                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                                                 |
|                                                                                                                                                                                                                   |
| [    ][  [@(] Html.Syncfusion().Schedule()([\"FlatSchedule\"])] |
|                                                                                                                                                                                                                   |
| [       .DataSource(([IEnumerable])Model)]                                                                                               |
|                                                                                                                                                                                                                   |
| [       .BindList(columns =\>]                                                                                                                                   |
|                                                                                                                                                                                                                   |
| [       {]                                                                                                                                                       |
|                                                                                                                                                                                                                   |
| [           columns.IdField([\"AppId\"]);]                                                                                               |
|                                                                                                                                                                                                                   |
| [           columns.SubjectField([\"Subject\"]);]                                                                                        |
|                                                                                                                                                                                                                   |
| [           columns.LocationField([\"Location\"]);]                                                                                      |
|                                                                                                                                                                                                                   |
| [           columns.StartTimeField([\"StartTime\"]);]                                                                                    |
|                                                                                                                                                                                                                   |
| [           columns.EndTimeField([\"EndTime\"]);]                                                                                        |
|                                                                                                                                                                                                                   |
| [           columns.DescriptionField([\"Descrip\"]);]                                                                                    |
|                                                                                                                                                                                                                   |
| [           columns.OwnerField([\"Resource\"]);]                                                                                         |
|                                                                                                                                                                                                                   |
| [           columns.ReminderField([\"Reminder\"]);]                                                                                      |
|                                                                                                                                                                                                                   |
| [       })[)]]                                                                                                                       |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                               |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

4.   Set the **AllowReminder()** method to create/update appointments with reminders.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[]**                                                                                                                                                   |
|                                                                                                                                                                                                       |
| **[View\[aspx\]]**                                                                                                                                       |
|                                                                                                                                                                                                       |
| [    [\<%][=]Html.Syncfusion().Schedule()([\"FlatSchedule\"])]                  |
|                                                                                                                                                                                                       |
| [       .DataSource(([IEnumerable])Model)]                                                                                       |
|                                                                                                                                                                                                       |
| [       .BindList(columns =\>]                                                                                                                           |
|                                                                                                                                                                                                       |
| [       {]                                                                                                                                               |
|                                                                                                                                                                                                       |
| [           columns.IdField([\"AppId\"]);]                                                                                       |
|                                                                                                                                                                                                       |
| [           columns.SubjectField([\"Subject\"]);]                                                                                |
|                                                                                                                                                                                                       |
| [           columns.LocationField([\"Location\"]);]                                                                              |
|                                                                                                                                                                                                       |
| [           columns.StartTimeField([\"StartTime\"]);]                                                                            |
|                                                                                                                                                                                                       |
| [           columns.EndTimeField([\"EndTime\"]);]                                                                                |
|                                                                                                                                                                                                       |
| [           columns.DescriptionField([\"Descrip\"]);]                                                                            |
|                                                                                                                                                                                                       |
| [           columns.OwnerField([\"Resource\"]);]                                                                                 |
|                                                                                                                                                                                                       |
| [           columns.ReminderField([\"Reminder\"]);]                                                                              |
|                                                                                                                                                                                                       |
| [       })]                                                                                                                                              |
|                                                                                                                                                                                                       |
| [       .CurrentView([ScheduleViewMode].Week)    ]                                                                               |
|                                                                                                                                                                                                       |
| [       .Skins([ScheduleSkins].Sandune)]                                                                                         |
|                                                                                                                                                                                                       |
| [       .AllowAddNew([true])]                                                                                                       |
|                                                                                                                                                                                                       |
| [       .AllowEdit([true])]                                                                                                         |
|                                                                                                                                                                                                       |
| **[       .][ ][AllowReminder ([true])]** |
|                                                                                                                                                                                                       |
| [    [%\>]]                                                                                                                  |
|                                                                                                                                                                                                       |
| []                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                                       |
|                                                                                                                                                                                                       |
| **[View\[cshtml\]]**                                                                                                                                     |
|                                                                                                                                                                                                       |
| [@(][ Html.Syncfusion().Schedule()([\"FlatSchedule\"])] |
|                                                                                                                                                                                                       |
| [       .DataSource(([IEnumerable])Model)]                                                                                   |
|                                                                                                                                                                                                       |
| [       .BindList(columns =\>]                                                                                                                       |
|                                                                                                                                                                                                       |
| [       {]                                                                                                                                           |
|                                                                                                                                                                                                       |
| [           columns.IdField([\"AppId\"]);]                                                                                   |
|                                                                                                                                                                                                       |
| [           columns.SubjectField([\"Subject\"]);]                                                                            |
|                                                                                                                                                                                                       |
| [           columns.LocationField([\"Location\"]);]                                                                          |
|                                                                                                                                                                                                       |
| [           columns.StartTimeField([\"StartTime\"]);]                                                                        |
|                                                                                                                                                                                                       |
| [           columns.EndTimeField([\"EndTime\"]);]                                                                            |
|                                                                                                                                                                                                       |
| [           columns.DescriptionField([\"Descrip\"]);]                                                                        |
|                                                                                                                                                                                                       |
| [           columns.OwnerField([\"Resource\"]);]                                                                             |
|                                                                                                                                                                                                       |
| [           columns.ReminderField([\"Reminder\"]);]                                                                          |
|                                                                                                                                                                                                       |
| [       })]                                                                                                                                          |
|                                                                                                                                                                                                       |
| [       .CurrentView([ScheduleViewMode].Week)    ]                                                                           |
|                                                                                                                                                                                                       |
| [       .Skins([ScheduleSkins].Sandune)]                                                                                     |
|                                                                                                                                                                                                       |
| [       .AllowAddNew([true])]                                                                                                   |
|                                                                                                                                                                                                       |
| [       .AllowEdit([true])]                                                                                                     |
|                                                                                                                                                                                                       |
| [       . AllowReminder ([true])]                                                                                               |
|                                                                                                                                                                                                       |
| [       [)]]                                                                                                             |
|                                                                                                                                                                                                       |
| []                                                                                                                                                   |
|                                                                                                                                                                                                       |
| []                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

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
| [        [///][ it used to bind the Schedule]]                                                                                                     |
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

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**[[]]{.MsoIntenseEmphasis}                                                                                       |
|                                                                                                                                                                                                                                                    |
| [  ][       [///][ ][\<summary\>]]                                          |
|                                                                                                                                                                                                                                                    |
| [        [///][ Post Requests are mapped to this method. This method invokes the HtmlActionResult]]                                                        |
|                                                                                                                                                                                                                                                    |
| [        [///][ from the Schedule. Required response is generated.]]                                                                                       |
|                                                                                                                                                                                                                                                    |
| [        [///][ ][\</summary\>]]                                                                                                      |
|                                                                                                                                                                                                                                                    |
| [        [///][ ][\<param name=\"args\"\>][Contains post action properties ][\</param\>]]  |
|                                                                                                                                                                                                                                                    |
| [        [///][ ][\<returns\>]]                                                                                                       |
|                                                                                                                                                                                                                                                    |
| [        [///][ HtmlActionResult which returns data displayed on the Schedule]]                                                                            |
|                                                                                                                                                                                                                                                    |
| [        [///][ ][\</returns\>]]                                                                                                      |
|                                                                                                                                                                                                                                                    |
| [        \[[AcceptVerbs]([HttpVerbs].Post)\]]                                                                                                         |
|                                                                                                                                                                                                                                                    |
| [        [public] [ActionResult] Index([Params] args, [SchedulePropertiesModel] model)]                  |
|                                                                                                                                                                                                                                                    |
| [        {]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                    |
| [NorthwindDataClassesDataContext][ db = [new] [NorthwindDataClassesDataContext]();]         |
|                                                                                                                                                                                                                                                    |
| [int][ intMax = db.AppointmentTables.ToList().Count \> 0 ? db.AppointmentTables.ToList().Max(p =\> p.AppId) : 1;]                           |
|                                                                                                                                                                                                                                                    |
| [            model.SetCurrentCultureInfo();]                                                                                                                                                          |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                    |
| [           [// Create New appointment with Reminder and insert into database]]                                                                                                 |
|                                                                                                                                                                                                                                                    |
| [            [if] (args.CurrentAction == [\"Save\"])]                                                                                                    |
|                                                                                                                                                                                                                                                    |
| [            {]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                    |
| [                [DateTime] startTime = [Convert].ToDateTime(args.StartTime);]                                                                        |
|                                                                                                                                                                                                                                                    |
| [                [DateTime] endTime = [Convert].ToDateTime(args.EndTime);]                                                                            |
|                                                                                                                                                                                                                                                    |
| [                [AppointmentTable] appoint = [new] [AppointmentTable]()]                                                        |
|                                                                                                                                                                                                                                                    |
| [                {]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                    |
| [                    AppId = intMax + 1,]                                                                                                                                                             |
|                                                                                                                                                                                                                                                    |
| [                    StartTime = startTime,]                                                                                                                                                          |
|                                                                                                                                                                                                                                                    |
| [                    EndTime = endTime,]                                                                                                                                                              |
|                                                                                                                                                                                                                                                    |
| [                    Subject = args.Subject,]                                                                                                                                                         |
|                                                                                                                                                                                                                                                    |
| [                    Location = args.Location,]                                                                                                                                                       |
|                                                                                                                                                                                                                                                    |
| [                    Descrip = args.Description,]                                                                                                                                                     |
|                                                                                                                                                                                                                                                    |
| [                    Resource = args.Owner,]                                                                                                                                                          |
|                                                                                                                                                                                                                                                    |
| **[                    Reminder = [Convert].ToInt32(args.Reminder)]**                                                                                                         |
|                                                                                                                                                                                                                                                    |
| [                };]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                    |
| [                db.AppointmentTables.InsertOnSubmit(appoint);]                                                                                                                                       |
|                                                                                                                                                                                                                                                    |
| [            }]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                    |
| [            [// Update existing apppointment with Reminder]]                                                                                                                   |
|                                                                                                                                                                                                                                                    |
| [            [else] [if] (args.CurrentAction == [\"Edit\"])]                                                                        |
|                                                                                                                                                                                                                                                    |
| [            {]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                    |
| [var][ filterData = db.AppointmentTables.Where(c =\> c.AppId == [Convert].ToInt32(args.AppID));]                    |
|                                                                                                                                                                                                                                                    |
| [                [if] (filterData.Count() \> 0)]                                                                                                                                 |
|                                                                                                                                                                                                                                                    |
| [                {]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                    |
| [                    [DateTime] startTime = [Convert].ToDateTime(args.StartTime);]                                                                    |
|                                                                                                                                                                                                                                                    |
| [                    [DateTime] endTime = [Convert].ToDateTime(args.EndTime);]                                                                        |
|                                                                                                                                                                                                                                                    |
| [     AppointmentTable][ appoint = db.AppointmentTables.Single(A =\> A.AppId == [Convert].ToInt32(args.AppID));] |
|                                                                                                                                                                                                                                                    |
| [                    appoint.StartTime = startTime;]                                                                                                                                                  |
|                                                                                                                                                                                                                                                    |
| [                    appoint.EndTime = endTime;]                                                                                                                                                      |
|                                                                                                                                                                                                                                                    |
| [                    appoint.Subject = args.Subject;]                                                                                                                                                 |
|                                                                                                                                                                                                                                                    |
| [                    appoint.Location = args.Location;]                                                                                                                                               |
|                                                                                                                                                                                                                                                    |
| [                    appoint.Descrip = args.Description;]                                                                                                                                             |
|                                                                                                                                                                                                                                                    |
| [                    appoint.Resource = args.Owner;]                                                                                                                                                  |
|                                                                                                                                                                                                                                                    |
| **[                    appoint.Reminder = [Convert].ToInt32(args.Reminder);]**                                                                                                |
|                                                                                                                                                                                                                                                    |
| [                }]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                    |
| [            }]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                    |
| [            [//to reflect in database]]                                                                                                                                        |
|                                                                                                                                                                                                                                                    |
| [            db.SubmitChanges();]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                    |
| [ActionResult][ result = db.AppointmentTables.ScheduleActions\<[ScheduleHtmlActionResult]\>();]                  |
|                                                                                                                                                                                                                                                    |
| [            [return] result;]                                                                                                                                                   |
|                                                                                                                                                                                                                                                    |
| [        }]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

8.   Run the application. The Schedule's reminder dialog will appear as shown below.

[] 

{border="0"}

[] 

Figure 120: Reminder Dialog

[] 

[]{#related-topics}

