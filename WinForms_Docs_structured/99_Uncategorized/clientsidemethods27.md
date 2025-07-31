---
title: clientsidemethods27.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\clientsidemethods27.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



#### Client Side Methods {#client-side-methods style="tab-stops: 0pt"}

The Percent text box control supports a rich set of client-side methods to control its behavior.

[] 

Methods

  ---------- -------------------------------------------------- ------------- ---------------------------------------------------------
  Name       Parameters                                         Return type   Description
  getValue   NA                                                 String        Returns the current value of the text box as string
  setValue   Value(the value to be displayed in the text box)   NA            Sets the value of the text box with the specified value
  ---------- -------------------------------------------------- ------------- ---------------------------------------------------------

 

The following steps guide you in using client side methods.

1.   In **View**, invoke the Percent text box helper with control ID as the first argument.

**[]**  

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                       |
|                                                                                                                                                                                          |
| [  ] [\<%] [{                                ]           |
|                                                                                                                                                                                          |
| [    Html.MobSyncfusion().PercentTextbox([\"myPercent\")]]                                                                   |
|                                                                                                                                                                                          |
| [                          .Render();]                                                                                                               |
|                                                                                                                                                                                          |
| [       }[%\>]]                                                                                                          |
|                                                                                                                                                                                          |
| **[\[Razor\]]**                                                                                                                                      |
|                                                                                                                                                                                          |
| [    ] [\@{] []                                          |
|                                                                                                                                                                                          |
| [           Html.MobSyncfusion().PercentTextbox([\"myPercent\"])]                                                            |
|                                                                                                                                                                                          |
| [                          .Render();       [}]] [] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.     In JavaScript, use the methods as they are given in the following code:

**[]**  

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Javascript\]]**                                                                                                                                                                           |
|                                                                                                                                                                                                                                    |
| [\<] [script] [ [type] [=\"text/javascript\"\>] ] |
|                                                                                                                                                                                                                                    |
| [        [function] Value() {]                                                                                                                                            |
|                                                                                                                                                                                                                                    |
| [            [var] perObj = \$find([\"][myPercent][\"]);]                                           |
|                                                                                                                                                                                                                                    |
| [            [var] currentValue = perObj.getValue();]                                                                                                                     |
|                                                                                                                                                                                                                                    |
| [           perObj.setValue(100);]                                                                                                                                                             |
|                                                                                                                                                                                                                                    |
| [        }    ]                                                                                                                                                                                |
|                                                                                                                                                                                                                                    |
| [       [\</][script][\>]]                                                                                                    |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Build and run the application.

 

[]{#related-topics}

