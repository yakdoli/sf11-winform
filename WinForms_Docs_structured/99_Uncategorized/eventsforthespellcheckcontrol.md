---
title: eventsforthespellcheckcontrol.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\eventsforthespellcheckcontrol.md
created_at: 2025-07-03
---






#### Events for the SpellCheck Control {#events-for-the-spellcheck-control style="tab-stops: 0pt"}

Support has been incorporated into the SpellCheck for Client and Server-side events.

Client-side events can be triggered at the start and end of the SpellCheck of every control.

A Server-side event can be triggered at the end of the SpellCheck of all the controls.

Use Case Scenarios-

**For Client-Side Events:**

The user can change the properties of the control at the beginning and end of the SpellCheck of that control.

For Example-

Consider a page on which you have three text boxes. You have started the SpellCheck control, but you don't know for which one the SpellCheck is going on, since the control will check the text in all the three text boxes.

In order to see which text box is getting checked, you can modify the properties of the control while the SpellCheck is running, so that this textbox gets highlighted.

For Server-Side Events:

The Server-side events for the SpellCheck control allow the user to save data to the server without any errors in spelling.

Properties

There is only one Server-side property for the events of the Spellchecker control:

 


+--------------+-------------------------------------------------------------------------------------------+------------------+---------------------------------------------+--------------+
| Property     | Description                                                                               | Type of Property | Value it accepts                            | Dependencies |
+--------------+-------------------------------------------------------------------------------------------+------------------+---------------------------------------------+--------------+
| Autopostback | Allow us to specify the postback of the control which needs to be fired.                  | bool             | [·      ]True  | NA           |
|              |                                                                                           |                  |                                             |              |
|              |                                                                                           |                  | [·      ]False |              |
|              |                                                                                           |                  |                                             |              |
|              | If Autopostback is set to **true**,then both Client and **Server-side** events are fired. |                  |                                             |              |
|              |                                                                                           |                  |                                             |              |
|              |                                                                                           |                  | Default value is False                      |              |
|              |                                                                                           |                  |                                             |              |
|              | If Autopostback is set to **false**, then only the **client-side** events are fired.      |                  |                                             |              |
+--------------+-------------------------------------------------------------------------------------------+------------------+---------------------------------------------+--------------+


 


Note: There are no properties for Client-side events.


 

 

Events

 

Client Side Events

 


  -------------------------------- --------------------------------------------------------------------------------------------------------------------
  Name                             Description
  ClientSideOnSpellCheckStarted    Allows you to specify the client-side function when SpellCheck is started.
  ClientSideOnSpellCheckComplete   Allows you to specify the client-side function (which executes after the Spellcheckcompletion) for the SpellCheck.
  -------------------------------- --------------------------------------------------------------------------------------------------------------------


 

Server Side Events

 

  ---------------------- -----------------------------------------------------------------------------------------------------------------
  Name                   Description
  OnSpellCheckComplete   Allow us to specify the server side function for the spell-check which executes after the spellcheckcompletion.
  ---------------------- -----------------------------------------------------------------------------------------------------------------

 

More:





