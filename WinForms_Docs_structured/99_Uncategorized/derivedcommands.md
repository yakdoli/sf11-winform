---
title: derivedcommands.md
original_path: WinForms_Docs/99_Uncategorized/derivedcommands.md
created_at: 2025-08-05
---






##### Derived Commands {#derived-commands style="tab-stops: 0pt"}

[] 

The Undo / Redo architecture of the Essential Grid is complete as shipped with the product. If, for some reason, you need to handle special grid requirements that cannot be performed with the standard implementation, the Undo / Redo architecture is extensible. To extend it, you need to derive custom command classes from either the abstract class **SyncfusionCommand** or the abstract class **GridModelCommand**. In your derived class, you will need to add whatever members you need in order to track enough state information that will allow you to Undo / Redo the action that is being done. Then you have to implement an execute method and other abstract members of the base class. If you do a search in the Essential Grid source code for GridModelCommand, you will see many examples of the derived command classes.

 

Once you have your derived SyncfusionCommand class, whenever the action is taken, you will have to create a proper instance of your derived SyncfusionCommand class and add it to the **GridControl.CommandStack.UndoStack**. Thus when Essential Grid needs to undo this action, your command will be popped from the **UndoStack**, and its execute method will be called indicating that this action needs to be undone (Also, at this point Essential Grid will add this same instance to the RedoStack so that the action can later be redone if necessary).

 

[]{#p298} 

 

[]{#related-topics}

