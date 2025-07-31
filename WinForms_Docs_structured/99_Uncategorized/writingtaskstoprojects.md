---
title: writingtaskstoprojects.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\writingtaskstoprojects.md
created_at: 2025-07-03
---








  









### Writing Tasks to Projects {#writing-tasks-to-projects style="tab-stops: 0pt"}

**RootTask** property of the **Project** class contains the **Children** property that returns the list of **Task** objects. The **Children** property is used to update the tasks.

The following code snippet demonstrates writing tasks to a project.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                |
| [// Creating an instance of the Project]                                                                                                                                                     |
|                                                                                                                                                                                                                                                |
| [Project][ P = [new] [Project]();]                                                                        |
|                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                |
| [// Creating two tasks to be added to the project]                                                                                                                                           |
|                                                                                                                                                                                                                                                |
| [Task][ task1 = [new] [Task]([\"Task1\"]);]                                       |
|                                                                                                                                                                                                                                                |
| [task1.Duration = new [TimeSpan](8, 0, 0);]                                                                                                                                        |
|                                                                                                                                                                                                                                                |
| [Task][ task2 = new Task([\"Task2\"]);]                                                                                        |
|                                                                                                                                                                                                                                                |
| [task2.Duration = new [TimeSpan](8, 0, 0);]                                                                                                                                        |
|                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                |
| [// Adding the tasks to the RootTask of project][]                                                                                                       |
|                                                                                                                                                                                                                                                |
| [P.RootTask.Children.Add(task1);]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                |
| [P.RootTask.Children.Add(task2);]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                |
| [// Calculating Task IDs and UIDs]                                                                                                                                                           |
|                                                                                                                                                                                                                                                |
| [P.CalculateTaskIDs();]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                |
| [// Link \"Task1\" and \"Task2\"]                                                                                                                                                            |
|                                                                                                                                                                                                                                                |
| [TaskLink][ link = [new] [TaskLink](task1, task2, [TaskLinkType].FinishToStart);] |
|                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                |
| [// Saving the project]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                |
| [P.Save([\"ProjectWithTasks.xml\"]);]                                                                                                                                              |
|                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                         |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                     |
|                                                                                                                                                                                                                      |
| [\' Creating an instance of the Project]                                                                                                                           |
|                                                                                                                                                                                                                      |
| [Dim][ P [As] Project = [New] Project()[]]                      |
|                                                                                                                                                                                                                      |
| **[]**                                                                                                                                                                           |
|                                                                                                                                                                                                                      |
| [\' Creating tasks that are to be linked]                                                                                                                          |
|                                                                                                                                                                                                                      |
| [Dim][ task1 [As] Task = [New] Task([\"Task1\"])]             |
|                                                                                                                                                                                                                      |
| [task1.Duration = new [TimeSpan](8, 0, 0)]                                                                                                               |
|                                                                                                                                                                                                                      |
| [Dim][ task2 [As] Task = [New] Task([\"Task2\"])]             |
|                                                                                                                                                                                                                      |
| [task2.Duration = new [TimeSpan](8, 0, 0)]                                                                                                               |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                                      |
| [\' Adding the tasks to the RootTask of the Project][]                                                                         |
|                                                                                                                                                                                                                      |
| [P.RootTask.Children.Add(task1)]                                                                                                                                                 |
|                                                                                                                                                                                                                      |
| [P.RootTask.Children.Add(task2)]                                                                                                                                                 |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                                      |
| [\' Calculating Task IDs and UIDs][]                                                                                           |
|                                                                                                                                                                                                                      |
| [P.CalculateTaskIDs()]                                                                                                                                                           |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                                      |
| [\' Creating a link between task1 and task2]                                                                                                                       |
|                                                                                                                                                                                                                      |
| [Dim][ link [As] TaskLink = [New] TaskLink(task1, task2, TaskLinkType.FinishToStart)] |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                                      |
| [\' Saving the project][]                                                                                                      |
|                                                                                                                                                                                                                      |
| [P.Save([\"ProjectWithTasks.xml\"])]                                                                                                                     |
|                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

The project file created using above code will look as shown in the following screenshot.

 

{border="0"}

Figure 9: Project File Created

 

[]{#related-topics}

