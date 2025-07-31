---
title: dependencyrelationship1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\dependencyrelationship1.md
created_at: 2025-07-03
---








  









## Dependency Relationship {#dependency-relationship style="tab-stops: 0pt"}

Dependency relationship is  the relationship between two tasks. These relationship has been caterogrised into four types based on the start and finish date of the task. They are:

[·      ]FinishToStart

[·      ]FinishToFinish

[·      ]StartToStart

[·      ]StartToFinish

 

**Finish-to-start**---You cannot start a task until the other task is completed.

 

{border="0"}

Figure 18: Finish-to-start[]

[] 

**Finish-to-finish**---You cannot finish a task until the other task is completed.

[] 

{border="0"}

Figure 19: Finish-to-finish[]

 

**[Start-to-start]**[---You cannot start a task until the other task is also started.]

[] 

{border="0"}

Figure 20: Start-to-start[]

[] 

**Start-to-Finish---**You cannot finish a task until another the other task is started.

[] 

{border="0"}

Figure 21: Start-to-Finish[]

[] 

Properties


+-----------------------+--------------------------------------------------------------------------------+-----------------+-------------+-----------------+
| Property              | Description                                                                    | Type            | Data Type   | Reference links |
+-----------------------+--------------------------------------------------------------------------------+-----------------+-------------+-----------------+
| Prodecessor           | This enables you to set the relationship between the task.                     | **Object**      | Object      | NA              |
+-----------------------+--------------------------------------------------------------------------------+-----------------+-------------+-----------------+
| GanttTaskRelationship | This contains four relationships. They are:                                    | **Predecessor** | Enum        | NA              |
|                       |                                                                                |                 |             |                 |
|                       | [·      ]StartToStart                             |                 |             |                 |
|                       |                                                                                |                 |             |                 |
|                       | [·      ]StartToFinish                            |                 |             |                 |
|                       |                                                                                |                 |             |                 |
|                       | [·      ]FinishToFinish                           |                 |             |                 |
|                       |                                                                                |                 |             |                 |
|                       | [·      ]FinishToStart                            |                 |             |                 |
|                       |                                                                                |                 |             |                 |
|                       | You can asign this to the *TaskDetails* to set the relationship between tasks. |                 |             |                 |
+-----------------------+--------------------------------------------------------------------------------+-----------------+-------------+-----------------+


[] 

Specifing the Relationship between Tasks

The following code illustrates how to add the Dependency Relationship between tasks:

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                               |
|                                                                                                                                                                                                                                |
| [GanttItemSource][ = [new] [ObservableCollection]\<[TaskDetails]\>();]            |
|                                                                                                                                                                                                                                |
| [GanttItemSource = ][GetDataSourceStartToStart();]                                                                                                     |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                                                |
| [ObservableCollection][\<[TaskDetails]\> GetDataSourceStartToStart()\                                                                              |
| {\                                                                                                                                                                                                                             |
| [ObservableCollection]\<[TaskDetails]\> task = [ObservableCollection]\<[TaskDetails]\>();] |
|                                                                                                                                                                                                                                |
| [\                                                                                                                                                                                                                             |
| task.Add([new] [TaskDetails] { TaskId = 1, ]                                                                                                  |
|                                                                                                                                                                                                                                |
| [                           TaskName = [\"Scope\"], ]                                                                                                              |
|                                                                                                                                                                                                                                |
| [                           StartDate = [new] [DateTime](2011, 1, 3), ]                                                                       |
|                                                                                                                                                                                                                                |
| [                           FinishDate = [new] [DateTime](2011, 1, 14),  ]                                                                    |
|                                                                                                                                                                                                                                |
| [                           Progress = 40d });\                                                                                                                                                                                |
| task\[0\].Child.Add([new] [TaskDetails] { TaskId = 2, ]                                                                                       |
|                                                                                                                                                                                                                                |
| [                    TaskName = [\"Determine project office scope\"], ]                                                                                            |
|                                                                                                                                                                                                                                |
| [                    StartDate = [new] [DateTime](2011, 1, 3), ]                                                                              |
|                                                                                                                                                                                                                                |
| [                    FinishDate = [new] [DateTime](2011, 1, 5), ]                                                                             |
|                                                                                                                                                                                                                                |
| [                    Progress = 20d });\                                                                                                                                                                                       |
| task\[0\].Child.Add([new] [TaskDetails] { TaskId = 3, ]                                                                                       |
|                                                                                                                                                                                                                                |
| [                    TaskName = [\"Justify Project Offfice via business model\"], ]                                                                                |
|                                                                                                                                                                                                                                |
| [                    StartDate = [new] [DateTime](2011, 1, 6), ]                                                                              |
|                                                                                                                                                                                                                                |
| [                    FinishDate = [new] [DateTime](2011, 1, 7), ]                                                                             |
|                                                                                                                                                                                                                                |
| [                    Progress = 20d });\                                                                                                                                                                                       |
| task\[0\].Child.Add([new] [TaskDetails] { TaskId = 4, ]                                                                                       |
|                                                                                                                                                                                                                                |
| [                    TaskName = [\"Secure executive sponsorship\"], ]                                                                                              |
|                                                                                                                                                                                                                                |
| [                    StartDate = [new] [DateTime](2011, 1, 10), ]                                                                             |
|                                                                                                                                                                                                                                |
| [                    FinishDate = [new] [DateTime](2011, 1, 14), ]                                                                            |
|                                                                                                                                                                                                                                |
| [                    Progress = 20d });]                                                                                                                                                   |
|                                                                                                                                                                                                                                |
| [task\[0\].Child.Add([new] [TaskDetails] { TaskId = 5, ]                                                                                      |
|                                                                                                                                                                                                                                |
| [                    TaskName = [\"Secure complete\"], ]                                                                                                           |
|                                                                                                                                                                                                                                |
| [                    StartDate = [new] [DateTime](2011, 1, 14), ]                                                                             |
|                                                                                                                                                                                                                                |
| [                    FinishDate = [new] [DateTime](2011, 1, 14), ]                                                                            |
|                                                                                                                                                                                                                                |
| [                    Progress = 20d });]                                                                                                                                                   |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [//Adding dependency relationShip ][\                                                                                                                                        |
| task\[0\].Child\[1\].Predecessor.Add([new] [Predecessor]() { GanttTaskIndex = 2, ]                                                            |
|                                                                                                                                                                                                                                |
| [             GanttTaskRelationship = [GanttTaskRelationship].StartToStart });\                                                                                                                        |
| \                                                                                                                                                                                                                              |
| ]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                |
| [task\[0\].Child\[2\].Predecessor.Add([new] [Predecessor]() { GanttTaskIndex = 3, ]                                                           |
|                                                                                                                                                                                                                                |
| [             GanttTaskRelationship = [GanttTaskRelationship].StartToFinish });]                                                                                   |
|                                                                                                                                                                                                                                |
| [\                                                                                                                                                                                                                             |
| task\[0\].Child\[3\].Predecessor.Add([new] [Predecessor]() { GanttTaskIndex = 3, ]                                                            |
|                                                                                                                                                                                                                                |
| [             GanttTaskRelationship = [GanttTaskRelationship].FinishToFinish });]                                                                                  |
|                                                                                                                                                                                                                                |
| [return ][task;]                                                                                                                          |
|                                                                                                                                                                                                                                |
| [}\                                                                                                                                                                                                                            |
| \                                                                                                                                                                                                                              |
| ][]                                                                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

Figure 22: Dependency Relationship  []

Samples Link

To view samples:

1.   Select Start -\> Programs -\> Syncfusion -\> Essential Studio x.x.xx -\> Dashboard.

2.   Click **Run Samples** for WPF under User Interface Edition panel .

3.   Select **Gantt**.

4.   Expand the **Connectors Features** item in the **Sample Browser**.

5.   Choose the **Predecessor samples** to launch.

 

More:





