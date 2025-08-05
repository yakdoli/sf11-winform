---
title: howtodetectwhetheranewsymbolorshapehasbeenaddedremovedfromadiagram.md
original_path: WinForms_Docs/04_Controls/Diagram/howtodetectwhetheranewsymbolorshapehasbeenaddedremovedfromadiagram.md
created_at: 2025-08-05
---








  









## How To Detect Whether a New Symbol Or Shape Has Been Added / Removed From A Diagram {#how-to-detect-whether-a-new-symbol-or-shape-has-been-added-removed-from-a-diagram style="tab-stops: 0pt"}

[] 

You can make use of the **Diagram.Model.EventSink.NodeCollectionChanged** to detect whether a new node (symbol, shape or link) has been added/removed from a diagram. The event\'s **CollectionExEventArgs** argument provides information about the node ensuing the add / remove operation.

 

The following code snippet updates a label with information on the type of the node that is added/deleted from the diagram.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                          |
|                                                                                                                                                                                                         |
| []                                                                                                                                                    |
|                                                                                                                                                                                                         |
| [diagram1.Model.EventSink.NodeCollectionChanged += [new] [CollectionExEventHandler](EventSink_NodeCollectionChanged);] |
|                                                                                                                                                                                                         |
| []                                                                                                                                                    |
|                                                                                                                                                                                                         |
| [//ChildrenChangeComplete Event]                                                                                                                      |
|                                                                                                                                                                                                         |
| [//Update Label2 depending on whether a Shape is added or deleted from the Diagram]                                                                   |
|                                                                                                                                                                                                         |
| [ [private] [void] EventSink_NodeCollectionChanged([CollectionExEventArgs] evtArgs)]              |
|                                                                                                                                                                                                         |
| [ {]                                                                                                                                                                |
|                                                                                                                                                                                                         |
| [            [Node] n = evtArgs.Element [as] [Node];]                                          |
|                                                                                                                                                                                                         |
| []                                                                                                                                                                  |
|                                                                                                                                                                                                         |
| [            [//ChangeType specifies whether the Collection change is Insertion/Removal]]                                                     |
|                                                                                                                                                                                                         |
| [            [if] (evtArgs.ChangeType == [CollectionExChangeType].Insert)]                                             |
|                                                                                                                                                                                                         |
| [            {]                                                                                                                                                     |
|                                                                                                                                                                                                         |
| [                [this].label2.ForeColor = [Color].Blue;]                                                              |
|                                                                                                                                                                                                         |
| []                                                                                                                                                                  |
|                                                                                                                                                                                                         |
| [                [//Gets the Name of the inserted element]]                                                                                   |
|                                                                                                                                                                                                         |
| [                [this].label2.Text = [\"Last Node Added : \"] + n.Name.ToString();]                                   |
|                                                                                                                                                                                                         |
| [            }]                                                                                                                                                     |
|                                                                                                                                                                                                         |
| [            [else] [if] (evtArgs.ChangeType == [CollectionExChangeType].Remove)]                 |
|                                                                                                                                                                                                         |
| [            {]                                                                                                                                                     |
|                                                                                                                                                                                                         |
| [                [this].label2.ForeColor = [Color].Red;]                                                               |
|                                                                                                                                                                                                         |
| []                                                                                                                                                                  |
|                                                                                                                                                                                                         |
| [                [//Gets the Name of the removed element]]                                                                                    |
|                                                                                                                                                                                                         |
| [                [this].label2.Text = [\"Last Node Removed : \"] + n.Name.ToString();]                                 |
|                                                                                                                                                                                                         |
| [            }]                                                                                                                                                     |
|                                                                                                                                                                                                         |
| [ }        ]                                                                                                                                                        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                            |
| [EventSink.NodeCollectionChanged += [new] [CollectionExEventHandler](EventSink_NodeCollectionChanged)]                                                                    |
|                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                            |
| [Me][.Diagram1.Model.EventSink.NodeCollectionChanged+=[New] [CollectionExEventHandler](EventSink_NodeCollectionChanged)] |
|                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                            |
| [ [\'ChildrenChangeComplete Event]]                                                                                                                                                              |
|                                                                                                                                                                                                                                                            |
| [ [\'Update Label2 depending on whether a Shape is added or deleted from the Diagram]]                                                                                                           |
|                                                                                                                                                                                                                                                            |
| [ [Private] [Sub] Model_ChildrenChangeComplete([ByVal] evtArgs [As] CollectionExEventArgs)]                                        |
|                                                                                                                                                                                                                                                            |
| [        [Dim] n [As] Node = [TryCast](evtArgs.Element, Node)]                                                                                          |
|                                                                                                                                                                                                                                                            |
| [        \'[ChangeType specifies whether the Collection change is Insertion/Removal]]                                                                                                            |
|                                                                                                                                                                                                                                                            |
| [        [If] evtArgs.ChangeType = CollectionExChangeType.Insert [Then]]                                                                                                     |
|                                                                                                                                                                                                                                                            |
| [            [Me].label2.ForeColor = Color.Blue]                                                                                                                                                  |
|                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                            |
| [            \'[Gets the Name of the inserted element]]                                                                                                                                          |
|                                                                                                                                                                                                                                                            |
| [            [Me].label2.Text = [\"Last Node Added: \"] + n.Name.ToString()]                                                                                              |
|                                                                                                                                                                                                                                                            |
| [        [ElseIf] evtArgs.ChangeType = CollectionExChangeType.Remove [Then]]                                                                                                 |
|                                                                                                                                                                                                                                                            |
| [            [Me].label2.ForeColor = Color.Red]                                                                                                                                                   |
|                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                            |
| [            \'[Gets the Name of the removed element]]                                                                                                                                           |
|                                                                                                                                                                                                                                                            |
| [            [Me].label2.Text = [\"Last Node Removed: \"] + n.Name.ToString()]                                                                                            |
|                                                                                                                                                                                                                                                            |
| [        [End] [If]]                                                                                                                                                         |
|                                                                                                                                                                                                                                                            |
| [    [End] [Sub]]                                                                                                                                                            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p81} 

 

[]{#related-topics}

