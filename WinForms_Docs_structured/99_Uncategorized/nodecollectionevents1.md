---
title: nodecollectionevents1.md
original_path: WinForms_Docs/99_Uncategorized/nodecollectionevents1.md
created_at: 2025-08-05
---






##### Node Collection Events {#node-collection-events style="tab-stops: 0pt"}

[] 

This topic discusses the events that are fired while adding or removing the node to or from the node collection. The below table discusses all the available node collection events.

[] 


  ------------------------ ------------------------------------------------------------
  DiagramViewerEventSink   Description
  NodeCollectionChanged    Triggered after the node collection changes are completed.
  NodeCollectionChanging   Triggered when the node collection is edited.
  ------------------------ ------------------------------------------------------------


[] 

EventArgs members can be accessed using the following members.

[] 


+-----------------------------------+---------------------------------------------------------------------------------------+
| NodeCollection EventArgs Member   | Description                                                                           |
+-----------------------------------+---------------------------------------------------------------------------------------+
| Cancel                            | Indicates whether the NodeCollectionChanged event should be canceled.                 |
+-----------------------------------+---------------------------------------------------------------------------------------+
| ChangeType                        | It returns the following possible values:                                             |
|                                   |                                                                                       |
|                                   | []  |
|                                   |                                                                                       |
|                                   | [·      ]Insert - whether the node is inserted           |
|                                   |                                                                                       |
|                                   | [·      ]Remove -- whether the node is removed           |
+-----------------------------------+---------------------------------------------------------------------------------------+
| Element                           | Returns whether the head or tail end is moved.                                        |
+-----------------------------------+---------------------------------------------------------------------------------------+
| Elements                          | Returns the elements collection on which the event occurs.                            |
+-----------------------------------+---------------------------------------------------------------------------------------+
| Index                             | Returns the zero-based index into the collection on which the event occurred.         |
+-----------------------------------+---------------------------------------------------------------------------------------+
| Owner                             | Returns the base class onto which the node is added.                                  |
+-----------------------------------+---------------------------------------------------------------------------------------+


[] 

Inside the NodeCollectionChanged event handler, user can identify whether a node is added or removed from the node collection using simple message box as follows.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                           |
| [private][ [void] Form1_Load([object] sender, [EventArgs] e)]                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                           |
| [{]                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                           |
| [    ((DiagramViewerEventSink)diagram1.EventSink).NodeCollectionChanged += [new] CollectionExEventHandler(Form1_NodeCollectionChanged)((DiagramViewerEventSink)diagram1.EventSink).NodeCollectionChanging += [new] CollectionExEventHandler(Form1_NodeCollectionChanging);] |
|                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                           |
| [    [RectangleF] rect = [new] [RectangleF](100, 100, 100, 100);]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                           |
| [    RichTextNode richText = [new] RichTextNode([\"\"], rect);]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                           |
| [    richText.Text = [\"Rich text box\"];]                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                           |
| [    NodeCollection nodeStack = [new] NodeCollection();]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                           |
| [    nodeStack.Add(richText);]                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                           |
| [    [MessageBox].Show(nodeStack.Count.ToString());]                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                           |
| [}]                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                           |
| [private][ [void] Form1_NodeCollectionChanging(CollectionExEventArgs e)]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                           |
| [{]                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                           |
| [    [MessageBox].Show([\"NodeCollectionChanging event fired\"]);]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                           |
| [}]                                                                                                                                                                                                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [Private][ [Sub] Form1_Load([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)]                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [    [DirectCast](diagram1.EventSink, DiagramViewerEventSink).NodeCollectionChanged += [New] CollectionExEventHandler(Form1_NodeCollectionChanged)([DirectCast](diagram1.EventSink, DiagramViewerEventSink)).NodeCollectionChanging += [New] CollectionExEventHandler(Form1_NodeCollectionChanging)] |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [    [Dim] rect [As] [New] RectangleF(100, 100, 100, 100)]                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [    [Dim] richText [As] [New] RichTextNode([\"\"], rect)]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [    richText.Text = [\"Rich text box\"]]                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [    [Dim] nodeStack [As] [New] NodeCollection()]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [    nodeStack.Add(richText)]                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [    MessageBox.Show(nodeStack.Count.ToString())]                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [End][ [Sub]]                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [Private][ [Sub] Form1_NodeCollectionChanging([ByVal] e [As] CollectionExEventArgs)]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [    MessageBox.Show([\"NodeCollectionChanging event fired\"])]                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [End][ [Sub]]                                                                                                                                                                                                                                                                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Sample diagrams are as follows,

[] 

{border="0"}

**[]** 

Figure 95: Node Collection Changing Event

**[]** 

{border="0"}

**[]** 

Figure 96: Node collection Changed Event

 

[]{#p57} 

 

[]{#related-topics}

