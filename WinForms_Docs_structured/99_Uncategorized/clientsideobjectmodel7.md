---
title: clientsideobjectmodel7.md
original_path: WinForms_Docs/99_Uncategorized/clientsideobjectmodel7.md
created_at: 2025-08-05
---






##### Client-Side Object Model {#client-side-object-model style="tab-stops: 0pt"}

[] 

Methods

**[]** 


  ----------------------------------- ----------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Method                              Parameter   Description
  Refresh                             string      []{#DDE_LINK1}**For .NET Framework version 2.0 only.** Sends callback to server without page refreshing and triggers CallbackRefresh server side TabStrip\'s event. To perform callback the **EnableCallbacks** property must be set to true .
  GetMultiPageID                      \-          Gets a value specifies the id of the multipage control to be integrated with tabstrip.
  SetMultiPageID                      string      Sets a value specifies the id of the multipage control to be integrated with tabstrip.
  SelectTabByText(\"TabText\")                    Selects TabStrip item based on the TabText.
  SelectTabByID(\"TabStripItemID\")               Selects TabStrip item based on the ID of the TabStrip item
  SelectTabByIndex(Index)                         Selects TabStrip Item based on index.
  SelectTab(TabStripItemObj)                      Selects TabStrip item based on the Tabstrip Object
  ----------------------------------- ----------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


[] 

TabStrip\'s ClientEventData Object

**[]** 


  ------------ ------------- -----------------------------------------------------------------------------------
  Property     Parameter     Description
  ID           string        Specifies the client side item identifier.
  Text         string        Specifies the item text.
  PageViewID   string        Specifies ID of PageView element.
  Tooltip      string        Specifies the help message that showing when user moves mouse over TabStrip item.
  Disabled     bool          Specifies whether item is disabled.
  TemplateID   string        Specifies template ID which associates item with custom template.
  NaviURL      string        Specifies the item\'s target URL.
  HtmlID       string        Specifies the client side TabStrip identifier.
  Element      HTMLElement   Represents HTML item element.
  Event        object        Represents event.
  ------------ ------------- -----------------------------------------------------------------------------------


**[]** 

**[]** 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[JavaScript\]]**                                                                                                                              |
|                                                                                                                                                                                                       |
| []                                                                                                                                   |
|                                                                                                                                                                                                       |
| [function][ OnItemSelect( EventData )]                                           |
|                                                                                                                                                                                                       |
| [{]                                                                                                                                               |
|                                                                                                                                                                                                       |
| [       [var] sText = [\"You selected item \'\"] + EventData.Text + [\"\'\"];] |
|                                                                                                                                                                                                       |
| [       alert( sText );]                                                                                                                          |
|                                                                                                                                                                                                       |
| [}]                                                                                                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

The following code illustrates how to select the tab by **SelectTabByText** method.

[] 

+------------------------------------------------------------------------------------------------------------------+
| **[\[Javascript\]]**                                                |
|                                                                                                                  |
| [function][ selectbytext()] |
|                                                                                                                  |
| [     {   ]                                                                  |
|                                                                                                                  |
| [         Tab1_client.SelectTabByText([\"Tab1\"]);]  |
|                                                                                                                  |
| [         [return] [false];]       |
|                                                                                                                  |
| [     }]                                                                     |
+------------------------------------------------------------------------------------------------------------------+

**[]** 

The following code illustrates how to select the tab by **SelectTabByID** method.

+----------------------------------------------------------------------------------------------------------------+
| **[\[Javascript\]]**                                              |
|                                                                                                                |
| [function][ selectbyid()] |
|                                                                                                                |
| [     {  ]                                                                 |
|                                                                                                                |
| [         Tab1_client.SelectTabByID([\"Tab1\"]);]  |
|                                                                                                                |
| [         [return] [false];]     |
|                                                                                                                |
| [     }]                                                                   |
+----------------------------------------------------------------------------------------------------------------+

[     ]

The following code illustrates how to select the tab by **SelectTabByIndex** method[.]

[] 

+-------------------------------------------------------------------------------------------------------------------+
| **[\[Javascript\]]**                                                 |
|                                                                                                                   |
| [function][ selectbyindex()] |
|                                                                                                                   |
| [     {  ]                                                                    |
|                                                                                                                   |
| [         Tab1_client.SelectTabByIndex(0);]                                   |
|                                                                                                                   |
| [         [return] [false];]        |
|                                                                                                                   |
| [     }]                                                                      |
+-------------------------------------------------------------------------------------------------------------------+

[] 

The following code illustrates selects the tab by the Tab Item's client object.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Javascript\]]**                                                                             |
|                                                                                                                                               |
| [function][ selectbytabobj()]                            |
|                                                                                                                                               |
| [     {  ]                                                                                                |
|                                                                                                                                               |
| [         [var] obj = Tab1_client.FindItemByID([\"Tab1\"]);] |
|                                                                                                                                               |
| [         Tab1_client.SelectTab(obj);]                                                                    |
|                                                                                                                                               |
| [         [return] [false];]                                    |
|                                                                                                                                               |
| [     }]                                                                                                  |
+-----------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

