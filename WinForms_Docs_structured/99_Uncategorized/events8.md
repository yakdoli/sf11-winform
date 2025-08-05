---
title: events8.md
original_path: WinForms_Docs/99_Uncategorized/events8.md
created_at: 2025-08-05
---






##### Events {#events style="tab-stops: 0pt"}

This section discusses the client-side events of the MaskedEditTextBox control.

 

###### []{#_Client-Side_Events_5}5.1.2.4.3.1 Client-Side Events {#client-side-events style="tab-stops: 0pt"}

[] 

The MaskedEditTextBox control raises client side events that you can use to execute client side java script routines. This technique avoids postback and makes the control faster and more responsive.

 

The following are client side events supported by the MaskedEditTextBox control.

[] 


  ------------------------- -------------------------------------------------------------------------------------------------------
  Event                     Description
  ClientSideOnFocusIn       Represents the client side handler which will be called when control is in focus.
  ClientSideOnFocusOut      Represents the client side handler which will be called when focus is shifted from the control.
  ClientSideOnMouseOut      Represents the client side handler which will be called when mouse pointer leaves the control.
  ClientSideOnMouseOver     Represents the client side handler which will be called when mouse pointer is moved over the control.
  ClientSideOnValueChange   Represents the client side handler which will be called when the  value of control is changed.
  ------------------------- -------------------------------------------------------------------------------------------------------


[] 

To raise and process client side events

[] 

1.   The client side events must be set to the respective functions to be executed when the events are triggered. The html view of the event settings are shown below.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\<][ssw][:][MaskedEditTextBox][ [id ][= \"MaskedEditTextBox1\"] [runat ][= \"server\"] [Width ][= \"248px\" ][ClientSideOnFocusIn ][= \"GetDetails(\'OnFocus\', this)\"] [ClientSideOnFocusOut ][= \"GetDetails(\'OnBlur\', this)\"] [ClientSideOnMouseOver ][= \"GetDetails(\'OnMoseOver\', this)\"] [ClientSideOnMouseOut ][= \"GetDetails(\'OnMouseOut, this)\"] [ClientSideOnValueChange ][= \"GetDetails(\'OnValueChange\', this)\"\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [\</][ssw][:][MaskedEditTextBox][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   For the respective function names set to the client events, write the specific java script function. Here, for all the events, it lists the details of the corresponding event being fired and its details.

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

 

[]{#related-topics}

