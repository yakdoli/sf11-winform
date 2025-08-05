---
title: usingviewcustomization5.md
original_path: WinForms_Docs/99_Uncategorized/usingviewcustomization5.md
created_at: 2025-08-05
---






##### Using View Customization {#using-view-customization style="tab-stops: 0pt"}

The steps to customize the Delete an appointment using View Customization are as follows:

1.   [Create a model in the application]{.UGHyperlink}[.][ ]

2.   [Create a strongly typed view]{.UGHyperlink}[.][ ]

3.   In **View**, you can use its **Model** property in DataSource in order to bind the data source and bind your database fields into the corresponding Schedule fields.

4.   Set the AllowDelete() method to perform **delete an appointment** through **AppointmentDoubleClick** event.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**                                                                                                                            |
|                                                                                                                                                                                            |
| [    [\<%][=]Html.Syncfusion().Schedule()([\"DeleteAppointment \"])] |
|                                                                                                                                                                                            |
| [        .DataSource(Model)]                                                                                                                  |
|                                                                                                                                                                                            |
| [        .Skins([ScheduleSkins].Sandune)]                                                                             |
|                                                                                                                                                                                            |
| **[        .AllowDelete([true])]**                                                                                       |
|                                                                                                                                                                                            |
| [        .BindList(columns =\>]                                                                                                               |
|                                                                                                                                                                                            |
| [        {]                                                                                                                                   |
|                                                                                                                                                                                            |
| [           columns.IdField([\"AppId\"]);]                                                                            |
|                                                                                                                                                                                            |
| [           columns.SubjectField([\"Subject\"]);]                                                                     |
|                                                                                                                                                                                            |
| [           columns.LocationField([\"Location\"]);]                                                                   |
|                                                                                                                                                                                            |
| [           columns.StartTimeField([\"StartTime\"]);]                                                                 |
|                                                                                                                                                                                            |
| [           columns.EndTimeField([\"EndTime\"]);]                                                                     |
|                                                                                                                                                                                            |
| [           columns.DescriptionField([\"Descrip\"]);]                                                                 |
|                                                                                                                                                                                            |
| [           columns.OwnerField([\"Resource\"]);]                                                                      |
|                                                                                                                                                                                            |
| [        })]                                                                                                                                  |
|                                                                                                                                                                                            |
| [    [%\>]]                                                                                                       |
|                                                                                                                                                                                            |
| []                                                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                                           |
|                                                                                                                                                                                                             |
| [    ][]                                                                                                      |
|                                                                                                                                                                                                             |
| [@(][ Html.Syncfusion().Schedule()([\"DeleteAppointment \"])] |
|                                                                                                                                                                                                             |
| [        .DataSource(Model)]                                                                                                                               |
|                                                                                                                                                                                                             |
| [        .Skins([ScheduleSkins].Sandune)]                                                                                          |
|                                                                                                                                                                                                             |
| [        .AllowDelete([true])]                                                                                                        |
|                                                                                                                                                                                                             |
| [        .BindList(columns =\>]                                                                                                                            |
|                                                                                                                                                                                                             |
| [        {]                                                                                                                                                |
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
| [        })[)]]                                                                                                                |
|                                                                                                                                                                                                             |
| []                                                                                                                                                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   Add a **ContextMenuItem** (Delete Appointment) in the **ContextMenuItems** **()** method to delete an appointment through context-menu.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**                                                                                                                                                   |
|                                                                                                                                                                                                                   |
| [    [\<%][=]Html.Syncfusion().Schedule()([\"DeleteAppointment \"])]                        |
|                                                                                                                                                                                                                   |
| [        .DataSource(Model)]                                                                                                                                         |
|                                                                                                                                                                                                                   |
| [        .Skins([ScheduleSkins].Sandune)]                                                                                                    |
|                                                                                                                                                                                                                   |
| **[        . AllowDelete ([true])]**                                                                                                            |
|                                                                                                                                                                                                                   |
| **[        .ContextMenuItems(([List]\<[ContextMenuItem]\>)ViewData\[[\"ContextMenus\"]\])]** |
|                                                                                                                                                                                                                   |
| [        .BindList(columns =\>]                                                                                                                                      |
|                                                                                                                                                                                                                   |
| [        {]                                                                                                                                                          |
|                                                                                                                                                                                                                   |
| [           columns.IdField([\"AppId\"]);]                                                                                                   |
|                                                                                                                                                                                                                   |
| [           columns.SubjectField([\"Subject\"]);]                                                                                            |
|                                                                                                                                                                                                                   |
| [           columns.LocationField([\"Location\"]);]                                                                                          |
|                                                                                                                                                                                                                   |
| [           columns.StartTimeField([\"StartTime\"]);]                                                                                        |
|                                                                                                                                                                                                                   |
| [           columns.EndTimeField([\"EndTime\"]);]                                                                                            |
|                                                                                                                                                                                                                   |
| [           columns.DescriptionField([\"Descrip\"]);]                                                                                        |
|                                                                                                                                                                                                                   |
| [           columns.OwnerField([\"Resource\"]);]                                                                                             |
|                                                                                                                                                                                                                   |
| [        })]                                                                                                                                                         |
|                                                                                                                                                                                                                   |
| [    [%\>]]                                                                                                                              |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]][ ]**                                                                                                 |
|                                                                                                                                                                                                                   |
| [   [@(] Html.Syncfusion().Schedule()([\"DeleteAppointment \"])]                                             |
|                                                                                                                                                                                                                   |
| [        .DataSource(Model)]                                                                                                                                     |
|                                                                                                                                                                                                                   |
| [        .Skins([ScheduleSkins].Sandune)]                                                                                                |
|                                                                                                                                                                                                                   |
| [        . AllowDelete ([true])]                                                                                                            |
|                                                                                                                                                                                                                   |
| [        .ContextMenuItems(([List]\<[ContextMenuItem]\>)ViewData\[[\"ContextMenus\"]\])] |
|                                                                                                                                                                                                                   |
| [        .BindList(columns =\>]                                                                                                                                  |
|                                                                                                                                                                                                                   |
| [        {]                                                                                                                                                      |
|                                                                                                                                                                                                                   |
| [           columns.IdField([\"AppId\"]);]                                                                                               |
|                                                                                                                                                                                                                   |
| [           columns.SubjectField([\"Subject\"]);]                                                                                        |
|                                                                                                                                                                                                                   |
| [           columns.LocationField([\"Location\"]);]                                                                                      |
|                                                                                                                                                                                                                   |
| [           columns.StartTimeField([\"StartTime\"]);]                                                                                    |
|                                                                                                                                                                                                                   |
| [           columns.EndTimeField([\"EndTime\"]);]                                                                                        |
|                                                                                                                                                                                                                   |
| [           columns.DescriptionField([\"Descrip\"]);]                                                                                    |
|                                                                                                                                                                                                                   |
| [           columns.OwnerField([\"Resource\"]);]                                                                                         |
|                                                                                                                                                                                                                   |
| [        })[)]]                                                                                                                      |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

6.   In Controller, add the Syncfusion.Mvc.Schedule, Syncfusion.Mvc.Shared namespaces.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**[[]]{.MsoIntenseEmphasis} |
|                                                                                                                                                              |
| [using][ Syncfusion.Mvc.Schedule;]                    |
|                                                                                                                                                              |
| [using][ Syncfusion.Mvc.Shared;]                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

7.   Create context-menu item for deleting an appointment and storing it in **Viewdata** for access from the **View** page. Set its data source and render the view.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**[[]]{.MsoIntenseEmphasis}                                                                                                    |
|                                                                                                                                                                                                                                                                 |
| [        [///][ ][\<summary\>]]                                                                                                                    |
|                                                                                                                                                                                                                                                                 |
| [        [///][ It is used to bind the Schedule]]                                                                                                                       |
|                                                                                                                                                                                                                                                                 |
| [        [///][ ][\</summary\>]]                                                                                                                   |
|                                                                                                                                                                                                                                                                 |
| [        [///][ ][\<returns\>][View page, it displays the Schedule][\</returns\>]]                      |
|                                                                                                                                                                                                                                                                 |
| [        [public] [ActionResult] Index()]                                                                                                                             |
|                                                                                                                                                                                                                                                                 |
| [        {]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                 |
| [ContextMenuItem][ deleteApp = [new] [ContextMenuItem]() ]                                               |
|                                                                                                                                                                                                                                                                 |
| [{ ]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                 |
| [MenuID = [\"DeleteAppointment\"], ]                                                                                                                                                       |
|                                                                                                                                                                                                                                                                 |
| [MenuName = [\"Delete Appointment\"], ]                                                                                                                                                    |
|                                                                                                                                                                                                                                                                 |
| [CommandName = [ContextCommandNames].DeleteAppointment]                                                                                                                                    |
|                                                                                                                                                                                                                                                                 |
| [ };]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                 |
| [                                ViewData\[[\"ContextMenus\"]\] = [new] [List]\<[ContextMenuItem]\>() { deleteApp };] |
|                                                                                                                                                                                                                                                                 |
| [                [var] data = [new] [NorthwindDataClassesDataContext]().AppointmentTables.Take(200);]                                            |
|                                                                                                                                                                                                                                                                 |
| [                [return] View(data);]                                                                                                                                                        |
|                                                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

8.   Create a post method for Index action and bind the data source to Schedule, as shown in the code displayed below:

[[]]{.MsoIntenseEmphasis} 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**[[]]{.MsoIntenseEmphasis}                                                                                      |
|                                                                                                                                                                                                                                                   |
| [  ][      [///][ ][\<summary\>]]                                          |
|                                                                                                                                                                                                                                                   |
| [        [///][ Post Requests are mapped to this method. This method invokes the HtmlActionResult]]                                                       |
|                                                                                                                                                                                                                                                   |
| [        [///][ from the Schedule. Required response is generated.]]                                                                                      |
|                                                                                                                                                                                                                                                   |
| [        [///][ ][\</summary\>]]                                                                                                     |
|                                                                                                                                                                                                                                                   |
| [        [///][ ][\<param name=\"args\"\>][Contains post action properties ][\</param\>]] |
|                                                                                                                                                                                                                                                   |
| [        [///][ ][\<returns\>]]                                                                                                      |
|                                                                                                                                                                                                                                                   |
| [        [///][ HtmlActionResult which returns data displayed on the Schedule]]                                                                           |
|                                                                                                                                                                                                                                                   |
| [        [///][ ][\</returns\>]]                                                                                                     |
|                                                                                                                                                                                                                                                   |
| [        \[[AcceptVerbs]([HttpVerbs].Post)\]]                                                                                                        |
|                                                                                                                                                                                                                                                   |
| [        [public] [ActionResult] Index([Params] args)]                                                                          |
|                                                                                                                                                                                                                                                   |
| [        {]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                   |
| [NorthwindDataClassesDataContext][ db = [new] [NorthwindDataClassesDataContext]();]        |
|                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                   |
| [            [// Select the particular appointment with args.AppID and delete it]]                                                                                             |
|                                                                                                                                                                                                                                                   |
| [            [if] (args.CurrentAction == [\"Delete\"])]                                                                                                 |
|                                                                                                                                                                                                                                                   |
| [            {]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                   |
| [                [AppointmentTable] app = db.AppointmentTables.Where(c =\> c.AppId == [Convert].ToInt32(args.AppID)).FirstOrDefault();]              |
|                                                                                                                                                                                                                                                   |
| [                [if] (app != [null]) db.AppointmentTables.DeleteOnSubmit(app);]                                                                           |
|                                                                                                                                                                                                                                                   |
| [            }]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                   |
| [            [//to reflect in database]]                                                                                                                                       |
|                                                                                                                                                                                                                                                   |
| [            db.SubmitChanges();]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                   |
| [            [ActionResult] result = db.AppointmentTables.ScheduleActions\<[ScheduleHtmlActionResult]\>();]                                          |
|                                                                                                                                                                                                                                                   |
| [            [return] result;]                                                                                                                                                  |
|                                                                                                                                                                                                                                                   |
| [        }]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

9.   Run the application. The Schedule's appointment window will appear as shown below when double-clicking any appointment**.**

[] 

{border="0"}

[] 

Figure 110: Appointment Dialog when Double-clicking an Appointment

[] 

10.  [On the Appointment dialog toolbar, click  **Delete**.   ]{.NumberedListChar}[    **\[OR\]**]

[] 

Right-click an appointment and click **Delete Appointment.** The confirmation dialog will appear as shown below.

[] 

{border="0"}

[] 

Figure 111: Appointment dialog with confirmation alert

[] 

11.  On the confirmation dialog, click **OK**.

[] 

[]{#related-topics}

