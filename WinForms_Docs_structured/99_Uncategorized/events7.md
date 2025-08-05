---
title: events7.md
original_path: WinForms_Docs/99_Uncategorized/events7.md
created_at: 2025-08-05
---






##### Events {#events style="tab-stops: 0pt"}

 

This section discusses the client-side and server-side events of the DropDownCalendarControl.

 

###### []{#_Client-Side_Events_4}5.1.2.3.3.1 Client-Side Events {#client-side-events style="tab-stops: 0pt"}

[] 

The DropDownCalendarControl raises client side events that can be used to execute client side java script routines. This technique avoids postback and makes the control faster and more responsive.

The following are client-side events that are supported by the DropDownCalendarControl.

[] 


  ------------------------- ------------------------------------------------------------------------------------------------------
  Event                     Description
  ClientSideOnFocusIn       Specifies the client side handler which will be called when control is in focus.
  ClientSideOnFocusOut      Specifies the client side handler which will be called when focus is shifted from the control.
  ClientSideOnMouseOut      Specifies the client side handler which will be called when mouse pointer leaves the control.
  ClientSideOnMouseOver     Specifies the client side handler which will be called when mouse pointer is moved over the control.
  ClientSideOnValueChange   Specifies the client side handler which will be called when the  value of control is changed.
  ------------------------- ------------------------------------------------------------------------------------------------------


[] 

To raise and process client side events

[] 

1.   The client side events must be set to the respective functions to be executed when the events are triggered. The html view of the event settings are shown below.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\<][ssw][:][DropDownCalendar][ [Control] [id ][= \"DropDownCalendar Control1\"] [runat ][= \"server\"] [Width ][= \"248px\"] [ClientSideOnFocusIn ][= \"GetDetails(\'OnFocus\', this)\"] [ClientSideOnFocusOut ][= \"GetDetails(\'OnBlur\', this)\"] [ClientSideOnMouseOver ][= \"GetDetails(\'OnMoseOver\', this)\"] [ClientSideOnMouseOut ][= \"GetDetails(\'OnMouseOut\', this)\"] [ClientSideOnValueChange ][= \"GetDetails(\'OnValueChange\', this)\"\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\</][ssw][:][DropDownCalendar][ [Control][\>]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

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
| [          sRes =sRes+ [\"ID\"]+[\"\\t\\t\"]+[\":\"] +oData \[[\"ID\"]\]+[\"\\n\"];]                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                     |
| [          sRes =sRes+ [\"Text\"]+[\"\\t\\t\"]+[\":\"] +oData \[[\"Text\"]\]+[\"\\n\"];]                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                     |
| [          [return] sRes;        ]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                     |
| [      }]                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                     |
| [\</][script][\>]                                                                                                                              |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

###### 5.1.2.3.3.2 Server-Side Events {#server-side-events style="tab-stops: 0pt"}

[] 

The server side events for the DropDownCalendar Control are as follows.

[] 


+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Server-Side Event                 | Description                                                                                                                                                                                                                                    |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| TextChanged                       | Occurs when the Text of DropDownCalendarControl changes between posts to the server.                                                                                                                                                           |
|                                   |                                                                                                                                                                                                                                                |
|                                   |                                                                                                                                                                                                                                                |
|                                   |                                                                                                                                                                                                                                                |
|                                   | **[\[C#\]]**                                                                                                                                                                                               |
|                                   |                                                                                                                                                                                                                                                |
|                                   | **[]**                                                                                                                                                                                                     |
|                                   |                                                                                                                                                                                                                                                |
|                                   | [protected][ [void] DropDownCalendarControl1_TextChanged([object] sender, [EventArgs] e)]  |
|                                   |                                                                                                                                                                                                                                                |
|                                   | [{]                                                                                                                                                                                                        |
|                                   |                                                                                                                                                                                                                                                |
|                                   | [      Label1.Text = DropDownCalendarControl1.Text;]                                                                                                                                                       |
|                                   |                                                                                                                                                                                                                                                |
|                                   | [}]                                                                                                                                                                                                        |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ValueChanged                      | Occurs when the Value of DropDownCalendarControl changes between posts to the server.                                                                                                                                                          |
|                                   |                                                                                                                                                                                                                                                |
|                                   | []                                                                                                                                                                                           |
|                                   |                                                                                                                                                                                                                                                |
|                                   | **[\[C#\]]**                                                                                                                                                                                               |
|                                   |                                                                                                                                                                                                                                                |
|                                   | **[]**                                                                                                                                                                                                     |
|                                   |                                                                                                                                                                                                                                                |
|                                   | [protected][ [void] DropDownCalendarControl1_ValueChanged([object] sender, [EventArgs] e)] |
|                                   |                                                                                                                                                                                                                                                |
|                                   | [{]                                                                                                                                                                                                        |
|                                   |                                                                                                                                                                                                                                                |
|                                   | [      Label2.Text = DropDownCalendarControl1.Value.ToShortDateString();]                                                                                                                                  |
|                                   |                                                                                                                                                                                                                                                |
|                                   | [}]                                                                                                                                                                                                        |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| VisibleMonthChanged               | Occurs when visible month of popup Calendar is changed.                                                                                                                                                                                        |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| RenderDay                         | Occurs when each day cell in the current month of popup Calendar is being rendered.                                                                                                                                                            |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 


{border="0"}Note: AutoPostBack property has been depreciated. To execute the server side events, the AutoPostBackOnTextChanged and the AutoPostBackOnValueChanged properties must be enabled for the respective events, which triggers a postback and handles the server side event. If AutoPostBackOnValueChanged or AutoPostBackOnTextChanged is set to True, then Postback will be performed, only when the user changes the date in the DropDownCalendarControl\'s input html element and leaves the control.


[] 

To execute the server side **VisibleMonthChanged** event, the **AutoPostBackOnVisibleMonthChanged** property must be set to **True**.

[] 

For more details, see [Server-Side Events]{.UGHyperlink} topic of Calendar control.

[]{#p79} 

[]{#related-topics}

