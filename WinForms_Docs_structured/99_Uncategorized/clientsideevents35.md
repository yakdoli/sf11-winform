---
title: clientsideevents35.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\clientsideevents35.md
created_at: 2025-07-03
---






#### Client-Side Events {#client-side-events style="tab-stops: 0pt"}

The percent text box control supports client-side event handling.

**[]** 

Events

 

  ----------------------- --------------------------------------------------------------------------- ----------- ----------------
  Name                    Description                                                                 Arguments   Reference Link
  ClientSideFocusIn       This event is raised when the percent text box gains focus.                 inst,args   \-
  ClientSideFocusOut      This event is raised when the percent text box loses focus.                 inst,args   \-
  ClientSideMouseOut      This event is raised when the mouse pointer leaves the percent text box.    inst,args   \-
  ClientSideMouseOver     This event is raised when the mouse pointer enters the percent text box.    inst,args   \-
  ClientSideValueChange   This event is raised when the value of the percent text box  changes.       inst,args   \-
  ----------------------- --------------------------------------------------------------------------- ----------- ----------------

*[[]]{.underline}* 

Using Builder

The following steps explain the handling of client-side events through Builder.

1.   In **View**, invoke the percent text box helper followed by the **ClientSideFocusIn, ClientSideFocusOut, ClientSideMouseOver, ClientSideMouseOut,** and **ClientSideValueChange** methods with the desired handlers as arguments.[]

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                          |
| [\<%][=][Html.Syncfusion().PercentTextBox([\"myNumeric1\"])] |
|                                                                                                                                                                                                                                                                          |
| [              **.ClientSideFocusIn([\"OnFocusIn\"])**]                                                                                                                                         |
|                                                                                                                                                                                                                                                                          |
| **[              .ClientSideFocusOut([\"OnFocusOut\"])]**                                                                                                                                       |
|                                                                                                                                                                                                                                                                          |
| **[             .ClientSideMouseOver([\"OnMouseOver\"])]**                                                                                                                                      |
|                                                                                                                                                                                                                                                                          |
| **[              .ClientSideMouseOut([\"OnMouseOut\"])]**                                                                                                                                       |
|                                                                                                                                                                                                                                                                          |
| **[              .ClientSideValueChange([\"OnValueChange\"])]**[%\>]                                                       |
|                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [@(][new][ [HtmlString](][Html.Syncfusion().PercentTextBox([\"myNumeric1\"])] |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [              **.ClientSideFocusIn([\"OnFocusIn\"])**]                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                    |
| **[              .ClientSideFocusOut([\"OnFocusOut\"])]**                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                    |
| **[             .ClientSideMouseOver([\"OnMouseOver\"])]**                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                    |
| **[              .ClientSideMouseOut([\"OnMouseOut\"])]**                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                    |
| **[              .ClientSideValueChange([\"OnValueChange\"])]**[.ToString())[)]]                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   In JavaScript, define the handlers.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[JavaScript\]]**                                                                                                                                                                       |
|                                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                                     |
|                                                                                                                                                                                                                                |
| [\<][script][ [type][=\"text/javascript\"\>]] |
|                                                                                                                                                                                                                                |
| [        [function] OnFocusIn(inst, args) {]                                                                                                                          |
|                                                                                                                                                                                                                                |
| [            [//inst      - instance of percent text box client-side object]]                                                                                    |
|                                                                                                                                                                                                                                |
| [            [//args:]]                                                                                                                                          |
|                                                                                                                                                                                                                                |
| [            [//  \_value   - current value of the percent text box]]                                                                                            |
|                                                                                                                                                                                                                                |
| [        }]                                                                                                                                                                                |
|                                                                                                                                                                                                                                |
| [        [function] OnFocusOut(inst, args) {]                                                                                                                         |
|                                                                                                                                                                                                                                |
| [            [//inst      - instance of percent text box client-side object]]                                                                                    |
|                                                                                                                                                                                                                                |
| [            [//args:]]                                                                                                                                          |
|                                                                                                                                                                                                                                |
| [            [//  \_value   - current value of the percent text box]]                                                                                            |
|                                                                                                                                                                                                                                |
| [        }]                                                                                                                                                                                |
|                                                                                                                                                                                                                                |
| [        [function] OnMouseOver(inst, args) {]                                                                                                                        |
|                                                                                                                                                                                                                                |
| [            [//inst      - instance of percent text box client-side object]]                                                                                    |
|                                                                                                                                                                                                                                |
| [            [//args:]]                                                                                                                                          |
|                                                                                                                                                                                                                                |
| [            [//  \_value   - current value of the percent text box]]                                                                                            |
|                                                                                                                                                                                                                                |
| [        }]                                                                                                                                                                                |
|                                                                                                                                                                                                                                |
| [        [function] OnMouseOut(inst, args) {]                                                                                                                         |
|                                                                                                                                                                                                                                |
| [            [//inst      - instance of percent text box client-side object]]                                                                                    |
|                                                                                                                                                                                                                                |
| [            [//args:]]                                                                                                                                          |
|                                                                                                                                                                                                                                |
| [            [//  \_value   - current value of the percent text box]]                                                                                            |
|                                                                                                                                                                                                                                |
| [        }]                                                                                                                                                                                |
|                                                                                                                                                                                                                                |
| [        [function] OnValueChange(inst, args) {]                                                                                                                      |
|                                                                                                                                                                                                                                |
| [            [//inst      - instance of percent text box client-side object]]                                                                                    |
|                                                                                                                                                                                                                                |
| [            [//args:]]                                                                                                                                          |
|                                                                                                                                                                                                                                |
| [            [//  \_value   - current value of the percent text box]]                                                                                            |
|                                                                                                                                                                                                                                |
| [        }        ]                                                                                                                                                                        |
|                                                                                                                                                                                                                                |
| [      [\</][script][\>]]                                                                                                 |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

3.   Build and run the application.**

**[]** 

Using Properties Model

The following steps explain how to handle client-side events through the properties model.

1.   In the controller, create an instance of **PercentTextBoxModel**.**

2.   Define the **ClientSideFocusIn**, **ClientSideFocusOut**, **ClientSideMouseOver**, **ClientSideMouseOut**, and **ClientSideValueChange** properties and pass the instance through the **view-specific data** to **View**.**

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                                                              |
|                                                                                                                                                                                       |
| **[]**                                                                                                                                            |
|                                                                                                                                                                                       |
| [public][ [ActionResult] Index()]                                        |
|                                                                                                                                                                                       |
| [        {]                                                                                                                                       |
|                                                                                                                                                                                       |
| [            [//Creating instance of PercentTextBoxModel]]                                                                  |
|                                                                                                                                                                                       |
| [            [PercentTextBoxModel] myModel = [new] [PercentTextBoxModel]();] |
|                                                                                                                                                                                       |
| [            **myModel.ClientSideFocusIn = [\"OnFocusIn\"];**]                                                            |
|                                                                                                                                                                                       |
| **[            myModel.ClientSideFocusOut = [\"OnFocusOut\"];]**                                                          |
|                                                                                                                                                                                       |
| **[            myModel.ClientSideMouseOver = [\"OnMouseOver\"];]**                                                        |
|                                                                                                                                                                                       |
| **[            myModel.ClientSideMouseOut = [\"OnMouseOut\"];]**                                                          |
|                                                                                                                                                                                       |
| **[            myModel.ClientSideValueChange = [\"OnValueChange\"];]**                                                    |
|                                                                                                                                                                                       |
| []                                                                                                                                                |
|                                                                                                                                                                                       |
| [            [//pass the instance through view data to the view]]                                                           |
|                                                                                                                                                                                       |
| [            ViewData\[[\"myPercent\"]\] = myModel;]                                                                      |
|                                                                                                                                                                                       |
| [            [return] View();]                                                                                               |
|                                                                                                                                                                                       |
| [        }]                                                                                                                                       |
|                                                                                                                                                                                       |
| []                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

***[[[]]]{.underline}*** 

3.   In **View**, invoke the percent text box helper with the view data key as the Control ID.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                           |
| [\<%][=][Html.Syncfusion().PercentTextBox([\"myPercent\"]) [%\>]] |
|                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [@(][new][ [HtmlString](][Html.Syncfusion().PercentTextBox([\"myPercent\"])][.ToString())[)]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[4.   ]In JavaScript, define the handlers.[]

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Javascript\]]**                                                                                                                                                                       |
|                                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                                     |
|                                                                                                                                                                                                                                |
| [\<][script][ [type][=\"text/javascript\"\>]] |
|                                                                                                                                                                                                                                |
| [        [function] OnFocusIn(inst, args) {]                                                                                                                          |
|                                                                                                                                                                                                                                |
| [            [//inst      - instance of percent textbox client side object]]                                                                                     |
|                                                                                                                                                                                                                                |
| [            [//args:]]                                                                                                                                          |
|                                                                                                                                                                                                                                |
| [            [//  \_value   - current value of the percent textbox]]                                                                                             |
|                                                                                                                                                                                                                                |
| [        }]                                                                                                                                                                                |
|                                                                                                                                                                                                                                |
| [        [function] OnFocusOut(inst, args) {]                                                                                                                         |
|                                                                                                                                                                                                                                |
| [            [//inst      - instance of percent textbox client side object]]                                                                                     |
|                                                                                                                                                                                                                                |
| [            [//args:]]                                                                                                                                          |
|                                                                                                                                                                                                                                |
| [            [//  \_value   - current value of the percent textbox]]                                                                                             |
|                                                                                                                                                                                                                                |
| [        }]                                                                                                                                                                                |
|                                                                                                                                                                                                                                |
| [        [function] OnMouseOver(inst, args) {]                                                                                                                        |
|                                                                                                                                                                                                                                |
| [            [//inst      - instance of percent textbox client side object]]                                                                                     |
|                                                                                                                                                                                                                                |
| [            [//args:]]                                                                                                                                          |
|                                                                                                                                                                                                                                |
| [            [//  \_value   - current value of the percent textbox]]                                                                                             |
|                                                                                                                                                                                                                                |
| [        }]                                                                                                                                                                                |
|                                                                                                                                                                                                                                |
| [        [function] OnMouseOut(inst, args) {]                                                                                                                         |
|                                                                                                                                                                                                                                |
| [            [//inst      - instance of percent textbox client side object]]                                                                                     |
|                                                                                                                                                                                                                                |
| [            [//args:]]                                                                                                                                          |
|                                                                                                                                                                                                                                |
| [            [//  \_value   - current value of the percent textbox]]                                                                                             |
|                                                                                                                                                                                                                                |
| [        }]                                                                                                                                                                                |
|                                                                                                                                                                                                                                |
| [        [function] OnValueChange(inst, args) {]                                                                                                                      |
|                                                                                                                                                                                                                                |
| [            [//inst      - instance of percent textbox client side object]]                                                                                     |
|                                                                                                                                                                                                                                |
| [            [//args:]]                                                                                                                                          |
|                                                                                                                                                                                                                                |
| [            [//  \_value   - current value of the percent textbox]]                                                                                             |
|                                                                                                                                                                                                                                |
| [        }        ]                                                                                                                                                                        |
|                                                                                                                                                                                                                                |
| [\</][script][\>]                                                         |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

5.   Build and run the application.

You can observe the handlers being invoked when the corresponding events are triggered.

 

[]{#related-topics}

