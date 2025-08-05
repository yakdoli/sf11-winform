---
title: minitoolbarevents1.md
original_path: WinForms_Docs/99_Uncategorized/minitoolbarevents1.md
created_at: 2025-08-05
---






##### MiniToolBar Events {#minitoolbar-events style="tab-stops: 0pt"}

[] 

This section discusses about various events that can be handled for the MiniToolBar control. Following are the events covered.

[] 

[] 

 

 

 

###### 3.15.1.3.3.1        ItemAdded Event {#itemadded-event style="tab-stops: 0pt"}

[] 

This event is handled when a ToolStripItem has been added to the ToolStrip\'s Item collection.

 

**Event Data**

 

The ToolStripItemEventHandler receives an argument of type ToolStripItemEventArgs containing data related to this event. The following type ToolStripItemEventArgs member provide information specific to this event.[]{#p1172}

[] 


  -------- -----------------------------------------------------------------------
  Member   Description
  Item     Gets a System.Windows.Forms.ToolStripItem for which to handle events.
  -------- -----------------------------------------------------------------------


[]{#p1173}**[]** 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                               |
|                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                              |
| [private][ [void] miniToolBar1_ItemAdded([object] sender, [ToolStripItemEventArgs] arg)] |
|                                                                                                                                                                                                                                              |
| [{]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                              |
| [// You can see the below line in output window during runtime.]                                                                                                                           |
|                                                                                                                                                                                                                                              |
| [Console][.WriteLine([\"ItemAdded event is raised\"]);]                                                                          |
|                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                              |
| [e.Item = ][true][;]                                                                    |
|                                                                                                                                                                                                                                              |
| [//Display the ToolStripItem]                                                                                                                                                              |
|                                                                                                                                                                                                                                              |
| [Console][.WriteLine([\"ToolStrip Item Name : \"] + arg.Item.ToString());]                                                       |
|                                                                                                                                                                                                                                              |
| [}][]                                                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                         |
| [Private][ [Sub] miniToolBar1_ItemAdded([ByVal] sender [As] [Object], [ByVal] e [As] [ToolStripItemEventArgs])] |
|                                                                                                                                                                                                                                                                                                                                                         |
| [You can see the below line in output window during runtime.]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                         |
| [Console.Write([\"ItemAdded event is raised\"])]                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                         |
| [e.Item = ][True]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                         |
| [\'Display the ToolStripItem]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                         |
| [Console.Write([\"ToolStrip Item Name : \"] + arg.Item.ToString)]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                         |
| [End][ [Sub]][]                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

###### 3.15.1.3.3.2        ItemClicked Event {#itemclicked-event style="tab-stops: 0pt"}

[] 

This event is handled when a ToolStripItem has been added to the ToolStrip\'s Item collection.

 

**Event Data**

 

The ToolStripItemClickedEventHandler receives an argument of type ToolStripItemEventArgs containing data related to this event. The following type ToolStripItemEventArgs member provide information specific to this event.

[] 


  ------------- ------------------------------------------------------------------
  Member        Description
  ClickedItem   Gets the item that is clicked on System.Windows.Forms.Toolstrip.
  ------------- ------------------------------------------------------------------


[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                     |
| [private][ [void] miniToolBar1_ItemClicked([object] sender, [ToolStripItemClickedEventArgs] e)] |
|                                                                                                                                                                                                                                                     |
| [{]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                     |
| [// You can see the below line in output window during runtime.]                                                                                                                                  |
|                                                                                                                                                                                                                                                     |
| [Console][.WriteLine([\"ItemClicked event is raised\"]);]                                                                               |
|                                                                                                                                                                                                                                                     |
| [//Display the ToolStripItem that is clicked]                                                                                                                                                     |
|                                                                                                                                                                                                                                                     |
| [Console][.WriteLine([\"ToolStrip Item Name : \"] + arg.ClickedItem.ToString());]                                                       |
|                                                                                                                                                                                                                                                     |
| [}]                                                                                                                                                                                                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [Private][ [Sub] miniToolBar1_ItemClicked([ByVal] sender [As] [Object], [ByVal] e [As] [ToolStripItemClickedEventArgs])] |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [\'You can see the below line in output window during runtime.]                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [Console.Write([\"ItemClicked event is raised\"])]                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [\'Display the ToolStripItem that is clicked]                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [Console.Write([\"ToolStrip Item Name : \"] + arg.ClickedItem.ToString)]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [End][ [Sub]][]                                                                                                                                                                                       |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

###### 3.15.1.3.3.3        ItemRemoved Event {#itemremoved-event style="tab-stops: 0pt"}

[] 

This event is handled when a ToolStripItem has been removed from the ToolStrip\'s Item collection.

[] 

Event Data

**[]** 

The ToolStripItemEventHandler receives an argument of type ToolStripItemEventArgs containing data related to this event. The following ToolStripItemEventArgs member provide information specific to this event.

[] 


  -------- -----------------------------------------------------------------------
  Member   Description
  Item     Gets a System.Windows.Forms.ToolStripItem for which to handle events.
  -------- -----------------------------------------------------------------------


[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                               |
|                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                              |
| [private][ [void] miniToolBar1_ItemClicked([object] sender, [ToolStripItemEventArgs] e)] |
|                                                                                                                                                                                                                                              |
| [{]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                              |
| [e.Item = ][true][;]                                                                    |
|                                                                                                                                                                                                                                              |
| [}]                                                                                                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p1174}[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                           |
| [Private][ [Sub] miniToolBar1_ItemClicked([ByVal] sender [As] [Object], [ByVal] e [As] [ToolStripItemEventArgs])] |
|                                                                                                                                                                                                                                                                                                                                                           |
| [e.Item = ][True]                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                           |
| [End][ [Sub]][]                                                                                                                                                                                |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

###### 3.15.1.3.3.4        BeginDrag Event {#begindrag-event style="tab-stops: 0pt"}

[] 

This event is handled when the toolstrip has started to move with a ToolStripPanel.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                       |
|                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                  |
|                                                                                                                                                                                                                                      |
| [private][ [void] miniToolBar1_BeginDrag([object] sender, System.[EventArgs] e)] |
|                                                                                                                                                                                                                                      |
| [{]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                      |
| [//You can see the below line in output window during runtime.]                                                                                                                    |
|                                                                                                                                                                                                                                      |
| [Console][.Write([\"BeginDrag Event is raised\"]);]                                                                      |
|                                                                                                                                                                                                                                      |
| [}][]                                                                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                   |
| [Private][ [Sub] miniToolBar1_BeginDrag([ByVal] sender [As] [Object], [ByVal] e [As] System.[EventArgs])] |
|                                                                                                                                                                                                                                                                                                                                                   |
| [/You can see the below line in output window during runtime.]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                   |
| [Console][.Write([\"BeginDrag Event is raised\"]);]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                   |
| [End][ [Sub]][]                                                                                                                                                                        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

###### 3.15.1.3.3.5        Opening Event {#opening-event style="tab-stops: 0pt"}

[] 

This event occurs when the drop down is opening.

 

**Event Data**

 

The CancelEventHandler receives an argument of type CancelEventArgs containing data related to this event. The following CancelEventArgs members provide information specific to this event.

[] 


  -------- -----------------------------------------------------------------------
  Member   Description
  Cancel   Gets or Sets a value indicating whether the event should be canceled.
  -------- -----------------------------------------------------------------------


[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                         |
| [private][ [void] miniToolBar1_Opening([object] sender, System.ComponentModel.[CancelEventArgs] e)] |
|                                                                                                                                                                                                                                                         |
| [{]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                         |
| [//EventArgs can give the options to Allow or Cancel the event by this method.]                                                                                                                     |
|                                                                                                                                                                                                                                                         |
| [//Cancel is the boolean property which can prevent docking event when it is true.]                                                                                                                 |
|                                                                                                                                                                                                                                                         |
| [e.Cancel=][true][;]                                                                               |
|                                                                                                                                                                                                                                                         |
| [}][]                                                                                                                                                                           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                      |
| [Private][ [Sub] miniToolBar1_Opening([ByVal] sender [As] [Object], [ByVal] e [As] System.ComponentModel.[CancelEventArgs])] |
|                                                                                                                                                                                                                                                                                                                                                                      |
| [//EventArgs can give the options to Allow or Cancel the event by this method.]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                      |
| [//Cancel is the boolean property which can prevent docking event when it is true.]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                      |
| [e.Cancel=][true][;]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                      |
| [End][ [Sub]][]                                                                                                                                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

###### 3.15.1.3.3.6        Opened Event {#opened-event style="tab-stops: 0pt"}

[] 

This event occurs when the drop down has opened.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                    |
|                                                                                                                                                                                                                                   |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                                                   |
| [private][ [void] miniToolBar1_Opened([object] sender, System.[EventArgs] e)] |
|                                                                                                                                                                                                                                   |
| [{]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                   |
| [// You can see the below line in output window during runtime.]                                                                                                                |
|                                                                                                                                                                                                                                   |
| [Console][.Write([\" Opened Event is raised\"]);]                                                                     |
|                                                                                                                                                                                                                                   |
| [}]                                                                                                                                                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p1175}[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                |
| [Private][ [Sub] miniToolBar1_Opened([ByVal] sender [As] [Object], [ByVal] e [As] System.[EventArgs])] |
|                                                                                                                                                                                                                                                                                                                                                |
| [\'You can see the below line in output window during runtime.]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                |
| [Console][.Write([\" Opened Event is raised\"]);]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                |
| [End][ [Sub]][]                                                                                                                                                                     |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

[]{#related-topics}

