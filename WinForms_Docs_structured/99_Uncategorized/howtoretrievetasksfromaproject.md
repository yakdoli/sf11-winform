---
title: howtoretrievetasksfromaproject.md
original_path: WinForms_Docs/99_Uncategorized/howtoretrievetasksfromaproject.md
created_at: 2025-08-05
---








  









## How to retrieve tasks from a project? {#how-to-retrieve-tasks-from-a-project style="tab-stops: 0pt"}

The tasks present in a project can be retrieved using the **GetTaskByUID** method.

The following code snippet illustrates retrieving tasks using this method:

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                     |
|                                                                                                                                                                                                                      |
| **[]**                                                                                                                                                                           |
|                                                                                                                                                                                                                      |
| [// Opening the project file]                                                                                                                                      |
|                                                                                                                                                                                                                      |
| [Project][ project = [ProjectReader].Open([@\"D:\\ProjectWithTasks.xml\"]);] |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                                      |
| [// Retrieving a task by UID]                                                                                                                                      |
|                                                                                                                                                                                                                      |
| [Task][ task = project.GetTaskByUID(2);]                                                                                     |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                                      |
| [// Viewing retrieved task information]                                                                                                                            |
|                                                                                                                                                                                                                      |
| [Console][.WriteLine([\"Task Name: \"] + task.Name);]                                                |
|                                                                                                                                                                                                                      |
| [Console][.WriteLine([\"Task Start Date: \"] + task.Start);]                                         |
|                                                                                                                                                                                                                      |
| [Console][.WriteLine([\"Task Finish Date: \"] + task.Finish);]                                       |
|                                                                                                                                                                                                                      |
| [Console][.WriteLine([\"No. of Sub Tasks: \"] + task.Children.Count);]                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                |
|                                                                                                                                                                                                                 |
| [\' Opening the project file]                                                                                                                                 |
|                                                                                                                                                                                                                 |
| [Dim][ project [As] Project = ProjectReader.Open([\"ProjectWithTasks.xml\"])] |
|                                                                                                                                                                                                                 |
| **[]**                                                                                                                                                                      |
|                                                                                                                                                                                                                 |
| [\' Retrieving a task by UID]                                                                                                                                 |
|                                                                                                                                                                                                                 |
| [Dim][ task [As] Task = project.GetTaskByUID(2)]                                                      |
|                                                                                                                                                                                                                 |
| []                                                                                                                                                                          |
|                                                                                                                                                                                                                 |
| [\' Viewing retrieved task information][]                                                                                 |
|                                                                                                                                                                                                                 |
| [Console][.WriteLine([\"Task Name: \"] + task.Name)]                                            |
|                                                                                                                                                                                                                 |
| [Console][.WriteLine([\"Task Start Date: \"] + task.Start)]                                     |
|                                                                                                                                                                                                                 |
| [Console][.WriteLine([\"Task Finish Date: \"] + task.Finish)]                                   |
|                                                                                                                                                                                                                 |
| [Console][.WriteLine([\"No. of Sub Tasks: \"] + task.Children.Count)]                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

**[5.5 How to retrieve resources from a project?]**

The resources present in a project can be retrieved using the **GetResourceByUID** method.

The following code snippet illustrates how to retrieve tasks using this method:

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                    |
|                                                                                                                                                                                                                     |
| **[]**                                                                                                                                                                          |
|                                                                                                                                                                                                                     |
| [// Opening the project file]                                                                                                                                     |
|                                                                                                                                                                                                                     |
| [Project][ project = [ProjectReader].Open([\"ProjectWithResources.xml\"]);] |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                              |
|                                                                                                                                                                                                                     |
| [// Retrieving a resource by UID]                                                                                                                                 |
|                                                                                                                                                                                                                     |
| [Resource][ resource = project.GetResourceByUID(1);]                                                                        |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                              |
|                                                                                                                                                                                                                     |
| [// Viewing retrieved resource information]                                                                                                                       |
|                                                                                                                                                                                                                     |
| [Console][.WriteLine([\"Resource Name: \"] + resource.Name);]                                       |
|                                                                                                                                                                                                                     |
| [Console][.WriteLine([\"Type: \"] + resource.Type);]                                                |
|                                                                                                                                                                                                                     |
| [Console][.WriteLine([\"Work: \"] + resource.Work);]                                                |
|                                                                                                                                                                                                                     |
| [Console][.WriteLine([\"Remaining Work: \"] + resource.RemainingWork);]                             |
|                                                                                                                                                                                                                     |
| [Console][.WriteLine([\"Resource Calendar ID: \"] + resource.CalendarUID);]                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                    |
|                                                                                                                                                                                                                     |
| [\' Opening the project file]                                                                                                                                     |
|                                                                                                                                                                                                                     |
| [Dim][ project [As] Project = ProjectReader.Open([\"ProjectWithResources.xml\"])] |
|                                                                                                                                                                                                                     |
| **[]**                                                                                                                                                                          |
|                                                                                                                                                                                                                     |
| [\' Retrieving a resource by UID]                                                                                                                                 |
|                                                                                                                                                                                                                     |
| [Dim][ resource [As] Resource = project.GetResourceByUID(1)]                                              |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                              |
|                                                                                                                                                                                                                     |
| [\' Viewing retrieved resource information][]                                                                                 |
|                                                                                                                                                                                                                     |
| [Console][.WriteLine([\"Resource Name: \"] + resource.Name)]                                        |
|                                                                                                                                                                                                                     |
| [Console][.WriteLine([\"Type: \"] + resource.Type)]                                                 |
|                                                                                                                                                                                                                     |
| [Console][.WriteLine([\"Work: \"] + resource.Work)]                                                 |
|                                                                                                                                                                                                                     |
| [Console][.WriteLine([\"Remaining Work: \"] + resource.RemainingWork)]                              |
|                                                                                                                                                                                                                     |
| [Console][.WriteLine([\"Resource Calendar ID: \"] + resource.CalendarUID)]                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

**[5.6 How to retrieve resource assignments from a project?]**

The resource assignments present in a project can be retrieved using the **GetAssignmentByUID** method.

The following code snippet shows how to use this method:

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                             |
|                                                                                                                                                                                                              |
| **[]**                                                                                                                                                                   |
|                                                                                                                                                                                                              |
| [// Opening the project file]                                                                                                                              |
|                                                                                                                                                                                                              |
| [Project][ project = [ProjectReader].Open([\"SampleProject.xml\"]);] |
|                                                                                                                                                                                                              |
| []                                                                                                                                                                       |
|                                                                                                                                                                                                              |
| [// Retrieving an assignment by UID]                                                                                                                       |
|                                                                                                                                                                                                              |
| [Assignment][ assignment = project.GetAssignmentByUID(1);]                                                           |
|                                                                                                                                                                                                              |
| []                                                                                                                                                                       |
|                                                                                                                                                                                                              |
| [//Viewing retrived assignment information]                                                                                                                |
|                                                                                                                                                                                                              |
| [Console][.WriteLine([\"Resource: \"] + assignment.Resource.Name);]                          |
|                                                                                                                                                                                                              |
| [Console][.WriteLine([\"Assigned to: \"] + assignment.Task.Name);]                           |
|                                                                                                                                                                                                              |
| [Console][.WriteLine([\"Booking Type: \"] + assignment.BookingType);]                        |
|                                                                                                                                                                                                              |
| [Console][.WriteLine([\"Cost: \$\"] + assignment.Cost);]                                     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                             |
|                                                                                                                                                                                                              |
| [\' Opening the project file]                                                                                                                              |
|                                                                                                                                                                                                              |
| [Dim][ project [As] Project = ProjectReader.Open([\"SampleProject.xml\"])] |
|                                                                                                                                                                                                              |
| **[]**                                                                                                                                                                   |
|                                                                                                                                                                                                              |
| [\' Retrieving a resource by UID]                                                                                                                          |
|                                                                                                                                                                                                              |
| [Dim][ assignment [As] Assignment = project.GetAssignmentByUID(1)]                                 |
|                                                                                                                                                                                                              |
| []                                                                                                                                                                       |
|                                                                                                                                                                                                              |
| [\' Viewing retrieved assignment information][]                                                                        |
|                                                                                                                                                                                                              |
| [Console][.WriteLine([\"Resource: \"] + assignment.Resource.Name)]                           |
|                                                                                                                                                                                                              |
| [Console][.WriteLine([\"Assigned to: \"] + assignment.Task.Name)]                            |
|                                                                                                                                                                                                              |
| [Console][.WriteLine([\"Booking Type: \"] + assignment.BookingType)]                         |
|                                                                                                                                                                                                              |
| [Console][.WriteLine([\"Cost: \$\"] + assignment.Cost)]                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

