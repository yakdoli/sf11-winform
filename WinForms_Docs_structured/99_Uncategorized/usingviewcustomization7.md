---
title: usingviewcustomization7.md
original_path: WinForms_Docs/99_Uncategorized/usingviewcustomization7.md
created_at: 2025-08-05
---






##### Using View Customization {#using-view-customization style="tab-stops: 0pt"}

The steps to customize the drag and drop appointment through **View Customization** are as follows:

1.   [Create a model in the application]{.UGHyperlink}[.][ ]

[[2.   ]]{.UGHyperlink}[Create a strongly typed view.]{.UGHyperlink}[ ]{.UGHyperlink}

3.   In **View**, you can use its **Model** property in DataSource in order to bind the data source and bind your database fields into the corresponding Schedule fields.

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
| [       })]                                                                                                                             |
|                                                                                                                                                                                      |
| [    [%\>]]                                                                                                 |
|                                                                                                                                                                                      |
| []                                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                                                  |
|                                                                                                                                                                                                                    |
| [  ][     [@(] Html.Syncfusion().Schedule()([\"FlatSchedule\"])] |
|                                                                                                                                                                                                                    |
| [       .DataSource(([IEnumerable])Model)]                                                                                                |
|                                                                                                                                                                                                                    |
| [       .BindList(columns =\>]                                                                                                                                    |
|                                                                                                                                                                                                                    |
| [       {]                                                                                                                                                        |
|                                                                                                                                                                                                                    |
| [           columns.IdField([\"AppId\"]);]                                                                                                |
|                                                                                                                                                                                                                    |
| [           columns.SubjectField([\"Subject\"]);]                                                                                         |
|                                                                                                                                                                                                                    |
| [           columns.LocationField([\"Location\"]);]                                                                                       |
|                                                                                                                                                                                                                    |
| [           columns.StartTimeField([\"StartTime\"]);]                                                                                     |
|                                                                                                                                                                                                                    |
| [           columns.EndTimeField([\"EndTime\"]);]                                                                                         |
|                                                                                                                                                                                                                    |
| [           columns.DescriptionField([\"Descrip\"]);]                                                                                     |
|                                                                                                                                                                                                                    |
| [           columns.OwnerField([\"Resource\"]);]                                                                                          |
|                                                                                                                                                                                                                    |
| [       })[)]]                                                                                                                        |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                                |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                                |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Set the **AllowDragAndDrop()** method to perform dragging appointment.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**                                                                                                                                          |
|                                                                                                                                                                                                          |
| [    [\<%][=]Html.Syncfusion().Schedule()([\"FlatSchedule\"])]                     |
|                                                                                                                                                                                                          |
| [       .DataSource(([IEnumerable])Model)]                                                                                          |
|                                                                                                                                                                                                          |
| [       .BindList(columns =\>]                                                                                                                              |
|                                                                                                                                                                                                          |
| [       {]                                                                                                                                                  |
|                                                                                                                                                                                                          |
| [           columns.IdField([\"AppId\"]);]                                                                                          |
|                                                                                                                                                                                                          |
| [           columns.SubjectField([\"Subject\"]);]                                                                                   |
|                                                                                                                                                                                                          |
| [           columns.LocationField([\"Location\"]);]                                                                                 |
|                                                                                                                                                                                                          |
| [           columns.StartTimeField([\"StartTime\"]);]                                                                               |
|                                                                                                                                                                                                          |
| [           columns.EndTimeField([\"EndTime\"]);]                                                                                   |
|                                                                                                                                                                                                          |
| [           columns.DescriptionField([\"Descrip\"]);]                                                                               |
|                                                                                                                                                                                                          |
| [           columns.OwnerField([\"Resource\"]);]                                                                                    |
|                                                                                                                                                                                                          |
| [       })]                                                                                                                                                 |
|                                                                                                                                                                                                          |
| [       .CurrentView([ScheduleViewMode].Week)    ]                                                                                  |
|                                                                                                                                                                                                          |
| [       .Skins([ScheduleSkins].Sandune)]                                                                                            |
|                                                                                                                                                                                                          |
| **[       .][ ][AllowDragAndDrop ([true])]** |
|                                                                                                                                                                                                          |
| [    [%\>]]                                                                                                                     |
|                                                                                                                                                                                                          |
| []                                                                                                                                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                         |
| [   ][@(][ Html.Syncfusion().Schedule()([\"FlatSchedule\"])] |
|                                                                                                                                                                                                                                                         |
| [       .DataSource(([IEnumerable])Model)]                                                                                                                                     |
|                                                                                                                                                                                                                                                         |
| [       .BindList(columns =\>]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                         |
| [       {]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                         |
| [           columns.IdField([\"AppId\"]);]                                                                                                                                     |
|                                                                                                                                                                                                                                                         |
| [           columns.SubjectField([\"Subject\"]);]                                                                                                                              |
|                                                                                                                                                                                                                                                         |
| [           columns.LocationField([\"Location\"]);]                                                                                                                            |
|                                                                                                                                                                                                                                                         |
| [           columns.StartTimeField([\"StartTime\"]);]                                                                                                                          |
|                                                                                                                                                                                                                                                         |
| [           columns.EndTimeField([\"EndTime\"]);]                                                                                                                              |
|                                                                                                                                                                                                                                                         |
| [           columns.DescriptionField([\"Descrip\"]);]                                                                                                                          |
|                                                                                                                                                                                                                                                         |
| [           columns.OwnerField([\"Resource\"]);]                                                                                                                               |
|                                                                                                                                                                                                                                                         |
| [       })]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                         |
| [       .CurrentView([ScheduleViewMode].Week)    ]                                                                                                                             |
|                                                                                                                                                                                                                                                         |
| [       .Skins([ScheduleSkins].Sandune)]                                                                                                                                       |
|                                                                                                                                                                                                                                                         |
| [       . AllowDragAndDrop ([true])]                                                                                                                                              |
|                                                                                                                                                                                                                                                         |
| [       [)]]                                                                                                                                                               |
|                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   In Controller, add the Syncfusion.Mvc.Schedule, Syncfusion.Mvc.Shared namespaces.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**[[]]{.MsoIntenseEmphasis} |
|                                                                                                                                                              |
| [using][ Syncfusion.Mvc.Schedule;]                    |
|                                                                                                                                                              |
| [using][ Syncfusion.Mvc.Shared;]                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

6.   Set its **Data Source** and render the **View**.

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

7.   Create a post method for Index action and bind the data source to **Schedule**, as shown in the code displayed below.

[[]]{.MsoIntenseEmphasis} 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**[[]]{.MsoIntenseEmphasis}                                                                                               |
|                                                                                                                                                                                                                                                            |
| [  ][       [///][ ][\<summary\>]]                                                  |
|                                                                                                                                                                                                                                                            |
| [        [///][ Post Requests are mapped to this method. This method invokes the HtmlActionResult]]                                                                |
|                                                                                                                                                                                                                                                            |
| [        [///][ from the Schedule. Required response is generated.]]                                                                                               |
|                                                                                                                                                                                                                                                            |
| [        [///][ ][\</summary\>]]                                                                                                              |
|                                                                                                                                                                                                                                                            |
| [        [///][ ][\<param name=\"args\"\>][Contains post action properties ][\</param\>]]          |
|                                                                                                                                                                                                                                                            |
| [        [///][ ][\<returns\>]]                                                                                                               |
|                                                                                                                                                                                                                                                            |
| [        [///][ HtmlActionResult which returns data displayed on the Schedule]]                                                                                    |
|                                                                                                                                                                                                                                                            |
| [        [///][ ][\</returns\>]]                                                                                                              |
|                                                                                                                                                                                                                                                            |
| [        \[[AcceptVerbs]([HttpVerbs].Post)\]]                                                                                                                 |
|                                                                                                                                                                                                                                                            |
| [        [public] [ActionResult] Index([Params] args, [SchedulePropertiesModel] model)]                          |
|                                                                                                                                                                                                                                                            |
| [        {]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                            |
| [NorthwindDataClassesDataContext][ db = [new] [NorthwindDataClassesDataContext]();]                 |
|                                                                                                                                                                                                                                                            |
| [            model.SetCurrentCultureInfo();]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                            |
| [            [// Update existing apppointment with dragging arguments]]                                                                                                                 |
|                                                                                                                                                                                                                                                            |
| [            [if] (args.CurrentAction == [\"DragDrop\"])]                                                                                                        |
|                                                                                                                                                                                                                                                            |
| [            {]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                            |
| [ [var] filterData = db.AppointmentTables.Where(c =\> c.AppId == [Convert].ToInt32(args.AppID));]                                                                |
|                                                                                                                                                                                                                                                            |
| [                [if] (filterData.Count() \> 0)]                                                                                                                                         |
|                                                                                                                                                                                                                                                            |
| [                {]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                            |
| [                    [DateTime] startTime = [Convert].ToDateTime(args.StartTime);]                                                                            |
|                                                                                                                                                                                                                                                            |
| [                    [DateTime] endTime = [Convert].ToDateTime(args.EndTime);]                                                                                |
|                                                                                                                                                                                                                                                            |
| [     AppointmentTable][ appoint = db.AppointmentTables.Single(A =\> A.AppId ==         [Convert].ToInt32(args.AppID));] |
|                                                                                                                                                                                                                                                            |
| [                    appoint.StartTime = startTime;]                                                                                                                                                          |
|                                                                                                                                                                                                                                                            |
| [                    appoint.EndTime = endTime;]                                                                                                                                                              |
|                                                                                                                                                                                                                                                            |
| [     appoint.Resource = args.Owner;]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                            |
| [                }]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                            |
| [            }]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                            |
| [            [//to reflect in database]]                                                                                                                                                |
|                                                                                                                                                                                                                                                            |
| [            db.SubmitChanges();]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                            |
| [ActionResult][ result = db.AppointmentTables.ScheduleActions\<[ScheduleHtmlActionResult]\>();]                          |
|                                                                                                                                                                                                                                                            |
| [            [return] result;]                                                                                                                                                           |
|                                                                                                                                                                                                                                                            |
| [        }]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

8.   Run the application. The schedule will appear as shown below with the dragged appointment by arrow.

[] 

{border="0"}

[] 

Figure 116: Drag and Drop Appointment

[] 

[]{#related-topics}

