---
title: databinding31.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\03_Data_Binding\databinding31.md
created_at: 2025-07-03
---






#### Data Binding {#data-binding style="tab-stops: 0pt"}

Data Binding is the process of establishing a connection between the application UI and business logic. Data Binding can be unidirectional (Source -\> target or target -\> Source) or bidirectional (Source \<-\> target). You can bind the data to the AutoComplete through the **CustomSource** property. While binding the CustomSource to the AutoComplete, you must set the value of the **DisplayMemberPath** and the **SelectedValuePath** properties.

Adding Data Binding to an Application

You can use the **DisplayMemberPath** property to set the value for items that needs to be displayed in the drop-down list. Also you can use the **SelectedValuePath** property which can be used to set the value of the **SelectedValue** property. The below code snippet will be used to bind the Data Source to the AutoComplete.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\<][syncfusion][:][AutoComplete][ x][:][Name][=\"AutoComplete2\" ][Source][=\"Custom" ] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [DisplayMemberPath][=\"FirstName\"][ SelectedValuePath][=\"LastName\"\>][]                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [     ][\<][syncfusion][:][AutoComplete.CustomSource][\>][]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [            ][\<][local][:][EmployeeList][/\>][]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [     ][\</][syncfusion][:][AutoComplete.CustomSource][\>][]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\</][syncfusion][:][AutoComplete][\>][]                                                                                                                                                                                                                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[ ]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                            |
| [public][ [class] [EmployeeList]]                                                                                                                        |
|                                                                                                                                                                                                                                                                                            |
| [{]                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                            |
| [    [public] [int] EmployeeID { [get]; [set]; }]                                                                                                                  |
|                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                            |
| [    [public] [string] Name { [get]; [set]; }]                                                                                                                     |
|                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                            |
| [    [public] [string] Mailid { [get]; [set]; }]                                                                                                                   |
|                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                            |
| [    public][ EmployeeList() { }]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                            |
| [    public][ EmployeeList([string] name, [string] mail, [int] id)]                                                                    |
|                                                                                                                                                                                                                                                                                            |
| [    {]                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                            |
| [            Name = name;]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                            |
| [            Mailid = mail;]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                            |
| [            EmployeeID = id;]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                            |
| [    }]                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                            |
| [}]                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                            |
| [public][ [class] [EmployeeListCollection] : [ObservableCollection]\<[EmployeeList]\>]                   |
|                                                                                                                                                                                                                                                                                            |
| [{]                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                            |
| [   [public] EmployeeListCollection()]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                            |
| [   {]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                            |
| [            [this].Add([new] [EmployeeList]() { EmployeeID = 1001, Name = [\"John\"], Mailid = [\"john@syncfusion.com\"] });]       |
|                                                                                                                                                                                                                                                                                            |
| [            [this].Add([new] [EmployeeList]() { EmployeeID = 1002, Name = [\"Jerry\"], Mailid = [\"Jerry@syncfusion.com\"] });]     |
|                                                                                                                                                                                                                                                                                            |
| [            [this].Add([new] [EmployeeList]() { EmployeeID = 1003, Name = [\"Brad\"], Mailid = [\"Brad@syncfusion.com\"] });]       |
|                                                                                                                                                                                                                                                                                            |
| [            [this].Add([new] [EmployeeList]() { EmployeeID = 1004, Name = [\"lanze\"], Mailid = [\"lanze@syncfusion.com\"] });]     |
|                                                                                                                                                                                                                                                                                            |
| [            [this].Add([new] [EmployeeList]() { EmployeeID = 1005, Name = [\"Chambel\"], Mailid = [\"Chambel@syncfusion.com\"] });] |
|                                                                                                                                                                                                                                                                                            |
| [            [this].Add([new] [EmployeeList]() { EmployeeID = 1006, Name = [\"Crimson\"], Mailid = [\"Crimson@syncfusion.com\"] });] |
|                                                                                                                                                                                                                                                                                            |
| [    }]                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                            |
| [}][]                                                                                                                                                                                                 |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

{border="0"}

Figure 25: AutoComplete Bound with Data Source

 

Tables for properties, and events

Properties

Table 5: Property Table for Data Binding


  -------------- ---------------------------------------------------- -------------------- ------------------------------- -----------------
  Property       Description                                          Type                 Data Type                       Reference links
  CustomSource   Gets or sets the CustomSource of the AutoComplete.   DependencyProperty   Sytem.Collections.IEnumerable   
  -------------- ---------------------------------------------------- -------------------- ------------------------------- -----------------


 

Events

Table 6: Events Table for Data Binding


+--------------------------+--------------------------------------------------------------------------------------+------------------------------------+-----------------------------------+-----------------+
| Event                    | Description                                                                          | Arguments                          | Type                              | Reference links |
+--------------------------+--------------------------------------------------------------------------------------+------------------------------------+-----------------------------------+-----------------+
| SelectedValuePathChanged |  When the SelectedValuePath property value is changed, this event will be triggered. | DependencyObject,                  | DependencyPropertyChangedCallBack |                 |
|                          |                                                                                      |                                    |                                   |                 |
|                          | It cannot be cancelled.                                                              | DependencyPropertyChangedEventArgs |                                   |                 |
+--------------------------+--------------------------------------------------------------------------------------+------------------------------------+-----------------------------------+-----------------+
| CustomSourceChanged      |  When the CustomSource property value is changed, this event will be triggered.      | DependencyObject,                  | DependencyPropertyChangedCallBack |                 |
|                          |                                                                                      |                                    |                                   |                 |
|                          | It cannot be cancelled.                                                              | DependencyPropertyChangedEventArgs |                                   |                 |
+==========================+======================================================================================+====================================+===================================+=================+


**[]** 

Sample Link

WPF Sample Browser-\> Tools -\> Editors -\> AutoComplete Demo

 

[]{#related-topics}

