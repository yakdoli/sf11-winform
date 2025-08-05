---
title: clientsideevents18.md
original_path: WinForms_Docs/99_Uncategorized/clientsideevents18.md
created_at: 2025-08-05
---






##### Client-Side Events {#client-side-events style="tab-stops: 0pt"}

[] 

Client side events can be raised on user actions to perform the specified function without triggering a postback. The various client side events are listed below.

[] 


  ------------------------- ---------------------------------------------------------------------------------------------------------------
  Event                     Description
  ClientSideOnBeforeClose   Specifies the client-side function to trigger before closing the Window. Returns false to cancellable closed.
  ClientSideOnBeforeOpen    Specifies the client-side function to trigger before opening the Window. Returns false to cancelable opened.
  ClientSideOnCloseUp       Specifies the client-side function to trigger after Window is closed.
  ClientSideOnDragStart     Specifies the client-side function to trigger on Window Start drag. If false is returned no drag occurs.
  ClientSideOnDrag          Specifies the client-side function to trigger after dropping the Window control in document.
  ClientSideOnLoad          Specifies the client-side function to trigger after the Window and Window control's frame is loaded.
  ClientSideOnOpen          Specifies the client-side function to trigger after the Window is opened.
  ClientSideOnResizeEnd     Specifies the client-side function to trigger when the Window is resized.
  ClientSideOnResizeStart   Specifies the client-side function to trigger when Window starts resizing.
  ClientSideOnResize        Specifies the client-side function to trigger when the Window is resizing.
  ClientSideOnMove          Specifies the client-side function to trigger when the Window is moved.
  ClientSideBeforePinOn     Specifies the client-side function to trigger before the Window is Pinned On.
  ClientSideAfterPinOn      Specifies the client-side function to trigger after the Window is Pinned On.
  ClientSideBeforePinOff    Specifies the client-side function to trigger before the Window is Pinned Off.
  ClientSideAfterPinOff     Specifies the client-side function to trigger after the Window is Pinned Off.
  ClientSideBeforeRefresh   Specifies the client-side function to trigger before the Window is refreshed.
  ClientSideAfterRefresh    Specifies the client-side function to trigger after the Window is refreshed.
  ClientSideBeforeMin       Specifies the client-side function to trigger before the Window is minimized.
  ClientSideAfterMin        Specifies the client-side function to trigger after the Window is minimized.
  ClientSideBeforeMax       Specifies the client-side function to trigger before the Window is maximized.
  ClientSideAfterMax        Specifies the client-side function to trigger after the Window is maximized.
  ClientSideBeforeRestore   Specifies the client-side function to trigger before the Window is restored.
  ClientSideAfterRestore    Specifies the client-side function to trigger after the Window is restored.
  ------------------------- ---------------------------------------------------------------------------------------------------------------


[] 

To invoke the client side events, follow the below steps.

[] 

1.   In HTML view of the project, add the following content.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[aspx\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\<][script][ [language][=\"javascript\"\>]   ]                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [    [function] EventLog(eventName)]                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [    {]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [    [var] content=document.getElementById([\"eventLog\"]).value;]                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [    document.getElementById([\"eventLog\"]).value=eventName +[\" event is fired.\\n\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\\n\"]+content;]                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [    }]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [   ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [    [function] ClearEventLog()]                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [    {]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [        document.getElementById([\"eventLog\"]).value=[\"\"];]                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [    }]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\</][script][\>]                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\<][ssw][:][Window][ [ID][=\"Window1\"] [runat][=\"server\"] [AutoFormat][=\"WindowsXP Luna Blue\"] [Height][=\"230px\"]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [ [Width][=\"250px\"] [ClientSideOnBeforeClose][=\"EventLog(\'ClientSideOnBeforeClose\')\"] [ClientSideOnBeforeOpen][=\"EventLog(\'ClientSideOnBeforeOpen\')\"]]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [ [ClientSideOnCloseUp][=\"EventLog(\'ClientSideOnCloseUp\')\"] [ClientSideOnDragStart][=\"EventLog(\'ClientSideOnDragStart\'))\"]]                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [ [ClientSideOnDrop][=\"EventLog(\'ClientSideOnDrop\')\"] [ClientSideOnLoad][=\"EventLog(\'ClientSideOnLoad\')\"]]                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [ClientSideOnMove][=\"EventLog(\'ClientSideOnMove\')\"][ [ClientSideOnOpen][=\"EventLog(\'ClientSideOnOpen\')\"]]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [ [ClientSideOnResize][=\"EventLog(\'ClientSideOnResize\')\"] [ClientSideOnResizeEnd][=\"EventLog(\'ClientSideOnResizeEnd\')\"]]                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [ [ClientSideOnResizeStart][=\"EventLog(\'ClientSideOnResizeStart\')\"] [InitiallyShown][=\"True\"]]                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [ClientObjectId][=\"Window1\"\>]                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [   [\<][table] [id][=\"Table1\"] [align][=\"center\"] [height][=\"150\"] [runat][=\"server\"\>]]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [       [\<][tr] [id][=\"Tr1\"] [runat][=\"server\"\>]]                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [           [\<][td] [id][=\"Td1\"] [valign][=\"middle\"] [align][=\"center\"] [runat][=\"server\"\>]]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [               [\<][div] [style][=\"][vertical-align]: [middle];[\"\>]]                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [                   Sample Window[\</][div][\>]]                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [               [\<][br] [/\>]]                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [               [\<][br] [/\>]]                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [               [\<][br] [/\>]]                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [               [\<][input] [type][=\"Button\"] [value][=\"Close\"] [onclick][=\"Window1.Close()\"] [/\>]]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [           [\</][td][\>]]                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [       [\</][tr][\>]]                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [   [\</][table][\>]]                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\</][ssw][:][Window][\>]                                                                                                                                                                                                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Build and run the application. Then open, close, move and drag the window to trigger the events.

[] 

Code Analysis

**[]** 

[·      ]**ClientSideOnBeforeClose**

[] 

In the above example, the ClientSideOnBeforeClose property is set to the \'EventLog(eventName)\' client-side javascript function. This will get executed before closing the Window.

[] 

[·      ]**ClientSideOnBeforeOpen**

[] 

In the above example, the ClientSideOnBeforeOpen property is set to the \'EventLog(eventName)\' client-side javascript function. This will get executed before opening the Window.

[] 

[·      ]**ClientSideOnCloseUp**

[] 

In the above example, the ClientSideOnCloseUp property is set to the \'EventLog(eventName)\' client-side javascript function. This will get executed after Window is closed.

[] 

[·      ]**ClientSideOnDragStart**

[] 

In the above example, the ClientSideOnDragStart property is set to the \'EventLog(eventName)\' client-side javascript function. This will get executed on Window Start drag.

[] 

[·      ]**ClientSideOnDrag**

[] 

In the above example, the ClientSideOnDrag property is set to the \'EventLog(eventName)\' client-side javascript function. This will get executed after dropping the Window control in the document.

[] 

[·      ]**ClientSideOnLoad**

[] 

In the above example, the ClientSideOnLoad property is set to the \'EventLog(eventName)\' client-side javascript function. This will get executed after the Window and Window control's frame is loaded.

[] 

[·      ]**ClientSideOnOpen**

[] 

In the above example, the ClientSideOnOpen property is set to the \'EventLog(eventName)\' client-side javascript function. This will get executed after the Window is opened.

[] 

[·      ]**ClientSideOnResizeEnd**

[] 

In the above example, the ClientSideOnResizeEnd property is set to the \'EventLog(eventName)\' client-side javascript function. This will get executed when the Window is resized.

[] 

[·      ]**ClientSideOnResizeStart**

[] 

In the above example, the ClientSideOnResizeStart property is set to the \'EventLog(eventName)\' client-side javascript function. This will get executed when the Window resizing starts.

[] 

[·      ]**ClientSideOnResize**

[] 

In the above example, the ClientSideOnResize property is set to the \'EventLog(eventName)\' client-side javascript function. This will get executed when the Window is resizing.

[] 

[·      ]**ClientSideOnMove**

[] 

In the above example, the ClientSideOnMove property is set to the \'EventLog(eventName)\' client-side javascript function. This will get executed when the Window is moved.

 

[]{#related-topics}

