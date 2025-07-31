---
title: clientsideevents59.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\clientsideevents59.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



#### Client Side Events {#client-side-events style="tab-stops: 0pt"}

 

The MaskEdit text box control supports the client-side event handling.

[] 

Events

  ----------------------- ------------------------------------------------------------------------------------------------------------------------------- ----------- ----------------
  Name                    Description                                                                                                                     Arguments   Reference Link
  ClientSideFocusIn       Event triggers when the [MaskEdit]text box gains focus            inst,args   \-
   ClientSideFocusOut     Event triggers when the [MaskEdit]text box loses focus            inst,args   \-
  ClientSideValueChange   Event triggers when the value of the [MaskEdit]text box changes   inst,args   \-
  ----------------------- ------------------------------------------------------------------------------------------------------------------------------- ----------- ----------------

 

Using Builder

The following steps, explains how to handle the client-side events through the Builder:

1.   In **View**, invoke the MaskEdit text box helper followed by the **ClientSideFocusIn**, **ClientSideFocusOut** and **ClientSideValueChange** methods with desired handlers as arguments.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                |
|                                                                                                                                                                   |
| [\<%] [{]                                                             |
|                                                                                                                                                                   |
| [          Html.MobSyncfusion().MaskEditTextBox([\"myMask\"])]                                        |
|                                                                                                                                                                   |
| [             .Mask([\"(999)999-9999\"])]                                                             |
|                                                                                                                                                                   |
| **[             .ClientSideFocusIn([\"OnFocusIn\"])]** []         |
|                                                                                                                                                                   |
| **[             .ClientSideFocusOut([\"OnFocusOut\"])]** []       |
|                                                                                                                                                                   |
| **[             .ClientSideValueChange([\"OnValueChange\"])]** [] |
|                                                                                                                                                                   |
| [                              .Render();]                                                                                    |
|                                                                                                                                                                   |
| [                          }[%\>]]                                                                |
|                                                                                                                                                                   |
| [      []]                                                                                        |
|                                                                                                                                                                   |
| **[\[Razor\]]**                                                                                                               |
|                                                                                                                                                                   |
| [    [\@{]]                                                                                       |
|                                                                                                                                                                   |
| [            Html.MobSyncfusion().MaskEditTextBox([\"myMask\"])]                                      |
|                                                                                                                                                                   |
| [            .Mask([\"(999)999-9999\"])]                                                              |
|                                                                                                                                                                   |
| **[            .ClientSideFocusIn([\"OnFocusIn\"])]** []          |
|                                                                                                                                                                   |
| **[            .ClientSideFocusOut([\"OnFocusOut\"])]** []        |
|                                                                                                                                                                   |
| **[            .ClientSideValueChange([\"OnValueChange\"])]** []  |
|                                                                                                                                                                   |
| [                              .Render();]                                                                                    |
|                                                                                                                                                                   |
| [    [}]]                                                                                         |
|                                                                                                                                                                   |
| []                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

2.   Define the call back methods in the script to handle the specified events.

**[]**  

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[JavaScript\]]** [ ]                                                                                                                                   |
|                                                                                                                                                                                                                                    |
| [\<] [script] [ [type] [=\"text/javascript\"\>] ] |
|                                                                                                                                                                                                                                    |
| [        [function] OnFocusIn(inst, args) {]                                                                                                                              |
|                                                                                                                                                                                                                                    |
| [            [//inst      - instance of numeric text box client-side object]]                                                                                        |
|                                                                                                                                                                                                                                    |
| [            [//args:]]                                                                                                                                              |
|                                                                                                                                                                                                                                    |
| [            [//  \_value   - current value of the numeric text box]]                                                                                                |
|                                                                                                                                                                                                                                    |
| [        }]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                    |
| [        [function] OnFocusOut(inst, args) {]                                                                                                                             |
|                                                                                                                                                                                                                                    |
| [            [//inst      - instance of numeric text box client-side object]]                                                                                        |
|                                                                                                                                                                                                                                    |
| [            [//args:]]                                                                                                                                              |
|                                                                                                                                                                                                                                    |
| [            [//  \_value   - current value of the numeric text box]]                                                                                                |
|                                                                                                                                                                                                                                    |
| [        }      ]                                                                                                                                                                              |
|                                                                                                                                                                                                                                    |
| [        [function] OnValueChange(inst, args) {]                                                                                                                          |
|                                                                                                                                                                                                                                    |
| [            [//inst      - instance of numeric text box client-side object]]                                                                                        |
|                                                                                                                                                                                                                                    |
| [            [//args:]]                                                                                                                                              |
|                                                                                                                                                                                                                                    |
| [            [//  \_value   - current value of the numeric text box]]                                                                                                |
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

The following steps will explain how to handle the client-side events through the Properties model:

1.   In the **Controller**, create an instance of **MaskEditTextBoxModel**; define the **ClientSideFocusIn, ClientSideFocusOut** and **ClientSideValueChange** properties and pass the instance through the view-specific data to the view.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]** [ ]                                                                                        |
|                                                                                                                                                                                         |
| [public] [ [ActionResult] Index()]                                         |
|                                                                                                                                                                                         |
| [        {]                                                                                                                                         |
|                                                                                                                                                                                         |
| [            [MaskEditTextBoxModel] myModel = [new][MaskEditTextBoxModel] ();] |
|                                                                                                                                                                                         |
| [                     myModel.Mask = [\"999-99-999\"];]                                                                     |
|                                                                                                                                                                                         |
| [            **myModel.ClientSideFocusIn = [\"OnFocusIn\"];**]                                                              |
|                                                                                                                                                                                         |
| **[            myModel.ClientSideFocusOut = [\"OnFocusOut\"];]** []                     |
|                                                                                                                                                                                         |
| **[            myModel.ClientSideValueChange = [\"OnValueChange\"];]** []               |
|                                                                                                                                                                                         |
| [            ViewData\[[\"myMask\"]\] = myModel;]                                                                           |
|                                                                                                                                                                                         |
| [            [return] View();]                                                                                                 |
|                                                                                                                                                                                         |
| [        }] []                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

2.   In **View**, invoke the MaskEdit textbox helper with the ViewData key as the first argument.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                             |
|                                                                                                                                                                                |
| [  ] [\<%] [{                                ] |
|                                                                                                                                                                                |
| [    Html.MobSyncfusion().MaskEditTextbox([\"myMask\")]]                                                           |
|                                                                                                                                                                                |
| [                          .Render();]                                                                                                     |
|                                                                                                                                                                                |
| [       }[%\>]]                                                                                                |
|                                                                                                                                                                                |
| **[\[Razor\]]**                                                                                                                            |
|                                                                                                                                                                                |
| [    ] [\@{] []                                |
|                                                                                                                                                                                |
| [           Html.MobSyncfusion().MaskEditTextbox([\"myMask\"])]                                                    |
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
| [            [//inst      - instance of numeric textbox client side object]]                                                                                         |
|                                                                                                                                                                                                                                    |
| [            [//args:]]                                                                                                                                              |
|                                                                                                                                                                                                                                    |
| [            [//  \_value   - current value of the numeric textbox]]                                                                                                 |
|                                                                                                                                                                                                                                    |
| [        }]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                    |
| [        [function] OnFocusOut(inst, args) {]                                                                                                                             |
|                                                                                                                                                                                                                                    |
| [            [//inst      - instance of numeric textbox client side object]]                                                                                         |
|                                                                                                                                                                                                                                    |
| [            [//args:]]                                                                                                                                              |
|                                                                                                                                                                                                                                    |
| [            [//  \_value   - current value of the numeric textbox]]                                                                                                 |
|                                                                                                                                                                                                                                    |
| [        }]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                    |
| [        [function] OnValueChange(inst, args) {]                                                                                                                          |
|                                                                                                                                                                                                                                    |
| [            [//inst      - instance of numeric textbox client side object]]                                                                                         |
|                                                                                                                                                                                                                                    |
| [            [//args:]]                                                                                                                                              |
|                                                                                                                                                                                                                                    |
| [            [//  \_value   - current value of the numeric textbox]]                                                                                                 |
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

