---
title: usingundoredo.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingundoredo.md
created_at: 2025-07-03
---






#### Using Undo/Redo {#using-undoredo style="tab-stops: 0pt"}

[] 

Essential Grid supports Undo/Redo functionalities similar to the one achieved with MS-Office type application. To handle this functionality, a stack is maintained internally in Essential Grid, to save the changes handled, through which the following tasks can be accomplished by the users directly.

[] 

[·      ]Allows to control the stack-when to save/unsave the changes, and when to rollback changes

[·      ]Allows to create new transactions, and control each individual transaction(like cancelling, rollback) without affecting the others

[] 

The Undo/Redo architecture is extensible thereby allowing the users to derive the base class, and add some more requirements for the Essential Grid.

[] 

See Also

[]{#p295} 

 

More:









