---
title: howtobuildaresourceviewgantt.md
original_path: WinForms_Docs/03_Data_Binding/howtobuildaresourceviewgantt.md
created_at: 2025-08-05
---








  









## How to Build a Resource View Gantt {#how-to-build-a-resource-view-gantt style="TEXT-ALIGN: justify; tab-stops: 0pt"}

By default the Gantt will display single node in a row. This helps you to manage the project. When you want to manage the resources in a project, you need multiple nodes in a single row. Resource View Gantt enables you to manage the resources involved in the project.  

In normal Gantt, the node represents the task or activity of the project. In Resource View Gantt, the node represents Tasks assigned to a resource. Multiple tasks assigned to a resource can be displayed in a single row.  You can achieve this using the new mapping attribute of the *InLineTaskMapping*.

You can develop a populate Resource View Gantt by populating the collection of tasks in a single row by mapping the corresponding field in the underlying source to the *InLineTaskMapping*.

The following code illustrates this:

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [ ][\<][gantt][:][GanttControl][ Grid.Row][=\"1\"][ x][:][Name][=\"Gantt\"\>][\ |
| [                ][\<][gantt][:][GanttControl.TaskAttributeMapping][\>]\                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [                    ][\<][gantt][:][TaskAttributeMapping] \                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                            [ TaskNameMapping][=\"Name\"]\                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                            [ StartDateMapping][=\"StartDate\"] \                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                            [ ChildMapping][=\"SubItems\"]\                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                            [ FinishDateMapping][=\"FinishDate\"]\                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                            [ InLineTaskMapping][=\"InLineItems\"\>]\                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [                    ][\</][gantt][:][TaskAttributeMapping][\>]\                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [                ][\</][gantt][:][GanttControl.TaskAttributeMapping][\>]\                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [            ][\</][gantt][:][GanttControl][\>]]                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

The following is the sample data source for the Resource View Gantt**:**

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                         |
| [ ][ObservableCollection][\<[Item]\> teams = [new] [ObservableCollection]\<[Item]\>();\                                                                            |
|  \                                                                                                                                                                                                                                                                                                                                                                      |
|             teams.Add([new] [Item]() { Name = [\"RDU Team\"] });\                                                                                                                                                                                                                                  |
|             [Item] Person = [new] [Item]() { Name = [\"Robert\"] };\                                                                                                                                                                                                       |
|             Person.InLineItems.Add([new] [Item]() { StartDate = [new] [DateTime](2012, 01, 07), FinishDate = [new] [DateTime](2012, 01, 11), Name = [\"Market Analysis\"], Progress = 50d });\           |
|             Person.InLineItems.Add([new] [Item]() { StartDate = [new] [DateTime](2012, 01, 11), FinishDate = [new] [DateTime](2012, 01, 15), Name = [\"Competitor Analysis\"], Progress = 20d });\       |
|             Person.InLineItems.Add([new] [Item]() { StartDate = [new] [DateTime](2012, 01, 13), FinishDate = [new] [DateTime](2012, 01, 19), Name = [\"Desing Spec\"] });\                               |
|             teams\[0\].SubItems.Add(Person);\                                                                                                                                                                                                                                                                                                                           |
|  \                                                                                                                                                                                                                                                                                                                                                                      |
|             Person = [new] [Item]() { Name = [\"Michael\"] };\                                                                                                                                                                                                                                     |
|             Person.InLineItems.Add([new] [Item]() { StartDate = [new] [DateTime](2012, 01, 18), FinishDate = [new] [DateTime](2012, 01, 19), Name = [\"Basic Requirement Analysis\"], Progress = 40 });\ |
|             Person.InLineItems.Add([new] [Item]() { StartDate = [new] [DateTime](2012, 01, 19), FinishDate = [new] [DateTime](2012, 01, 21), Name = [\"Requirement Spec\"] });\                          |
|             teams\[0\].SubItems.Add(Person);\                                                                                                                                                                                                                                                                                                                           |
|  \                                                                                                                                                                                                                                                                                                                                                                      |
|             Person = [new] [Item]() { Name = [\"Anne\"] };\                                                                                                                                                                                                                                        |
|             Person.InLineItems.Add([new] [Item]() { StartDate = [new] [DateTime](2012, 01, 21), FinishDate = [new] [DateTime](2012, 01, 24), Name = [\"Estimation\"], Progress = 30 });\                 |
|             Person.InLineItems.Add([new] [Item]() { StartDate = [new] [DateTime](2012, 01, 24), FinishDate = [new] [DateTime](2012, 01, 26), Name = [\"Budget & Plan Spec\"] });\                        |
|             teams\[0\].SubItems.Add(Person);]                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

The following is the Data Structure used to build a Resource View Gantt:

 

{border="0"}

 

 

 

Data Structure:

[·      ]**Team** that hold info about the team.

[·      ]SubItems of **Team** will hold the list of **Resources**   in that particular team.

[·      ]InLineItems of each **Resource** will holds the tasks assigned to the particular resource.

 

Information Displayed in Gantt

**Grid Region:** Grid will display only the information about the team and its resources (Sub Items). It will not display the info about Assigned Tasks (InLineItems).

**Chart Region:** Chart will display only the information about the team and the tasks assigned to each resource in the team (InLineItems). It will not display the info about Resources (Sub Items)

 

 

{border="0"}

Figure 40: Information Displayed in Gantt

 

 

Samples Link

To view samples:

1.   Open **Syncfusion Dashboard**.

2.   Select **User Interface \> Silverlight**.

3.   Click **Run Samples**.

4.   Navigate to **Gantt \>** **Data Binding item \> Resource View Gantt sample**.

 

[]{#related-topics}

