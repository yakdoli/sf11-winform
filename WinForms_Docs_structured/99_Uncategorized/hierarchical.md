---
title: hierarchical.md
original_path: WinForms_Docs/99_Uncategorized/hierarchical.md
created_at: 2025-08-05
---








  









### Hierarchical {#hierarchical style="tab-stops: 0pt"}

[] 

The Parent-Children form of hierarchy is taken for our example scenario.

[] 

{border="0"}

Figure 65

[] 

[·      ]The Grid relations are given in code, using the GridRelationDescriptor.

[·      ]Tables namely Parent, Child and GrandChild are manually given relations, using the **GridRelationDescriptor** property.

[·      ]Here, the Tables and DataRelations are added manually to the Grouping Engine.

[·      ]Register any DataTable / List with the SourceListSet, so that the RelationDescriptor can resolve the name.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                             |
| [protected][ [void] Page_Load([object] sender, [EventArgs] e)]                                                          |
|                                                                                                                                                                                                                                                                             |
| [{]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                             |
| [        [if] (!IsPostBack)]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                             |
| [ {]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                             |
| [            [DataTable] parentTable = GetParentTable();]                                                                                                                                                          |
|                                                                                                                                                                                                                                                                             |
| [            [DataTable] childTable = GetChildTable();]                                                                                                                                                            |
|                                                                                                                                                                                                                                                                             |
| [            [DataTable] grandChildTable = GetGrandChildTable();]                                                                                                                                                  |
|                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                             |
| [            [// Manually specify relations in grouping engine. The DataSet does not need to have any DataRelations.]]                                                                                            |
|                                                                                                                                                                                                                                                                             |
| [            [// This is the same approach that should be used if you want to set up relation ships]]                                                                                                             |
|                                                                                                                                                                                                                                                                             |
| [            [// between independent IList.]]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                             |
| [            [GridRelationDescriptor] parentToChildRelationDescriptor = [new] [GridRelationDescriptor]();]                                                               |
|                                                                                                                                                                                                                                                                             |
| [            parentToChildRelationDescriptor.ChildTableName = [\"MyChildTable\"];    [// same as SourceListSetEntry.Name for childTable (see                below)]]                       |
|                                                                                                                                                                                                                                                                             |
| [            parentToChildRelationDescriptor.RelationKind = [RelationKind].RelatedMasterDetails;]                                                                                                                  |
|                                                                                                                                                                                                                                                                             |
| [            parentToChildRelationDescriptor.RelationKeys.Add([\"parentID\"], [\"ParentID\"]);]                                                                                           |
|                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                             |
| [            [// Add relation to ParentTable ]]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                             |
| [            GridGroupingControl1.TableDescriptor.Relations.Add(parentToChildRelationDescriptor);]                                                                                                                                      |
|                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                             |
| [            [GridRelationDescriptor] childToGrandChildRelationDescriptor = [new] [GridRelationDescriptor]();]                                                           |
|                                                                                                                                                                                                                                                                             |
| [            childToGrandChildRelationDescriptor.ChildTableName = [\"MyGrandChildTable\"];  [// same as SourceListSetEntry.Name for                         grandChhildTable (see below)]] |
|                                                                                                                                                                                                                                                                             |
| [            childToGrandChildRelationDescriptor.RelationKind = [RelationKind].RelatedMasterDetails;]                                                                                                              |
|                                                                                                                                                                                                                                                                             |
| [            childToGrandChildRelationDescriptor.RelationKeys.Add([\"childID\"], [\"ChildID\"]);]                                                                                         |
|                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                             |
| [            [// Add relation to ChildTable ]]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                             |
| [            parentToChildRelationDescriptor.ChildTableDescriptor.Relations.Add(childToGrandChildRelationDescriptor);]                                                                                                                  |
|                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                             |
| [            [// Register any DataTable/IList with SourceListSet, so that RelationDescriptor can resolve the name]]                                                                                               |
|                                                                                                                                                                                                                                                                             |
| [            [this].GridGroupingControl1.Engine.SourceListSet.Add([\"MyParentTable\"], parentTable);]                                                                                       |
|                                                                                                                                                                                                                                                                             |
| [            [this].GridGroupingControl1.Engine.SourceListSet.Add([\"MyChildTable\"], childTable);]                                                                                         |
|                                                                                                                                                                                                                                                                             |
| [            [this].GridGroupingControl1.Engine.SourceListSet.Add([\"MyGrandChildTable\"], grandChildTable);]                                                                               |
|                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                             |
| [            [this].GridGroupingControl1.DataMember = [\"DefaultView\"];]                                                                                                                   |
|                                                                                                                                                                                                                                                                             |
| [            [this].GridGroupingControl1.DataSource = parentTable;]                                                                                                                                                |
|                                                                                                                                                                                                                                                                             |
| [            [this].GridGroupingControl1.DataSourceCachingMode = DataSourceCachingMode.ViewState;]                                                                                                                 |
|                                                                                                                                                                                                                                                                             |
| [ }]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                 |
| [Protected][ [Sub] Page_Init([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)]                        |
|                                                                                                                                                                                                                                                                                                                                 |
| [Dim][ parentTable [As] Data.DataTable = GetParentTable()]                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                 |
| [Dim][ childTable [As] Data.DataTable = GetChildTable()]                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                 |
| [Dim][ grandChildTable [As] Data.DataTable = GetGrandChildTable()]                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                 |
| [\' Manually specify relations in grouping engine. The DataSet does not need to have any DataRelations.]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                 |
| [\' This is the same approach that should be used if you want to set up relation ships]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                 |
| [\' between independent IList.]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                 |
| [Dim][ parentToChildRelationDescriptor [As] Syncfusion.Web.UI.WebControls.Grid.Grouping.GridRelationDescriptor = [New] Syncfusion.Web.UI.WebControls.Grid.Grouping.GridRelationDescriptor()]     |
|                                                                                                                                                                                                                                                                                                                                 |
| [parentToChildRelationDescriptor.ChildTableName = [\"MyChildTable\"] [\' same as SourceListSetEntry.Name for childTable (see below)]]                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                 |
| [parentToChildRelationDescriptor.RelationKind = RelationKind.RelatedMasterDetails]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                 |
| [parentToChildRelationDescriptor.RelationKeys.Add([\"parentID\"], [\"ParentID\"])]                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                 |
| [\' Add relation to ParentTable ]                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                 |
| [GridGroupingControl1.TableDescriptor.Relations.Add(parentToChildRelationDescriptor)]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                 |
| [Dim][ childToGrandChildRelationDescriptor [As] Syncfusion.Web.UI.WebControls.Grid.Grouping.GridRelationDescriptor = [New] Syncfusion.Web.UI.WebControls.Grid.Grouping.GridRelationDescriptor()] |
|                                                                                                                                                                                                                                                                                                                                 |
| [childToGrandChildRelationDescriptor.ChildTableName = [\"MyGrandChildTable\"] [\' same as SourceListSetEntry.Name for grandChhildTable           (see below)]]                                                                                 |
|                                                                                                                                                                                                                                                                                                                                 |
| [childToGrandChildRelationDescriptor.RelationKind = RelationKind.RelatedMasterDetails]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                 |
| [childToGrandChildRelationDescriptor.RelationKeys.Add([\"childID\"], [\"ChildID\"])]                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                 |
| [\' Add relation to ChildTable ]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                 |
| [parentToChildRelationDescriptor.ChildTableDescriptor.Relations.Add(childToGrandChildRelationDescriptor)]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                 |
| [\' Register any DataTable/IList with SourceListSet, so that RelationDescriptor can resolve the name]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                 |
| [Me][.GridGroupingControl1.Engine.SourceListSet.Add([\"MyParentTable\"], parentTable)]                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                 |
| [Me][.GridGroupingControl1.Engine.SourceListSet.Add([\"MyChildTable\"], childTable)]                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                 |
| [Me][.GridGroupingControl1.Engine.SourceListSet.Add([\"MyGrandChildTable\"], grandChildTable)]                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                 |
| [Me][.GridGroupingControl1.DataMember = [\"DefaultView\"]]                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                 |
| [Me][.GridGroupingControl1.DataSource = parentTable]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                 |
| [End][ [Sub]]                                                                                                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[]{#p55}Figure 66

[]{#related-topics}

