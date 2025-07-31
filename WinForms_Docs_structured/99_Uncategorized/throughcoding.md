---
title: throughcoding.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\throughcoding.md
created_at: 2025-07-03
---








  









### Through Coding {#through-coding style="tab-stops: 0pt"}

[] 

To create the Schedule control programmatically:

[] 

1.   Add a new **Web Form** to your project.

2.   Drag the **Schedule** control from the toolbox onto the web form.

3.   In the .cs file, include the following directives.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                              |
|                                                                                                                                               |
| []                                                                                                        |
|                                                                                                                                               |
| [using][ Syncfusion.Web.UI.WebControls.Shared;]          |
|                                                                                                                                               |
| [using][ Syncfusion.Web.UI.WebControls.ScheduleControl;] |
+-----------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                               |
|                                                                                                                                                |
| []                                                                                                         |
|                                                                                                                                                |
| [Imports][ Syncfusion.Web.UI.WebControls.Shared]          |
|                                                                                                                                                |
| [Imports][ Syncfusion.Web.UI.WebControls.ScheduleControl] |
+------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Add any number of resources to the control. Resources can be any names, tangible elements, tasks, and so on. Create instances of the resources and add it to the Schedule control.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                             |
|                                                                                                                                                                                              |
| []                                                                                                                                                       |
|                                                                                                                                                                                              |
| [ScheduleWebResource][ res1 = [new] [ScheduleWebResource]();] |
|                                                                                                                                                                                              |
| [Scheduler1.Resources.Add(res1);]                                                                                                                        |
|                                                                                                                                                                                              |
| []                                                                                                                                                       |
|                                                                                                                                                                                              |
| [ScheduleWebResource][ res2 = [new] [ScheduleWebResource]();] |
|                                                                                                                                                                                              |
| [Scheduler1.Resources.Add(res2);]                                                                                                                        |
|                                                                                                                                                                                              |
| []                                                                                                                                                       |
|                                                                                                                                                                                              |
| [ScheduleWebResource][ res3 = [new] [ScheduleWebResource]();] |
|                                                                                                                                                                                              |
| [Scheduler1.Resources.Add(res3);]                                                                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                  |
| [Dim][ res1 [As] Syncfusion.Web.UI.WebControls.ScheduleControl.ScheduleWebResource = [New] ScheduleWebResource()] |
|                                                                                                                                                                                                                                                  |
| [Scheduler1.Resources.Add(res1)]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                  |
| [Dim][ res2 [As] Syncfusion.Web.UI.WebControls.ScheduleControl.ScheduleWebResource = [New] ScheduleWebResource()] |
|                                                                                                                                                                                                                                                  |
| [Scheduler1.Resources.Add(res2)]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                  |
| [Dim][ res3 [As] Syncfusion.Web.UI.WebControls.ScheduleControl.ScheduleWebResource = [New] ScheduleWebResource()] |
|                                                                                                                                                                                                                                                  |
| [Scheduler1.Resources.Add(res3)]                                                                                                                                                                             |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   Set the Name and Id properties for the resources.

[] 

**Name** property when set will be displayed on the header section of the control denoting the resource. **UniqueID** can be set for individual resources which can be used to associate the resources with the respective appointments.

[] 

+----------------------------------------------------------------------------------------+
| **[\[C#\]]**                                       |
|                                                                                        |
| []                                                 |
|                                                                                        |
| [res1.UniqueID = [\"1\"];]  |
|                                                                                        |
| [res1.Name = [\"Allen\"];]  |
|                                                                                        |
| []                                                 |
|                                                                                        |
| [res1.UniqueID = [\"2\"];]  |
|                                                                                        |
| [res1.Name = [\"Brian\"];]  |
|                                                                                        |
| []                                                 |
|                                                                                        |
| [res1.UniqueID = [\"3\"];]  |
|                                                                                        |
| [res1.Name = [\"George\"];] |
+----------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------+
| **[\[VB\]]**                                      |
|                                                                                       |
| []                                                |
|                                                                                       |
| [res1.UniqueID = [\"1\"]]  |
|                                                                                       |
| [res1.Name = [\"Allen\"]]  |
|                                                                                       |
| []                                 |
|                                                                                       |
| [res1.UniqueID = [\"2\"]]  |
|                                                                                       |
| [res1.Name = [\"Brian\"]]  |
|                                                                                       |
| []                                 |
|                                                                                       |
| [res1.UniqueID = [\"3\"]]  |
|                                                                                       |
| [res1.Name = [\"George\"]] |
+---------------------------------------------------------------------------------------+

[] 

6.   Any number of appointments can be tagged for a single resource, which will be displayed at the intersection of the time and the resource, and occupy that area for the specified time.

7.   Create instances for the appointments and add it to the Schedule control.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                   |
|                                                                                                                                                                                                    |
| []                                                                                                                                                             |
|                                                                                                                                                                                                    |
| [ScheduleWebAppointment][ app1 = [new] [ScheduleWebAppointment]();] |
|                                                                                                                                                                                                    |
| [Scheduler1.Appointments.Add(app1);]                                                                                                                           |
|                                                                                                                                                                                                    |
| []                                                                                                                                                             |
|                                                                                                                                                                                                    |
| [ScheduleWebAppointment][ app2 = [new] [ScheduleWebAppointment]();] |
|                                                                                                                                                                                                    |
| [Scheduler1.Appointments.Add(app2);]                                                                                                                           |
|                                                                                                                                                                                                    |
| []                                                                                                                                                             |
|                                                                                                                                                                                                    |
| [ScheduleWebAppointment][ app3 = [new] [ScheduleWebAppointment]();] |
|                                                                                                                                                                                                    |
| [Scheduler1.Appointments.Add(app3);]                                                                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                            |
| [Private][ app1 [As] Syncfusion.Web.UI.WebControls.ScheduleControl.ScheduleWebAppointment = [New] ScheduleWebAppointment()] |
|                                                                                                                                                                                                                                                            |
| [Scheduler1.Appointments.Add(app1)]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                            |
| [Private][ app2 [As] Syncfusion.Web.UI.WebControls.ScheduleControl.ScheduleWebAppointment = [New] ScheduleWebAppointment()] |
|                                                                                                                                                                                                                                                            |
| [Scheduler1.Appointments.Add(app2)]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                            |
| [Private][ app3 [As] Syncfusion.Web.UI.WebControls.ScheduleControl.ScheduleWebAppointment = [New] ScheduleWebAppointment()] |
|                                                                                                                                                                                                                                                            |
| [Scheduler1.Appointments.Add(app3)]                                                                                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

8.   Set the **Owner**, **Subject**, **StartTime** and **EndTime** properties for the appointments.

[] 

To view the above properties in detail, see [Assign Appointments to Resources]{.UGHyperlink}.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                             |
|                                                                                                                                              |
| []                                                                                                       |
|                                                                                                                                              |
| [app1.Owner = 1;]                                                                                        |
|                                                                                                                                              |
| [app1.StartTime = [new] [DateTime](2008, 08, 07, 17, 00, 00);] |
|                                                                                                                                              |
| [app1.EndTime = [new] [DateTime](2008, 08, 07, 18, 00, 00);]   |
|                                                                                                                                              |
| [app1.Subject = [\"Meeting with Allen\"];]                                        |
|                                                                                                                                              |
| []                                                                                                       |
|                                                                                                                                              |
| [app1.Owner = 2;]                                                                                        |
|                                                                                                                                              |
| [app1.StartTime = [new] [DateTime](2008, 08, 07, 10, 00, 00);] |
|                                                                                                                                              |
| [app1.EndTime = [new] [DateTime](2008, 08, 07, 11, 00, 00);]   |
|                                                                                                                                              |
| [app1.Subject = [\"Brian coming over\"];]                                         |
|                                                                                                                                              |
| []                                                                                                       |
|                                                                                                                                              |
| [app1.Owner = 3;]                                                                                        |
|                                                                                                                                              |
| [app1.StartTime = [new] [DateTime](2008, 08, 07, 13, 00, 00);] |
|                                                                                                                                              |
| [app1.EndTime = [new] [DateTime](2008, 08, 07, 14, 00, 00);]   |
|                                                                                                                                              |
| [app1.Subject = [\"Lunch with George\"];]                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                              |
|                                                                                               |
| []                                                        |
|                                                                                               |
| [app1.Owner = 1]                                          |
|                                                                                               |
| [app1.StartTime = New DateTime(2008, 08, 07, 5, 00, 00)]  |
|                                                                                               |
| [app1.EndTime = New DateTime(2008, 08, 07, 6, 00, 00)]    |
|                                                                                               |
| [app1.Subject = \"Meeting with Allen\"]                   |
|                                                                                               |
| []                                                        |
|                                                                                               |
| [app1.Owner = 2]                                          |
|                                                                                               |
| [app1.StartTime = New DateTime(2008, 08, 07, 10, 00, 00)] |
|                                                                                               |
| [app1.EndTime = New DateTime(2008, 08, 07, 11, 00, 00)]   |
|                                                                                               |
| [app1.Subject = \"Brian coming over\"]                    |
|                                                                                               |
| []                                                        |
|                                                                                               |
| [app1.Owner = 3]                                          |
|                                                                                               |
| [app1.StartTime = New DateTime(2008, 08, 07, 1, 00, 00)]  |
|                                                                                               |
| [app1.EndTime = New DateTime(2008, 08, 07, 2, 00, 00)]    |
|                                                                                               |
| [app1.Subject = \"Lunch with George\"]                    |
+-----------------------------------------------------------------------------------------------+

[] 

9.   Run the application. The output will be displayed as shown below.

[] 

{border="0"}[]

[] 

See Also

[] 

[Through Designer]{.UGHyperlink}[]{.UGHyperlink}

 

[]{#p17} 

[]{#related-topics}

