---
title: usingviewcustomization11.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingviewcustomization11.md
created_at: 2025-07-03
---






#### [Using View Customization] {#using-view-customization style="MARGIN-TOP: 0pt; tab-stops: 0pt"}

The steps to customize Print feature using View Customization are as follows:

[] 

1.   Create a model in the application.

2.   Create a strongly typed view.

3.   In **View**, you can use  **Model** property in **DataSource** in order to bind the data source and bind your database fields into the corresponding **Schedule** fields.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [ **View\[aspx\]**]                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                            |
| [    [\<%][=]Html.Syncfusion().Schedule()([\"FlatSchedule\"])]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                            |
| [                       .DataSource(([IEnumerable])][ ViewData\[[\"data\"]\]][)][] |
|                                                                                                                                                                                                                                                                                                                                                            |
| [       .BindList(columns =\>]                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                            |
| [       {]                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                            |
| [           columns.IdField([\"AppId\"]);]                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                            |
| [           columns.SubjectField([\"Subject\"]);]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                            |
| [           columns.LocationField([\"Location\"]);]                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                            |
| [           columns.StartTimeField([\"StartTime\"]);]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                            |
| [           columns.EndTimeField([\"EndTime\"]);]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                            |
| [           columns.DescriptionField([\"Descrip\"]);]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                            |
| [           columns.OwnerField([\"Resource\"]);]                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                            |
| [       })]                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                            |
| [    [%\>]]                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [ **View\[cshtml\]**]                                                                                                          |
|                                                                                                                                                                             |
| [    [@(] Html.Syncfusion().Schedule()([\"FlatSchedule\"])]            |
|                                                                                                                                                                             |
| [                     .DataSource(([IEnumerable]) ViewData\[[\"data\"]\])] |
|                                                                                                                                                                             |
| [       .BindList(columns =\>]                                                                                             |
|                                                                                                                                                                             |
| [       {]                                                                                                                 |
|                                                                                                                                                                             |
| [           columns.IdField([\"AppId\"]);]                                                         |
|                                                                                                                                                                             |
| [           columns.SubjectField([\"Subject\"]);]                                                  |
|                                                                                                                                                                             |
| [           columns.LocationField([\"Location\"]);]                                                |
|                                                                                                                                                                             |
| [           columns.StartTimeField([\"StartTime\"]);]                                              |
|                                                                                                                                                                             |
| [           columns.EndTimeField([\"EndTime\"]);]                                                  |
|                                                                                                                                                                             |
| [           columns.DescriptionField([\"Descrip\"]);]                                              |
|                                                                                                                                                                             |
| [           columns.OwnerField([\"Resource\"]);]                                                   |
|                                                                                                                                                                             |
| [       })[)]]                                                                                 |
|                                                                                                                                                                             |
| []                                                                                                                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Set the **ShowPrint()** method to show the Print icon on the *Viewstrip* toolbar to print a Schedule and add the context menu to perform **print an appointment by ContextMenuItems()** method.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                           |
| [    [\<%][=]Html.Syncfusion().Schedule()([\"FlatSchedule\"])]                                                                                      |
|                                                                                                                                                                                                                                                                           |
| [       .DataSource(([IEnumerable])][ ViewData\[[\"data\"]\]][)] |
|                                                                                                                                                                                                                                                                           |
| [       .BindList(columns =\>]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                           |
| [       {]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                           |
| [           columns.IdField([\"AppId\"]);]                                                                                                                                                           |
|                                                                                                                                                                                                                                                                           |
| [           columns.SubjectField([\"Subject\"]);]                                                                                                                                                    |
|                                                                                                                                                                                                                                                                           |
| [           columns.LocationField([\"Location\"]);]                                                                                                                                                  |
|                                                                                                                                                                                                                                                                           |
| [           columns.StartTimeField([\"StartTime\"]);]                                                                                                                                                |
|                                                                                                                                                                                                                                                                           |
| [           columns.EndTimeField([\"EndTime\"]);]                                                                                                                                                    |
|                                                                                                                                                                                                                                                                           |
| [           columns.DescriptionField([\"Descrip\"]);]                                                                                                                                                |
|                                                                                                                                                                                                                                                                           |
| [           columns.OwnerField([\"Resource\"]);]                                                                                                                                                     |
|                                                                                                                                                                                                                                                                           |
| [       })]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                           |
| **[        .ContextMenuItems(([List]\<[ContextMenuItem]\>)ViewData\[[\"ContextMenu\"]\])]**                                        |
|                                                                                                                                                                                                                                                                           |
| [       .CurrentView([ScheduleViewMode].Week)    ]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                           |
| [       .Skins([ScheduleSkins].Sandune)]                                                                                                                                                             |
|                                                                                                                                                                                                                                                                           |
| **[       .ShowPrint([true])]**                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                           |
| [    [%\>]]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [ **View\[cshtml\]**]                                                                                                          |
|                                                                                                                                                                             |
| [    [@(] Html.Syncfusion().Schedule()([\"FlatSchedule\"])]            |
|                                                                                                                                                                             |
| [                     .DataSource(([IEnumerable]) ViewData\[[\"data\"]\])] |
|                                                                                                                                                                             |
| [       .BindList(columns =\>]                                                                                             |
|                                                                                                                                                                             |
| [       {]                                                                                                                 |
|                                                                                                                                                                             |
| [           columns.IdField([\"AppId\"]);]                                                         |
|                                                                                                                                                                             |
| [           columns.SubjectField([\"Subject\"]);]                                                  |
|                                                                                                                                                                             |
| [           columns.LocationField([\"Location\"]);]                                                |
|                                                                                                                                                                             |
| [           columns.StartTimeField([\"StartTime\"]);]                                              |
|                                                                                                                                                                             |
| [           columns.EndTimeField([\"EndTime\"]);]                                                  |
|                                                                                                                                                                             |
| [           columns.DescriptionField([\"Descrip\"]);]                                              |
|                                                                                                                                                                             |
| [           columns.OwnerField([\"Resource\"]);]                                                   |
|                                                                                                                                                                             |
| [       })[)]]                                                                                 |
|                                                                                                                                                                             |
| []                                                                                                                         |
|                                                                                                                                                                             |
| []                                                                                                                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   In Controller, add the Syncfusion.Mvc.Schedule, Syncfusion.Mvc.Shared namespaces.

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

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**[[]]{.MsoIntenseEmphasis}                                                                                    |
|                                                                                                                                                                                                                                                 |
| [        [///][ ][\<summary\>]]                                                                                                    |
|                                                                                                                                                                                                                                                 |
| [        [///][ It is used to bind the Schedule]]                                                                                                       |
|                                                                                                                                                                                                                                                 |
| [        [///][ ][\</summary\>]]                                                                                                   |
|                                                                                                                                                                                                                                                 |
| [        [///][ ][\<returns\>][View page, it displays the Schedule][\</returns\>]]      |
|                                                                                                                                                                                                                                                 |
| [        [public] [ActionResult] Index()]                                                                                                             |
|                                                                                                                                                                                                                                                 |
| [        {]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                 |
| [                [ContextMenuItem] quickPrint = [new] [ContextMenuItem]()]                                                    |
|                                                                                                                                                                                                                                                 |
| [                {]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                 |
| [                                MenuID=[\"Print\"],]                                                                                                                      |
|                                                                                                                                                                                                                                                 |
| [                                MenuName=[\"Quick Print\"],]                                                                                                              |
|                                                                                                                                                                                                                                                 |
| [                                CommandName=[ContextCommandNames].QuickPrint]                                                                                             |
|                                                                                                                                                                                                                                                 |
| [                };]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                 |
| [                ViewData\[[\"ContextMenu\"]\] = [new] [List]\<[ContextMenuItem]\>() { quickPrint };] |
|                                                                                                                                                                                                                                                 |
| [              [var] data = [new] [NorthwindDataClassesDataContext]().AppointmentTables.Take(200);]                              |
|                                                                                                                                                                                                                                                 |
| [ViewData\[[\"data\"]\] = data;]                                                                                                                                           |
|                                                                                                                                                                                                                                                 |
| [                [return] View();]                                                                                                                                            |
|                                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                 |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

7.   Create a post method for Index action and bind the data source to **Schedule** as shown in the code displayed below.

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

[[]]{.MsoIntenseEmphasis} 

[] 

8.   Run the application.  To print a schedule, click the **Print** icon. The **Print** window will appear as shown below.

[] 

{border="0"}

[] 

Figure 124: Print a Schedule

[] 

To print an appointment, make sure the **Quick Print** context menu item is added. After this setting, perform the following:

9.   Right click the appointment, and click Quick Print.

[] 

{border="0"}

[] 

Figure 125: Print an appointment

[] 

[]{#related-topics}

