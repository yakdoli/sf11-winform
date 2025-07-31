---
title: usingviewcustomization16.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingviewcustomization16.md
created_at: 2025-07-03
---






#### Using View Customization {#using-view-customization style="tab-stops: 0pt"}

The steps to customize client-side events using view customization are as follows:

1.  [Create a model in the application.](http://help.syncfusion.com/ug_93/User%20Interface/ASP.NET%20MVC/Schedule/Documents/addingamodeltotheapplication.htm)

2.  [Create a strongly typed view.](http://help.syncfusion.com/ug_93/User%20Interface/ASP.NET%20MVC/Schedule/Documents/stronglytypedview.htm)

3.  In the **view**, you can use its **Model** property in **DataSource** to bind the data source and bind your database fields into the corresponding schedule fields.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View]**                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                 |
| [ ][    [\<%][=]Html.Syncfusion().Schedule()([\"FlatSchedule\"])] |
|                                                                                                                                                                                                                                                 |
| [       .DataSource(([IEnumerable]) Model)]                                                                                                                                         |
|                                                                                                                                                                                                                                                 |
| [       .BindList(columns =\>]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                 |
| [       {]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                 |
| [           columns.IdField([\"AppId\"]);]                                                                                                                                          |
|                                                                                                                                                                                                                                                 |
| [           columns.SubjectField([\"Subject\"]);]                                                                                                                                   |
|                                                                                                                                                                                                                                                 |
| [           columns.LocationField([\"Location\"]);]                                                                                                                                 |
|                                                                                                                                                                                                                                                 |
| [           columns.StartTimeField([\"StartTime\"]);]                                                                                                                               |
|                                                                                                                                                                                                                                                 |
| [           columns.EndTimeField([\"EndTime\"]);]                                                                                                                                   |
|                                                                                                                                                                                                                                                 |
| [           columns.DescriptionField([\"Descrip\"]);]                                                                                                                               |
|                                                                                                                                                                                                                                                 |
| [           columns.OwnerField([\"Resource\"]);]                                                                                                                                    |
|                                                                                                                                                                                                                                                 |
| [       })]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                 |
| [    [%\>]]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.  Set the **EnableClientSideEvents()** method to handle client side events and define client side functions for appointment selection ,cell double-click and cell single-click.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View]**                                                                                                                              |
|                                                                                                                                                                             |
| []                                                                                                                                      |
|                                                                                                                                                                             |
| [    [\<%][=]Html.Syncfusion().Schedule()([\"FlatSchedule\"])] |
|                                                                                                                                                                             |
| [                .DataSource(([IEnumerable]) ViewData\[[\"data\"]\])]                   |
|                                                                                                                                                                             |
| [                .BindList(columns =\>]                                                                                                 |
|                                                                                                                                                                             |
| [                {]                                                                                                                     |
|                                                                                                                                                                             |
| [                columns.IdField([\"AppId\"]);]                                                                 |
|                                                                                                                                                                             |
| [                columns.SubjectField([\"Subject\"]);]                                                          |
|                                                                                                                                                                             |
| [                columns.LocationField([\"Location\"]);]                                                        |
|                                                                                                                                                                             |
| [columns.StartTimeField([\"StartTime\"]);]                                                                      |
|                                                                                                                                                                             |
| [                columns.EndTimeField([\"EndTime\"]);]                                                          |
|                                                                                                                                                                             |
| [                columns.DescriptionField([\"Descrip\"]);]                                                      |
|                                                                                                                                                                             |
| [                columns.OwnerField([\"Resource\"]);]                                                           |
|                                                                                                                                                                             |
| [                })]                                                                                                                    |
|                                                                                                                                                                             |
| [                .CurrentView([ScheduleViewMode].Week)    ]                                                     |
|                                                                                                                                                                             |
| [.Skins([ScheduleSkins].Sandune)]                                                                               |
|                                                                                                                                                                             |
| **[.EnableClientSideEvents([true])]**                                                                              |
|                                                                                                                                                                             |
| ```                                                                                                                                              |
|              .ClientSideOnCellSingleClick("onCellSingleClick")                                                                                                              |
| ```                                                                                                                                                                         |
|                                                                                                                                                                             |
| **[.ClientSideOnAppointmentSelection([\"onAppointmentSelection\"])]**[]     |
|                                                                                                                                                                             |
| **[.ClientSideOnCellDoubleClick([\"onCellDblClick\"])]**                                                        |
|                                                                                                                                                                             |
| []                                                                                                                                      |
|                                                                                                                                                                             |
| [    [%\>]]                                                                                                 |
|                                                                                                                                                                             |
| []                                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.  In the **controller**, add the **Syncfusion.Mvc.Schedule** and **Syncfusion.Mvc.Shared** namespaces.

[] 

+-------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                    |
|                                                                                                                         |
| []                                                     |
|                                                                                                                         |
| [using][ Syncfusion.Mvc.Schedule;] |
|                                                                                                                         |
| [using][ Syncfusion.Mvc.Shared;]   |
|                                                                                                                         |
| []                                                     |
+-------------------------------------------------------------------------------------------------------------------------+

[] 

6.  Set its data source and render the view.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                                                              |
|                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                            |
|                                                                                                                                                                                                                                   |
| [        [///][ ][\<summary\>]]                                                                                               |
|                                                                                                                                                                                                                                   |
| [        [///][ it used to bind the Schedule]]                                                                                                     |
|                                                                                                                                                                                                                                   |
| [        [///][ ][\</summary\>]]                                                                                              |
|                                                                                                                                                                                                                                   |
| [        [///][ ][\<returns\>][View page, it displays the Schedule][\</returns\>]] |
|                                                                                                                                                                                                                                   |
| [        [public] [ActionResult] Index()]                                                                                                        |
|                                                                                                                                                                                                                                   |
| [        {]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                   |
| [            [var] data = [new] [NorthwindDataClassesDataContext]().AppointmentTables.Take(200);]                           |
|                                                                                                                                                                                                                                   |
| [ViewData\[[\"data\"]\] = data;]                                                                                                                                      |
|                                                                                                                                                                                                                                   |
| [            [return] View();]                                                                                                                                           |
|                                                                                                                                                                                                                                   |
| [        }]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                   |
| []                                                                                                                                                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

7.  Create a post method for **Index** action and bind the data source to the schedule as shown in the code displayed below.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                                                                     |
|                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                          |
| [  ][      [///][ ][\<summary\>]]                                                   |
|                                                                                                                                                                                                                                          |
| [        [///][ Post Requests are mapped to this method. This method invokes the HtmlActionResult]]                                                       |
|                                                                                                                                                                                                                                          |
| [        [///][ from the Schedule. Required response is generated.]]                                                                                      |
|                                                                                                                                                                                                                                          |
| [        [///][ ][\</summary\>]]                                                                                                     |
|                                                                                                                                                                                                                                          |
| [        [///][ ][\<param name=\"args\"\>][Contains post action properties ][\</param\>]] |
|                                                                                                                                                                                                                                          |
| [        [///][ ][\<returns\>]]                                                                                                      |
|                                                                                                                                                                                                                                          |
| [        [///][ HtmlActionResult which returns data displayed on the Schedule]]                                                                           |
|                                                                                                                                                                                                                                          |
| [        [///][ ][\</returns\>]]                                                                                                     |
|                                                                                                                                                                                                                                          |
| [        \[[AcceptVerbs]([HttpVerbs].Post)\]]                                                                                                        |
|                                                                                                                                                                                                                                          |
| [        [public] [ActionResult] Index([Params] args)]                                                                          |
|                                                                                                                                                                                                                                          |
| [        {]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                          |
| [IEnumerable][ data = [new] [NorthwindDataClassesDataContext]().AppointmentTables.Take(200);]       |
|                                                                                                                                                                                                                                          |
| [                [return] data.ScheduleActions\<[ScheduleHtmlActionResult]\>();]                                                                        |
|                                                                                                                                                                                                                                          |
| [        }]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

8.  Declare the functions in script to handle the client-side events.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[JavaScript\]]**                                                                                                                                                                        |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                 |
| [  ][    [\<][script] [type][=\"text/javascript\"\>]] |
|                                                                                                                                                                                                                                 |
| [        [// To handle the appointment selection event]]                                                                                                          |
|                                                                                                                                                                                                                                 |
| [        [function] onAppointmentSelection(sender, args) {]                                                                                                            |
|                                                                                                                                                                                                                                 |
| [            [// sender - Schedule control details]]                                                                                                              |
|                                                                                                                                                                                                                                 |
| [            [// args - id -\> selected appointment id]]                                                                                                          |
|                                                                                                                                                                                                                                 |
| [            [// args - currentItem -\> selected appointment details]]                                                                                            |
|                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                 |
| [        [// To handle the cell double click ]]                                                                                                                   |
|                                                                                                                                                                                                                                 |
| [        [function] onCellDblClick(sender, args) {]                                                                                                                    |
|                                                                                                                                                                                                                                 |
| [            [// sender - Schedule control details]]                                                                                                              |
|                                                                                                                                                                                                                                 |
| [            [// args - selectedDate -\> selected cell\'s date]]                                                                                                  |
|                                                                                                                                                                                                                                 |
| [            [// args - selectedStartTime -\> selected cell\'s start time]]                                                                                       |
|                                                                                                                                                                                                                                 |
| [            [// args - selectedEndTime -\> selected cell\'s end time]]                                                                                           |
|                                                                                                                                                                                                                                 |
| [            [// args - selectedResourceId -\> selected cell\'s owner id]]                                                                                        |
|                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                 |
| [        [// To handle the cell single click ]]                                                                                                                   |
|                                                                                                                                                                                                                                 |
| [        [function] onCellSingleClick(sender, args) {]                                                                                                                 |
|                                                                                                                                                                                                                                 |
| [            [// sender - Schedule control details]]                                                                                                              |
|                                                                                                                                                                                                                                 |
| [            [// args - selectedDate -\> selected cell\'s date]]                                                                                                  |
|                                                                                                                                                                                                                                 |
| [            [// args - selectedStartTime -\> selected cell\'s start time]]                                                                                       |
|                                                                                                                                                                                                                                 |
| [            [// args - selectedEndTime -\> selected cell\'s end time]]                                                                                           |
|                                                                                                                                                                                                                                 |
| [            [// args - selectedResourceId -\> selected cell\'s owner id]]                                                                                        |
|                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                 |
| [    [\</][script][\>]]                                                                                                    |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

9.  Run the application. The schedule will appear when the cell is clicked as shown below.

{border="0"}

Figure 138: Cell Single Click Event

 

[]{#related-topics}

