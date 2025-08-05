---
title: vs2010codeduitesting.md
original_path: WinForms_Docs/99_Uncategorized/vs2010codeduitesting.md
created_at: 2025-08-05
---






#### VS 2010 Coded UI Testing {#vs-2010-coded-ui-testing style="tab-stops: 0pt"}

Essential Grid WPF now supports automated UI testing with VS 2010 Coded UI technology. The Grid Test plugin blends in with the automated UI Testing framework in VS 2010 by implementing the following classes:

 

[·      ]UITechnologyManager

[·      ]UITestPropertyProvider

[·      ]UIActionFilter

[] 

The architectural diagram is as follows:

{border="0"}

Figure 115: Architectural Diagram

[] 

[·      ]Grid Test Plugin implements the necessary details to communicate with the VS 2010 Test Framework.

[·      ]The Grid application host runs with a .NET Remoting channel hosted internally to communicate with the Test plugin through an interface. The data is then channeled across to the VS 2010 Test Framework to identify the Cells.

 

Properties

Following are the properties exposed in Coded UI Testing:

**[]** 

[·      ]CellValue

[·      ]Text

[·      ]Description

[·      ]SelectedRanges

[·      ]Background

[·      ]Foreground

[·      ]Borders

[·      ]Format

[·      ]FormulaTag

 

Creating a Coded UI Test With Essential Grid WPF

Initial steps before creating the Coded UI Test project:

 

[·      ]Prepare the Grid sample application.

[·      ]Write Unit tests using VS 2010.

[·      ]Testing the application with generated Coded UI Tests.

 

Preparing the Grid application

 

1.   Syncfusion.VisualStudio.TestTools.UITest.GridExtensions.dll contains implementation to easily change an existing application to the test application that the plugin would require. Add a reference to this assembly.

2.   Open App.xaml.

 


[{border="0"}]Note: The following code appears.


+---------------------------------------------------------------------------------------------------------------+
| [\[XAML\]]                                                                |
|                                                                                                               |
| [\<Application x:Class=\"WpfApplication3.App\"]                           |
|                                                                                                               |
| [    xmlns=\"http://schemas.microsoft.com/winfx/2006/xaml/presentation\"] |
|                                                                                                               |
| [    xmlns:x=\"http://schemas.microsoft.com/winfx/2006/xaml\"]            |
|                                                                                                               |
| [    StartupUri=\"Window1.xaml\"\>]                                       |
|                                                                                                               |
| [    \<Application.Resources\>]                                           |
|                                                                                                               |
| [         ]                                                               |
|                                                                                                               |
| [    \</Application.Resources\>]                                          |
|                                                                                                               |
| [\</Application\>]                                                        |
+---------------------------------------------------------------------------------------------------------------+

[] 

3.   Change Application to Syncfusion:GridControlTestApplication as follows.

 

+------------------------------------------------------------------------------------------------------------------------+
| [\[XAML\]]                                                                |
|                                                                                                                        |
| [\<syncfusion:GridControlTestApplication x:Class=\"WpfApplication3.App\"] |
|                                                                                                                        |
| [    xmlns=\"http://schemas.microsoft.com/winfx/2006/xaml/presentation\"] |
|                                                                                                                        |
| [    xmlns:syncfusion=\"http://schemas.syncfusion.com/wpf\"]              |
|                                                                                                                        |
| [    xmlns:x=\"http://schemas.microsoft.com/winfx/2006/xaml\"]            |
|                                                                                                                        |
| [    StartupUri=\"Window1.xaml\"\>]                                       |
|                                                                                                                        |
| [    \<syncfusion:GridControlTestApplication.Resources\>]                 |
|                                                                                                                        |
| []                                                                        |
|                                                                                                                        |
| [    \</syncfusion:GridControlTestApplication.Resources\>]                |
|                                                                                                                        |
| [\</syncfusion:GridControlTestApplication\>]                              |
+------------------------------------------------------------------------------------------------------------------------+

[] 

4.   For the code behind file (App.xaml.cs), make sure to inherit from GridControlTestApplication.

**[]** 

+-------------------------------------------------------------------------------------------------+
| [namespace WpfApplication3]                                 |
|                                                                                                 |
| [{]                                                         |
|                                                                                                 |
| [    /// \<summary\>]                                       |
|                                                                                                 |
| [    /// Interaction logic for App.xaml]                    |
|                                                                                                 |
| [    /// \</summary\>]                                      |
|                                                                                                 |
| [    public partial class App : GridControlTestApplication] |
|                                                                                                 |
| [    {]                                                     |
|                                                                                                 |
| [    }]                                                     |
|                                                                                                 |
| [}]                                                         |
+-------------------------------------------------------------------------------------------------+

[] 

5.   Build the application to make it ready for testing.

 


[{border="0"}]Note: The GridControlTestApplication works only with a single Grid instance in the window. For multiple instances the IGridInteropService interface has to be implemented.


 

Creating Unit Tests with VS2010

**[]** 

1.   Create a new Test Project in VS2010,

{border="0"}

Figure 116: New Project

**[]** 

***[]*** 

2.   Add a new Coded UI Test item for the project.

 

{border="0"}

 Figure 117: Add Coded UI Test

 

 

3.   Add a TestMethod called HelloWorld_Test.

[] 

The following code illustrates this.

 

+-----------------------------------------------------------------------------+
| [      \[TestMethod\]]                  |
|                                                                             |
| [        public void HelloWorld_Test()] |
|                                                                             |
| [        {]                             |
|                                                                             |
| []                                      |
|                                                                             |
| [        }]                             |
+-----------------------------------------------------------------------------+

[] 

4.   Build and run the Grid application that you configured.

[·      ]Right-click on the TestMethod body and then select as below,

{border="0"}

Figure 118: Generate Code

***[]*** 

***[]*** 

5.   Click on the record button to perform actions, you can add a Hello World text in a grid cell \[x, y\] in this scenario.

[] 

{border="0"}

Figure 119: UI Recorder

***[]*** 

[] 

{border="0"}

Figure 120: Hello World Text In a Cell

***[]*** 

[] 

6.   Click on Generate code in the Coded UI Test Builder.

{border="0"}

Figure 121: Add And Generate

[] 

7.   You can assert the cell value using the cross-hair present in the Coded UI Test builder.

8.   Click on the cross-hair and hover to the Hello World cell.


{border="0"}Note:  The assert window is displayed as below.


[] 

[] 

{border="0"}

Figure 122: Assert Window

***[]*** 

9.   Add asserts to the properties displayed in the assert window and generate the assert method.

10.  Close the Coded UI Test builder.

*[]* 


Note: Coded UI Unit Test is created.


The following code generates automatically.

[] 

+-------------------------------------------------------------------------------------------+
| [\[TestMethod\]]                             |
|                                                                                           |
| [        public void HelloWorld_Test()]      |
|                                                                                           |
| [        {]                                  |
|                                                                                           |
| [            this.UIMap.HelloWorldMethod();] |
|                                                                                           |
| [            this.UIMap.HelloWorldAssert();] |
|                                                                                           |
| [        }]                                  |
+-------------------------------------------------------------------------------------------+

**[]** 

Testing the Application with Generated Coded UI Test

1.   Build and run the Grid WPF application.

2.   Build the test project and run the Unit tests using VS 2010.

[] 

{border="0"}

Figure 123: Test List

 

3.   Run the test HelloWorld_Test.

[o  ]This will automatically focus the running Grid application and perform automated testing.


 

[{border="0"}]Note: The sample test procedure mentioned above requires the sample to be run individually, in normal automated testing, this would be included in the TestInitialize method to start the application.


**[]** 

{border="0"}\
Figure 124: *Test Result*

**** 

**** 

[]{#related-topics}

