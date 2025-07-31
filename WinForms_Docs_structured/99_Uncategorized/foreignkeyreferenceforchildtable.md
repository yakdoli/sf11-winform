---
title: foreignkeyreferenceforchildtable.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\foreignkeyreferenceforchildtable.md
created_at: 2025-07-03
---






#### Foreign Key Reference For Child Table {#foreign-key-reference-for-child-table style="tab-stops: 0pt"}

When you want to create a relation between the child and grandchild table with ForeignKeyReference, set the *RelationKind* property of *GridRelationDescriptor* to *ForeignKeyReference*.

[] 

[] 

The following code illustrates this:

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                            |
| [public][ Form1()]                                                                                                                                                    |
|                                                                                                                                                                                                                                                            |
| [     {]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                            |
| [// To Add relation to ParentTable][]                                                                                                                                |
|                                                                                                                                                                                                                                                            |
| [                  [GridRelationDescriptor] parentToChildRelationDescriptor = [new] [GridRelationDescriptor]();]                                  |
|                                                                                                                                                                                                                                                            |
| [                  parentToChildRelationDescriptor.ChildTableName = [\"MyChildTable\"];    [// same as SourceListSetEntry.Name for childTable (see below)]]              |
|                                                                                                                                                                                                                                                            |
| [                  parentToChildRelationDescriptor.RelationKind = [RelationKind].RelatedMasterDetails;]                                                                                        |
|                                                                                                                                                                                                                                                            |
| [                  parentToChildRelationDescriptor.RelationKeys.Add([\"parentID\"], [\"ParentID\"]);]                                                                  |
|                                                                                                                                                                                                                                                            |
| [            parentToChildRelationDescriptor.ChildTableDescriptor.VisibleColumns.Add([\"Name\"]);]                                                                                             |
|                                                                                                                                                                                                                                                            |
| [            parentToChildRelationDescriptor.ChildTableDescriptor.VisibleColumns.Add([\"MyGrandChildTable_Name\"]);]                                                                           |
|                                                                                                                                                                                                                                                            |
| [                  ]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                            |
| [                  gridGroupingControl1.TableDescriptor.Relations.Add(parentToChildRelationDescriptor);]                                                                                                               |
|                                                                                                                                                                                                                                                            |
| [            ][]                                                                                                                                                      |
|                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                            |
| [   ][ [// To add Relation to GrandChildTable in Childtable like look up]]                                                                      |
|                                                                                                                                                                                                                                                            |
| [            [GridRelationDescriptor] childToGrandChildRelationDescriptor = [new] [GridRelationDescriptor]();]                                    |
|                                                                                                                                                                                                                                                            |
| [                  childToGrandChildRelationDescriptor.ChildTableName = [\"MyGrandChildTable\"];  [// same as SourceListSetEntry.Name for grandChhildTable (see below)]] |
|                                                                                                                                                                                                                                                            |
| [                  childToGrandChildRelationDescriptor.RelationKind = [RelationKind].ForeignKeyReference;]                                                                                     |
|                                                                                                                                                                                                                                                            |
| [                  childToGrandChildRelationDescriptor.RelationKeys.Add([\"childID\"], [\"GrandChildID\"]);]                                                           |
|                                                                                                                                                                                                                                                            |
| [            childToGrandChildRelationDescriptor.ChildTableDescriptor.VisibleColumns.Add([\"GrandChildID\"]);]                                                                                 |
|                                                                                                                                                                                                                                                            |
| [            childToGrandChildRelationDescriptor.ChildTableDescriptor.VisibleColumns.Add([\"Name\"]);]                                                                                         |
|                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                            |
| [    //Add relation to ChildTable]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                            |
| [            parentToChildRelationDescriptor.ChildTableDescriptor.Relations.Add(childToGrandChildRelationDescriptor);]                                                                                                 |
|                                                                                                                                                                                                                                                            |
| [        ]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                            |
| [}]                                                                                                                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**[]                                                                                                         |
|                                                                                                                                                                                                |
| [Public][ [Sub] [New]()]                                        |
|                                                                                                                                                                                                |
| [            [\' To Add relation to ParentTable]]                                                                                    |
|                                                                                                                                                                                                |
| [            [Dim] parentToChildRelationDescriptor [As] [New] GridRelationDescriptor()]     |
|                                                                                                                                                                                                |
| [            parentToChildRelationDescriptor.ChildTableName = [\"MyChildTable\"]]                                                  |
|                                                                                                                                                                                                |
| [            parentToChildRelationDescriptor.RelationKind = RelationKind.RelatedMasterDetails]                                                             |
|                                                                                                                                                                                                |
| [            parentToChildRelationDescriptor.RelationKeys.Add([\"parentID\"], [\"ParentID\"])]             |
|                                                                                                                                                                                                |
| [            parentToChildRelationDescriptor.ChildTableDescriptor.VisibleColumns.Add([\"Name\"])]                                  |
|                                                                                                                                                                                                |
| [            parentToChildRelationDescriptor.ChildTableDescriptor.VisibleColumns.Add([\"MyGrandChildTable_Name\"])]                |
|                                                                                                                                                                                                |
| []                                                                                                                                                         |
|                                                                                                                                                                                                |
| [            gridGroupingControl1.TableDescriptor.Relations.Add(parentToChildRelationDescriptor)]                                                          |
|                                                                                                                                                                                                |
| []                                                                                                                                                         |
|                                                                                                                                                                                                |
| [            [\' To add Relation to GrandChildTable in Childtable like look up]]                                                     |
|                                                                                                                                                                                                |
| [            [Dim] childToGrandChildRelationDescriptor [As] [New] GridRelationDescriptor()] |
|                                                                                                                                                                                                |
| [            childToGrandChildRelationDescriptor.ChildTableName = [\"MyGrandChildTable\"]]                                         |
|                                                                                                                                                                                                |
| [            childToGrandChildRelationDescriptor.RelationKind = RelationKind.ForeignKeyReference]                                                          |
|                                                                                                                                                                                                |
| [            childToGrandChildRelationDescriptor.RelationKeys.Add([\"childID\"], [\"GrandChildID\"])]      |
|                                                                                                                                                                                                |
| [            childToGrandChildRelationDescriptor.ChildTableDescriptor.VisibleColumns.Add([\"GrandChildID\"])]                      |
|                                                                                                                                                                                                |
| [            childToGrandChildRelationDescriptor.ChildTableDescriptor.VisibleColumns.Add([\"Name\"])]                              |
|                                                                                                                                                                                                |
| []                                                                                                                                                         |
|                                                                                                                                                                                                |
| [            [\'Add relation to ChildTable]]                                                                                         |
|                                                                                                                                                                                                |
| [            parentToChildRelationDescriptor.ChildTableDescriptor.Relations.Add(childToGrandChildRelationDescriptor)]                                      |
|                                                                                                                                                                                                |
| [        [End] [Sub]]                                                                                            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#related-topics}

