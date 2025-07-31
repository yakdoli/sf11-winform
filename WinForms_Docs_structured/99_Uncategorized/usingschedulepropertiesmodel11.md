---
title: usingschedulepropertiesmodel11.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingschedulepropertiesmodel11.md
created_at: 2025-07-03
---






#### [Using SchedulePropertiesModel] {#using-schedulepropertiesmodel style="MARGIN-TOP: 0pt; tab-stops: 0pt"}

The steps to customize Print feature using SchedulePropertiesModel are as follows:

1.   C[reating] a model in the application.[ ]

2.   Adding the following code in the Index.aspx file, to create the **Schedule** control in **View**.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**[[]]{.MsoIntenseEmphasis}                                                                                                     |
|                                                                                                                                                                                                                                                                |
| [       [\<%][=]Html.Syncfusion().Schedule()([\"FlatSchedule\"] ,[\"ScheduleModel\"])[]] |
|                                                                                                                                                                                                                                                                |
| [       .BindList(columns =\>]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                |
| [       {]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                |
| [           columns.IdField([\"AppId\"]);]                                                                                                                                                |
|                                                                                                                                                                                                                                                                |
| [           columns.SubjectField([\"Subject\"]);]                                                                                                                                         |
|                                                                                                                                                                                                                                                                |
| [           columns.LocationField([\"Location\"]);]                                                                                                                                       |
|                                                                                                                                                                                                                                                                |
| [           columns.StartTimeField([\"StartTime\"]);]                                                                                                                                     |
|                                                                                                                                                                                                                                                                |
| [           columns.EndTimeField([\"EndTime\"]);]                                                                                                                                         |
|                                                                                                                                                                                                                                                                |
| [           columns.DescriptionField([\"Descrip\"]);]                                                                                                                                     |
|                                                                                                                                                                                                                                                                |
| [           columns.OwnerField([\"Resource\"]);]                                                                                                                                          |
|                                                                                                                                                                                                                                                                |
| [       })]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                |
| [        [%\>]]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**[[]]{.MsoIntenseEmphasis}                                                  |
|                                                                                                                                                                                                               |
| [    [@(] Html.Syncfusion().Schedule()([\"FlatSchedule\"] ,[\"ScheduleModel\"])] |
|                                                                                                                                                                                                               |
| [       .BindList(columns =\>]                                                                                                                               |
|                                                                                                                                                                                                               |
| [       {]                                                                                                                                                   |
|                                                                                                                                                                                                               |
| [           columns.IdField([\"AppId\"]);]                                                                                           |
|                                                                                                                                                                                                               |
| [           columns.SubjectField([\"Subject\"]);]                                                                                    |
|                                                                                                                                                                                                               |
| [           columns.LocationField([\"Location\"]);]                                                                                  |
|                                                                                                                                                                                                               |
| [           columns.StartTimeField([\"StartTime\"]);]                                                                                |
|                                                                                                                                                                                                               |
| [           columns.EndTimeField([\"EndTime\"]);]                                                                                    |
|                                                                                                                                                                                                               |
| [           columns.DescriptionField([\"Descrip\"]);]                                                                                |
|                                                                                                                                                                                                               |
| [           columns.OwnerField([\"Resource\"]);]                                                                                     |
|                                                                                                                                                                                                               |
| [       })[)]]                                                                                                                   |
|                                                                                                                                                                                                               |
| []                                                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

3.   In **Controller**, add the Syncfusion.Mvc.Schedule, Syncfusion.Mvc.Shared namespaces.

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

4.   Create a **SchedulePropertiesModel** in the **Index** method. Use **ShowPrint** property to show the **Print** icon on the **viewstrip** toolbar.

5.   Create a context menu to perform print an appointment by using **ContextMenuItems** property.

6.   Pass this **SchedulePropertiesModel** from Controller to View using **ViewData** class as given below.

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
| [            [ContextMenuItem] quickPrint = [new] [ContextMenuItem]()]                                                   |
|                                                                                                                                                                                                                                            |
| [            {]                                                                                                                                                                               |
|                                                                                                                                                                                                                                            |
| [                MenuID = [\"Print\"],]                                                                                                                               |
|                                                                                                                                                                                                                                            |
| [                MenuName = [\"Quick Print\"],]                                                                                                                       |
|                                                                                                                                                                                                                                            |
| [                CommandName = [ContextCommandNames].QuickPrint]                                                                                                      |
|                                                                                                                                                                                                                                            |
| [            };][]                                                                                                             |
|                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                            |
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
| **[            scheduleModel.ShowPrint = [true];]**                                                                                                                      |
|                                                                                                                                                                                                                                            |
| **[            scheduleModel.ContextMenuItems = [new] [List]\<[ContextMenuItem]\>() { quickPrint };]**                   |
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

7.   Create a post method for Index action and bind the data source to Schedule as shown in the code displayed below.

[[]]{.MsoIntenseEmphasis} 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**[[]]{.MsoIntenseEmphasis}                                                                                         |
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
| [        [public] [ActionResult] Index([Params] args, [SchedulePropertiesModel] model)]                    |
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

8.   Run the application. To print a **Schedule**, click the **Print** icon. The **Print** window will appear as shown below.

[] 

{border="0"}

[] 

Figure 126: Print a Schedule

[] 

To print an appointment, make sure the **Quick Print** context menu item is added.After this setting, do the following:

9.   Right click the appointment, and click **Quick Print**.

[] 

{border="0"}

[] 

Figure 127: Print an appointment

[] 

[]{#related-topics}

