---
title: creatingscheduleusingschedulepropertymodel1.md
original_path: WinForms_Docs/99_Uncategorized/creatingscheduleusingschedulepropertymodel1.md
created_at: 2025-08-05
---








  









### Creating Schedule using Schedule Property Model {#creating-schedule-using-schedule-property-model style="tab-stops: 0pt"}

To create a schedule using Schedule Property Model:

 

1.   Select the Index.aspx from **View**-\>**Home** folder.

2.   Add the following code in the FlatSchedule.aspx file, to create the **Schedule** control in **View**:

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[View\]]                                                                                                |
|                                                                                                                                                        |
| []                                                                                                        |
|                                                                                                                                                        |
| [    [\<%]=Html.Syncfusion().Schedule()(\"FlatSchedule\", \"ScheduleModel\")] |
|                                                                                                                                                        |
| [       .BindList(columns =\>]                                                                            |
|                                                                                                                                                        |
| [       {]                                                                                                |
|                                                                                                                                                        |
| [           columns.IdField(\"AppId\");]                                                                  |
|                                                                                                                                                        |
| [           columns.SubjectField(\"Subject\");]                                                           |
|                                                                                                                                                        |
| [           columns.LocationField(\"Location\");]                                                         |
|                                                                                                                                                        |
| [           columns.StartTimeField(\"StartTime\");]                                                       |
|                                                                                                                                                        |
| [           columns.EndTimeField(\"EndTime\");]                                                           |
|                                                                                                                                                        |
| [           columns.DescriptionField(\"Descrip\");]                                                       |
|                                                                                                                                                        |
| [           columns.OwnerField(\"Resource\");]                                                            |
|                                                                                                                                                        |
| [       })]                                                                                               |
|                                                                                                                                                        |
| [    [%\>]]                                                                   |
|                                                                                                                                                        |
| []                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Double-click the **HomeController.cs** from **Controller/Home** folder.

The HomeController.cs page is displayed on the main window.

[] 

{border="0"}

[] 

Figure 50: HomeController.cs Page[]

***[]*** 

4.   Include the **Syncfusion.Mvc.Shared, Syncfusion.Mvc.Schedule** namespaces to **HomeController** by using the following code:

[] 

\[Controller\]

[using] Syncfusion.Mvc.Schedule;

[using] Syncfusion.Mvc.Shared;

[] 

5.   Edit the **Index** method as given below:

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[Controller\]]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                    |
| [                [///][ ][\<summary\>]]                                                                                               |
|                                                                                                                                                                                                                                                    |
| [                 [///][ It is used to bind the Schedule]]                                                                                                 |
|                                                                                                                                                                                                                                                    |
| [                [///][ ][\</summary\>]]                                                                                              |
|                                                                                                                                                                                                                                                    |
| [                [///][ ][\<returns\>][View page, it displays the Schedule][\</returns\>]] |
|                                                                                                                                                                                                                                                    |
| [                [public] [ActionResult] FlatSchedule()]                                                                                                 |
|                                                                                                                                                                                                                                                    |
| [                {]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                    |
| [                 [var] data = [new] [NorthwindDataClassesDataContext]().AppointmentTables.Take(200);]                              |
|                                                                                                                                                                                                                                                    |
| [                [SchedulePropertiesModel] model = [new] [SchedulePropertiesModel]()]                                            |
|                                                                                                                                                                                                                                                    |
| [                {]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                    |
| [                                DataSource=data,]                                                                                                                                                    |
|                                                                                                                                                                                                                                                    |
| [                                Skins=[ScheduleSkins].Sandune]                                                                                                               |
|                                                                                                                                                                                                                                                    |
| [                };]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                    |
| [                                ViewData\[[\"ScheduleModel\"]\] = model;]                                                                                                    |
|                                                                                                                                                                                                                                                    |
| [                                [return] View();]                                                                                                                               |
|                                                                                                                                                                                                                                                    |
| [                }]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Code details:

a.  Object created for SchedulePropertiesModel and the following Schedule properties are assigned to the model:

DataSource                   - Gets or sets DataSource for the Schedule[ ]control

Skins                            - Gets or sets Schedule Skin

a.  Pass the model to View using ViewData. This will pass the Schedule properties from Controller to View.

Syntax :

ViewData\[\"model_id\"\] = object_name;

b.  Create a post method for Index action and bind the data source to Schedule, as shown in the code displayed below.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[Controller\]]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                            |
| [        ][///][ ][\<summary\>][] |
|                                                                                                                                                                                                                                                                                                            |
| [        [///][ Post Requests are mapped to this method. This method invokes the HtmlActionResult]]                                                                                                                |
|                                                                                                                                                                                                                                                                                                            |
| [        [///][ from the Schedule. Required response is generated.]]                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                            |
| [        [///][ ][\</summary\>]]                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                            |
| [        [///][ ][\<param name=\"args\"\>][Contains post action properties ][\</param\>]]                                                          |
|                                                                                                                                                                                                                                                                                                            |
| [        [///][ ][\<returns\>]]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                            |
| [        [///][ HtmlActionResult which returns data displayed on the Schedule]]                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                            |
| [        [///][ ][\</returns\>]]                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                            |
| [        \[[AcceptVerbs]([HttpVerbs].Post)\]]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                            |
| [        [public] [ActionResult] FlatSchedule([Params] args)]                                                                                                                            |
|                                                                                                                                                                                                                                                                                                            |
| [        {]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                            |
| [IEnumerable][ data = [new] [NorthwindDataClassesDataContext]().AppointmentTables.Take(200);]                                                       |
|                                                                                                                                                                                                                                                                                                            |
| [                [return] data.ScheduleActions\<[ScheduleHtmlActionResult]\>();]                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                            |
| [        }]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


{border="0"}Note: Essential Schedule is fully Ajax enabled. For tab navigation/date navigation/crud actions, the entire page will not be refreshed. The Schedule contents alone will be refreshed using Ajax calls. So the above method is necessary to achieve the Schedule actions.


Code details:

a.  Get the data source and store it in an IEnumeable collection.

b.  Call the ScheduleAction helper with the Type of Model, which invokes the custom action result. This will process the data source returns and the required response while calling tab navigation/date navigation actions.

c.  Run the application.

[] 

{border="0"}

[] 

Figure 51: Schedule Control Added to the Application[]

[] 

A sample which demonstrates a basic Schedule control that can be downloaded from the following link:

[[http://help.syncfusion.com/Support/Schedule_Mvc/v8.3.0.20/MVCScheduleSample.zip]{.UGHyperlink}](http://help.syncfusion.com/Support/Schedule_Mvc/v8.3.0.20/MVCScheduleSample.zip)[]{.UGHyperlink}


{border="0"}Note: The version number for the assemblies has been set to 8.3.0.20 in the Web.config file of the attached sample. Change the version number to the appropriate version in the Web-2008.config or Web-2010.config files (available in root directory) and those will automatically be updated in the Web.config file.


[] 

[]{#related-topics}

