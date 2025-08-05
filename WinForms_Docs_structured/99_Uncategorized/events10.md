---
title: events10.md
original_path: WinForms_Docs/99_Uncategorized/events10.md
created_at: 2025-08-05
---






##### Events {#events style="tab-stops: 0pt"}

 

This section discusses the client-side events of the PercentTextBox control.

[]{#p114} 

###### []{#_Client-Side_Events_7}5.1.2.6.3.1 Client-Side Events {#client-side-events style="tab-stops: 0pt"}

[] 

The PercentTextBox control raises client side events that you can use to execute client side java script routines. This technique avoids postback and makes the control faster and more responsive.

The following are client side events supported by PercentTextBox control.

[] 


  ------------------------- ------------------------------------------------------------------------------------------------------
  Event                     Description
  ClientSideOnFocusIn       Specifies the client side handler which will be called when control is in focus.
  ClientSideOnFocusOut      Specifies the client side handler which will be called when focus is shifted from the control.
  ClientSideOnMouseOut      Specifies the client side handler which will be called when mouse pointer leaves the control.
  ClientSideOnMouseOver     Specifies the client side handler which will be called when mouse pointer is moved over the control.
  ClientSideOnValueChange   Specifies the client side handler which will be called when the  value of the control is changed.
  ------------------------- ------------------------------------------------------------------------------------------------------


[] 

To raise and process client side events

[] 

1.   The client events must be set to the respective functions that has to be executed, when that event is triggered. The below code snippet shows the html view of the settings.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\<][ssw][:][PercentTextBox][ [id ][= \"PercentTextBox1\"] [runat ][= \"server\"] [Width ][= \"248px\"] [ClientSideOnFocusIn ][= \"GetDetails(\'OnFocus\', this)\"] [ClientSideOnFocusOut ][= \"GetDetails(\'OnBlur\', this)\"] [ClientSideOnMouseOver ][= \"GetDetails(\'OnMoseOver\', this)\"] [ClientSideOnMouseOut ][=  \"GetDetails(\'OnMouseOut\', this)\"] [ClientSideOnValueChange ][= \"GetDetails(\'OnValueChange\', this)\"\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\</][ssw][:][PercentTextBox][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   For the respective function names set to the client events, write the specific java script function. Here, for all the events, it lists the details of the corresponding event being fired.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\<][script][ [language][=\"javascript\"] [type][=\"text/javascript\"\>]] |
|                                                                                                                                                                                                                                                                                                                                                     |
| [   [function] GetDetails( sCapt, oData )]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                     |
| [      {]                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                     |
| [          [var] sRes = [\"\"] ;]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                     |
| [          [var] sText = [\"\"];]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                     |
| [          sRes = sCapt ;]                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                     |
| [          sRes = oData \[[\"ID\"]\];]                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                     |
| [          sRes = sRes.substring(0,(sRes.length-1));]                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                     |
| [          sRes =  sRes + [\":\\t\"] + sCapt + [\" Event is fired.\\n\"];]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                     |
| [          sRes =sRes+ [\"ID\"]+[\"\\t\\t\"]+[\":\"] +oData \[[\"ID\"]\]+[\"\\n\"];]                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                     |
| [          sRes =sRes+ [\"Text\"]+[\"\\t\\t\"]+[\":\"] +oData \[[\"Text\"]\]+[\"\\n\"];]                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                     |
| [          [return] sRes;        ]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                     |
| [      }]                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                     |
| [\</][script][\>]                                                                                                                              |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p115} 

[]{#related-topics}

