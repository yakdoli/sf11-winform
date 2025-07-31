---
title: creatinganapplicationwithoffice2010uiappearance1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\creatinganapplicationwithoffice2010uiappearance1.md
created_at: 2025-07-03
---






##### Creating an Application with Office 2010 UI Appearance {#creating-an-application-with-office-2010-ui-appearance style="tab-stops: 0pt"}

Users can create the appearance of the Office 2010 UI in WPF applications by applying Office 2010 UI themes to the Ribbon control. The Office 2010 UI in the Ribbon control supports the following themes:

[·      ]Office2010Black

[·      ]Office2010Blue

[·      ]Office2010Silver

The Office 2010 UI themes can be applied to the Ribbon control, as shown in the following code snippets.[]

**** 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]   ]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **[     ]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [    ][\<][syncfusion][:][Ribbon][ shared][:][SkinManager.VisualStyle][=\"Office2010Black\" ] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [                                                      ][Name][=\"MyRibbon\"\>][           ][]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [            ][\<][syncfusion][:][RibbonTab][ Caption][=\"Tab1\"\>][]                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [                ][\<][syncfusion][:][RibbonBar][ Header][=\"Ribbon Bar1\"/\>][]                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [                ][\<][syncfusion][:][RibbonBar][ Header][=\"Ribbon Bar1\"/\>][]                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [                ][\<][syncfusion][:][RibbonBar][ Header][=\"Ribbon Bar1\"/\>][]                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [            ][\</][syncfusion][:][RibbonTab][\>][]                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [     ][\</][syncfusion][:][Ribbon][\>]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

***[]*** 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]   ]**                                                                                                                                                                          |
|                                                                                                                                                                                                                              |
| **[     ]**                                                                                                                                                                              |
|                                                                                                                                                                                                                              |
| [public][ [void] RibbonWindow_Loaded([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                              |
| [   {]                                                                                                                                                                                   |
|                                                                                                                                                                                                                              |
| [    [SkinManager].SetVisualStyle([this].MyRibbon, [VisualStyle].Office2010Black);]                                 |
|                                                                                                                                                                                                                              |
| [   }]                                                                                                                                                                                   |
|                                                                                                                                                                                                                              |
| []                                                                                                                                                                                       |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

