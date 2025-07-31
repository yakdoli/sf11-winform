---
title: workingwithwizardcontrol.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\workingwithwizardcontrol.md
created_at: 2025-07-03
---






##### Working with Wizard Control {#working-with-wizard-control style="tab-stops: 0pt"}

[] 

This section contains the following topics:[]{#p642}

###### []{#_Next_Page_and}3.50.3.2.4.1        Next Page and Previous Page Navigation {#next-page-and-previous-page-navigation style="tab-stops: 0pt"}

[] 

You can set the navigation to the Next and Previous pages by using the **NextPage** and **PreviousPage** properties respectively. To set these properties, use the below code.

[] 

+---------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                  |
|                                                                                                                                 |
| []                                                            |
|                                                                                                                                 |
| [WizardControl wizardControl = [new] WizardControl();] |
|                                                                                                                                 |
| [grid.Children.Add(wizardControl);]                                         |
|                                                                                                                                 |
| [WizardPage wizardPage1 = [new] WizardPage();]         |
|                                                                                                                                 |
| [WizardPage wizardPage2 = [new] WizardPage();]         |
|                                                                                                                                 |
| [WizardPage wizardPage3 = [new] WizardPage();]         |
|                                                                                                                                 |
| [wizardControl.Foreground = [Brushes].SlateBlue;]   |
|                                                                                                                                 |
| [wizardPage1.Title = [\"Wizard Page1\"];]           |
|                                                                                                                                 |
| [wizardPage2.Title = [\"Wizard Page2\"];]           |
|                                                                                                                                 |
| [wizardPage3.Title = [\"Wizard Page3\"];]           |
|                                                                                                                                 |
| [wizardControl.Items.Add(wizardPage1);]                                     |
|                                                                                                                                 |
| [wizardControl.Items.Add(wizardPage2);]                                     |
|                                                                                                                                 |
| [wizardControl.Items.Add(wizardPage3);]                                     |
|                                                                                                                                 |
| [wizardPage1.NextPage = wizardPage3;]                                       |
|                                                                                                                                 |
| [wizardPage3.PreviousPage = wizardPage1;  ]                                 |
+---------------------------------------------------------------------------------------------------------------------------------+

[] 

See Also

[] 

[]{#p643}[]

###### 3.50.3.2.4.2        Closing the Wizard Window {#closing-the-wizard-window style="tab-stops: 0pt"}

[] 

You can close the Wizard control window by clicking the **Cancel** or **Finish** button by enabling the **CloseWindowOnCancel** or **CloseWindowOnFinish** properties respectively.

 

To enable these properties, refer the below code

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\<][syncfusion][:][WizardControl][ Name][=\"wizardControl\"][ CloseWindowOnCancel][=\"True\"][ CloseWindowOnFinish][=\"True\"\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [    ][\<][syncfusion][:][WizardPage][ Name][=\"wizardPage\"/\>]                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\</][syncfusion][:][WizardControl][\>]                                                                                                                                                                                                                                                                                                                                                                                                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                  |
|                                                                                                                                 |
| []                                                            |
|                                                                                                                                 |
| [WizardControl wizardControl = [new] WizardControl();] |
|                                                                                                                                 |
| [grid.Children.Add(wizardControl);]                                         |
|                                                                                                                                 |
| [WizardPage wizardPage = [new] WizardPage();]          |
|                                                                                                                                 |
| [wizardControl.Items.Add(wizardPage);]                                      |
|                                                                                                                                 |
| [wizardControl.CloseWindowOnCancel = [true];]          |
|                                                                                                                                 |
| [wizardControl.CloseWindowOnFinish = [true]; ]         |
+---------------------------------------------------------------------------------------------------------------------------------+

[]{#p644} 

[]{#related-topics}

