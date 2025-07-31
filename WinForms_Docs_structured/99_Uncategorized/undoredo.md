---
title: undoredo.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\undoredo.md
created_at: 2025-07-03
---








  









### Undo / Redo {#undo-redo style="tab-stops: 0pt"}

[] 

The actions can be recorded into the history manager such that the undo and redo operations can be performed. The recording can be controlled and the undo and redo actions can be performed using the following tools.

[] 


  ---------------------- -----------------------------------------------------------------------------------------------------
  History Manager Tool   Description
  Undo                   Undo the previous action.
  Redo                   Redo the previous action. Redo action can be performed only after an undo action.
  StartAtomicAction      Stops recording the actions and hence will not be added to the undo history manager.
  EndAtomicAction        Cancels the StartAtomicAction process and turns on the recording of actions in the history manager.
  ---------------------- -----------------------------------------------------------------------------------------------------


[] 

Programmatically, it is implemented as follows:

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                             |
|                                                                                                                                                                                                                            |
| []                                                                                                                                                                     |
|                                                                                                                                                                                                                            |
| [this][.diagram1.Model.HistoryManager.Undo(); ]                                                       |
|                                                                                                                                                                                                                            |
| [this][.diagram1.Model.HistoryManager.Redo();]                                                        |
|                                                                                                                                                                                                                            |
| [this][.diagram1.Model.HistoryManager.StartAtomicAction([\"Custom Action\"]);] |
|                                                                                                                                                                                                                            |
| [this][.diagram1.Model.HistoryManager.EndAtomicAction();]                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                          |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                     |
|                                                                                                                                                                                                                         |
| [Me][.diagram1.Model.HistoryManager.Undo()]                                                        |
|                                                                                                                                                                                                                         |
| [Me][.diagram1.Model.HistoryManager.Redo()]                                                        |
|                                                                                                                                                                                                                         |
| [Me][.diagram1.Model.HistoryManager.StartAtomicAction([\"Custom Action\"])] |
|                                                                                                                                                                                                                         |
| [Me][.diagram1.Model.HistoryManager.EndAtomicAction()]                                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p47} 

 

[]{#related-topics}

