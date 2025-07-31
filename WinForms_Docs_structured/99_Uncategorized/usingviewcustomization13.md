---
title: usingviewcustomization13.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingviewcustomization13.md
created_at: 2025-07-03
---






#### [Using View customization] {#using-view-customization style="MARGIN-TOP: 0pt; tab-stops: 0pt"}

The steps to customize TimeMode using View Customization are as follows:

1.   [[Create a model in the application]]{.UGHyperlink}[.]

[[2.   ]]{.UGHyperlink}[[Create a strongly typed view.]]{.UGHyperlink}[[]]{.UGHyperlink}

3.   In View, you can use its **Model** property in **DataSource** in order to bind the data source and bind your database fields into the corresponding Schedule fields.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**                                                                                                                      |
|                                                                                                                                                                                      |
| []                                                                                                                                      |
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
| [           columns.StartTimeField([\"StartTime\"]);]                                                           |
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

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                                                        |
|                                                                                                                                                                                                                          |
| []                                                                                                                                                                          |
|                                                                                                                                                                                                                          |
| [    ][         [@(] Html.Syncfusion().Schedule()([\"FlatSchedule\"])] |
|                                                                                                                                                                                                                          |
| [       .DataSource(([IEnumerable])Model)]                                                                                                      |
|                                                                                                                                                                                                                          |
| [       .BindList(columns =\>]                                                                                                                                          |
|                                                                                                                                                                                                                          |
| [       {]                                                                                                                                                              |
|                                                                                                                                                                                                                          |
| [           columns.IdField([\"AppId\"]);]                                                                                                      |
|                                                                                                                                                                                                                          |
| [           columns.SubjectField([\"Subject\"]);]                                                                                               |
|                                                                                                                                                                                                                          |
| [           columns.LocationField([\"Location\"]);]                                                                                             |
|                                                                                                                                                                                                                          |
| [           columns.StartTimeField([\"StartTime\"]);]                                                                                           |
|                                                                                                                                                                                                                          |
| [           columns.EndTimeField([\"EndTime\"]);]                                                                                               |
|                                                                                                                                                                                                                          |
| [           columns.DescriptionField([\"Descrip\"]);]                                                                                           |
|                                                                                                                                                                                                                          |
| [           columns.OwnerField([\"Resource\"]);]                                                                                                |
|                                                                                                                                                                                                                          |
| [       })[)]]                                                                                                                              |
|                                                                                                                                                                                                                          |
| []                                                                                                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

4.   Set the **TimeMode()** method to activate the TimeMode for appointments and timelines.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**                                                                                                                      |
|                                                                                                                                                                                      |
| []                                                                                                                                      |
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
| **[       .TimeMode([ScheduleTimeMode].Hours24)]**                                                              |
|                                                                                                                                                                                      |
| [       .CurrentView([ScheduleViewMode].Week)    ]                                                              |
|                                                                                                                                                                                      |
| [       .Skins([ScheduleSkins].Sandune)]                                                                        |
|                                                                                                                                                                                      |
| [    [%\>]]                                                                                                 |
|                                                                                                                                                                                      |
| []                                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                          |
| [    ][@(][ Html.Syncfusion().Schedule()([\"FlatSchedule\"])] |
|                                                                                                                                                                                                                                                          |
| [       .DataSource(([IEnumerable])Model)]                                                                                                                                      |
|                                                                                                                                                                                                                                                          |
| [       .BindList(columns =\>]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                          |
| [       {]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                          |
| [           columns.IdField([\"AppId\"]);]                                                                                                                                      |
|                                                                                                                                                                                                                                                          |
| [           columns.SubjectField([\"Subject\"]);]                                                                                                                               |
|                                                                                                                                                                                                                                                          |
| [           columns.LocationField([\"Location\"]);]                                                                                                                             |
|                                                                                                                                                                                                                                                          |
| [           columns.StartTimeField([\"StartTime\"]);]                                                                                                                           |
|                                                                                                                                                                                                                                                          |
| [           columns.EndTimeField([\"EndTime\"]);]                                                                                                                               |
|                                                                                                                                                                                                                                                          |
| [           columns.DescriptionField([\"Descrip\"]);]                                                                                                                           |
|                                                                                                                                                                                                                                                          |
| [           columns.OwnerField([\"Resource\"]);]                                                                                                                                |
|                                                                                                                                                                                                                                                          |
| [       })]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                          |
| [       .TimeMode([ScheduleTimeMode].Hours24)]                                                                                                                                  |
|                                                                                                                                                                                                                                                          |
| [       .CurrentView([ScheduleViewMode].Week)    ]                                                                                                                              |
|                                                                                                                                                                                                                                                          |
| [       .Skins([ScheduleSkins].Sandune)]                                                                                                                                        |
|                                                                                                                                                                                                                                                          |
| [       [)]]                                                                                                                                                                |
|                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

5.   In Controller, add the Syncfusion.Mvc.Schedule, Syncfusion.Mvc.Shared namespaces.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                         |
|                                                                                                                                           |
| [[]]{.MsoIntenseEmphasis}                                                                    |
|                                                                                                                                           |
| [using][ Syncfusion.Mvc.Schedule;] |
|                                                                                                                                           |
| [using][ Syncfusion.Mvc.Shared;]   |
|                                                                                                                                           |
| []                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------+

[] 

6.   Set its data source and render the view.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                                                                                                          |
|                                                                                                                                                                                                                                            |
| [[]]{.MsoIntenseEmphasis}                                                                                                                                                                     |
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

7.   Create a post method for **Index** action and bind the data source to Schedule, as shown in the code displayed below.

[[]]{.MsoIntenseEmphasis} 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                      |
| [[]]{.MsoIntenseEmphasis}                                                                                                                                                                               |
|                                                                                                                                                                                                                                                      |
| [  ][       [///][ ][\<summary\>]]                                            |
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
| [            [return] data.ScheduleActions\<[ScheduleHtmlActionResult]\>();]                                                                               |
|                                                                                                                                                                                                                                                      |
| [        }]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

8.   Run the application. The Schedule will appear as shown in the following screenshot.

[] 

{border="0"}

[] 

Figure 130: TimeMode - Hours12

[] 

{border="0"}

[] 

Figure 131: TimeMode - Hours24

[] 

[]{#_Using_SchedulePropertiesModel_12} 

 

 

 

[]{#related-topics}

