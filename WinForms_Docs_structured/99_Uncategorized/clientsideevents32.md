---
title: clientsideevents32.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\clientsideevents32.md
created_at: 2025-07-03
---






#### Client Side Events {#client-side-events style="tab-stops: 0pt"}

Mask Edit textbox supports client side event handling.

Events

 

+-----------------------+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+-----------------+
| Name                  | Description                                                            | Type of property                                                                                 | Arguments       |
+-----------------------+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+-----------------+
| ClientSideFocusIn     | This event is raised when the mask edit text box  gains focus          | [[string]]{.UGHyperlink} | inst,args       |
|                       |                                                                        |                                                                                                  |                 |
|                       |                                                                        |                                                                                                  |                 |
|                       |                                                                        |                                                                                                  |                 |
|                       |                                                                        |                                                                                                  |                 |
+-----------------------+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+-----------------+
| ClientSideFocusOut    | This event is raised when the mask edit text box  loses focus          | [[string]]{.UGHyperlink} | inst,args       |
|                       |                                                                        |                                                                                                  |                 |
|                       |                                                                        |                                                                                                  |                 |
|                       |                                                                        |                                                                                                  |                 |
|                       |                                                                        |                                                                                                  |                 |
+-----------------------+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+-----------------+
| ClientSideMouseOut    | This event is raised on mouse out of the mask edit text box            | [[string]]{.UGHyperlink} | inst,args       |
|                       |                                                                        |                                                                                                  |                 |
|                       |                                                                        |                                                                                                  |                 |
|                       |                                                                        |                                                                                                  |                 |
|                       |                                                                        |                                                                                                  |                 |
+-----------------------+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+-----------------+
| ClientSideMouseOver   | This event is raised on mouse over the mask edit text box              | [[string]]{.UGHyperlink} | inst,args       |
|                       |                                                                        |                                                                                                  |                 |
|                       |                                                                        |                                                                                                  |                 |
|                       |                                                                        |                                                                                                  |                 |
|                       |                                                                        |                                                                                                  |                 |
+-----------------------+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+-----------------+
| ClientSideValueChange | This event is raised when the value of the mask edit text box  changes | [[string]]{.UGHyperlink} | inst, args      |
|                       |                                                                        |                                                                                                  |                 |
|                       |                                                                        |                                                                                                  |                 |
+-----------------------+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+-----------------+

 

Using Builder

The following steps explain the setting of the Syncfusion theme for the mask edit using Builder.

1.   In **View**, invoke the mask edit textbox helper followed by the **ClientSideFocusIn, ClientSideFocusOut, ClinetSideMouseOut, ClientSideMouseOver** and **ClientSideValueChange** methods with the desired handlers as arguments.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                           |
| [\<%][=][Html.Syncfusion().MaskEditTextBox([\"myMaskEdit\"])] |
|                                                                                                                                                                                                                                                                           |
| [.Mask([\"(999)999-9999\"])]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                           |
| [.**ClientSideFocusIn([\"OnFocus\"])**]                                                                                                                                                          |
|                                                                                                                                                                                                                                                                           |
| **[.ClientSideMouseOut([\"OnMouseOut\"])]**                                                                                                                                                      |
|                                                                                                                                                                                                                                                                           |
| **[.ClientSideMouseOver([\"OnMouseOver\"])]**                                                                                                                                                    |
|                                                                                                                                                                                                                                                                           |
| **[.ClientSideValueChange([\"OnValueChange\"])]**[ [%\>]]                                                           |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                            |
| [\@{][ Html.Syncfusion().MaskEditTextBox([\"myMaskEdit\"])]                                                                  |
|                                                                                                                                                                                                                                                                            |
| [.Mask([\"(999)999-9999\"])]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                            |
| [.**ClientSideFocusIn([\"OnFocus\"])**]                                                                                                                                                           |
|                                                                                                                                                                                                                                                                            |
| **[.ClientSideMouseOut([\"OnMouseOut\"])]**                                                                                                                                                       |
|                                                                                                                                                                                                                                                                            |
| **[.ClientSideMouseOver([\"OnMouseOver\"])]**                                                                                                                                                     |
|                                                                                                                                                                                                                                                                            |
| **[.ClientSideValueChange([\"OnValueChange\"])]**[.Render();][ [}]] |
|                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

2.   In the Javascript, define the handlers.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[Javascript\]**                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
| [\<][script][ [type][=\"text/javascript\"\>]] |
|                                                                                                                                                                                                                                 |
| [        [function] OnFocus(inst, args) {]                                                                                                                             |
|                                                                                                                                                                                                                                 |
| [            [//inst              - instance of mask edit client side object]]                                                                                        |
|                                                                                                                                                                                                                                 |
| [            [//args:]]                                                                                                                                               |
|                                                                                                                                                                                                                                 |
| [            [//  \_stripValue     - stripped value of the mask edit textbox]]                                                                                        |
|                                                                                                                                                                                                                                 |
| [            [//  \_unstripValue   - unstripped value of the mask edit textbox]]                                                                                      |
|                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
| [        [function] OnFocusOut(inst, args) {]                                                                                                                          |
|                                                                                                                                                                                                                                 |
| [            [//inst              - instance of mask edit client side object]]                                                                                        |
|                                                                                                                                                                                                                                 |
| [            [//args:]]                                                                                                                                               |
|                                                                                                                                                                                                                                 |
| [            [//  \_stripValue     - stripped value of the mask edit textbox]]                                                                                        |
|                                                                                                                                                                                                                                 |
| [            [//  \_unstripValue   - unstripped value of the mask edit textbox]]                                                                                      |
|                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
| [        [function] OnMouseOut(inst, args) {]                                                                                                                          |
|                                                                                                                                                                                                                                 |
| [            [//inst              - instance of mask edit client side object]]                                                                                        |
|                                                                                                                                                                                                                                 |
| [            [//args:]]                                                                                                                                               |
|                                                                                                                                                                                                                                 |
| [            [//  \_stripValue     - stripped value of the mask edit textbox]]                                                                                        |
|                                                                                                                                                                                                                                 |
| [            [//  \_unstripValue   - unstripped value of the mask edit textbox]]                                                                                      |
|                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
| [        [function] OnMouseOver(inst, args) {]                                                                                                                         |
|                                                                                                                                                                                                                                 |
| [            [//inst              - instance of mask edit client side object]]                                                                                        |
|                                                                                                                                                                                                                                 |
| [            [//args:]]                                                                                                                                               |
|                                                                                                                                                                                                                                 |
| [            [//  \_stripValue     - stripped value of the mask edit textbox]]                                                                                        |
|                                                                                                                                                                                                                                 |
| [            [//  \_unstripValue   - unstripped value of the mask edit textbox]]                                                                                      |
|                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
| [        [function] OnValueChange(inst, args) {]                                                                                                                       |
|                                                                                                                                                                                                                                 |
| [            [//inst              - instance of mask edit client side object]]                                                                                        |
|                                                                                                                                                                                                                                 |
| [            [//args:]]                                                                                                                                               |
|                                                                                                                                                                                                                                 |
| [            [//  \_stripValue     - stripped value of the mask edit textbox]]                                                                                        |
|                                                                                                                                                                                                                                 |
| [            [//  \_unstripValue   - unstripped value of the mask edit textbox]]                                                                                      |
|                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
| [\</][script][\>]                                                         |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

3.   Build and run the application.

[] 

Using PropertiesModel

The following steps explain the setting of Syncfusion theme for the mask edit using the Properties model.

1.   In the **Controller**, create an instance of **MaskEditTextBoxModel**, set the **AutoFormat** property and pass the instance through **view specific data** to **View** as given below.**

*[[]]{.underline}* 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[Controller\]**                                                                                                                                                                                   |
|                                                                                                                                                                                                      |
|                                                                                                                                                                                                      |
|                                                                                                                                                                                                      |
| [ public][ [ActionResult] Index()]                            |
|                                                                                                                                                                                                      |
| [        {]                                                                                                                                         |
|                                                                                                                                                                                                      |
| [            [//create an instance of MaskEditTextBoxModel]]                                                                  |
|                                                                                                                                                                                                      |
| [            [MaskEditTextBoxModel] myModel = [new] [MaskEditTextBoxModel]();] |
|                                                                                                                                                                                                      |
| [            myModel.Mask = [\"999-99-999\"];]                                                                              |
|                                                                                                                                                                                                      |
| **[            myModel.ClientSideFocusIn = [\"OnFocus\"];]**                                                                |
|                                                                                                                                                                                                      |
| **[            myModel.ClientSideFocusOut = [\"OnFocusOut\"];]**                                                            |
|                                                                                                                                                                                                      |
| **[            myModel.ClientSideMouseOut = [\"OnMouseOut\"];]**                                                            |
|                                                                                                                                                                                                      |
| **[            myModel.ClientSideMouseOver = [\"OnMouseOver\"];]**                                                          |
|                                                                                                                                                                                                      |
| **[            myModel.ClientSideValueChange = [\"OnValueChange\"];]**                                                      |
|                                                                                                                                                                                                      |
| **[]**                                                                                                                                              |
|                                                                                                                                                                                                      |
| [            ]                                                                                                                                      |
|                                                                                                                                                                                                      |
| [            [//pass the instance through view data to the view]]                                                             |
|                                                                                                                                                                                                      |
| [            ViewData\[[\"myMaskEdit\"]\] = myModel;]                                                                       |
|                                                                                                                                                                                                      |
| [            [return] View();]                                                                                                 |
|                                                                                                                                                                                                      |
| [        }]                                                                                                                                         |
|                                                                                                                                                                                                      |
| []                                                                                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

*[[]]{.underline}* 

2.   In **View**, invoke the mask edit textbox helper with view data key as the Control ID.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                            |
| [\<%][=][Html.Syncfusion().MaskEditTextBox([\"myMaskEdit\"])[%\>]] |
|                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                    |
| [\@{][ ][Html.Syncfusion().MaskEditTextBox([\"myMaskEdit\"]).Render();[}]] |
|                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

3.   In the javascript, define the hanlders as given below.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[Javascirpt\]**                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
| [\<][script][ [type][=\"text/javascript\"\>]] |
|                                                                                                                                                                                                                                 |
| [        [function] OnFocus(inst, args) {]                                                                                                                             |
|                                                                                                                                                                                                                                 |
| [            [//inst              - instance of mask edit client side object]]                                                                                        |
|                                                                                                                                                                                                                                 |
| [            [//args:]]                                                                                                                                               |
|                                                                                                                                                                                                                                 |
| [            [//  \_stripValue     - stripped value of the mask edit textbox]]                                                                                        |
|                                                                                                                                                                                                                                 |
| [            [//  \_unstripValue   - unstripped value of the mask edit textbox]]                                                                                      |
|                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
| [        [function] OnFocusOut(inst, args) {]                                                                                                                          |
|                                                                                                                                                                                                                                 |
| [            [//inst              - instance of mask edit client side object]]                                                                                        |
|                                                                                                                                                                                                                                 |
| [            [//args:]]                                                                                                                                               |
|                                                                                                                                                                                                                                 |
| [            [//  \_stripValue     - stripped value of the mask edit textbox]]                                                                                        |
|                                                                                                                                                                                                                                 |
| [            [//  \_unstripValue   - unstripped value of the mask edit textbox]]                                                                                      |
|                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
| [        [function] OnMouseOut(inst, args) {]                                                                                                                          |
|                                                                                                                                                                                                                                 |
| [            [//inst              - instance of mask edit client side object]]                                                                                        |
|                                                                                                                                                                                                                                 |
| [            [//args:]]                                                                                                                                               |
|                                                                                                                                                                                                                                 |
| [            [//  \_stripValue     - stripped value of the mask edit textbox]]                                                                                        |
|                                                                                                                                                                                                                                 |
| [            [//  \_unstripValue   - unstripped value of the mask edit textbox]]                                                                                      |
|                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
| [        [function] OnMouseOver(inst, args) {]                                                                                                                         |
|                                                                                                                                                                                                                                 |
| [            [//inst              - instance of mask edit client side object]]                                                                                        |
|                                                                                                                                                                                                                                 |
| [            [//args:]]                                                                                                                                               |
|                                                                                                                                                                                                                                 |
| [            [//  \_stripValue     - stripped value of the mask edit textbox]]                                                                                        |
|                                                                                                                                                                                                                                 |
| [            [//  \_unstripValue   - unstripped value of the mask edit textbox]]                                                                                      |
|                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
| [        [function] OnValueChange(inst, args) {]                                                                                                                       |
|                                                                                                                                                                                                                                 |
| [            [//inst              - instance of mask edit client side object]]                                                                                        |
|                                                                                                                                                                                                                                 |
| [            [//args:]]                                                                                                                                               |
|                                                                                                                                                                                                                                 |
| [            [//  \_stripValue     - stripped value of the mask edit textbox]]                                                                                        |
|                                                                                                                                                                                                                                 |
| [            [//  \_unstripValue   - unstripped value of the mask edit textbox]]                                                                                      |
|                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
| [\</][script][\>]                                                         |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

4.   Build and run the application.

You can observe the defined callbacks triggering when the corresponding events are raised.

[]{#related-topics}

