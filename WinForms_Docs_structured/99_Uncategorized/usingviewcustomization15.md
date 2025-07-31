---
title: usingviewcustomization15.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingviewcustomization15.md
created_at: 2025-07-03
---






#### Using View Customization {#using-view-customization style="tab-stops: 0pt"}

The steps to customize Calendar Navigation using View Customization are as follows:

1.   Create a model in the application.

[[2.   ]]{.UGHyperlink}Create a strongly typed view[[.]]{.UGHyperlink}

3.   In **View**, you can use its **Model** property in **DataSource** in order to bind the data source and bind your database fields into the corresponding Schedule fields.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**                                                                                                                      |
|                                                                                                                                                                                      |
| [    [\<%][=]Html.Syncfusion().Schedule()([\"FlatSchedule\"])] |
|                                                                                                                                                                                      |
| [       .DataSource(([IEnumerable]) Model)]                                                                     |
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

+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                |
|                                                                                                                                                                  |
| [    [@(] Html.Syncfusion().Schedule()([\"FlatSchedule\"])] |
|                                                                                                                                                                  |
| [       .DataSource(([IEnumerable]) Model)]                                             |
|                                                                                                                                                                  |
| [       .BindList(columns =\>]                                                                                  |
|                                                                                                                                                                  |
| [       {]                                                                                                      |
|                                                                                                                                                                  |
| [           columns.IdField([\"AppId\"]);]                                              |
|                                                                                                                                                                  |
| [           columns.SubjectField([\"Subject\"]);]                                       |
|                                                                                                                                                                  |
| [           columns.LocationField([\"Location\"]);]                                     |
|                                                                                                                                                                  |
| [           columns.StartTimeField([\"StartTime\"]);]                                   |
|                                                                                                                                                                  |
| [           columns.EndTimeField([\"EndTime\"]);]                                       |
|                                                                                                                                                                  |
| [           columns.DescriptionField([\"Descrip\"]);]                                   |
|                                                                                                                                                                  |
| [           columns.OwnerField([\"Resource\"]);]                                        |
|                                                                                                                                                                  |
| [       })[)]]                                                                      |
|                                                                                                                                                                  |
| []                                                                                                                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

4.   Set the **ShowNavigationPane()** method to show **Calendar Navigator**.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**                                                                                                                      |
|                                                                                                                                                                                      |
| [    [\<%][=]Html.Syncfusion().Schedule()([\"FlatSchedule\"])] |
|                                                                                                                                                                                      |
| [       .DataSource(([IEnumerable]) ViewData\[[\"data\"]\])]                            |
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
| [       .CurrentView([ScheduleViewMode].Week)    ]                                                              |
|                                                                                                                                                                                      |
| [       .Skins([ScheduleSkins].Sandune)]                                                                        |
|                                                                                                                                                                                      |
| **[       .ShowNavigationPane([true])]**                                                                           |
|                                                                                                                                                                                      |
| [    [%\>]]                                                                                                 |
|                                                                                                                                                                                      |
| []                                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                               |
|                                                                                                                                                                 |
| [][]                                                              |
|                                                                                                                                                                 |
| [   [@(] Html.Syncfusion().Schedule()([\"FlatSchedule\"])] |
|                                                                                                                                                                 |
| [       .DataSource(([IEnumerable]) ViewData\[[\"data\"]\])]   |
|                                                                                                                                                                 |
| [       .BindList(columns =\>]                                                                                 |
|                                                                                                                                                                 |
| [       {]                                                                                                     |
|                                                                                                                                                                 |
| [           columns.IdField([\"AppId\"]);]                                             |
|                                                                                                                                                                 |
| [           columns.SubjectField([\"Subject\"]);]                                      |
|                                                                                                                                                                 |
| [           columns.LocationField([\"Location\"]);]                                    |
|                                                                                                                                                                 |
| [           columns.StartTimeField([\"StartTime\"]);]                                  |
|                                                                                                                                                                 |
| [           columns.EndTimeField([\"EndTime\"]);]                                      |
|                                                                                                                                                                 |
| [           columns.DescriptionField([\"Descrip\"]);]                                  |
|                                                                                                                                                                 |
| [           columns.OwnerField([\"Resource\"]);]                                       |
|                                                                                                                                                                 |
| [       })]                                                                                                    |
|                                                                                                                                                                 |
| [       .CurrentView([ScheduleViewMode].Week)    ]                                     |
|                                                                                                                                                                 |
| [       .Skins([ScheduleSkins].Sandune)]                                               |
|                                                                                                                                                                 |
| [       .ShowNavigationPane([true])]                                                      |
|                                                                                                                                                                 |
| [       [)]]                                                                       |
|                                                                                                                                                                 |
| []                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

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
| [ViewData\[[\"data\"]\] = data;]                                                                                                                                      |
|                                                                                                                                                                                                                                            |
| [            [return] View();]                                                                                                                                           |
|                                                                                                                                                                                                                                            |
| [        }]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

7.   Create a post method for **Index** action and bind the data source to Schedule, as shown in the code displayed below.

[[]]{.MsoIntenseEmphasis} 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**[[]]{.MsoIntenseEmphasis}                                                                                         |
|                                                                                                                                                                                                                                                      |
| [  ][      [///][ ][\<summary\>]]                                             |
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
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

8.   Run the application, the Schedule will appear as shown in the following screenshot.

[] 

{border="0"}

Figure 136: Calendar Navigation[]

[]{#related-topics}

