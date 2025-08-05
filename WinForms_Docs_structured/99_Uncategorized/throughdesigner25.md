---
title: throughdesigner25.md
original_path: WinForms_Docs/99_Uncategorized/throughdesigner25.md
created_at: 2025-08-05
---






##### Through Designer {#through-designer style="tab-stops: 0pt"}

[] 

To create WaitingPopup control that should appear during some process indicating the loading or refreshing process, follow the below steps.

[] 

{border="0"}

[] 

Figure 421: WaitingPopup initiated for a html element

[] 

1.   Drag the WaitingPopup control onto the application. The WaitingPopup can be initiated to indicate the loading or processing state that has been initiated by some user or system action.

2.   Here is a simple example to display the waiting popup on click action. When the user clicks the **ShowPopUp** button, the client side function is invoked and the WaitingPopup control is displayed.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[script\]]**                                                                                                                                                                        |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                    |
|                                                                                                                                                                                                                             |
| [\<][script][ [type][=\"text/jscript\"\>]] |
|                                                                                                                                                                                                                             |
| [    [function] ShowPopUp()]                                                                                                                                       |
|                                                                                                                                                                                                                             |
| [    {]                                                                                                                                                                                 |
|                                                                                                                                                                                                                             |
| [        Popup1.ShowPopup()]                                                                                                                                                            |
|                                                                                                                                                                                                                             |
| [    }]                                                                                                                                                                                 |
|                                                                                                                                                                                                                             |
| [\</][script][\>]                                                      |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[aspx\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\<][input][ [class][=\"lblBold\"] [onclick][=\"ShowPopUp()\"] [type][=\"button\"] [value][=\"Click\"] [/\>]]                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\<][cc1][:][WaitingPopup][ [ID][=\"WaitingPopup1\"] [runat][=\"server\"] [Width][=\"56px\"] [OnBeforePopup][=\"AssignValue(this)\"] [CloseTimeOut][=\"2000\"] [ClientObjectID][=\"Popup1\"] [DisableOnShowElementID][=\"div1\"\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\<][img][ [src][=\"images/LoadImg.gif\"] [/\> ]Loading\...]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\</][cc1][:][WaitingPopup][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\<][div][ [id][=\"div1\"] [align][=\"center\"] [style][=\"border-right: #c8c8c8 1px solid; border-top: #c8c8c8 1px solid; border-left: #c8c8c8 1px solid; width: 308px; border-bottom: #c8c8c8 1px solid; height: 90px; background-color: #faebd7;\"\> \</][div][\>]]                                                                                                                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The waiting popup can be displayed on the page or any html control. Also the controls can be disabled during the loading process and many more features can be applied, which has been discussed in [Concepts and Features]{.UGHyperlink} topic.

[] 

3.   Build and run the application.

[] 

See Also

[] 

[Creating WaitingPopup Through Code]{.UGHyperlink}[]{.UGHyperlink}

 

[]{#related-topics}

