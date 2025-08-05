---
title: externalpropertybinding1.md
original_path: WinForms_Docs/03_Data_Binding/externalpropertybinding1.md
created_at: 2025-08-05
---








  









### External Property Binding {#external-property-binding style="tab-stops: 0pt"}

Essential Gantt for WPF allow you to bind any type of *IEnumerable* source to Gantt.You can bind any collection to Gantt using the *TaskAttributeMapping* class. This will get the mapping name of the requied fields from the underlying soruce. With this mapping the Gantt will get the required information to render the Chart nodes.

The following code illustrate how to map the properties using the *TaskAttributeMapping* class:

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                 |
|                                                                                                                                                                                                    |
| [\                                                                                                                                                                                                 |
| [ \<][gantt][:][TaskAttributeMapping][ TaskIdMapping][=\"Id\"]\ |
|                     [ TaskNameMapping][=\"Name\"]\                                                                                                        |
|                     [ StartDateMapping][=\"StartDate\"] \                                                                                                 |
|                     [ ChildMapping][=\"ChildTask\"]\                                                                                                      |
|                     [ FinishDateMapping][=\"EndDate\"]\                                                                                                   |
|                     [ DurationMapping][=\"Duration\"]\                                                                                                    |
|                     [ ResourceInfoMapping][=\"Resource\"]\                                                                                                |
|                     [ ProgressMapping][=\"Complete\"]\                                                                                                    |
|                     [ PredecessorMapping][=\"Predecessor\"\>]\                                                                                            |
| [ \</][gantt][:][TaskAttributeMapping][\>]]     |
|                                                                                                                                                                                                    |
| []                                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                             |
|                                                                                                                                              |
| [  [TaskAttributeMapping] attributes = [new] [TaskAttributeMapping]();\ |
|   attributes.TaskIdMapping = [\"Id\"];\                                                                              |
|   attributes.TaskNameMapping = [\"Name\"];\                                                                          |
|   attributes.StartDateMapping = [\"StartDate\"];\                                                                    |
|   attributes.FinishDateMapping = [\"EndDate\"];\                                                                     |
|   attributes.DurationMapping = [\"Duration\"];\                                                                      |
|   attributes.ChildMapping = [\"ChildTask\"];\                                                                        |
|   attributes.ResourceInfoMapping = [\"Resource\"];\                                                                  |
|   attributes.ProgressMapping = [\"Predecessor\"];]                               |
|                                                                                                                                              |
| []                                                                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------+

 

The following code illustrates how to bind the external source to Gantt control:

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\<][Sync][:][GanttControl][ x][:][Name][=\"Gantt\" ][ItemsSource][=\"{][Binding][ GanttItemSource][}\"\>][\ |
| [      ][\<][Sync][:][GanttControl.TaskMapping][\>]\                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [           ][\<][Sync][:][TaskCollectionMapping][ TaskIdMapping][=\"Id\"]\                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                       [ TaskNameMapping][=\"Name\"]\                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                       [ StartDateMapping][=\"SDate\"]\                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                       [ FinishDateMapping][=\"EDate\"]\                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                       [ ResourceNameMapping][=\"ResName\"]\                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                       [ ChildMapping][=\"ChildTask\"]\                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                       [ PredecessorMapping][=\"Predecessor\"]\                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                       [ ProgressMapping][=\"Complete\" /\>]\                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [            ][\</][Sync][:][GanttControl.TaskMapping][\>]\                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\</][Sync][:][GanttControl][\>]][]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                        |
|                                                                                                                                                                         |
| [ //Initializing Gantt][\                                                                                             |
| [ GanttControl] Gantt = [new] [GanttControl]();]               |
|                                                                                                                                                                         |
| [ [ViewModel] model=  [new] [ViewModel]();]                    |
|                                                                                                                                                                         |
| []                                                                                                                                  |
|                                                                                                                                                                         |
| [ TaskAttributeMapping][ attributes = [new] [TaskAttributeMapping]();\ |
|  attributes.TaskIdMapping = [\"Id\"];\                                                                                                          |
|  attributes.TaskNameMapping = [\"Name\"];\                                                                                                      |
|  attributes.StartDateMapping = [\"StartDate\"];\                                                                                                |
|  attributes.FinishDateMapping = [\"EndDate\"];\                                                                                                 |
|  attributes.DurationMapping = [\"Duration\"];\                                                                                                  |
|  attributes.ChildMapping = [\"ChildTask\"];\                                                                                                    |
|  attributes.ResourceInfoMapping = [\"Resource\"];\                                                                                              |
|  attributes.ProgressMapping = [\"Predecessor\"];]                                                           |
|                                                                                                                                                                         |
| []                                                                                                                                  |
|                                                                                                                                                                         |
| []                                                                                                                                  |
|                                                                                                                                                                         |
| [ Gantt.TaskAttributeMapping = attributes;]                                                                                         |
|                                                                                                                                                                         |
| [ Gantt.ItemsSource = model.GanttItemSource;]                                                                                       |
|                                                                                                                                                                         |
| []                                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                 |
|                                                                                                                                                                                                                  |
| [GanttItemSource][ = [new] [ObservableCollection]\<[Task]\>();]     |
|                                                                                                                                                                                                                  |
| [GanttItemSource = ][GetDataSourceStartToStart();]                                                                                       |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                              |
|                                                                                                                                                                                                                  |
| [ObservableCollection][\<[Task]\> GetDataSourceStartToStart()\                                                                       |
| {\                                                                                                                                                                                                               |
| [ObservableCollection]\<[Task]\> task = [ObservableCollection]\<[Task]\>();] |
|                                                                                                                                                                                                                  |
| [\                                                                                                                                                                                                               |
| task.Add([new] [Task] { Id = 1, ]                                                                                               |
|                                                                                                                                                                                                                  |
| [                    Name = [\"Scope\"], ]                                                                                                           |
|                                                                                                                                                                                                                  |
| [                    StartDate = [new] [DateTime](2011, 1, 3), ]                                                                |
|                                                                                                                                                                                                                  |
| [                    EndDate = [new] [DateTime](2011, 1, 14),]                                                                  |
|                                                                                                                                                                                                                  |
| [                    Progress = 40d });\                                                                                                                                                                         |
| task\[0\].ChildTask.Add([new] [Task] { Id = 2, ]                                                                                |
|                                                                                                                                                                                                                  |
| [                    Name = [\"Determine project office scope\"], ]                                                                                  |
|                                                                                                                                                                                                                  |
| [                    StartDate = [new] [DateTime](2011, 1, 3), ]                                                                |
|                                                                                                                                                                                                                  |
| [                    EndDate = [new] [DateTime](2011, 1, 5), ]                                                                  |
|                                                                                                                                                                                                                  |
| [                    Progress = 20d });\                                                                                                                                                                         |
| task\[0\].ChildTask.Add([new] [Task] { Id = 3, ]                                                                                |
|                                                                                                                                                                                                                  |
| [                    Name = [\"Justify Project Offfice via business model\"], ]                                                                      |
|                                                                                                                                                                                                                  |
| [                    StartDate = [new] [DateTime](2011, 1, 6), ]                                                                |
|                                                                                                                                                                                                                  |
| [                    EndDate = [new] [DateTime](2011, 1, 7), ]                                                                  |
|                                                                                                                                                                                                                  |
| [                    Progress = 20d });\                                                                                                                                                                         |
| task\[0\].ChildTask.Add([new] [Task] { Id = 4, ]                                                                                |
|                                                                                                                                                                                                                  |
| [                    Name = [\"Secure executive sponsorship\"], ]                                                                                    |
|                                                                                                                                                                                                                  |
| [                    StartDate = [new] [DateTime](2011, 1, 10), ]                                                               |
|                                                                                                                                                                                                                  |
| [                    EndDate = [new] [DateTime](2011, 1, 14), ]                                                                 |
|                                                                                                                                                                                                                  |
| [                    Progress = 20d });]                                                                                                                                     |
|                                                                                                                                                                                                                  |
| [task\[0\].ChildTask.Add([new] [Task] { Id = 5, ]                                                                               |
|                                                                                                                                                                                                                  |
| [                    Name = [\"Secure complete\"], ]                                                                                                 |
|                                                                                                                                                                                                                  |
| [                    StartDate = [new] [DateTime](2011, 1, 14), ]                                                               |
|                                                                                                                                                                                                                  |
| [                    EndDate = [new] [DateTime](2011, 1, 14), ]                                                                 |
|                                                                                                                                                                                                                  |
| [                    Progress = 20d });]                                                                                                                                     |
|                                                                                                                                                                                                                  |
| [return ][task;]                                                                                                            |
|                                                                                                                                                                                                                  |
| [}\                                                                                                                                                                                                              |
| \                                                                                                                                                                                                                |
| ][]                                                                                                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 {border="0"}

Figure 17: External Property Binding[]

Samples Link

To view samples:

1.   Select Start -\> Programs -\> Syncfusion -\> Essential Studio x.x.xx -\> Dashboard.

2.   Click **Run Samples** for WPF under User Interface Edition panel .

3.   Select **Gantt**.

4.   Expand the DataBinding Features item in the Sample Browser.

5.   Choose the External Property Binding samples to launch.

 

[]{#related-topics}

