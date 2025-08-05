---
title: clientsideevents16.md
original_path: WinForms_Docs/99_Uncategorized/clientsideevents16.md
created_at: 2025-08-05
---






##### Client-side Events {#client-side-events style="tab-stops: 0pt"}

[] 

The PopupContainer control provides the flexibility to invoke functions on client side which can be triggered on some user action.\
To invoke the client side events:

[] 

1.   In HTML view of the project, add the following client side javascript content inside the \<script\> tags.

2.   Here, methods like **OnPopup**, **OnPopUpCloseup** and **OnBeforePopup** are called to display the event that is being called before the popup container is shown, when the popup container is shown and after the container is closed.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\<][script][ [type][=\"text/javascript\"\>]] |
|                                                                                                                                                                                                                                |
| [function][ OnPopup()]                                                                                                                    |
|                                                                                                                                                                                                                                |
| [{]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                |
| [        var][ oEl = document.getElementById([\"txtEvent\"]);]                                                     |
|                                                                                                                                                                                                                                |
| [        oEl.innerHTML = [\"PopupControlContainer is being shown\"];]                                                                                               |
|                                                                                                                                                                                                                                |
| [}]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                |
| [function][ OnPopupCloseUp()]                                                                                                             |
|                                                                                                                                                                                                                                |
| [{]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                |
| [        [var] oEl = document.getElementById([\"txtEvent\"]);]                                                                                 |
|                                                                                                                                                                                                                                |
| [        oEl.innerHTML = [\"PopupControlContainer has been closed\"];]                                                                                              |
|                                                                                                                                                                                                                                |
| [}]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                |
| [function][ OnBeforePopup()]                                                                                                              |
|                                                                                                                                                                                                                                |
| [{]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                |
| [        var][ oEl1 = document.getElementById([\"textBeforePopup\"]);]                                             |
|                                                                                                                                                                                                                                |
| [        [var] oEl2 = document.getElementById([\"text1\"]);]                                                                                   |
|                                                                                                                                                                                                                                |
| [        oEl1.innerHTML = oEl2.value;]                                                                                                                                                     |
|                                                                                                                                                                                                                                |
| [}]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                |
| [\</][script][\>]                                                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Build and run the application. On performing some action like clicking the popup to open and on close the client actions will be triggered.

[] 

{border="0"}

**[]** 

Figure 416: Before the Popup container is shown the Client side event is called

**[]** 

{border="0"}

**[]** 

Figure 417: When the Popup container is shown the Client side event is called

[] 

{border="0"}

**[]** 

Figure 418: After the Popup container is closed the Client side event is called

 

[]{#related-topics}

