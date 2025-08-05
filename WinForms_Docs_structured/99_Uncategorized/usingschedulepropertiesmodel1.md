---
title: usingschedulepropertiesmodel1.md
original_path: WinForms_Docs/99_Uncategorized/usingschedulepropertiesmodel1.md
created_at: 2025-08-05
---






#### Using SchedulePropertiesModel {#using-schedulepropertiesmodel style="tab-stops: 0pt"}

The steps to customize the **ViewStrip** toolbar using **SchedulePropertiesModel** are as follows:

1.   [Create a model in the application]{.UGHyperlink}[.][ ]

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
| [       })]                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                              |
| [       [%\>]][]                                                                                                                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**[[]]{.MsoIntenseEmphasis}                                                   |
|                                                                                                                                                                                                                |
| [   ][ ][    ]                                                      |
|                                                                                                                                                                                                                |
| [      [@(] Html.Syncfusion().Schedule()([\"FlatSchedule\"],[\"ScheduleModel\"])] |
|                                                                                                                                                                                                                |
| [       .BindList(columns =\>]                                                                                                                                |
|                                                                                                                                                                                                                |
| [       {]                                                                                                                                                    |
|                                                                                                                                                                                                                |
| [           columns.IdField([\"AppId\"]);]                                                                                            |
|                                                                                                                                                                                                                |
| [           columns.SubjectField([\"Subject\"]);]                                                                                     |
|                                                                                                                                                                                                                |
| [           columns.LocationField([\"Location\"]);]                                                                                   |
|                                                                                                                                                                                                                |
| [           columns.StartTimeField([\"StartTime\"]);]                                                                                 |
|                                                                                                                                                                                                                |
| [           columns.EndTimeField([\"EndTime\"]);]                                                                                     |
|                                                                                                                                                                                                                |
| [           columns.DescriptionField([\"Descrip\"]);]                                                                                 |
|                                                                                                                                                                                                                |
| [           columns.OwnerField([\"Resource\"]);]                                                                                      |
|                                                                                                                                                                                                                |
| [       })[)]]                                                                                                                    |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

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

4.   Create a **SchedulePropertiesModel** in the **Index** method and set **CurrentView** property to activate the view type feature. Pass this **SchedulePropertiesModel** from Controller to View using **ViewData** class as shown below.

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
| **[            scheduleModel.CurrentView = [ScheduleViewMode].Week;]**                                                                                                |
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

5.   Create a post method for Index action and bind the data source to **Schedule**, as shown in the code displayed below:

[[]]{.MsoIntenseEmphasis} 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                      |
| [        [///][ ][\<summary\>]]                                                                                                         |
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
| [        }]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

6.   Run the application. The Schedule will appear as shown below when the CurrentView property is Day.[]

[] 

{border="0"}

Figure 100: ViewType -- Day

[] 

The Schedule will appear as shown below when CurrentView property is Week.

{border="0"}

Figure 101: ViewType -- Week

[] 

The Schedule will appear as shown below when the CurrentView property is Workweek.

[] 

{border="0"}

[] 

Figure 102: ViewType -- Workweek

[] 

The Schedule will appear as shown below when the CurrentView property is Month.

[] 

{border="0"}

[] 

Figure 103: ViewType -- Month

[] 

[]{#related-topics}

