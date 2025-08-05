---
title: transactions.md
original_path: WinForms_Docs/99_Uncategorized/transactions.md
created_at: 2025-08-05
---






##### Transactions {#transactions style="tab-stops: 0pt"}

[] 

A[ ]transaction[ ]is a series of steps that should be treated as a single action in the Undo / Redo architecture. For example, you may have a record-oriented grid where you may want to group any changes in the current row as one transaction. This way when the user wants to undo the last change, all the changes in the row are undone. It is possible to group a series of actions into a single Undo / Redo step through the use of these three **GridCommandStack** methods: **BeginTrans**, **CommitTrans** and **RollBack**.

 

A call to BeginTrans will mark the start of a series of actions that are to be treated as a single Undo / Redo step. Once BeginTrans has begun, all the changes are marked as being a member of a single transaction until either CommitTrans or RollBack is called. CommitTrans signals a successful end to the transaction. A call to RollBack will cause all the changes in the current transaction to be undone and will end the transaction processing. A RollBack call will return the grid in the same state that it was in, immediately prior to the call to BeginTrans.

 

It is possible to nest transactions. If you are in the middle of a transaction, it is OK to call BeginTrans again. But, when such nested transactions are undone, they are treated as part of a single parent transaction.

 

[]{#p297} 

 

[]{#related-topics}

