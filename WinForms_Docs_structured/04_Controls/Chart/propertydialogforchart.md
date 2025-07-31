---
title: propertydialogforchart.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\propertydialogforchart.md
created_at: 2025-07-03
---






##### Property Dialog for Chart {#property-dialog-for-chart style="tab-stops: 0pt"}

The property dialog or property window lets you to modify the values of properties of the Chart control at run time. The property dialog helps you to accurately modify the look and feel of the control.

The property dialog has tabbed structure. There are five tabs available by default, namely Chart, ChartArea, ChartSeries, ChartAxis and ChartLegend. You can also add custom tabs to property window, which would help you to access the properties that are not available in these default tabs (For example, you can add custom tab which would modify the Chart Annotation points).

The property window has [[localization support]{.UGHyperlink}](http://help.syncfusion.com/ug_84/User%20Interface/WPF/Chart/default.htm?turl=localizationsupport.htm). The properties and their options can be viewed in local languages just by adding .resx file with local string for corresponding key values in the application.

 


Note: Any changes done in the property window will directly affect the Chart control from Essential studio version 9.1 onwards whereas earlier versions have a preview chart in the property window to view the modifications.


 

Use Case Scenarios

[·      ]When the Chart control is used in an application and deployed, the end user or client can customize the look and feel of the Chart at run time. End user can set their own brushes, headers for Chart, Annotation Labels of Chart and etc. using the Chart property window.

[·      ]If you need to change the Annotation labels of the Chart Control at run time, then you can add a custom tab, in which you can define controls to change the Chart Annotation label's properties. The property window will have this addition tab added to it and hence you can modify the Annotation labels of Chart at run time.

 

Tables for Properties, Methods, and Events

Properties

*[Table ][167][: Property Table]*


  -------------------- ------------------------------------------------------------------------------ --------------------- ------------------- -----------------
  Property             Description                                                                    Type                  Data Type           Reference links
  PropertyWindowTabs   Represents the collection of tabs that are displayed in the property window.   Dependency property   TabItemCollection   NA
  -------------------- ------------------------------------------------------------------------------ --------------------- ------------------- -----------------


[] 

Methods

*[Table ][168][: Method Table]*


+---------------------+------------------------------------+-----------------------------------+-----------+-----------------+---------------------+
| **Method**          | **Description**                    | **Parameters**                    | **Type**  | **Return Type** | **Reference links** |
+---------------------+------------------------------------+-----------------------------------+-----------+-----------------+---------------------+
| ShowPropertyWindow  | Displays the Chart Property window | public void ShowPropertyDialog()  | N/A       | Void            | NA                  |
|                     |                                    |                                   |           |                 |                     |
|                     |                                    |                                   |           |                 |                     |
+---------------------+------------------------------------+-----------------------------------+-----------+-----------------+---------------------+
| ClosePropertyWindow | Hides the Chart Property window    | public void ClosePropertyDialog() | N/A       | Void            | NA                  |
|                     |                                    |                                   |           |                 |                     |
|                     |                                    |                                   |           |                 |                     |
+=====================+====================================+===================================+===========+=================+=====================+


[] 

Events

*[Table ][169][: Events Table]*


+----------------------------+--------------------------------------------------------------------+---------------------------------------------------+--------------+---------------------+
| **Event**                  | **Description**                                                    | **Arguments**                                     | **Type**     | **Reference links** |
+----------------------------+--------------------------------------------------------------------+---------------------------------------------------+--------------+---------------------+
| ChartPropertyWindowOpening | The property is triggered before the property window is displayed. | ChartPropertyWindowCancelEventArgs e.             | Routed Event |                     |
|                            |                                                                    |                                                   |              |                     |
|                            | This event is cancellable.                                         | e.PropertyWindow gives the entire property window |              |                     |
+----------------------------+--------------------------------------------------------------------+---------------------------------------------------+--------------+---------------------+
| ChartPropertyWindowOpened  | The property is triggered after the property window is displayed.  | ChartPropertyWindowCancelEventArgs e.             | Routed Event |                     |
|                            |                                                                    |                                                   |              |                     |
|                            |                                                                    | e.PropertyWindow gives the entire property window |              |                     |
|                            |                                                                    |                                                   |              |                     |
|                            |                                                                    |                                                   |              |                     |
|                            |                                                                    |                                                   |              |                     |
|                            |                                                                    |                                                   |              |                     |
+----------------------------+--------------------------------------------------------------------+---------------------------------------------------+--------------+---------------------+
| ChartPropertyWindowClosing | The property is triggered before the property window is displayed. | ChartPropertyWindowCancelEventArgs e.             | Routed Event |                     |
|                            |                                                                    |                                                   |              |                     |
|                            | This event is cancellable.                                         | e.PropertyWindow gives the entire property window |              |                     |
|                            |                                                                    |                                                   |              |                     |
|                            |                                                                    |                                                   |              |                     |
+----------------------------+--------------------------------------------------------------------+---------------------------------------------------+--------------+---------------------+
| ChartPropertyWindowClosed  | The property is triggered before the property window is displayed. | ChartPropertyWindowCancelEventArgs e.             | Routed Event |                     |
|                            |                                                                    |                                                   |              |                     |
|                            |                                                                    | e.PropertyWindow gives the entire property window |              |                     |
|                            |                                                                    |                                                   |              |                     |
|                            |                                                                    |                                                   |              |                     |
+============================+====================================================================+===================================================+==============+=====================+


[][] 

Sample Link

To run the UI WPF sample:

1.   Open Essential Studio Dashboard by selecting Start -\> Program -\> Syncfusion-\> Essential Studio \<\<Version Number\>\> -\> Dashboard.[]

2.   Select Run locally installed samples, from the WPF drop-down list on the User Interface pane.[]

3.   Select Chart in the sample browser.[]

4.   Select User Interaction -\> Property Dialog Demo on the Essential Chart pane and click the Run Sample button.[]

 

To open the sample project:

Go to the following sample location in your system: 

***"\<sample installation location\>\\Syncfusion\\EssentialStudio\\Version Number \\WPF\\Chart.WPF\\Samples\\3.5\\WindowsSamples\\User Interaction\\Property Dialog Demo"***

This location contains two sub folders CS and VB.  You can open the sample projects from the respective folders based on your application developing language.

            []

Adding Property Dialog to an Application

There are two ways to invoke the Property dialog. They are, using **Toolbar** and **ShowPropertyDialog**. The following section will brief these two options.

[] 

Opening Property Dialog through code

[] 

+-------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                              |
|                                                                                                                               |
| []                                                                           |
|                                                                                                                               |
| [Chart1.ShowPropertyDialog();]**[]** |
|                                                                                                                               |
|                                                                                                                               |
+-------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

Figure 253: Chart Property Dialog

Using Toolbar

 

By clicking the Properties Tool Item in the Toolbar, the property settings dialog can be invoked.

 

{border="0"}

Figure 254: Chart Property Dialog opened through Toolbar

 

Adding custom tabs to property window of Chart

You can include a custom tab to the property window in your application easily by adding a tab to the **PropertyWindowTabs** property. The below code snippet will explain adding custom tab to the property window through XAML and in C#.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\<][syncfusion][:][Chart][ Margin][=\"20\"][ Grid.Row][=\"1\"][ Grid.Column][=\"0\"][ Name][=\"Chart1\"\>][] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [            ][\<][syncfusion][:][Chart.PropertyWindowTabs][\>][]                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [                ][\<][TabItem][ Header][=\"AnnotationLabels\"\>][]                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [                    ][\<][TabItem.Content][\>][]                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [                    ][\</][TabItem.Content][\>][]                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [                ][\</][TabItem][\>][]                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [            ][\</][syncfusion][:][Chart.PropertyWindowTabs][\>][]                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\</][syncfusion][:][Chart][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                |
|                                                                                                                                                                                 |
| [TabItem][ CustomTab = [new] [TabItem]();] |
|                                                                                                                                                                                 |
| [Chart1.PropertyWindowTabs.Add(CustomTab);]                                                                                                 |
|                                                                                                                                                                                 |
|                                                                                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Listen to opening and closing of the property window

You can listen to opening of the property window by adding a delegate method to the event ChartPropertyWindowOpening. Similarly, you can listen to opening of the property window by adding a delegate method to the event ChartPropertyWindowClosing.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                          |
|                                                                                                                                                                                                           |
| [Chart1.ChartPropertyWindowOpening += [new] [ChartPropertyWindowCancelEventHandler](Chart1_ChartPropertyWindowOpening);] |
|                                                                                                                                                                                                           |
| []                                                                                                                                                                    |
|                                                                                                                                                                                                           |
| [Chart1.ChartPropertyWindowClosing += [new] [ChartPropertyWindowCancelEventHandler](Chart1_ChartPropertyWindowClosing);] |
|                                                                                                                                                                                                           |
|                                                                                                                                                                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\<][syncfusion][:][Chart][ Margin][=\"20\"][ Grid.Row][=\"1\"][ Grid.Column][=\"0\"][ Name][=\"Chart1\"][ ChartPropertyWindowOpening][=\"Chart1_ChartPropertyWindowOpening\"][ ChartPropertyWindowClosing][=\"Chart1_ChartPropertyWindowClosing\" /\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#related-topics}

