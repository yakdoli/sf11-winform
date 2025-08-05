---
title: usingschedulepropertiesmodel13.md
original_path: WinForms_Docs/99_Uncategorized/usingschedulepropertiesmodel13.md
created_at: 2025-08-05
---






#### [Using SchedulePropertiesModel] {#using-schedulepropertiesmodel style="MARGIN-TOP: 0pt; tab-stops: 0pt"}

The steps to customize TimeMode using SchedulePropertiesModel are as follows:

1.   [[Create a model in the application]]{.UGHyperlink}[.]

2.   Add the following code in the Index.aspx file, to create the Schedule control in **View**.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                               |
| [[]]{.MsoIntenseEmphasis}                                                                                                                                                                                                                                        |
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
| [      [%\>]]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\][]{.MsoIntenseEmphasis}]**                                                                                                                    |
|                                                                                                                                                                                                             |
| [  [@(] Html.Syncfusion().Schedule()([\"FlatSchedule\"] ,[\"ScheduleModel\"])] |
|                                                                                                                                                                                                             |
| [       .BindList(columns =\>]                                                                                                                             |
|                                                                                                                                                                                                             |
| [       {]                                                                                                                                                 |
|                                                                                                                                                                                                             |
| [           columns.IdField([\"AppId\"]);]                                                                                         |
|                                                                                                                                                                                                             |
| [           columns.SubjectField([\"Subject\"]);]                                                                                  |
|                                                                                                                                                                                                             |
| [           columns.LocationField([\"Location\"]);]                                                                                |
|                                                                                                                                                                                                             |
| [           columns.StartTimeField([\"StartTime\"]);]                                                                              |
|                                                                                                                                                                                                             |
| [           columns.EndTimeField([\"EndTime\"]);]                                                                                  |
|                                                                                                                                                                                                             |
| [           columns.DescriptionField([\"Descrip\"]);]                                                                              |
|                                                                                                                                                                                                             |
| [           columns.OwnerField([\"Resource\"]);]                                                                                   |
|                                                                                                                                                                                                             |
| [       })[)]]                                                                                                                 |
|                                                                                                                                                                                                             |
| []                                                                                                                                                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

3.   In Controller, add the Syncfusion.Mvc.Schedule, Syncfusion.Mvc.Shared namespaces.

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

4.   Create a **SchedulePropertiesModel** in the **Index** method and set **TimeMode** property to activate the TimeMode for appointment and timelines. Pass this **SchedulePropertiesModel** from Controller to View using **ViewData** class like as shown below.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                                                                                                          |
|                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                            |
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
| [            [SchedulePropertiesModel] schduleModel = [new] [SchedulePropertiesModel]();]                                |
|                                                                                                                                                                                                                                            |
| [            scheduleModel.DataSource = data;]                                                                                                                                                |
|                                                                                                                                                                                                                                            |
| **[            scheduleModel.TimeMode = [ScheduleTimeMode].Hours24;]**                                                                                                |
|                                                                                                                                                                                                                                            |
| [            scheduleModel.Skins = [ScheduleSkins].Sandune;]                                                                                                          |
|                                                                                                                                                                                                                                            |
| [            scheduleModel.CurrentView = [ScheduleViewMode].Week;]                                                                                                    |
|                                                                                                                                                                                                                                            |
| [            ViewData\[[\"ScheduleModel\"]\] = ScheduleModel;]                                                                                                        |
|                                                                                                                                                                                                                                            |
| [            [return] View();]                                                                                                                                           |
|                                                                                                                                                                                                                                            |
| [        }]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   Create a post method for **Index** action and bind the data source to Schedule, as shown in the code displayed below.

[[]]{.MsoIntenseEmphasis} 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                      |
| [[]]{.MsoIntenseEmphasis}                                                                                                                                                                               |
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
| [            [return] data.ScheduleActions\<[ScheduleHtmlActionResult]\>();]                                                                               |
|                                                                                                                                                                                                                                                      |
| [        }]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[[]]{.MsoIntenseEmphasis} 

6.   Run the application. The Schedule will appear as shown below when the **TimeMode** property is Hours12.

[] 

{border="0"}

[] 

Figure 132: TimeMode - Hours12

[] 

The Schedule will appear as shown below when the **TimeMode** property is Hours24.

[] 

{border="0"}

[] 

Figure 133: TimeMode - Hours24

[] 

[]{#related-topics}

