---
title: creatingtasklinks.md
original_path: WinForms_Docs/99_Uncategorized/creatingtasklinks.md
created_at: 2025-08-05
---








  









### Creating Task links {#creating-task-links style="tab-stops: 0pt"}

A task link is created using the default constructor of the **TaskLink** class. It accepts three parameters. The first parameter defines the predecessor **Task**, second parameter defines the successor **Task** and third parameter defines the task link type from values specified by **TaskLinkType** enumeration type.

The following example illustrates how to create links between two tasks.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                |
| [// Creating two tasks that are to be linked]                                                                                                                                                |
|                                                                                                                                                                                                                                                |
| [Task][ task1 = [new] [Task]([\"Task1\"]);]                                       |
|                                                                                                                                                                                                                                                |
| [Task task2 = new Task([\"Task2\"]);]                                                                                                                                              |
|                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                |
| [// Link task1 and task2]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                |
| [TaskLink][ link = [new] [TaskLink](task1, task2, [TaskLinkType].FinishToStart);] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                     |
|                                                                                                                                                                                                                      |
| **[]**                                                                                                                                                                           |
|                                                                                                                                                                                                                      |
| [\' Creating tasks that are to be linked]                                                                                                                          |
|                                                                                                                                                                                                                      |
| [Dim][ task1 [As] Task = [New] Task([\"Task1\"])]             |
|                                                                                                                                                                                                                      |
| [Dim][ task2 [As] Task = [New] Task([\"Task2\"])]             |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                                      |
| [\' Creating a link between task1 and task2]                                                                                                                       |
|                                                                                                                                                                                                                      |
| [Dim][ link [As] TaskLink = [New] TaskLink(task1, task2, TaskLinkType.FinishToStart)] |
|                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

