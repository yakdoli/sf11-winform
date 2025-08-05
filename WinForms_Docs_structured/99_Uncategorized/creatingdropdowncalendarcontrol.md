---
title: creatingdropdowncalendarcontrol.md
original_path: WinForms_Docs/99_Uncategorized/creatingdropdowncalendarcontrol.md
created_at: 2025-08-05
---






##### Creating DropDownCalendarControl {#creating-dropdowncalendarcontrol style="tab-stops: 0pt"}

 

The DropDownCalendarControl can be created at design time and can be created programmatically, which has been discussed in the following topics.

 

###### 5.1.2.3.1.1 Through Designer {#through-designer style="tab-stops: 0pt"}

[] 

You can create the DropDownCalendarControl using the designer as follows.

[] 

1.   Create a new ASP.NET Web application. For details, see [Creating ASP.NET Web Application]{.UGHyperlink}.

2.   Drag the **DropDownCalendar**Control onto your page from the controls toolbox.

3.      

[] 

{border="0"}

[] 

Figure 52: DropDownCalendarControl in Toolbox

[] 

4.   Customize the look and feel settings and the behavior and culture settings of the control as required. For details, see [Concepts and Features]{.UGHyperlink}.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\<][ssw][:][DropDownCalendarControl][ [ID][=\"DropDownCalendarControl1\"] [runat][=\"server\"\>\</][ssw][:][DropDownCalendarControl][\>]] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The figure below shows DropDownCalendarControl in design view.

[] 

{border="0"}

[] 

Figure 53: DropdownCalendarControl created Through Designer

 

###### 5.1.2.3.1.2 Through Code {#through-code style="tab-stops: 0pt"}

[] 

This tutorial shows how to create DropdownCalendarControl entirely with code.

To create DropDownCalendarControl in ASP.NET code, follow the below given steps.

[] 

1.   Add a new Web Form to your project.

2.   In .cs file, include the following directives.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                    |
|                                                                                                                                                                     |
| **[]**                                                                                                          |
|                                                                                                                                                                     |
| [using][ Syncfusion.Web.UI.WebControls.Tools;] |
|                                                                                                                                                                     |
| [using][ Syncfusion.Web.UI;]                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                     |
|                                                                                                                                                                      |
| **[]**                                                                                                           |
|                                                                                                                                                                      |
| [Imports][ Syncfusion.Web.UI.WebControls.Tools] |
|                                                                                                                                                                      |
| [Imports][ Syncfusion.Web.UI]                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   In code view, the control has to instantiated and added as follows.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                   |
|                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                         |
|                                                                                                                                                                                                                                  |
| [private][ Syncfusion.Web.UI.WebControls.Tools.DropDownCalendarControl dropdowncalendarctrl1;]              |
|                                                                                                                                                                                                                                  |
| [private][ [void] Page_Init([object] sender, System.EventArgs e)] |
|                                                                                                                                                                                                                                  |
| [{]                                                                                                                                                                          |
|                                                                                                                                                                                                                                  |
| [     BuildDropdownCalendarControl();]                                                                                                                                       |
|                                                                                                                                                                                                                                  |
| [}]                                                                                                                                                                          |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                                  |
| [public void][ BuildDropdownCalendarControl()]                                                              |
|                                                                                                                                                                                                                                  |
| [{]                                                                                                                                                                          |
|                                                                                                                                                                                                                                  |
| [     //Create an instance of DropDownCalendarControl]                                                                                                         |
|                                                                                                                                                                                                                                  |
| [     dropdowncalendarctrl1 = [new] DropDownCalendarControl();]                                                                                         |
|                                                                                                                                                                                                                                  |
| [     // Indicates ID of the Control]                                                                                                                          |
|                                                                                                                                                                                                                                  |
| [     dropdowncalendarctrl1.ID = \"DropDownCalendarControl1\";]                                                                                                              |
|                                                                                                                                                                                                                                  |
| [     [form1].Controls.Add(dropdowncalendarctrl1);]                                                                                                     |
|                                                                                                                                                                                                                                  |
| [}]                                                                                                                                                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **[]**                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Private][ dropdowncalendarctrl1 [As] Syncfusion.Web.UI.WebControls.Tools.DropDownCalendarControl]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Private][ [Sub] Page_Init([ByVal] sender [As] [Object], [ByVal] e [As] System.EventArgs) [Handles] [MyBase].Load] |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [     BuildDropdownCalendarControl()]                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [End][ [Sub]]                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Public][ [Sub] BuildDropdownCalendarControl()]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [         [               ]]                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [     \'Create an instance of DropDownCalendarControl]                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [     dropdowncalendarctrl1 = [new] DropDownCalendarControl()]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [     \'Indicates ID of the Control]                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [     dropdowncalendarctrl1.ID = \"DropDownCalendarControl1\"]                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [     form1.Controls.Add(dropdowncalendarctrl1)]                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [                        ]                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [End][ [Sub]]                                                                                                                                                                                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Build the project and view the **DropDownCalendarControl** in the browser.

 

[]{#related-topics}

