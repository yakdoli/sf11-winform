---
title: clientsideevents62.md
original_path: WinForms_Docs/99_Uncategorized/clientsideevents62.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



#### Client Side Events {#client-side-events style="tab-stops: 0pt"}

The Percent text box control supports the client-side events.

[] 

Events

  ----------------------- --------------------------------------------------------------- ----------- ----------------
  Name                    Description                                                     Arguments   Reference Link
  ClientSideFocusIn       Event triggers when the percent text box gains focus            inst,args   \-
   ClientSideFocusOut     Event triggers when the percent text box loses focus            inst,args   \-
  ClientSideValueChange   Event triggers when the value of the percent text box changes   inst,args   \-
  ----------------------- --------------------------------------------------------------- ----------- ----------------

 

Using Builder

The following steps, explains how to handle the client-side events through the Builder:

1.   In **View**, invoke the percent text box helper followed by the **ClientSideFocusIn**, **ClientSideFocusOut** and **ClientSideValueChange** methods with the desired handlers as arguments.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                 |
|                                                                                                                                                                    |
| [\<%] [{]                                                              |
|                                                                                                                                                                    |
| [          Html.MobSyncfusion().PercentTextbox([\"myPercent\"])]                                       |
|                                                                                                                                                                    |
| **[            .ClientSideFocusIn([\"OnFocusIn\"])]** []           |
|                                                                                                                                                                    |
| **[              .ClientSideFocusOut([\"OnFocusOut\"])]** []       |
|                                                                                                                                                                    |
| **[              .ClientSideValueChange([\"OnValueChange\"])]** [] |
|                                                                                                                                                                    |
| []                                                                                                                             |
|                                                                                                                                                                    |
| [                              .Render();]                                                                                     |
|                                                                                                                                                                    |
| [                          }[%\>]]                                                                 |
|                                                                                                                                                                    |
| [      []]                                                                                         |
|                                                                                                                                                                    |
| **[\[Razor\]]**                                                                                                                |
|                                                                                                                                                                    |
| [    [\@{]]                                                                                        |
|                                                                                                                                                                    |
| [                  Html.MobSyncfusion().PercentTextbox([\"myPercent \"])]                              |
|                                                                                                                                                                    |
| **[            .ClientSideFocusIn([\"OnFocusIn\"])]** []           |
|                                                                                                                                                                    |
| **[              .ClientSideFocusOut([\"OnFocusOut\"])]** []       |
|                                                                                                                                                                    |
| **[              .ClientSideValueChange([\"OnValueChange\"])]** [] |
|                                                                                                                                                                    |
| [                              .Render();]                                                                                     |
|                                                                                                                                                                    |
| [    [}]]                                                                                          |
|                                                                                                                                                                    |
| []                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

2.   Define the call back methods in the script to handle the specified events.

**[]**  

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[JavaScript\]]** [ ]                                                                                                                                   |
|                                                                                                                                                                                                                                    |
| [\<] [script] [ [type] [=\"text/javascript\"\>] ] |
|                                                                                                                                                                                                                                    |
| [        [function] OnFocusIn(inst, args) {]                                                                                                                              |
|                                                                                                                                                                                                                                    |
| [            [//inst      - instance of percent text box client-side object]]                                                                                        |
|                                                                                                                                                                                                                                    |
| [            [//args:]]                                                                                                                                              |
|                                                                                                                                                                                                                                    |
| [            [//  \_value   - current value of the percent text box]]                                                                                                |
|                                                                                                                                                                                                                                    |
| [        }]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                    |
| [        [function] OnFocusOut(inst, args) {]                                                                                                                             |
|                                                                                                                                                                                                                                    |
| [            [//inst      - instance of percent text box client-side object]]                                                                                        |
|                                                                                                                                                                                                                                    |
| [            [//args:]]                                                                                                                                              |
|                                                                                                                                                                                                                                    |
| [            [//  \_value   - current value of the percent text box]]                                                                                                |
|                                                                                                                                                                                                                                    |
| [        }      ]                                                                                                                                                                              |
|                                                                                                                                                                                                                                    |
| [        [function] OnValueChange(inst, args) {]                                                                                                                          |
|                                                                                                                                                                                                                                    |
| [            [//inst      - instance of percent text box client-side object]]                                                                                        |
|                                                                                                                                                                                                                                    |
| [            [//args:]]                                                                                                                                              |
|                                                                                                                                                                                                                                    |
| [            [//  \_value   - current value of the percent text box]]                                                                                                |
|                                                                                                                                                                                                                                    |
| [        }        ]                                                                                                                                                                            |
|                                                                                                                                                                                                                                    |
| [       [\</][script][\>]]                                                                                                    |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]**  

3.   Run the application.

**[]**  

**[Using Properties Model      ]**

The following steps, explains how to handle the client-side events through the Properties model:

1.   In the **Controller**, create an instance of **PercentTextBoxModel**; define the **ClientSideFocusIn, ClientSideFocusOut** and **ClientSideValueChange** properties and pass the instance through the view-specific data to the view.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]** [ ]                                                                                     |
|                                                                                                                                                                                      |
| [public] [ [ActionResult] Index()]                                      |
|                                                                                                                                                                                      |
| [        {]                                                                                                                                      |
|                                                                                                                                                                                      |
| [            [PercentTextBoxModel] myModel = [new][PercentTextBoxModel]();] |
|                                                                                                                                                                                      |
| [            **myModel.ClientSideFocusIn = [\"OnFocusIn\"];**]                                                           |
|                                                                                                                                                                                      |
| **[            myModel.ClientSideFocusOut = [\"OnFocusOut\"];]** []                  |
|                                                                                                                                                                                      |
| **[            myModel.ClientSideValueChange = [\"OnValueChange\"];]** []            |
|                                                                                                                                                                                      |
| [            ViewData\[[\"myPercent\"]\] = myModel;]                                                                     |
|                                                                                                                                                                                      |
| [            [return] View();]                                                                                              |
|                                                                                                                                                                                      |
| [        }] []                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

2.   In **View**, invoke the Percent textbox helper with the ViewData key as the first argument.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                             |
|                                                                                                                                                                                |
| [  ] [\<%] [{                                ] |
|                                                                                                                                                                                |
| [    Html.MobSyncfusion().PercentTextbox([\"myPercent\")]]                                                         |
|                                                                                                                                                                                |
| [                          .Render();]                                                                                                     |
|                                                                                                                                                                                |
| [       }[%\>]]                                                                                                |
|                                                                                                                                                                                |
| **[\[Razor\]]**                                                                                                                            |
|                                                                                                                                                                                |
| [    ] [\@{] []                                |
|                                                                                                                                                                                |
| [           Html.MobSyncfusion().PercentTextbox([\"myPercent\"])]                                                  |
|                                                                                                                                                                                |
| [                          .Render();]                                                                                                     |
|                                                                                                                                                                                |
| [       [}]] []                           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

3.   Define the call back methods in the script to handle the specified events.

**[]**  

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Javascript\]]** [ ]                                                                                                                                   |
|                                                                                                                                                                                                                                    |
| [\<] [script] [ [type] [=\"text/javascript\"\>] ] |
|                                                                                                                                                                                                                                    |
| [        [function] OnFocusIn(inst, args) {]                                                                                                                              |
|                                                                                                                                                                                                                                    |
| [            [//inst      - instance of percent textbox client side object]]                                                                                         |
|                                                                                                                                                                                                                                    |
| [            [//args:]]                                                                                                                                              |
|                                                                                                                                                                                                                                    |
| [            [//  \_value   - current value of the percent textbox]]                                                                                                 |
|                                                                                                                                                                                                                                    |
| [        }]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                    |
| [        [function] OnFocusOut(inst, args) {]                                                                                                                             |
|                                                                                                                                                                                                                                    |
| [        ] [    [//inst      - instance of percent textbox client side object]]                                     |
|                                                                                                                                                                                                                                    |
| [            [//args:]]                                                                                                                                              |
|                                                                                                                                                                                                                                    |
| [            [//  \_value   - current value of the percent textbox]]                                                                                                 |
|                                                                                                                                                                                                                                    |
| [        }]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                    |
| [        [function] OnValueChange(inst, args) {]                                                                                                                          |
|                                                                                                                                                                                                                                    |
| [            [//inst      - instance of percent textbox client side object]]                                                                                         |
|                                                                                                                                                                                                                                    |
| [            [//args:]]                                                                                                                                              |
|                                                                                                                                                                                                                                    |
| [            [//  \_value   - current value of the percent textbox]]                                                                                                 |
|                                                                                                                                                                                                                                    |
| [        }        ]                                                                                                                                                                            |
|                                                                                                                                                                                                                                    |
| [\</] [script] [\>] []                    |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]**  

4.   Run the application.

 

[]{#related-topics}

