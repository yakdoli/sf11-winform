---
title: throughcode5.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\throughcode5.md
created_at: 2025-07-03
---






##### Through Code {#through-code style="tab-stops: 0pt"}

[] 

This tutorial shows how to create Calendar control entirely with code.

 

To create Calendar control in ASP.NET code:

[] 

1.   Open ASP.NET Web application.

2.   In code view, add following subroutines to handle the page load event.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                             |
| [using][ System;]                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                             |
| [// add **using** deractive to have quality the use type of Syncfusion Calendar]                                                                                                                                          |
|                                                                                                                                                                                                                                                                                             |
| [using][ Syncfusion.Web.UI.WebControls.Shared;]                                                                                                                        |
|                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                             |
| [public][ [partial] [class] [CreatingCalendar_ThroughCode] : System.Web.UI.[Page]] |
|                                                                                                                                                                                                                                                                                             |
| [{]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                             |
| [       [protected] [void] Page_Load([object] sender, [EventArgs] e)]                                                                               |
|                                                                                                                                                                                                                                                                                             |
| [       {]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                             |
| [              BuildCalendarControl();]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                             |
| [       }]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                             |
| [       [private] [void] BuildCalendarControl()]                                                                                                                                              |
|                                                                                                                                                                                                                                                                                             |
| [       {]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                             |
| [              [Calendar] calendar = [new] [Calendar]();]                                                                                                                |
|                                                                                                                                                                                                                                                                                             |
| [              ]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                             |
| [              [//Set some Calendar\'s property programarically]]                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                             |
| [              calendar.ID = [\"Calendar1\"];]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                             |
| [              calendar.SelectedDate = [new] [DateTime]( 2007, 2, 2 );]                                                                                                                       |
|                                                                                                                                                                                                                                                                                             |
| [              calendar.VisibleMonth = [new] [DateTime]( 2007, 1, 1 );]                                                                                                                       |
|                                                                                                                                                                                                                                                                                             |
| [              calendar.HorizontalMonthsCount = 2;]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                             |
| [              calendar.Culture = [new] System.Globalization.[CultureInfo]( [\"en-US\"] );]                                                                            |
|                                                                                                                                                                                                                                                                                             |
| [              ]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                             |
| [              [//add Calendar control to Form]]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                             |
| [              form1.Controls.Add( calendar );]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                             |
| [       }]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 117

[]{#related-topics}

