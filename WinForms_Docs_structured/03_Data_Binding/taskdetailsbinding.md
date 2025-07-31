---
title: taskdetailsbinding.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\03_Data_Binding\taskdetailsbinding.md
created_at: 2025-07-03
---








  









### TaskDetails Binding {#taskdetails-binding style="tab-stops: 0pt"}

Essential Gantt for Silverlight includes an inbuilt classclled TaskDetails, which is inherited from the **IGanttTask** interface. A collection of the  TaskDetails can be bounded as an ItemsSource for the GanttControl.

 

Use Case Scenarios[[]]{.Heading3Char}

You can easily create the task details collection for your project using the TaskDetails class or by creating a new class by inheriting the *IGantt* interface.

 

Binding TaskDetials collection to Gantt Control

 

The following code illustrates how to bind the Task Detials to the Gantt Control:

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [ ][\<][Sync:GanttControl][ ][ItemsSource][=\"{Binding GanttItemSource}\"][ ][x:Name][=\"Gantt\"][ ][\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                          |
|                                                                                                                                                           |
| [ //Initializing Gantt][\                                                                               |
| [ GanttControl] Gantt = [new] [GanttControl]();] |
|                                                                                                                                                           |
| [ [ViewModel] model=  [new] [ViewModel]();\                                          |
|  Gantt.ItemsSource = model.GanttItemSource;]                                                                          |
|                                                                                                                                                           |
| []                                                                                                                    |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------+

 

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
| [                           StartDate = [new] [DateTime](2011, 1, 3), ]                                                                       |
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
| [                    Progress = 20d });\                                                                                                                                                                                       |
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
| [                    FinishDate = [new] [DateTime](2011, 1, 14), ]                                                                            |
|                                                                                                                                                                                                                                |
| [                    Progress = 20d });]                                                                                                                                                   |
|                                                                                                                                                                                                                                |
| [return ][task;]                                                                                                                          |
|                                                                                                                                                                                                                                |
| [}\                                                                                                                                                                                                                            |
| \                                                                                                                                                                                                                              |
| ][]                                                                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

Figure 16: BindingTask Details[]

Samples Link

To view samples:

1.   Select Start -\> Programs -\> Syncfusion -\> Essential Studio x.x.xx -\> Dashboard.

2.   Click **Run Samples** for Silverlight under User Interface Edition panel .

3.   Select **Gantt**.

4.   Expand the DataBinding Features item in the Sample Browser.

5.   Choose the Binding Task Details samples to launch.

[]{#related-topics}

