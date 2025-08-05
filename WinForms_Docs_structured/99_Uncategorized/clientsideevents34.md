---
title: clientsideevents34.md
original_path: WinForms_Docs/99_Uncategorized/clientsideevents34.md
created_at: 2025-08-05
---






#### Client-Side Events {#client-side-events style="tab-stops: 0pt"}

 

The numeric text box control supports client-side event handling.

 

Events

+-----------------------+---------------------------------------------------------------------------+-----------------+-----------------+
| Name                  | Description                                                               | Arguments       | Reference Link  |
+-----------------------+---------------------------------------------------------------------------+-----------------+-----------------+
| ClientSideFocusIn     | This event is raised when the numeric text box gains focus.               | inst,args       | \-              |
|                       |                                                                           |                 |                 |
|                       |                                                                           |                 |                 |
+-----------------------+---------------------------------------------------------------------------+-----------------+-----------------+
| ClientSideFocusOut    | This event is raised when the numeric text box loses focus.               | inst,args       | \-              |
|                       |                                                                           |                 |                 |
|                       |                                                                           |                 |                 |
+-----------------------+---------------------------------------------------------------------------+-----------------+-----------------+
| ClientSideMouseOut    | This event is raised when the mouse pointer leaves the numeric text box.  | inst,args       | \-              |
|                       |                                                                           |                 |                 |
|                       |                                                                           |                 |                 |
+-----------------------+---------------------------------------------------------------------------+-----------------+-----------------+
| ClientSideMouseOver   | This event is raised when the mouse pointer enters the numeric text box.  | inst,args       | \-              |
|                       |                                                                           |                 |                 |
|                       |                                                                           |                 |                 |
+-----------------------+---------------------------------------------------------------------------+-----------------+-----------------+
| ClientSideValueChange | This event is raised when the value of the numeric text box changes.      | inst,args       | \-              |
+-----------------------+---------------------------------------------------------------------------+-----------------+-----------------+

*[[]]{.underline}* 

Using Builder[]

The following steps explain how to handle client-side events through the builder.

1.   In **View**, invoke the numeric text box helper followed by the **ClientSideFocusIn**, **ClientSideFocusOut**, **ClientSideMouseOver**, **ClientSideMouseOut**, and **ClientSideValueChange** methods with the desired handlers as arguments.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                          |
| [\<%][=][Html.Syncfusion().NumericTextBox([\"myNumeric1\"])] |
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
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [@(][new][ [HtmlString](][Html.Syncfusion().NumericTextBox([\"myNumeric1\"])] |
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

[2.   ]In JavaScript, define the handlers.[]

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[JavaScript\]**                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                       |
| [\<][script][ [type][=\"text/javascript\"\>]] |
|                                                                                                                                                                                                                                                                       |
| [        [function] OnFocusIn(inst, args) {]                                                                                                                                                    |
|                                                                                                                                                                                                                                                                       |
| [            [//inst      - instance of numeric text box client-side object]]                                                                                                              |
|                                                                                                                                                                                                                                                                       |
| [            [//args:]]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                       |
| [            [//  \_value   - current value of the numeric text box]]                                                                                                                      |
|                                                                                                                                                                                                                                                                       |
| [        }]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                       |
| [        [function] OnFocusOut(inst, args) {]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                       |
| [            [//inst      - instance of numeric text box client-side object]]                                                                                                              |
|                                                                                                                                                                                                                                                                       |
| [            [//args:]]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                       |
| [            [//  \_value   - current value of the numeric text box]]                                                                                                                      |
|                                                                                                                                                                                                                                                                       |
| [        }]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                       |
| [        [function] OnMouseOver(inst, args) {]                                                                                                                                                  |
|                                                                                                                                                                                                                                                                       |
| [            [//inst      - instance of numeric text box client-side object]]                                                                                                              |
|                                                                                                                                                                                                                                                                       |
| [            [//args:]]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                       |
| [            [//  \_value   - current value of the numeric text box]]                                                                                                                      |
|                                                                                                                                                                                                                                                                       |
| [        }]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                       |
| [        [function] OnMouseOut(inst, args) {]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                       |
| [            [//inst      - instance of numeric text box client-side object]]                                                                                                              |
|                                                                                                                                                                                                                                                                       |
| [            [//args:]]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                       |
| [            [//  \_value   - current value of the numeric text box]]                                                                                                                      |
|                                                                                                                                                                                                                                                                       |
| [        }]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                       |
| [        [function] OnValueChange(inst, args) {]                                                                                                                                                |
|                                                                                                                                                                                                                                                                       |
| [            [//inst      - instance of numeric text box client-side object]]                                                                                                              |
|                                                                                                                                                                                                                                                                       |
| [            [//args:]]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                       |
| [            [//  \_value   - current value of the numeric text box]]                                                                                                                      |
|                                                                                                                                                                                                                                                                       |
| [        }        ]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                       |
| [       [\</][script][\>]]                                                                                                                          |
|                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                      |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Build and run the application.

**[]** 

Using Properties Model

The following steps explain how to handle client-side events through the properties model.

1.   In the **controller**, create an instance of **NumericTextBoxModel**; define the **ClientSideFocusIn, ClientSideFocusOut, ClientSideMouseOver, ClientSideMouseOut,** and **ClientSideValueChange** properties and pass the instance through the view-specific data to the view.**

*[[]]{.underline}* 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[Controller\]**                                                                                                                                                                                 |
|                                                                                                                                                                                                    |
|                                                                                                                                                                                                    |
|                                                                                                                                                                                                    |
| [public][ [ActionResult] Index()]                           |
|                                                                                                                                                                                                    |
| [        {]                                                                                                                                       |
|                                                                                                                                                                                                    |
| [            [//Creating instance of NumericTextBoxModel]]                                                                  |
|                                                                                                                                                                                                    |
| [            [NumericTextBoxModel] myModel = [new] [NumericTextBoxModel]();] |
|                                                                                                                                                                                                    |
| [            **myModel.ClientSideFocusIn = [\"OnFocusIn\"];**]                                                            |
|                                                                                                                                                                                                    |
| **[            myModel.ClientSideFocusOut = [\"OnFocusOut\"];]**                                                          |
|                                                                                                                                                                                                    |
| **[            myModel.ClientSideMouseOver = [\"OnMouseOver\"];]**                                                        |
|                                                                                                                                                                                                    |
| **[            myModel.ClientSideMouseOut = [\"OnMouseOut\"];]**                                                          |
|                                                                                                                                                                                                    |
| **[            myModel.ClientSideValueChange = [\"OnValueChange\"];]**                                                    |
|                                                                                                                                                                                                    |
| []                                                                                                                                                |
|                                                                                                                                                                                                    |
| [            [//pass the instance through view data to the view]]                                                           |
|                                                                                                                                                                                                    |
| [            ViewData\[[\"myNumeric\"]\] = myModel;]                                                                      |
|                                                                                                                                                                                                    |
| [            [return] View();]                                                                                               |
|                                                                                                                                                                                                    |
| [        }]                                                                                                                                       |
|                                                                                                                                                                                                    |
| **[[]]{.underline}**                                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[[[]]]{.underline}** 

2.   In **View**, invoke the numeric text box helper with the view data key as the control ID.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                           |
| **\**                                                                                                                                                                                                                                                                                                     |
| [\<%][=][Html.Syncfusion().NumericTextBox([\"myNumeric\"]) [%\>]] |
|                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [@(][new][ [HtmlString](][Html.Syncfusion().NumericTextBox([\"myNumeric\"])][.ToString())[)]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

3.   In JavaScript, define the handlers.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[Javascript\]**                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                       |
| [\<][script][ [type][=\"text/javascript\"\>]] |
|                                                                                                                                                                                                                                                                       |
| [        [function] OnFocusIn(inst, args) {]                                                                                                                                                    |
|                                                                                                                                                                                                                                                                       |
| [            [//inst      - instance of numeric textbox client side object]]                                                                                                               |
|                                                                                                                                                                                                                                                                       |
| [            [//args:]]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                       |
| [            [//  \_value   - current value of the numeric textbox]]                                                                                                                       |
|                                                                                                                                                                                                                                                                       |
| [        }]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                       |
| [        [function] OnFocusOut(inst, args) {]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                       |
| [            [//inst      - instance of numeric textbox client side object]]                                                                                                               |
|                                                                                                                                                                                                                                                                       |
| [            [//args:]]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                       |
| [            [//  \_value   - current value of the numeric textbox]]                                                                                                                       |
|                                                                                                                                                                                                                                                                       |
| [        }]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                       |
| [        [function] OnMouseOver(inst, args) {]                                                                                                                                                  |
|                                                                                                                                                                                                                                                                       |
| [            [//inst      - instance of numeric textbox client side object]]                                                                                                               |
|                                                                                                                                                                                                                                                                       |
| [            [//args:]]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                       |
| [            [//  \_value   - current value of the numeric textbox]]                                                                                                                       |
|                                                                                                                                                                                                                                                                       |
| [        }]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                       |
| [        [function] OnMouseOut(inst, args) {]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                       |
| [            [//inst      - instance of numeric textbox client side object]]                                                                                                               |
|                                                                                                                                                                                                                                                                       |
| [            [//args:]]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                       |
| [            [//  \_value   - current value of the numeric textbox]]                                                                                                                       |
|                                                                                                                                                                                                                                                                       |
| [        }]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                       |
| [        [function] OnValueChange(inst, args) {]                                                                                                                                                |
|                                                                                                                                                                                                                                                                       |
| [            [//inst      - instance of numeric textbox client side object]]                                                                                                               |
|                                                                                                                                                                                                                                                                       |
| [            [//args:]]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                       |
| [            [//  \_value   - current value of the numeric textbox]]                                                                                                                       |
|                                                                                                                                                                                                                                                                       |
| [        }        ]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                       |
| [\</][script][\>]                                                         |
|                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                      |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

4.   Build and run the application.

 

You can observe the handlers being invoked when the corresponding events are triggered.

[]{#related-topics}

