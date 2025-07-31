---
title: howtocreatethescheduleusingviewcustomizationwithdefaultview.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtocreatethescheduleusingviewcustomizationwithdefaultview.md
created_at: 2025-07-03
---








  









## How to Create the Schedule using View Customization with Default View? {#how-to-create-the-schedule-using-view-customization-with-default-view style="tab-stops: 0pt"}

 

1.   [Create a model in the application]{.UGHyperlink}[.]

2.   In the **Index** view, you can use **DataSource** in order to bind the data source. Then you need to explicitly specify the type of the data item.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**[[]]{.MsoIntenseEmphasis}                               |
|                                                                                                                                                                                          |
| [        [\<%][=]Html.Syncfusion().Schedule()([\"FlatSchedule\"])] |
|                                                                                                                                                                                          |
| [        .DataSource(([IEnumerable])Model)]                                                                         |
|                                                                                                                                                                                          |
| [        .AllowAddNew([true])]                                                                                         |
|                                                                                                                                                                                          |
| [        .AllowDelete([true])]                                                                                         |
|                                                                                                                                                                                          |
| [        .AllowDragAndDrop([true])]                                                                                    |
|                                                                                                                                                                                          |
| [        .AllowEdit([true])]                                                                                           |
|                                                                                                                                                                                          |
| [        .AllowMultipleResource([true])]                                                                               |
|                                                                                                                                                                                          |
| [        .AllowPriority([true])]                                                                                       |
|                                                                                                                                                                                          |
| [        .AllowRecurrence([true])]                                                                                     |
|                                                                                                                                                                                          |
| [        .AllowReminder([true])]                                                                                       |
|                                                                                                                                                                                          |
| [        .AllowResize([true])]                                                                                         |
|                                                                                                                                                                                          |
| [        .BindList(columns =\>]                                                                                                             |
|                                                                                                                                                                                          |
| [         {]                                                                                                                                |
|                                                                                                                                                                                          |
| [           columns.IdField([\"AppId\"]);]                                                                          |
|                                                                                                                                                                                          |
| [           columns.SubjectField([\"Subject\"]);]                                                                   |
|                                                                                                                                                                                          |
| [           columns.LocationField([\"Location\"]);]                                                                 |
|                                                                                                                                                                                          |
| [           columns.StartTimeField([\"StartTime\"]);]                                                               |
|                                                                                                                                                                                          |
| [           columns.EndTimeField([\"EndTime\"]);]                                                                   |
|                                                                                                                                                                                          |
| [           columns.DescriptionField([\"Descrip\"]);]                                                               |
|                                                                                                                                                                                          |
| [           columns.OwnerField([\"Resource\"]);]                                                                    |
|                                                                                                                                                                                          |
| [         })]                                                                                                                               |
|                                                                                                                                                                                          |
| [         .ShowNavigationPane([true])]                                                                                 |
|                                                                                                                                                                                          |
| [        .CurrentView([ScheduleViewMode].Day)]                                                                      |
|                                                                                                                                                                                          |
| [        .CurrentDate([new] [DateTime](2010,1,1))]                                             |
|                                                                                                                                                                                          |
| [        .Skins([ScheduleSkins].Sandune)]                                                                           |
|                                                                                                                                                                                          |
| [        [%\>]]                                                                                                 |
|                                                                                                                                                                                          |
| []                                                                                                                                          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**[[]]{.MsoIntenseEmphasis}        |
|                                                                                                                                                                     |
| [       [@(] Html.Syncfusion().Schedule()([\"FlatSchedule\"])] |
|                                                                                                                                                                     |
| [        .DataSource(([IEnumerable])Model)]                                                |
|                                                                                                                                                                     |
| [        .AllowAddNew([true])]                                                                |
|                                                                                                                                                                     |
| [        .AllowDelete([true])]                                                                |
|                                                                                                                                                                     |
| [        .AllowDragAndDrop([true])]                                                           |
|                                                                                                                                                                     |
| [        .AllowEdit([true])]                                                                  |
|                                                                                                                                                                     |
| [        .AllowMultipleResource([true])]                                                      |
|                                                                                                                                                                     |
| [        .AllowPriority([true])]                                                              |
|                                                                                                                                                                     |
| [        .AllowRecurrence([true])]                                                            |
|                                                                                                                                                                     |
| [        .AllowReminder([true])]                                                              |
|                                                                                                                                                                     |
| [        .AllowResize([true])]                                                                |
|                                                                                                                                                                     |
| [        .BindList(columns =\>]                                                                                    |
|                                                                                                                                                                     |
| [         {]                                                                                                       |
|                                                                                                                                                                     |
| [           columns.IdField([\"AppId\"]);]                                                 |
|                                                                                                                                                                     |
| [           columns.SubjectField([\"Subject\"]);]                                          |
|                                                                                                                                                                     |
| [           columns.LocationField([\"Location\"]);]                                        |
|                                                                                                                                                                     |
| [           columns.StartTimeField([\"StartTime\"]);]                                      |
|                                                                                                                                                                     |
| [           columns.EndTimeField([\"EndTime\"]);]                                          |
|                                                                                                                                                                     |
| [           columns.DescriptionField([\"Descrip\"]);]                                      |
|                                                                                                                                                                     |
| [           columns.OwnerField([\"Resource\"]);]                                           |
|                                                                                                                                                                     |
| [         })]                                                                                                      |
|                                                                                                                                                                     |
| [         .ShowNavigationPane([true])]                                                        |
|                                                                                                                                                                     |
| [        .CurrentView([ScheduleViewMode].Day)]                                             |
|                                                                                                                                                                     |
| [        .CurrentDate([new] [DateTime](2010,1,1))]                    |
|                                                                                                                                                                     |
| [        .Skins([ScheduleSkins].Sandune)[)]]                   |
|                                                                                                                                                                     |
| []                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

3.   In **Controller**, add the Syncfusion.Mvc.Schedule, Syncfusion.Mvc.Shared namespaces.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**[[]]{.MsoIntenseEmphasis}                           |
|                                                                                                                                                                                        |
| [using][ Syncfusion.Mvc.Schedule;]                                              |
|                                                                                                                                                                                        |
| [using][ Syncfusion.Mvc.Shared;][] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Set its data source and render the view.

[      ]

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[ \[Controller\]]**                                                                                                                                                                         |
|                                                                                                                                                                                                                                            |
| [ [///][ ][\<summary\>]]                                                                                                      |
|                                                                                                                                                                                                                                            |
| [        [///][It is used to bind the Schedule]]                                                                                                   |
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
| [        }][]                                                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   Create a post method for Index action and bind the data source to Schedule, as shown in the code displayed below.

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
| [                [return] data.ScheduleActions\<[ScheduleHtmlActionResult]\>();]                                                                           |
|                                                                                                                                                                                                                                                      |
| [        }][]                                                                                                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[[]]{.MsoIntenseEmphasis} 

[[]]{.MsoIntenseEmphasis} 

6.   Run the application. The Schedule will appear as shown below.

 

{border="0"}

Figure 161[: Essential Schedule Control]

[] 

[] 

[]{#related-topics}

