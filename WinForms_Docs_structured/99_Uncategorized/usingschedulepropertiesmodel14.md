---
title: usingschedulepropertiesmodel14.md
original_path: WinForms_Docs/99_Uncategorized/usingschedulepropertiesmodel14.md
created_at: 2025-08-05
---






#### Using SchedulePropertiesModel {#using-schedulepropertiesmodel style="tab-stops: 0pt"}

The steps to customize Multiple Resources using SchedulePropertiesModel are as follows:

1.   [Create a model in the application]{.UGHyperlink}[.][ ]

2.   Add the following code in the Index.aspx file, to create the Schedule control in **View**.

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
| [        [%\>]]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**[[]]{.MsoIntenseEmphasis}                                                                                                 |
|                                                                                                                                                                                                                                                              |
| [ ][    [@(]Html.Syncfusion().Schedule()([\"FlatSchedule\"], [\"ScheduleModel\"])] |
|                                                                                                                                                                                                                                                              |
| [       .BindList(columns =\>]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                              |
| [       {]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                              |
| [           columns.IdField([\"AppId\"]);]                                                                                                                                          |
|                                                                                                                                                                                                                                                              |
| [           columns.SubjectField([\"Subject\"]);]                                                                                                                                   |
|                                                                                                                                                                                                                                                              |
| [           columns.LocationField([\"Location\"]);]                                                                                                                                 |
|                                                                                                                                                                                                                                                              |
| [           columns.StartTimeField([\"StartTime\"]);]                                                                                                                               |
|                                                                                                                                                                                                                                                              |
| [           columns.EndTimeField([\"EndTime\"]);]                                                                                                                                   |
|                                                                                                                                                                                                                                                              |
| [           columns.DescriptionField([\"Descrip\"]);]                                                                                                                               |
|                                                                                                                                                                                                                                                              |
| [           columns.OwnerField([\"Resource\"]);]                                                                                                                                    |
|                                                                                                                                                                                                                                                              |
| [       })[)]]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

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

5.   Use AllowMultipleResource property to allow multiple resources.

6.   Add multiple resources by **Resources** collection.

7.   To view the resource names set the **ShowResourceHeader** property.

8.   Pass this **SchedulePropertiesModel** from **Controller** to **View** using **ViewData** class as shown below.

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
| [            [SchedulePropertiesModel] schduleModel = [new] [SchedulePropertiesModel]();]                                |
|                                                                                                                                                                                                                                            |
| [            ScheduleModel.DataSource = data;]                                                                                                                                                |
|                                                                                                                                                                                                                                            |
| [            [// Creating Multiple Resources]]                                                                                                                          |
|                                                                                                                                                                                                                                            |
| [            [ScheduleResource] Resource1 = [new] [ScheduleResource]()]                                                  |
|                                                                                                                                                                                                                                            |
| [            {]                                                                                                                                                                               |
|                                                                                                                                                                                                                                            |
| [                ResourceID = 1,]                                                                                                                                                             |
|                                                                                                                                                                                                                                            |
| [                ResourceName = [\"Andrew\"],]                                                                                                                        |
|                                                                                                                                                                                                                                            |
| [            };]                                                                                                                                                                              |
|                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                            |
|                                                                                                                                                                                                                                            |
| [            [ScheduleResource] Resource2 = [new] [ScheduleResource]()]                                                  |
|                                                                                                                                                                                                                                            |
| [            {]                                                                                                                                                                               |
|                                                                                                                                                                                                                                            |
| [                ResourceID = 2,]                                                                                                                                                             |
|                                                                                                                                                                                                                                            |
| [                ResourceName = [\"Michael\"],]                                                                                                                       |
|                                                                                                                                                                                                                                            |
| [            };]                                                                                                                                                                              |
|                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                            |
|                                                                                                                                                                                                                                            |
| [            [ScheduleResource] Resource3 = [new] [ScheduleResource]()]                                                  |
|                                                                                                                                                                                                                                            |
| [            {]                                                                                                                                                                               |
|                                                                                                                                                                                                                                            |
| [                ResourceID = 3,]                                                                                                                                                             |
|                                                                                                                                                                                                                                            |
| [                ResourceName = [\"Thomas\"],]                                                                                                                        |
|                                                                                                                                                                                                                                            |
| [            };]                                                                                                                                                                              |
|                                                                                                                                                                                                                                            |
| [            [// Adding resources to schedule control]]                                                                                                                 |
|                                                                                                                                                                                                                                            |
| **[scheduleModel.Resources = [new] [List]\<[ScheduleResource]\>() { Resource1, Resource2, Resource3 };]**                |
|                                                                                                                                                                                                                                            |
| **[            scheduleModel.AllowMultipleResource = [true];]**                                                                                                          |
|                                                                                                                                                                                                                                            |
| **[            scheduleModel.ShowResourceHeader = [true];]**                                                                                                             |
|                                                                                                                                                                                                                                            |
| [            scheduleModel.Skins = [ScheduleSkins].Sandune;]                                                                                                          |
|                                                                                                                                                                                                                                            |
| [            scheduleModel.CurrentView = [ScheduleViewMode].Day;]                                                                                                     |
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

9.   Create a post method for Index action and bind the data source to **Schedule**, as shown in the code displayed below.

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
| [        [public] [ActionResult] Index([Params] args)]                                                                             |
|                                                                                                                                                                                                                                                      |
| [        {]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                      |
| [IEnumerable][ data = [new] [NorthwindDataClassesDataContext]().AppointmentTables.Take(200);] |
|                                                                                                                                                                                                                                                      |
| [                [return] data.ScheduleActions\<[ScheduleHtmlActionResult]\>();]                                                                           |
|                                                                                                                                                                                                                                                      |
| [        }]                                                                                                                                                                                             |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

10.  Run the application. The Schedule will appear as shown in the following screenshot.

[] 

{border="0"}

Figure 135: Multiple Resources

[]{#related-topics}

