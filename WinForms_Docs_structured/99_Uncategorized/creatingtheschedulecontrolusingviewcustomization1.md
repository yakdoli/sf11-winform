---
title: creatingtheschedulecontrolusingviewcustomization1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\creatingtheschedulecontrolusingviewcustomization1.md
created_at: 2025-07-03
---








  









### Creating the Schedule Control Using View Customization {#creating-the-schedule-control-using-view-customization style="tab-stops: 0pt"}

To create the Schedule control using View customization:

9.   Right-click the **View-\>Home** folder.

10.  Click **Add**, and then select **View**.

11.  Name the **View FlatSchedule**.

12.  Check the box that says **Create a strongly-typed view**, and on the drop down menu select your model. In this case, it is "MvcSampleApplication.AppointmentTable".

[] 

[{border="0"}]

[] 

Figure 59: Strogly-typed View


{border="0"}Note: The View Data class drop-down list will be empty until you successfully build your application. It is a good idea to select the menu option build, build solution before opening the Add New dialog.


[] 

13.  In a **View Data Class**, make the model as IEnumerable collections as given below:

[] 

[] 

[{border="0"}]

[] 

Figure 60: View Data classes as IEumerable collection

[] 

14.  Add the following code in the **FlatSchedule.cshtml** file, to create the **Schedule** control in **View**:

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[]cshtml[\]]**                                                                                             |
|                                                                                                                                                                                                              |
| [  ][    [@(]Html.Syncfusion().Schedule()([\"FlatSchedule\"])] |
|                                                                                                                                                                                                              |
| [        .DataSource(([IEnumerable])Model)]                                                                                             |
|                                                                                                                                                                                                              |
| [       .BindList(columns =\>]                                                                                                                                  |
|                                                                                                                                                                                                              |
| [       {]                                                                                                                                                      |
|                                                                                                                                                                                                              |
| [           columns.IdField([\"AppId\"]);]                                                                                              |
|                                                                                                                                                                                                              |
| [           columns.SubjectField([\"Subject\"]);]                                                                                       |
|                                                                                                                                                                                                              |
| [           columns.LocationField([\"Location\"]);]                                                                                     |
|                                                                                                                                                                                                              |
| [           columns.StartTimeField([\"StartTime\"]);]                                                                                   |
|                                                                                                                                                                                                              |
| [           columns.EndTimeField([\"EndTime\"]);]                                                                                       |
|                                                                                                                                                                                                              |
| [           columns.DescriptionField([\"Descrip\"]);]                                                                                   |
|                                                                                                                                                                                                              |
| [           columns.OwnerField([\"Resource\"]);]                                                                                        |
|                                                                                                                                                                                                              |
| [       })]                                                                                                                                                     |
|                                                                                                                                                                                                              |
| [      .Skins([ScheduleSkins].Sandune)]                                                                                                 |
|                                                                                                                                                                                                              |
| [      [)]][ ]                                                                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

15.  Opens the \~/Controllers/HomeController.cs.

16.  Include the following namespaces in to HomeController:

Syncfusion.Mvc.Schedule

Syncfusion.Mvc.Shared

[] 

Include the Syncfusion.Mvc.Shared, Syncfusion.Mvc.Schedule namespaces to HomeController by using the following code:

+-------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                         |
|                                                                                                                                           |
| [using][ Syncfusion.Mvc.Schedule;] |
|                                                                                                                                           |
| [using][ Syncfusion.Mvc.Shared;]   |
+-------------------------------------------------------------------------------------------------------------------------------------------+

17.  Add two methods (one for loading View and one for handling the Schedule post actions).

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                      |
| [        [///][ ][\<summary\>]]                                                                                                         |
|                                                                                                                                                                                                                                                      |
| [        [///][ This method is used to bind the Schedule]]                                                                                                   |
|                                                                                                                                                                                                                                                      |
| [        [///][ ][\</summary\>]]                                                                                                        |
|                                                                                                                                                                                                                                                      |
| [        [///][ ][\<returns\>][View page, it displays the Schedule][\</returns\>]]           |
|                                                                                                                                                                                                                                                      |
| [        [public] [ActionResult] FlatSchedule()]                                                                                                           |
|                                                                                                                                                                                                                                                      |
| [        {]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                      |
| [var][ data = [new]    [NorthwindDataClassesDataContext]().AppointmentTables.Take(200);]         |
|                                                                                                                                                                                                                                                      |
| [                        [return] View(data);]                                                                                                                                     |
|                                                                                                                                                                                                                                                      |
| [        }]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                      |
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
| [        [public] [ActionResult] FlatSchedule([Params] args)]                                                                      |
|                                                                                                                                                                                                                                                      |
| [        {]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                      |
| [IEnumerable][ data = [new] [NorthwindDataClassesDataContext]().AppointmentTables.Take(200);] |
|                                                                                                                                                                                                                                                      |
| [                        [return] data.ScheduleActions\<[ScheduleHtmlActionResult]\>();]                                                                   |
|                                                                                                                                                                                                                                                      |
| [        }]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

18.  Run the application.

19.  Call this action in browser window  Home/FlatSchedule (i.e. http://localhost:55031/Home/FlatSchedule)

[] 

The following screenshot illustrates the sample output:

[] 

{border="0"}

[] 

Figure 61: Schedule Control added to the Application

***[]*** 

[]{#related-topics}

