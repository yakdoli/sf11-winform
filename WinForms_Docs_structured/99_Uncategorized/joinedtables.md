---
title: joinedtables.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\joinedtables.md
created_at: 2025-07-03
---








  









### Joined Tables {#joined-tables style="tab-stops: 0pt"}

 

[] 

[·      ]Tables are merged via ForeignKeyReference relation types and the resultant table is grouped.

[·      ]Summary descriptors are added to calculate the total and average shares for the different accounts.

[·      ]Frozen headers and scrollbar functionality of the grid can be toggled accordingly.

[·      ]Hyperlink control is added to the Item template, and data are retrieved relative to the \'AccountID\' and it is connected to the URL.

[·      ]We can customize the RelationDescriptor to display child columns in parent. This can be done by setting the**[ ]**RelationKind as "ForeignKeyReference" which will force the grid to render child columns next to parent columns instead of hierarchy view.

[·      ]Relationkey is added to define relation between the datasources.

[] 

Example

**** 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                           |
|                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                            |
| [// 1st DataSource (Displayed at LeftSide)][]                                                                                                        |
|                                                                                                                                                                                                                                            |
| [Parent1 = GetParent();]                                                                                                                                                                               |
|                                                                                                                                                                                                                                            |
| [// 2nd DataSource (Displayed at RightSide)][]                                                                                                       |
|                                                                                                                                                                                                                                            |
| [Child = GetChild();]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                            |
| [//Adding relation to parent table][]                                                                                                                |
|                                                                                                                                                                                                                                            |
| [GridRelationDescriptor][ ChildTableRelationDescriptor = [new] [GridRelationDescriptor]();]           |
|                                                                                                                                                                                                                                            |
| [ChildTableRelationDescriptor.ChildTableName = [\"Orders\"];]                                                                                                                  |
|                                                                                                                                                                                                                                            |
| [ChildTableRelationDescriptor.ChildTableDescriptor.AllowNew = [false];]                                                                                                           |
|                                                                                                                                                                                                                                            |
| [//Mentioning RelationKind as "ForeignKeyReference" will force the grid to render child columns next to parent columns. Instead of Hierarchy View][] |
|                                                                                                                                                                                                                                            |
| [ChildTableRelationDescriptor.RelationKind = [RelationKind].ForeignKeyReference;]                                                                                              |
|                                                                                                                                                                                                                                            |
| [// Key need to be added to define relation of two datasource][]                                                                                     |
|                                                                                                                                                                                                                                            |
| [ChildTableRelationDescriptor.RelationKeys.Add([\"Customer ID\"], [\"Customer ID\"]);]                                                                 |
|                                                                                                                                                                                                                                            |
| [GridGroupingControl1.TableDescriptor.Relations.Add(ChildTableRelationDescriptor);]                                                                                                                    |
|                                                                                                                                                                                                                                            |
| [//Register DataTable with SourceListSet,, so that RelationDescriptor can resolve the name ][]                                                       |
|                                                                                                                                                                                                                                            |
| [this][.GridGroupingControl1.Engine.SourceListSet.Add([\"Customers\"], Parent1);]                                             |
|                                                                                                                                                                                                                                            |
| [this][.GridGroupingControl1.Engine.SourceListSet.Add([\"Orders\"], Child);]                                                  |
|                                                                                                                                                                                                                                            |
| [this][.GridGroupingControl1.DataSource = Parent1;]                                                                                                   |
|                                                                                                                                                                                                                                            |
| [this][.GridGroupingControl1.DataBind();]                                                                                                             |
|                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

**** 

**** 

**** 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                           |
|                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                            |
| [\' 1st DataSource (Displayed at LeftSide)][]                                                                                                        |
|                                                                                                                                                                                                                                            |
| [Parent1 = GetParent()]                                                                                                                                                                                |
|                                                                                                                                                                                                                                            |
| [\' 2nd DataSource (Displayed at RightSide)][]                                                                                                       |
|                                                                                                                                                                                                                                            |
| [Child = GetChild()]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                            |
| [\'Adding relation to parent table][]                                                                                                                |
|                                                                                                                                                                                                                                            |
| [Dim][ ChildTableRelationDescriptor [As] GridRelationDescriptor = [New] GridRelationDescriptor()]           |
|                                                                                                                                                                                                                                            |
| [ChildTableRelationDescriptor.ChildTableName = \"Orders\"]                                                                                                                                             |
|                                                                                                                                                                                                                                            |
| [ChildTableRelationDescriptor.ChildTableDescriptor.AllowNew = [False]]                                                                                                            |
|                                                                                                                                                                                                                                            |
| [\'Mentioning RelationKind as "ForeignKeyReference" will force the grid to render child columns next to parent columns. Instead of Hierarchy View][] |
|                                                                                                                                                                                                                                            |
| [ChildTableRelationDescriptor.RelationKind = RelationKind.ForeignKeyReference]                                                                                                                         |
|                                                                                                                                                                                                                                            |
| [\' Key need to be added to define relation of two datasource][]                                                                                     |
|                                                                                                                                                                                                                                            |
| [ChildTableRelationDescriptor.RelationKeys.Add(\"Customer ID\", \"Customer ID\")]                                                                                                                      |
|                                                                                                                                                                                                                                            |
| [GridGroupingControl1.TableDescriptor.Relations.Add(ChildTableRelationDescriptor)]                                                                                                                     |
|                                                                                                                                                                                                                                            |
| [\'Register DataTable with SourceListSet,, so that RelationDescriptor can resolve the name ][]                                                       |
|                                                                                                                                                                                                                                            |
| [Me][.GridGroupingControl1.Engine.SourceListSet.Add(\"Customers\", Parent1)]                                                                          |
|                                                                                                                                                                                                                                            |
| [Me][.GridGroupingControl1.Engine.SourceListSet.Add(\"Orders\", Child)]                                                                               |
|                                                                                                                                                                                                                                            |
| [Me][.GridGroupingControl1.DataSource = Parent1]                                                                                                      |
|                                                                                                                                                                                                                                            |
| [Me][.GridGroupingControl1.DataBind()]                                                                                                                |
|                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

{border="0"}

Figure 71: Joined Tables

[] 

[] 

[]{#related-topics}

