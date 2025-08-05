---
title: relationsandhierarchy.md
original_path: WinForms_Docs/99_Uncategorized/relationsandhierarchy.md
created_at: 2025-08-05
---






##### Relations and Hierarchy {#relations-and-hierarchy style="tab-stops: 0pt"}

[] 

Grid Grouping control can display nested tables in a **hierarchy** using a master-detail configuration. In an hierarchical view, all the tables in the data source are inter-connected via relations. Generally a relation between any two tables can take any of the following forms: **1:1, 1:n, n:1** or **n:n**.

 

A grouping grid can automatically detect the data relations in a dataset for display. By default, a Relation is created for each such relation found in dataset. Hence the data relations defined in a dataset are sufficient enough for the grid to form the relations. No additional code is required in this case.

 

With nested tables, each record in the parent table will have an associated set of records in the child table. Every record in the relation is provided with a +/- button called **RecordPlusMinus** that can be expanded(as well as collapsed) to bring the underlying records in the child table into view. The number of tables that can be nested with relations using a Grid Grouping control is unlimited.

 

**Relations Collection**

 

The **TableDescriptor.Relations** collection defines relations for the table. By default a relation (**RelatedMasterDetails**) is created for each DataRelation found in a DataSet. Relations can either be related foreign key tables or nested child tables that can be expanded and collapsed. Each entry in this collection is owned by a RelationDescriptor that stores the details of a relation. All the RelationDescriptors for a given table is managed by the RelationDescriptor Collection which is returned by the TableDescriptor.Relations property.

 

The **TableDescriptor.RelationChildColumns** collection is internally initialized and contains the child key fields of the RelationDescriptor.RelationKeys collection of a RelationKind.RelatedMasterDetails relation. You should not modify this collection.

[] 

The **TableDescriptor.PrimaryKeyColumns** collection defines fields that form a unique primary key for the table. By default, the PrimaryKeyColumns collection is initialized from the child key fields of the RelationDescriptor.RelationKeys collection of a RelationKind.ForeignKeyReference relation. If the table is not a foreign table and a UniqueConstraint for a DataTable is present the collection is initialized with fields from that UniqueConstraint. Users can also manually modify the collection. If the table is the foreign table of a RelationKind.ForeignKeyReference relation, the parent table uses the fields that are defined in the PrimaryKeyColumns collection to lookup and identify records in the foreign table.

 

**Setting Up Relations Through Designer**

**[]** 

After binding an hierarchical dataset to the grouping grid, you could find the TableDescriptor.Relations collection populated with values. These values represent the relationship between the parent and child tables.

[] 

{border="0"}

[] 

*[Figure ][308][: Setting Up Relations by using the GridRelationDescriptor Collection Editor]*

[] 

[] 

[] 

Properties

[] 

[Here is a brief description on the properties used to setup a relation.]

[] 


+-----------------------------------+----------------------------------------------------------------------------------------------------------------+
| GridRelationDescriptor Property   | Description                                                                                                    |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------+
| Name                              | Specifies the relation name.                                                                                   |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------+
| ChildTableName                    | Specifies the name of the ChildTable.                                                                          |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------+
| RelationKeys                      | Defines the mapping between the parent and child columns in a master-detail relation.                          |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------+
| MappingName                       | Specifies the name of the PropertyDescriptor in the parent table that contains the details about the relation. |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------+
| RelationKind                      | Specifies the type of the relation.                                                                            |
|                                   |                                                                                                                |
|                                   |                                                                                                                |
|                                   |                                                                                                                |
|                                   | The options included are as follows.                                                                           |
|                                   |                                                                                                                |
|                                   |                                                                                                                |
|                                   |                                                                                                                |
|                                   | [·      ]RelatedMasterDetails                                                     |
|                                   |                                                                                                                |
|                                   | [·      ]ForeignKeyReference                                                      |
|                                   |                                                                                                                |
|                                   | [·      ]ForeignKey KeyWords                                                      |
|                                   |                                                                                                                |
|                                   | [·      ]UniformChildList                                                         |
|                                   |                                                                                                                |
|                                   | [·      ]ListItemReference                                                        |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------+
| AllowCacheChildList               |                                                                                                                |
|                                   |                                                                                                                |
|                                   | [·      ]Indicates whether the ChildList associated with a view can be cached.    |
|                                   |                                                                                                                |
|                                   | [·      ]Used with UniformChildList relation.                                     |
|                                   |                                                                                                                |
|                                   |                                                                                                                |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------+
| ChildTableDescriptor              | Specifies the table schema of Child Table.                                                                     |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------+


[] 

[] 

Different RelationKinds

 

Apart from the default Master-Detail type, Essential Grouping Grid supports a number of relations which could be enabled by specifying the relations manually in the grouping engine. In case of manual relations, the dataset does not need to have relations. This is the same approach that should be used if you want to setup relationships between independent IList collections.

[] 

Supported Relations

[] 

[[• ]]{.UGHyperlink}[RelatedMasterDetails]{.UGHyperlink}[]{.UGHyperlink}

[[• ]]{.UGHyperlink}[ForeignKeyReference]{.UGHyperlink}[]{.UGHyperlink}

[[• ]]{.UGHyperlink}[ForeignKey KeyWords]{.UGHyperlink}[]{.UGHyperlink}

[[• ]]{.UGHyperlink}[ListItemReference]{.UGHyperlink}[]{.UGHyperlink}

[[• ]]{.UGHyperlink}[UniformChildList]{.UGHyperlink}[]{.UGHyperlink}

[] 

The ForeignKey DropDown

 

When a **Foreign Key** relation (a relation for looking up values into a related child table using a key) is used, the child records are displayed using a DropDownList. Using this foreign key drop down, you could be able to edit the record. Here are the screen shots of the foreign key drop down.

 

ForeignKey DropDown showing Edit Button (button with Pencil Icon) clicking which allows you to edit the list

**[]** 

{border="0"}

***[]*** 

*[Figure ][309][: Edit button in the ForeignKey DropDown]*

**[]** 

Below image shows the state after clicking the Edit button.

**[]** 

{border="0"}

***[]*** 

*[Figure ][310][: Editing Records by clicking the Edit Button in the ForeignKey DropDown]*

 

[]{#p440} 

 

###### []{#_Related_Master_Details}4.3.4.3.5.1 Related Master Details Relation {#related-master-details-relation style="tab-stops: 0pt"}

[] 

**RelatedMasterDetails** is a Master-Details relation where matching keys in columns in the parent and child tables, define a relationship between two tables. This a 1:n relation where each record in the child table can only belong to one parent record.

 

This section demonstrates how to manually specify the master-detail relations between three independent tables that have the primary key and foreign key column in common.

[] 

Steps to setup RelatedMasterDetails relation

**[]** 

1.   Setup three datatables that have primary and foreign key columns in common.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                    |
|                                                                                                                                                                                                   |
| []                                                                                                                                              |
|                                                                                                                                                                                                   |
| [private][ [int] numberParentRows = 5;]                                                 |
|                                                                                                                                                                                                   |
| [private][ [int] numberChildRows = 20;]                                                 |
|                                                                                                                                                                                                   |
| [private][ [int] numberGrandChildRows = 50;]                                            |
|                                                                                                                                                                                                   |
| []                                                                                                                                                            |
|                                                                                                                                                                                                   |
| [// Create Parent Table.]                                                                                                                       |
|                                                                                                                                                                                                   |
| [private][ [DataTable] GetParentTable()]                                             |
|                                                                                                                                                                                                   |
| [{]                                                                                                                                                           |
|                                                                                                                                                                                                   |
| [    [DataTable] dt = [new] [DataTable]([\"ParentTable\"]);]     |
|                                                                                                                                                                                                   |
| []                                                                                                                                                            |
|                                                                                                                                                                                                   |
| [    dt.Columns.Add([new] [DataColumn]([\"parentID\"]));]                                |
|                                                                                                                                                                                                   |
| [    dt.Columns.Add([new] [DataColumn]([\"ParentName\"]));]                              |
|                                                                                                                                                                                                   |
| [    dt.Columns.Add([new] [DataColumn]([\"ParentDec\"]));]                               |
|                                                                                                                                                                                                   |
| []                                                                                                                                                            |
|                                                                                                                                                                                                   |
| [    [for]([int] i = 0; i \< numberParentRows; i++)]                                                                |
|                                                                                                                                                                                                   |
| [    {]                                                                                                                                                       |
|                                                                                                                                                                                                   |
| [        [DataRow] dr = dt.NewRow();]                                                                                                 |
|                                                                                                                                                                                                   |
| []                                                                                                                                                            |
|                                                                                                                                                                                                   |
| [        dr\[0\] = i;]                                                                                                                                        |
|                                                                                                                                                                                                   |
| [        dr\[1\] = [string].Format([\"parentName{0}\"], i);]                                                     |
|                                                                                                                                                                                                   |
| [        dr\[1\] = [string].Format([\"parentName{0}\"], i);]                                                     |
|                                                                                                                                                                                                   |
| [        dt.Rows.Add(dr);]                                                                                                                                    |
|                                                                                                                                                                                                   |
| [    }]                                                                                                                                                       |
|                                                                                                                                                                                                   |
| [    [return] dt;]                                                                                                                       |
|                                                                                                                                                                                                   |
| [}]                                                                                                                                                           |
|                                                                                                                                                                                                   |
| []                                                                                                                                                            |
|                                                                                                                                                                                                   |
| [// Create Child Table.]                                                                                                                        |
|                                                                                                                                                                                                   |
| [private][ [DataTable] GetChildTable()]                                              |
|                                                                                                                                                                                                   |
| [{]                                                                                                                                                           |
|                                                                                                                                                                                                   |
| [    [DataTable] dt = [new] [DataTable]([\"ChildTable\"]);]      |
|                                                                                                                                                                                                   |
| []                                                                                                                                                            |
|                                                                                                                                                                                                   |
| [    dt.Columns.Add([new] [DataColumn]([\"childID\"]));]                                 |
|                                                                                                                                                                                                   |
| [    dt.Columns.Add([new] [DataColumn]([\"Name\"]));]                                    |
|                                                                                                                                                                                                   |
| [    dt.Columns.Add([new] [DataColumn]([\"ParentID\"]));]                                |
|                                                                                                                                                                                                   |
| [                  ]                                                                                                                                          |
|                                                                                                                                                                                                   |
| [    [for]([int] i = 0; i \< numberChildRows; i++)]                                                                 |
|                                                                                                                                                                                                   |
| [    {]                                                                                                                                                       |
|                                                                                                                                                                                                   |
| [        [DataRow] dr = dt.NewRow();]                                                                                                 |
|                                                                                                                                                                                                   |
| [        dr\[0\] = i.ToString();]                                                                                                                             |
|                                                                                                                                                                                                   |
| [        dr\[1\] = [string].Format([\"ChildName{0}\"],i);]                                                       |
|                                                                                                                                                                                                   |
| [        dr\[2\] = (i % numberParentRows).ToString();]                                                                                                        |
|                                                                                                                                                                                                   |
| [        dt.Rows.Add(dr);]                                                                                                                                    |
|                                                                                                                                                                                                   |
| [    }]                                                                                                                                                       |
|                                                                                                                                                                                                   |
| [    [return] dt;]                                                                                                                       |
|                                                                                                                                                                                                   |
| [}]                                                                                                                                                           |
|                                                                                                                                                                                                   |
| []                                                                                                                                                            |
|                                                                                                                                                                                                   |
| [// Create Grand Child Table.]                                                                                                                  |
|                                                                                                                                                                                                   |
| [private][ [DataTable] GetGrandChildTable()]                                         |
|                                                                                                                                                                                                   |
| [{]                                                                                                                                                           |
|                                                                                                                                                                                                   |
| [    [DataTable] dt = [new] [DataTable]([\"GrandChildTable\"]);] |
|                                                                                                                                                                                                   |
| []                                                                                                                                                            |
|                                                                                                                                                                                                   |
| [    dt.Columns.Add([new] [DataColumn]([\"GrandChildID\"]));]                            |
|                                                                                                                                                                                                   |
| [    dt.Columns.Add([new] [DataColumn]([\"Name\"]));]                                    |
|                                                                                                                                                                                                   |
| [    dt.Columns.Add([new] [DataColumn]([\"ChildID\"]));]                                 |
|                                                                                                                                                                                                   |
| [                  ]                                                                                                                                          |
|                                                                                                                                                                                                   |
| [    [for]([int] i = 0; i \< numberGrandChildRows; i++)]                                                            |
|                                                                                                                                                                                                   |
| [    {]                                                                                                                                                       |
|                                                                                                                                                                                                   |
| [        [DataRow] dr = dt.NewRow();]                                                                                                 |
|                                                                                                                                                                                                   |
| [        dr\[0\] = i.ToString();]                                                                                                                             |
|                                                                                                                                                                                                   |
| [        dr\[1\] = [string].Format([\"GrandChildName{0}\"],i);]                                                  |
|                                                                                                                                                                                                   |
| [        dr\[2\] = (i % numberChildRows).ToString();]                                                                                                         |
|                                                                                                                                                                                                   |
| [        dt.Rows.Add(dr);]                                                                                                                                    |
|                                                                                                                                                                                                   |
| [    }]                                                                                                                                                       |
|                                                                                                                                                                                                   |
| [    [return] dt;]                                                                                                                       |
|                                                                                                                                                                                                   |
| [}]                                                                                                                                                           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                            |
|                                                                                                                                                                                                               |
| []                                                                                                                                                          |
|                                                                                                                                                                                                               |
| [Private][ numberParentRows [As] [Integer] = 5]                                |
|                                                                                                                                                                                                               |
| [Private][ numberChildRows [As] [Integer] = 20]                                |
|                                                                                                                                                                                                               |
| [Private][ numberGrandChildRows [As] [Integer] = 50]                           |
|                                                                                                                                                                                                               |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                               |
| [\' Create Parent Table.]                                                                                                                                   |
|                                                                                                                                                                                                               |
| [Private][ [Function] GetParentTable() [As] DataTable]                         |
|                                                                                                                                                                                                               |
| [Dim][ dt [As] [New] DataTable([\"ParentTable\"])]     |
|                                                                                                                                                                                                               |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                               |
| [dt.Columns.Add([New] DataColumn([\"parentID\"]))]                                                                           |
|                                                                                                                                                                                                               |
| [dt.Columns.Add([New] DataColumn([\"ParentName\"]))]                                                                         |
|                                                                                                                                                                                                               |
| [dt.Columns.Add([New] DataColumn([\"ParentDec\"]))]                                                                          |
|                                                                                                                                                                                                               |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                               |
| [Dim][ i [As] [Integer]]                                                       |
|                                                                                                                                                                                                               |
| [For][ i = 0 [To] numberParentRows - 1]                                                             |
|                                                                                                                                                                                                               |
| [Dim][ dr [As] DataRow = dt.NewRow()]                                                               |
|                                                                                                                                                                                                               |
| [dr(0) = i]                                                                                                                                                               |
|                                                                                                                                                                                                               |
| [dr(1) = [String].Format([\"parentName{0}\"], i)]                                                                            |
|                                                                                                                                                                                                               |
| [dr(1) = [String].Format([\"parentName{0}\"], i)]                                                                            |
|                                                                                                                                                                                                               |
| [dt.Rows.Add(dr)]                                                                                                                                                         |
|                                                                                                                                                                                                               |
| [Next][ i]                                                                                                               |
|                                                                                                                                                                                                               |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                               |
| [Return][ dt]                                                                                                            |
|                                                                                                                                                                                                               |
| [End][ [Function]]                                                                                  |
|                                                                                                                                                                                                               |
| []                                                                                                                                                           |
|                                                                                                                                                                                                               |
| [\' Create Child Table.]                                                                                                                                    |
|                                                                                                                                                                                                               |
| [Private][ [Function] GetChildTable() [As] DataTable]                          |
|                                                                                                                                                                                                               |
| [Dim][ dt [As] [New] DataTable([\"ChildTable\"])]      |
|                                                                                                                                                                                                               |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                               |
| [dt.Columns.Add([New] DataColumn([\"childID\"]))]                                                                            |
|                                                                                                                                                                                                               |
| [dt.Columns.Add([New] DataColumn([\"Name\"]))]                                                                               |
|                                                                                                                                                                                                               |
| [dt.Columns.Add([New] DataColumn([\"ParentID\"]))]                                                                           |
|                                                                                                                                                                                                               |
| [Dim][ i [As] [Integer]]                                                       |
|                                                                                                                                                                                                               |
| [For][ i = 0 [To] numberChildRows - 1]                                                              |
|                                                                                                                                                                                                               |
| [Dim][ dr [As] DataRow = dt.NewRow()]                                                               |
|                                                                                                                                                                                                               |
| [dr(0) = i.ToString()]                                                                                                                                                    |
|                                                                                                                                                                                                               |
| [dr(1) = [String].Format([\"ChildName{0}\"], i)]                                                                             |
|                                                                                                                                                                                                               |
| [dr(2) = (i [Mod] numberParentRows).ToString()]                                                                                                      |
|                                                                                                                                                                                                               |
| [dt.Rows.Add(dr)]                                                                                                                                                         |
|                                                                                                                                                                                                               |
| [Next][ i]                                                                                                               |
|                                                                                                                                                                                                               |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                               |
| [Return][ dt]                                                                                                            |
|                                                                                                                                                                                                               |
| [End][ [Function]]                                                                                  |
|                                                                                                                                                                                                               |
| []                                                                                                                                                           |
|                                                                                                                                                                                                               |
| [\' Create Grand Child Table.]                                                                                                                              |
|                                                                                                                                                                                                               |
| [Private][ [Function] GetGrandChildTable() [As] DataTable]                     |
|                                                                                                                                                                                                               |
| [Dim][ dt [As] [New] DataTable([\"GrandChildTable\"])] |
|                                                                                                                                                                                                               |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                               |
| [dt.Columns.Add([New] DataColumn([\"GrandChildID\"]))]                                                                       |
|                                                                                                                                                                                                               |
| [dt.Columns.Add([New] DataColumn([\"Name\"]))]                                                                               |
|                                                                                                                                                                                                               |
| [dt.Columns.Add([New] DataColumn([\"ChildID\"]))]                                                                            |
|                                                                                                                                                                                                               |
| [Dim][ i [As] [Integer]]                                                       |
|                                                                                                                                                                                                               |
| [For][ i = 0 [To] numberGrandChildRows - 1]                                                         |
|                                                                                                                                                                                                               |
| [Dim][ dr [As] DataRow = dt.NewRow()]                                                               |
|                                                                                                                                                                                                               |
| [dr(0) = i.ToString()]                                                                                                                                                    |
|                                                                                                                                                                                                               |
| [dr(1) = [String].Format([\"GrandChildName{0}\"], i)]                                                                        |
|                                                                                                                                                                                                               |
| [dr(2) = (i [Mod] numberChildRows).ToString()]                                                                                                       |
|                                                                                                                                                                                                               |
| [dt.Rows.Add(dr)]                                                                                                                                                         |
|                                                                                                                                                                                                               |
| [Next][ i]                                                                                                               |
|                                                                                                                                                                                                               |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                               |
| [Return][ dt]                                                                                                            |
|                                                                                                                                                                                                               |
| [End][ [Function]]                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Manually set up relationships between the tables and add the relation to the parent and child tables.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                          |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                                         |
| [GridRelationDescriptor][ parentToChildRelationDescriptor = [new] [GridRelationDescriptor]();]     |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                         |
| [// Same as SourceListSetEntry.Name for Child Table.]                                                                                                                                 |
|                                                                                                                                                                                                                                         |
| [parentToChildRelationDescriptor.ChildTableName = [\"MyChildTable\"];]                                                                                                      |
|                                                                                                                                                                                                                                         |
| [parentToChildRelationDescriptor.RelationKind = [RelationKind].RelatedMasterDetails;]                                                                                       |
|                                                                                                                                                                                                                                         |
| [parentToChildRelationDescriptor.RelationKeys.Add([\"parentID\"], [\"ParentID\"]);]                                                                 |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                         |
| [// Add relation to Parent Table.]                                                                                                                                                    |
|                                                                                                                                                                                                                                         |
| [gridGroupingControl1.TableDescriptor.Relations.Add(parentToChildRelationDescriptor);]                                                                                                              |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                         |
| [GridRelationDescriptor][ childToGrandChildRelationDescriptor = [new] [GridRelationDescriptor]();] |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                         |
| [// Same as SourceListSetEntry.Name for Grand Child Table.]                                                                                                                           |
|                                                                                                                                                                                                                                         |
| [childToGrandChildRelationDescriptor.ChildTableName = [\"MyGrandChildTable\"];]                                                                                             |
|                                                                                                                                                                                                                                         |
| [childToGrandChildRelationDescriptor.RelationKind = [RelationKind].RelatedMasterDetails;]                                                                                   |
|                                                                                                                                                                                                                                         |
| [childToGrandChildRelationDescriptor.RelationKeys.Add([\"childID\"], [\"ChildID\"]);]                                                               |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                         |
| [// Add relation to Child Table.]                                                                                                                                                     |
|                                                                                                                                                                                                                                         |
| [parentToChildRelationDescriptor.ChildTableDescriptor.Relations.Add(childToGrandChildRelationDescriptor);]                                                                                          |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                             |
|                                                                                                                                                                                                                |
| []                                                                                                                                                           |
|                                                                                                                                                                                                                |
| [Dim][ parentToChildRelationDescriptor [As] [New] GridRelationDescriptor()]     |
|                                                                                                                                                                                                                |
| []                                                                                                                                                           |
|                                                                                                                                                                                                                |
| [\' Same as SourceListSetEntry.Name for Child Table.]                                                                                                        |
|                                                                                                                                                                                                                |
| [parentToChildRelationDescriptor.ChildTableName = [\"MyChildTable\"]]                                                                              |
|                                                                                                                                                                                                                |
| [parentToChildRelationDescriptor.RelationKind = RelationKind.RelatedMasterDetails]                                                                                         |
|                                                                                                                                                                                                                |
| [parentToChildRelationDescriptor.RelationKeys.Add([\"parentID\"], [\"ParentID\"])]                                         |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [\' Add relation to Parent Table.]                                                                                                                           |
|                                                                                                                                                                                                                |
| [gridGroupingControl1.TableDescriptor.Relations.Add(parentToChildRelationDescriptor)]                                                                                      |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [Dim][ childToGrandChildRelationDescriptor [As] [New] GridRelationDescriptor()] |
|                                                                                                                                                                                                                |
| []                                                                                                                                                           |
|                                                                                                                                                                                                                |
| [\' Same as SourceListSetEntry.Name for Grand Child Table.]                                                                                                  |
|                                                                                                                                                                                                                |
| [childToGrandChildRelationDescriptor.ChildTableName = [\"MyGrandChildTable\"]]                                                                     |
|                                                                                                                                                                                                                |
| [childToGrandChildRelationDescriptor.RelationKind = RelationKind.RelatedMasterDetails]                                                                                     |
|                                                                                                                                                                                                                |
| [childToGrandChildRelationDescriptor.RelationKeys.Add([\"childID\"], [\"ChildID\"])]                                       |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [\' Add relation to Child Table.]                                                                                                                            |
|                                                                                                                                                                                                                |
| [parentToChildRelationDescriptor.ChildTableDescriptor.Relations.Add(childToGrandChildRelationDescriptor)]                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Register the datatables with Engine.SourceListSet so that the RelationDescriptor can resolve the name.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                 |
|                                                                                                                                                                                                                |
| []                                                                                                                                                           |
|                                                                                                                                                                                                                |
| [this][.gridGroupingControl1.Engine.SourceListSet.Add([\"MyParentTable\"], parentTable);]         |
|                                                                                                                                                                                                                |
| [this][.gridGroupingControl1.Engine.SourceListSet.Add([\"MyChildTable\"], childTable);]           |
|                                                                                                                                                                                                                |
| [this][.gridGroupingControl1.Engine.SourceListSet.Add([\"MyGrandChildTable\"], grandChildTable);] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                          |
|                                                                                                                                                                                                             |
| []                                                                                                                                                        |
|                                                                                                                                                                                                             |
| [Me][.gridGroupingControl1.Engine.SourceListSet.Add([\"MyParentTable\"], parentTable)]         |
|                                                                                                                                                                                                             |
| [Me][.gridGroupingControl1.Engine.SourceListSet.Add([\"MyChildTable\"], ChildTable)]           |
|                                                                                                                                                                                                             |
| [Me][.gridGroupingControl1.Engine.SourceListSet.Add([\"MyGrandChildTable\"], grandChildTable)] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Finally bind the hierarchical data source, which has been created through the above steps, to a grouping grid by assigning the parent table to the datasource.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                               |
|                                                                                                                                              |
| []                                                                                         |
|                                                                                                                                              |
| [this][.gridGroupingControl1.DataSource = parentTable;] |
+----------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                        |
|                                                                                                                                           |
| []                                                                                      |
|                                                                                                                                           |
| [Me][.gridGroupingControl1.DataSource = parentTable] |
+-------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   When you run the sample, you could find the tables connected with Master-Details relation.

[] 

{border="0"}

[] 

*[Figure ][311][: RelatedMasterDetails Relation]*

[] 


{border="0"}Note: For more details, refer the following browser sample:


[] 


\<Install Location\>\\Syncfusion\\EssentialStudio\\\[Version Number\]\\Windows\\Grid.Grouping.Windows\\Samples\\2.0\\Relations And Hierarchy\\Related Master Details Demo


 

[]{#p441} 

 

###### []{#_Foreign_Key_Reference}4.3.4.3.5.2 Foreign Key Reference Relation {#foreign-key-reference-relation style="tab-stops: 0pt"}

[] 

**ForeignKeyReference** is a foreign-key relation for looking up values where an id column in the main table can be used to look up a record in a related table. This is an n:1 relation where multiple records in the parent table can reference the same record in the related table. Fields in the related table can be referenced using a \'.\' dot in the FieldDescriptor.MappingName of the main table.

 

**Steps to setup ForeignKeyReference relation**

 

This section sets up a foreignkeyreference relation between a data table and the collection **USStates**. The data table represents the Parent Table of the relation and the USStates collection serves as the related child list where in the values can be looked up using a key. The collection derives from ArrayList in which every item is an **USState** object having two properties named **Key** and **Name**. It also defines a method named **CreateDefaultCollection()** that returns an instance of itself populated with a set of values.

 

A foreignkeyreference relation can be set up between the lists by defining a relation descriptor with its attributes carrying the relation details and adding this descriptor to the Relations collection of the main table.

 

The following steps demonstrate this process.

[] 

1.   Create a collection named **USStates** in which each entry stores a **USState** object.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                           |
|                                                                                                                                                                                                                          |
| []                                                                                                                                                                     |
|                                                                                                                                                                                                                          |
| [// US States Collection.]                                                                                                                                             |
|                                                                                                                                                                                                                          |
| [\[[Serializable]\]]                                                                                                                                         |
|                                                                                                                                                                                                                          |
| [public][ [class] [USStatesCollection] : [ArrayList]]          |
|                                                                                                                                                                                                                          |
| [{]                                                                                                                                                                                  |
|                                                                                                                                                                                                                          |
| [    [public] [new] [USState] [this]\[[int] index\]]                     |
|                                                                                                                                                                                                                          |
| [    {]                                                                                                                                                                              |
|                                                                                                                                                                                                                          |
| [        [get]]                                                                                                                                                 |
|                                                                                                                                                                                                                          |
| [        {]                                                                                                                                                                          |
|                                                                                                                                                                                                                          |
| [            [return] ([USState]) [base]\[index\];]                                                                |
|                                                                                                                                                                                                                          |
| [        }]                                                                                                                                                                          |
|                                                                                                                                                                                                                          |
| [        [set]]                                                                                                                                                 |
|                                                                                                                                                                                                                          |
| [        {]                                                                                                                                                                          |
|                                                                                                                                                                                                                          |
| [            [base]\[index\] = [value];]                                                                                                   |
|                                                                                                                                                                                                                          |
| [        }]                                                                                                                                                                          |
|                                                                                                                                                                                                                          |
| [    }]                                                                                                                                                                              |
|                                                                                                                                                                                                                          |
| []                                                                                                                                                                                   |
|                                                                                                                                                                                                                          |
| [    [public] [static] [USStatesCollection] CreateDefaultCollection()]                                             |
|                                                                                                                                                                                                                          |
| [    {]                                                                                                                                                                              |
|                                                                                                                                                                                                                          |
| [        [USStatesCollection] states = [new] [USStatesCollection]();]                                           |
|                                                                                                                                                                                                                          |
| [        states.Add([new] [USState]([\"AL\"], [\"Alabama\"]));]                         |
|                                                                                                                                                                                                                          |
| [        states.Add([new] [USState]([\"AK\"], [\"Alaska\"]));]                          |
|                                                                                                                                                                                                                          |
| [        states.Add([new] [USState]([\"CA\"], [\"California\"]));]                      |
|                                                                                                                                                                                                                          |
| [        states.Add([new] [USState]([\"FL\"], [\"Florida\"]));]                         |
|                                                                                                                                                                                                                          |
| [        states.Add([new] [USState]([\"GA\"], [\"Georgia\"]));]                         |
|                                                                                                                                                                                                                          |
| [        states.Add([new] [USState]([\"IN\"], [\"Indiana\"]));]                         |
|                                                                                                                                                                                                                          |
| [        states.Add([new] [USState]([\"MS\"], [\"Mississippi\"]));]                     |
|                                                                                                                                                                                                                          |
| [        states.Add([new] [USState]([\"NJ\"], [\"New Jersey\"]));]                      |
|                                                                                                                                                                                                                          |
| [        states.Add([new] [USState]([\"NM\"], [\"New Mexico\"]));]                      |
|                                                                                                                                                                                                                          |
| [        states.Add([new] [USState]([\"NY\"], [\"New York\"]));]                        |
|                                                                                                                                                                                                                          |
| [        states.Add([new] [USState]([\"TX\"], [\"Texas\"]));]                           |
|                                                                                                                                                                                                                          |
| [        states.Add([new] [USState]([\"WA\"], [\"Washington\"]));]                      |
|                                                                                                                                                                                                                          |
| [        states.Add([new] [USState]([\"PE\"], [\"Prince Edward Island\"]));]            |
|                                                                                                                                                                                                                          |
| [        states.Add([new] [USState]([\"YT\"], [\"Yukon Territories\"]));]               |
|                                                                                                                                                                                                                          |
| [        [return] states;]                                                                                                                                      |
|                                                                                                                                                                                                                          |
| [    }]                                                                                                                                                                              |
|                                                                                                                                                                                                                          |
| []                                                                                                                                                                                   |
|                                                                                                                                                                                                                          |
| [    [public] [override] [bool] IsReadOnly]                                                                           |
|                                                                                                                                                                                                                          |
| [    {]                                                                                                                                                                              |
|                                                                                                                                                                                                                          |
| [        [get]]                                                                                                                                                 |
|                                                                                                                                                                                                                          |
| [        {]                                                                                                                                                                          |
|                                                                                                                                                                                                                          |
| [            [return] [true];]                                                                                                             |
|                                                                                                                                                                                                                          |
| [        }]                                                                                                                                                                          |
|                                                                                                                                                                                                                          |
| [    }]                                                                                                                                                                              |
|                                                                                                                                                                                                                          |
| []                                                                                                                                                                                   |
|                                                                                                                                                                                                                          |
| [    [public] [override] [bool] IsFixedSize]                                                                          |
|                                                                                                                                                                                                                          |
| [    {]                                                                                                                                                                              |
|                                                                                                                                                                                                                          |
| [        [get]]                                                                                                                                                 |
|                                                                                                                                                                                                                          |
| [        {]                                                                                                                                                                          |
|                                                                                                                                                                                                                          |
| [            [return] [true];]                                                                                                             |
|                                                                                                                                                                                                                          |
| [        }]                                                                                                                                                                          |
|                                                                                                                                                                                                                          |
| [    }]                                                                                                                                                                              |
|                                                                                                                                                                                                                          |
| []                                                                                                                                                                                   |
|                                                                                                                                                                                                                          |
| [}]                                                                                                                                                                                  |
|                                                                                                                                                                                                                          |
| []                                                                                                                                                                                   |
|                                                                                                                                                                                                                          |
| [// US State Class.]                                                                                                                                                   |
|                                                                                                                                                                                                                          |
| [\[[Serializable]\]]                                                                                                                                         |
|                                                                                                                                                                                                                          |
| [public][ [class] [USState]]                                                           |
|                                                                                                                                                                                                                          |
| [{]                                                                                                                                                                                  |
|                                                                                                                                                                                                                          |
| [    [private] [string] \_code;]                                                                                                           |
|                                                                                                                                                                                                                          |
| [    [private] [string] \_name;]                                                                                                           |
|                                                                                                                                                                                                                          |
| []                                                                                                                                                                                   |
|                                                                                                                                                                                                                          |
| [    [public]  USState()]                                                                                                                                       |
|                                                                                                                                                                                                                          |
| [    {]                                                                                                                                                                              |
|                                                                                                                                                                                                                          |
| [    }]                                                                                                                                                                              |
|                                                                                                                                                                                                                          |
| []                                                                                                                                                                                   |
|                                                                                                                                                                                                                          |
| [    [public]  USState([string] key, [string] name)]                                                                  |
|                                                                                                                                                                                                                          |
| [    {]                                                                                                                                                                              |
|                                                                                                                                                                                                                          |
| [        [this].\_code = key;]                                                                                                                                  |
|                                                                                                                                                                                                                          |
| [        [this].\_name = name;]                                                                                                                                 |
|                                                                                                                                                                                                                          |
| [    }]                                                                                                                                                                              |
|                                                                                                                                                                                                                          |
| []                                                                                                                                                                                   |
|                                                                                                                                                                                                                          |
| [    \[[Browsable]([true])\]]                                                                                                           |
|                                                                                                                                                                                                                          |
| [    [public] [string] Key]                                                                                                                |
|                                                                                                                                                                                                                          |
| [    {]                                                                                                                                                                              |
|                                                                                                                                                                                                                          |
| [        [get]]                                                                                                                                                 |
|                                                                                                                                                                                                                          |
| [        {]                                                                                                                                                                          |
|                                                                                                                                                                                                                          |
| [            [return] \_code;]                                                                                                                                  |
|                                                                                                                                                                                                                          |
| [        }]                                                                                                                                                                          |
|                                                                                                                                                                                                                          |
| [        [set]]                                                                                                                                                 |
|                                                                                                                                                                                                                          |
| [        {]                                                                                                                                                                          |
|                                                                                                                                                                                                                          |
| [            \_code = [value];]                                                                                                                                 |
|                                                                                                                                                                                                                          |
| [        }]                                                                                                                                                                          |
|                                                                                                                                                                                                                          |
| [    }]                                                                                                                                                                              |
|                                                                                                                                                                                                                          |
| []                                                                                                                                                                                   |
|                                                                                                                                                                                                                          |
| [    \[[Browsable]([true])\]]                                                                                                           |
|                                                                                                                                                                                                                          |
| [    [public] [string] Name]                                                                                                               |
|                                                                                                                                                                                                                          |
| [    {]                                                                                                                                                                              |
|                                                                                                                                                                                                                          |
| [          [get]]                                                                                                                                               |
|                                                                                                                                                                                                                          |
| [        {]                                                                                                                                                                          |
|                                                                                                                                                                                                                          |
| [            [return] \_name ;]                                                                                                                                 |
|                                                                                                                                                                                                                          |
| [        }]                                                                                                                                                                          |
|                                                                                                                                                                                                                          |
| [        [set]]                                                                                                                                                 |
|                                                                                                                                                                                                                          |
| [        {]                                                                                                                                                                          |
|                                                                                                                                                                                                                          |
| [            \_name = [value];]                                                                                                                                 |
|                                                                                                                                                                                                                          |
| [        }]                                                                                                                                                                          |
|                                                                                                                                                                                                                          |
| [    }]                                                                                                                                                                              |
|                                                                                                                                                                                                                          |
| []                                                                                                                                                                                   |
|                                                                                                                                                                                                                          |
| [    [public] [override] [string] ToString()]                                                                         |
|                                                                                                                                                                                                                          |
| [    {]                                                                                                                                                                              |
|                                                                                                                                                                                                                          |
| [        [return] [this].\_name + [\"(\"] + [this].\_code + [\")\"];] |
|                                                                                                                                                                                                                          |
| [    }]                                                                                                                                                                              |
|                                                                                                                                                                                                                          |
| [}]                                                                                                                                                                                  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                      |
| [\' US States Collection.]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                      |
| [\<Serializable()\>  \_]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                      |
| [Public][ [Class] USStatesCollection]                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                      |
| [Inherits][ ArrayList]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                      |
| [        ]                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                      |
| [Default][ [Public] [Shadows] [Property] Item(index [As] [Integer]) [As] USState] |
|                                                                                                                                                                                                                                                                                                      |
| [Get]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                      |
| [Return][ [CType]([MyBase].Item(index), USState)]                                                                                                                     |
|                                                                                                                                                                                                                                                                                                      |
| [End][ [Get]]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                      |
| [Set]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                      |
| [MyBase][.Item(index) = Value]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                      |
| [End][ [Set]]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                      |
| [End][ [Property]        ]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                      |
| [        ]                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                      |
| [Public][ [Shared] [Function] CreateDefaultCollection() [As] USStatesCollection]                                                                 |
|                                                                                                                                                                                                                                                                                                      |
| [      [Dim] states [As] [New] USStatesCollection()]                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                      |
| [      states.Add([New] USState([\"AL\"], [\"Alabama\"]))]                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                      |
| [      states.Add([New] USState([\"AK\"], [\"Alaska\"]))]                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                      |
| [      states.Add([New] USState([\"CA\"], [\"California\"]))]                                                                                                                               |
|                                                                                                                                                                                                                                                                                                      |
| [      states.Add([New] USState([\"FL\"], [\"Florida\"]))]                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                      |
| [      states.Add([New] USState([\"GA\"], [\"Georgia\"]))]                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                      |
| [      states.Add([New] USState([\"IN\"], [\"Indiana\"]))]                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                      |
| [      states.Add([New] USState([\"MS\"], [\"Mississippi\"]))]                                                                                                                              |
|                                                                                                                                                                                                                                                                                                      |
| [      states.Add([New] USState([\"NJ\"], [\"New Jersey\"]))]                                                                                                                               |
|                                                                                                                                                                                                                                                                                                      |
| [      states.Add([New] USState([\"NM\"], [\"New Mexico\"]))]                                                                                                                               |
|                                                                                                                                                                                                                                                                                                      |
| [      states.Add([New] USState([\"NY\"], [\"New York\"]))]                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                      |
| [      states.Add([New] USState([\"TX\"], [\"Texas\"]))]                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                      |
| [      states.Add([New] USState([\"WA\"], [\"Washington\"]))]                                                                                                                               |
|                                                                                                                                                                                                                                                                                                      |
| [      states.Add([New] USState([\"PE\"], [\"Prince Edward Island\"]))]                                                                                                                     |
|                                                                                                                                                                                                                                                                                                      |
| [      states.Add([New] USState([\"YT\"], [\"Yukon Territories\"]))]                                                                                                                        |
|                                                                                                                                                                                                                                                                                                      |
| [      Return][ states]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                      |
| [End][ [Function]]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                      |
| [Public][ [Overrides] [ReadOnly] [Property] IsReadOnly() [As] [Boolean]]                               |
|                                                                                                                                                                                                                                                                                                      |
| [Get]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                      |
| [Return][ [True]]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                      |
| [End][ [Get]]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                      |
| [End][ [Property]]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                      |
| [        ]                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                      |
| [Public][ [Overrides] [ReadOnly] [Property] IsFixedSize() [As] [Boolean]]                              |
|                                                                                                                                                                                                                                                                                                      |
| [Get]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                      |
| [Return][ [True]]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                      |
| [End][ [Get]]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                      |
| [End][ [Property]]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                      |
| [End][ [Class]]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                      |
| [\' US State Class.]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                      |
| [\<Serializable()\>  \_]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                      |
| [Public][ [Class] USState]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                      |
| [Private][ \_code [As] [String]]                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                      |
| [Private][ \_name [As] [String]]                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                      |
| [        ]                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                      |
| [Public][ [Sub] [New]()]                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                      |
| [End][ [Sub]]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                      |
| [        ]                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                      |
| [Public][ [Sub] [New](key [As] [String], name [As] [String])]                     |
|                                                                                                                                                                                                                                                                                                      |
| [Me][.\_code = key]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                      |
| [Me][.\_name = name]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                      |
| [End][ [Sub]]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                      |
| [        ]                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                      |
| [\<Browsable([True])\>  \_]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                      |
| [Public][ [Property] Key() [As] [String]]                                                                                                        |
|                                                                                                                                                                                                                                                                                                      |
| [Get]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                      |
| [Return][ \_code]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                      |
| [End][ [Get]]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                      |
| [Set]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                      |
| [\_code = value]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                      |
| [End][ [Set]]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                      |
| [End][ [Property]]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                      |
| [        ]                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                      |
| [\<Browsable([True])\>  \_]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                      |
| [Public][ [Property] Name() [As] [String]]                                                                                                       |
|                                                                                                                                                                                                                                                                                                      |
| [Get]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                      |
| [Return][ \_name]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                      |
| [End][ [Get]]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                      |
| [Set]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                      |
| [\_name = value]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                      |
| [End][ [Set]]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                      |
| [End][ [Property]]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                      |
| [        ]                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                      |
| [Public][ [Overrides] [Function] ToString() [As] [String]]                                                                  |
|                                                                                                                                                                                                                                                                                                      |
| [Return][ [Me].\_name + [\"(\"] + [Me].\_code + [\")\"]]                                                              |
|                                                                                                                                                                                                                                                                                                      |
| [End][ [Function]]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                      |
| [End][ [Class]]                                                                                                                                                                            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Create an object of USStates and add this object into the SourceListSet with a lookup name.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                 |
|                                                                                                                                                                                                |
| []                                                                                                                                           |
|                                                                                                                                                                                                |
| [USStatesCollection usStates = USStatesCollection.CreateDefaultCollection();]                                                                              |
|                                                                                                                                                                                                |
| [this][.gridGroupingControl1.Engine.SourceListSet.Add([\"USStates\"], usStates);] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                |
|                                                                                                                                                                                                   |
| []                                                                                                                                              |
|                                                                                                                                                                                                   |
| [Dim][ usStates [As] USStatesCollection = USStatesCollection.CreateDefaultCollection()] |
|                                                                                                                                                                                                   |
| [Me][.gridGroupingControl1.Engine.SourceListSet.Add([\"USStates\"], usStates)]       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Creates a datatable with the **Key** from **USState** as one of the columns.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                  |
|                                                                                                                                                                                 |
| []                                                                                                                            |
|                                                                                                                                                                                 |
| [DataTable][ table = [new] [DataTable]();] |
|                                                                                                                                                                                 |
| [table.Columns.Add([\"Id\"], [typeof]([string]));]                        |
|                                                                                                                                                                                 |
| [table.Columns.Add([\"State\"], [typeof]([string]));]                     |
|                                                                                                                                                                                 |
| []                                                                                                                                          |
|                                                                                                                                                                                 |
| [// Adding rows.]                                                                                                             |
|                                                                                                                                                                                 |
| [for][ ([int] i = 0; i \< 25; i++)]                                   |
|                                                                                                                                                                                 |
| [{]                                                                                                                                         |
|                                                                                                                                                                                 |
| [    table.Rows.Add(table.NewRow());]                                                                                                       |
|                                                                                                                                                                                 |
| [    table.Rows\[i\]\[0\] = i;]                                                                                                             |
|                                                                                                                                                                                 |
| [    table.Rows\[i\]\[1\] = usStates\[i % 8\].Key;]                                                                                         |
|                                                                                                                                                                                 |
| [}]                                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                  |
|                                                                                                                                                                     |
| []                                                                                                                |
|                                                                                                                                                                     |
| [Dim][ table [As] [New] DataTable()] |
|                                                                                                                                                                     |
| [table.Columns.Add([\"Id\"], [GetType]([String]))]            |
|                                                                                                                                                                     |
| [table.Columns.Add([\"State\"], [GetType]([String]))]         |
|                                                                                                                                                                     |
| [            ]                                                                                                                  |
|                                                                                                                                                                     |
| [\' Adding rows.]                                                                                                 |
|                                                                                                                                                                     |
| [Dim][ i [As] [Integer]]             |
|                                                                                                                                                                     |
| [For][ i = 0 [To] 24]                                     |
|                                                                                                                                                                     |
| [table.Rows.Add(table.NewRow())]                                                                                                |
|                                                                                                                                                                     |
| [table.Rows(i)(0) = i]                                                                                                          |
|                                                                                                                                                                     |
| [table.Rows(i)(1) = usStates((i [Mod] 8)).Key]                                                             |
|                                                                                                                                                                     |
| [Next][ i]                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Establish the ForeignKeyReference relationship.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                 |
|                                                                                                                                                                                                                |
| []                                                                                                                                                           |
|                                                                                                                                                                                                                |
| [GridTableDescriptor][ mainTd = [this].gridGroupingControl1.TableDescriptor;]                     |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [GridRelationDescriptor][ usStatesRd = [new] [GridRelationDescriptor]();] |
|                                                                                                                                                                                                                |
| [usStatesRd.Name = [\"State\"];]                                                                                                                   |
|                                                                                                                                                                                                                |
| [usStatesRd.RelationKind = [RelationKind].ForeignKeyReference;]                                                                                    |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [// SourceListSet name for look up.]                                                                                                                         |
|                                                                                                                                                                                                                |
| [usStatesRd.ChildTableName = [\"USStates\"];  ]                                                                                                    |
|                                                                                                                                                                                                                |
| [usStatesRd.RelationKeys.Add([\"State\"], [\"Key\"]);]                                                                     |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [// Format ChildList.]                                                                                                                                       |
|                                                                                                                                                                                                                |
| [usStatesRd.ChildTableDescriptor.Appearance.AlternateRecordFieldCell.BackColor = [Color].FromArgb(255, 245, 227);]                                 |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [// To hide the Key column.]                                                                                                                                 |
|                                                                                                                                                                                                                |
| [usStatesRd.ChildTableDescriptor.VisibleColumns.Add([\"Name\"]);]                                                                                  |
|                                                                                                                                                                                                                |
| [usStatesRd.ChildTableDescriptor.SortedColumns.Add([\"Name\"]);]                                                                                   |
|                                                                                                                                                                                                                |
| [usStatesRd.ChildTableDescriptor.AllowEdit = [false];]                                                                                                |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [// Disallow users to modify states.]                                                                                                                        |
|                                                                                                                                                                                                                |
| [usStatesRd.ChildTableDescriptor.AllowNew = [false];]                                                                                                 |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [mainTd.Relations.Add(usStatesRd);]                                                                                                                                        |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [// Assign data source.]                                                                                                                                     |
|                                                                                                                                                                                                                |
| [this][.gridGroupingControl1.DataSource = table;]                                                                         |
|                                                                                                                                                                                                                |
| [mainTd.Name = [\"ForeignKeyReference\"];]                                                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                 |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                               |
|                                                                                                                                                                                                                    |
| [Dim][ mainTd [As] GridTableDescriptor = [Me].gridGroupingControl1.TableDescriptor] |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                                             |
|                                                                                                                                                                                                                    |
| [Dim][ usStatesRd [As] [New] GridRelationDescriptor()]                              |
|                                                                                                                                                                                                                    |
| [usStatesRd.Name = [\"State\"]]                                                                                                                        |
|                                                                                                                                                                                                                    |
| [usStatesRd.RelationKind = RelationKind.ForeignKeyReference]                                                                                                                   |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                                             |
|                                                                                                                                                                                                                    |
| [\' SourceListSet name for look up.]                                                                                                                             |
|                                                                                                                                                                                                                    |
| [usStatesRd.ChildTableName = [\"USStates\"]]                                                                                                           |
|                                                                                                                                                                                                                    |
| [usStatesRd.RelationKeys.Add([\"State\"], [\"Key\"])]                                                                          |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                               |
|                                                                                                                                                                                                                    |
| [\' Format ChildList.]                                                                                                                                           |
|                                                                                                                                                                                                                    |
| [usStatesRd.ChildTableDescriptor.Appearance.AlternateRecordFieldCell.BackColor = Color.FromArgb(255, 245, 227)]                                                                |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                                             |
|                                                                                                                                                                                                                    |
| [\' To hide the Key Column.]                                                                                                                                     |
|                                                                                                                                                                                                                    |
| [usStatesRd.ChildTableDescriptor.VisibleColumns.Add([\"Name\"])]                                                                                       |
|                                                                                                                                                                                                                    |
| [usStatesRd.ChildTableDescriptor.SortedColumns.Add([\"Name\"])]                                                                                        |
|                                                                                                                                                                                                                    |
| [usStatesRd.ChildTableDescriptor.AllowEdit = [False]]                                                                                                     |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                                |
|                                                                                                                                                                                                                    |
| [\' Disallow users to modify states.]                                                                                                                            |
|                                                                                                                                                                                                                    |
| [usStatesRd.ChildTableDescriptor.AllowNew = [False]]                                                                                                      |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                                             |
|                                                                                                                                                                                                                    |
| [mainTd.Relations.Add(usStatesRd)]                                                                                                                                             |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                               |
|                                                                                                                                                                                                                    |
| [\' Assign data source.]                                                                                                                                         |
|                                                                                                                                                                                                                    |
| [Me][.gridGroupingControl1.DataSource = table]                                                                                |
|                                                                                                                                                                                                                    |
| [mainTd.Name = [\"ForeignKeyReference\"]]                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   Here is a sample output that displays a look up child list for the data column **State** with value **Georgia.**

**[]** 

{border="0"}

[] 

*[Figure ][312][: ForeignKeyReference Relation]*

[] 


{border="0"}Note: For more details, refer the following browser sample:

 

\<Install Location\>\\Syncfusion\\EssentialStudio\\\[Version Number\]\\Windows\\Grid.Grouping.Windows\\Samples\\2.0\\Relations And Hierarchy\\Foreign-Key Reference Demo


[] 

GridForeignKeyHelper

[] 

GridForeignKeyHelper is a helper class that makes it easy for the users to use foreign key relations to do foreign key look ups. With this class available, the users can easily hook up a foreign table by a single method call instead of going through all the steps described above.

 

The GridForeignKeyHelper class exposes a static method called SetupForeignTableLookUp that accepts grouping grid, main table, foreign table, main table column, foreign table value column and foreign table display column and sets up the Foreign Key relation using these parameter values.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                        |
| [string][ valueColInMainTable = [\"Country\"], valueColInForeignTable = [\"CountryCode\"], displayColInForeignTable = [\"CountryName\"];] |
|                                                                                                                                                                                                                                                                                                        |
| [GridForeignKeyHelper.SetupForeignTableLookUp(gridGroupingControl1, valueColInMainTable, countries, valueColInForeignTable, displayColInForeignTable);]                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                               |
| [Dim][ valueColInMainTable [As] [String] = [\"Country\"], valueColInForeignTable [As] [String] = [\"CountryCode\"],] |
|                                                                                                                                                                                                                                                                                                                                               |
| [displayColInForeignTable [As] [String] = [\"CountryName\"]]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                               |
| [GridForeignKeyHelper.SetupForeignTableLookUp(gridGroupingControl1, valueColInMainTable, countries, valueColInForeignTable, displayColInForeignTable)]                                                                                                                                                    |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p442} 

 

###### []{#_Foreign_Key_KeyWords}4.3.4.3.5.3 Foreign Key KeyWords Relation {#foreign-key-keywords-relation style="tab-stops: 0pt"}

[] 

**ForeignKeyKeyWords** is a unique relation kind which, is offered by the grouping engine. It is a foreign key relation where matching keys in the columns of the parent and child table define a relationship between the two tables. This is an m:n relation. Field summaries of the related child table can be referenced using a '.' dot in the FieldDescriptor.MappingName of the main table. This relation kind allows you to have multi-valued columns in the grid.

 

**Example**

**[]** 

Say you have a Customers table. Each customer can have a list of purchased items. With MasterDetails, for a given customer, the underlying child list (the list of items purchased by that customer) will be displayed in a separate table once the RecordPlusMinus button is clicked. Instead if you want to view the entire record along with the related child records in a single row, then ForeignKeyKeyWords would be the right choice to use.

 

The following example illustrates creation of ForeignKeyKeyWords relation.

[] 

1.   Create two data tables Customers and Items and add a list of records into them.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                              |
|                                                                                                                                                                                             |
| []                                                                                                                                        |
|                                                                                                                                                                                             |
| [private][ [int] numberParentRows = 6;]                                           |
|                                                                                                                                                                                             |
| [private][ [int] numberChildRows = 20;]                                           |
|                                                                                                                                                                                             |
| []                                                                                                                                                      |
|                                                                                                                                                                                             |
| [private][ [DataTable] GetParentTable()]                                       |
|                                                                                                                                                                                             |
| [{]                                                                                                                                                     |
|                                                                                                                                                                                             |
| [    [DataTable] dt = [new] [DataTable]([\"Customers\"]);] |
|                                                                                                                                                                                             |
| []                                                                                                                                                      |
|                                                                                                                                                                                             |
| [    dt.Columns.Add([new] [DataColumn]([\"customerID\"]));]                        |
|                                                                                                                                                                                             |
| [    dt.Columns.Add([new] [DataColumn]([\"CustomerName\"]));]                      |
|                                                                                                                                                                                             |
| [    dt.Columns.Add([new] [DataColumn]([\"Address\"]));]                           |
|                                                                                                                                                                                             |
| []                                                                                                                                                      |
|                                                                                                                                                                                             |
| [    [for]([int] i = 0; i \< numberParentRows; ++i)]                                                          |
|                                                                                                                                                                                             |
| [    {]                                                                                                                                                 |
|                                                                                                                                                                                             |
| [        [DataRow] dr = dt.NewRow();]                                                                                           |
|                                                                                                                                                                                             |
| [        dr\[0\] = i;]                                                                                                                                  |
|                                                                                                                                                                                             |
| [        dr\[1\] = [string].Format([\"CustomerName{0}\"], i);]                                             |
|                                                                                                                                                                                             |
| [        dr\[2\] = [string].Format([\"Address{0}\"], i);]                                                  |
|                                                                                                                                                                                             |
| [        dt.Rows.Add(dr);]                                                                                                                              |
|                                                                                                                                                                                             |
| [    }]                                                                                                                                                 |
|                                                                                                                                                                                             |
| []                                                                                                                                                      |
|                                                                                                                                                                                             |
| [    [return] dt;]                                                                                                                 |
|                                                                                                                                                                                             |
| [}]                                                                                                                                                     |
|                                                                                                                                                                                             |
| []                                                                                                                                                      |
|                                                                                                                                                                                             |
| [private][ [DataTable] GetChildTable()]                                        |
|                                                                                                                                                                                             |
| [{]                                                                                                                                                     |
|                                                                                                                                                                                             |
| [    [DataTable] dt = [new] [DataTable]([\"Items\"]);]     |
|                                                                                                                                                                                             |
| []                                                                                                                                                      |
|                                                                                                                                                                                             |
| [    dt.Columns.Add([new] [DataColumn]([\"ItemID\"])); ]                           |
|                                                                                                                                                                                             |
| [    dt.Columns.Add([new] [DataColumn]([\"ItemName\"]));]                          |
|                                                                                                                                                                                             |
| [    dt.Columns.Add([new] [DataColumn]([\"CustomerID\"]));]                        |
|                                                                                                                                                                                             |
| [    dt.Columns.Add([new] [DataColumn]([\"Price\"])); ]                            |
|                                                                                                                                                                                             |
| [    [Random] rand = [new] [Random]();]                                            |
|                                                                                                                                                                                             |
| [    [for]([int] i = 0; i \< numberChildRows; ++i)]                                                           |
|                                                                                                                                                                                             |
| [    {]                                                                                                                                                 |
|                                                                                                                                                                                             |
| [        [DataRow] dr = dt.NewRow();]                                                                                           |
|                                                                                                                                                                                             |
| [        dr\[0\] = i.ToString();]                                                                                                                       |
|                                                                                                                                                                                             |
| [        dr\[1\] = [string].Format([\"ItemName{0}\"],i);]                                                  |
|                                                                                                                                                                                             |
| [        dr\[2\] = (i % numberParentRows).ToString();]                                                                                                  |
|                                                                                                                                                                                             |
| [        dr\[3\] = rand.Next(500).ToString();]                                                                                                          |
|                                                                                                                                                                                             |
| [        dt.Rows.Add(dr);]                                                                                                                              |
|                                                                                                                                                                                             |
| [    }]                                                                                                                                                 |
|                                                                                                                                                                                             |
| [            ]                                                                                                                                          |
|                                                                                                                                                                                             |
| [    [return] dt;]                                                                                                                 |
|                                                                                                                                                                                             |
| [}]                                                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                  |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                |
|                                                                                                                                                                                                                     |
| [Private][ numberParentRows [As] [Integer] = 6]                                      |
|                                                                                                                                                                                                                     |
| [Private][ numberChildRows [As] [Integer] = 20]                                      |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                              |
|                                                                                                                                                                                                                     |
| [Private][ [Function] GetParentTable() [As] DataTable]                               |
|                                                                                                                                                                                                                     |
| [Dim][ dt [As] DataTable = [New] DataTable([\"Customers\"])] |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                              |
|                                                                                                                                                                                                                     |
| [dt.Columns.Add([New] DataColumn([\"customerID\"]))]                                                                               |
|                                                                                                                                                                                                                     |
| [dt.Columns.Add([New] DataColumn([\"CustomerName\"]))]                                                                             |
|                                                                                                                                                                                                                     |
| [dt.Columns.Add([New] DataColumn([\"Address\"]))]                                                                                  |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                              |
|                                                                                                                                                                                                                     |
| [Dim][ i [As] [Integer] = 0]                                                         |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                              |
|                                                                                                                                                                                                                     |
| [Do][ [While] i \< numberParentRows]                                                                      |
|                                                                                                                                                                                                                     |
| [Dim][ dr [As] DataRow = dt.NewRow()]                                                                     |
|                                                                                                                                                                                                                     |
| [dr(0) = i]                                                                                                                                                                     |
|                                                                                                                                                                                                                     |
| [dr(1) = [String].Format([\"CustomerName{0}\"], i)]                                                                                |
|                                                                                                                                                                                                                     |
| [dr(2) = [String].Format([\"Address{0}\"], i)]                                                                                     |
|                                                                                                                                                                                                                     |
| [dt.Rows.Add(dr)]                                                                                                                                                               |
|                                                                                                                                                                                                                     |
| [i += 1]                                                                                                                                                                        |
|                                                                                                                                                                                                                     |
| [Loop]                                                                                                                                                             |
|                                                                                                                                                                                                                     |
| [Return][ dt]                                                                                                                  |
|                                                                                                                                                                                                                     |
| [End][ [Function]]                                                                                        |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                                     |
| [Private][ [Function] GetChildTable() [As] DataTable]                                |
|                                                                                                                                                                                                                     |
| [Dim][ dt [As] DataTable = [New] DataTable([\"Items\"])]     |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                              |
|                                                                                                                                                                                                                     |
| [dt.Columns.Add([New] DataColumn([\"ItemID\"]))]                                                                                   |
|                                                                                                                                                                                                                     |
| [dt.Columns.Add([New] DataColumn([\"ItemName\"]))]                                                                                 |
|                                                                                                                                                                                                                     |
| [dt.Columns.Add([New] DataColumn([\"CustomerID\"]))]                                                                               |
|                                                                                                                                                                                                                     |
| [dt.Columns.Add([New] DataColumn([\"Price\"]))]                                                                                    |
|                                                                                                                                                                                                                     |
| [Dim][ rand [As] Random = [New] Random()]                                            |
|                                                                                                                                                                                                                     |
| [Dim][ i [As] [Integer] = 0]                                                         |
|                                                                                                                                                                                                                     |
| [Do][ [While] i \< numberChildRows]                                                                       |
|                                                                                                                                                                                                                     |
| [Dim][ dr [As] DataRow = dt.NewRow()]                                                                     |
|                                                                                                                                                                                                                     |
| [dr(0) = i.ToString()]                                                                                                                                                          |
|                                                                                                                                                                                                                     |
| [dr(1) = [String].Format([\"ItemName{0}\"], i)]                                                                                    |
|                                                                                                                                                                                                                     |
| [dr(2) = (i [Mod] numberParentRows).ToString()]                                                                                                            |
|                                                                                                                                                                                                                     |
| [dr(3) = rand.Next(500).ToString()]                                                                                                                                             |
|                                                                                                                                                                                                                     |
| [dt.Rows.Add(dr)]                                                                                                                                                               |
|                                                                                                                                                                                                                     |
| [i += 1]                                                                                                                                                                        |
|                                                                                                                                                                                                                     |
| [Loop]                                                                                                                                                             |
|                                                                                                                                                                                                                     |
| [Return][ dt]                                                                                                                  |
|                                                                                                                                                                                                                     |
| [End][ [Function]]                                                                                        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Register the child table (Items) into the SourceListSet of the grouping engine.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                |
|                                                                                                                                                                                               |
| []                                                                                                                                          |
|                                                                                                                                                                                               |
| [DataTable][ parentTable = GetParentTable();]                                                         |
|                                                                                                                                                                                               |
| [DataTable][ childTable = GetChildTable();]                                                           |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [this][.gridGroupingControl1.Engine.SourceListSet.Add([\"Items\"], childTable);] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                         |
|                                                                                                                                                                                            |
| []                                                                                                                                       |
|                                                                                                                                                                                            |
| [Dim ][parentTable [As ]DataTable = GetParentTable()]                            |
|                                                                                                                                                                                            |
| [Dim ][childTable [As ]DataTable = GetChildTable()]                              |
|                                                                                                                                                                                            |
| []                                                                                                                                                     |
|                                                                                                                                                                                            |
| [Me][.gridGroupingControl1.Engine.SourceListSet.Add([\"Items\"], childTable)] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Assign the datasource to the grid.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                               |
|                                                                                                                                              |
| []                                                                                         |
|                                                                                                                                              |
| [this][.gridGroupingControl1.DataSource = parentTable;] |
+----------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                        |
|                                                                                                                                           |
| []                                                                                      |
|                                                                                                                                           |
| [Me][.gridGroupingControl1.DataSource = parentTable] |
+-------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Establish ForeignKeyKeyWords relationship between the tables.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                    |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                              |
|                                                                                                                                                                                                                   |
| [GridRelationDescriptor][ childRelation = [new] [GridRelationDescriptor]();] |
|                                                                                                                                                                                                                   |
| [childRelation.RelationKind = [RelationKind].ForeignKeyKeyWords;]                                                                                     |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                                   |
| [// SourceListSet name for look up.]                                                                                                                            |
|                                                                                                                                                                                                                   |
| [childRelation.ChildTableName = [\"Items\"]; ]                                                                                                        |
|                                                                                                                                                                                                                   |
| [childRelation.RelationKeys.Add([\"customerID\"], [\"CustomerID\"]);]                                                         |
|                                                                                                                                                                                                                   |
| [childRelation.ChildTableDescriptor.AllowEdit = [true];]                                                                                                 |
|                                                                                                                                                                                                                   |
| [childRelation.ChildTableDescriptor.AllowNew = [true];]                                                                                                  |
|                                                                                                                                                                                                                   |
| [this][.gridGroupingControl1.TableDescriptor.Relations.Add(childRelation);]                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                              |
|                                                                                                                                                                                                                   |
| [Dim][ childRelation [As] GridRelationDescriptor = [New] GridRelationDescriptor()] |
|                                                                                                                                                                                                                   |
| [childRelation.RelationKind = RelationKind.ForeignKeyKeyWords]                                                                                                                |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                                   |
| [\' SourceListSet name for look up.]                                                                                                                            |
|                                                                                                                                                                                                                   |
| [childRelation.ChildTableName = [\"Items\"]]                                                                                                          |
|                                                                                                                                                                                                                   |
| [childRelation.RelationKeys.Add([\"customerID\"], [\"CustomerID\"])]                                                          |
|                                                                                                                                                                                                                   |
| [childRelation.ChildTableDescriptor.AllowEdit = [True];]                                                                                                 |
|                                                                                                                                                                                                                   |
| [childRelation.ChildTableDescriptor.AllowNew = [True];]                                                                                                  |
|                                                                                                                                                                                                                   |
| [Me][.gridGroupingControl1.TableDescriptor.Relations.Add(childRelation)]                                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   Here is a sample output.

[] 

{border="0"}

[] 

*[Figure ][313][: ForeignKeyKeyWords Relation]*

[] 


{border="0"}Note: For more details, refer the following browser sample:

 

\<Install Location\>\\Syncfusion\\EssentialStudio\\\[Version Number\]\\Windows\\Grid.Grouping.Windows\\Samples\\2.0\\Relations And Hierarchy\\Employee Territory Order Demo


 

[]{#p443} 

 

###### []{#_ListItem_Reference_Relation}4.3.4.3.5.4 ListItem Reference Relation {#listitem-reference-relation style="tab-stops: 0pt"}

[] 

**ListItemReference** is an object reference relation for looking up values from a strong typed collection. Like ForeignKeyReference, it is also an n:1 relation where multiple records in the parent table can reference the same record in the related table. One difference between the ForeignKeyReference and ListItemReference is that the former uses a key to look up the values where as the later uses an object to look up the values in a nested collection.

 

**Steps to setup ListItemReference relation**

 

This section sets up a ListItemReference relation between a data table and the collection **Countries**. The data table represents the Parent Table of the relation and the Countries collection serves as the related child list where in the values can be looked up using an object of the child list. The collection derives from ArrayList in which every item is a **Country** object having two properties, **CountryCode** and **Name**. It also defines a method named **CreateDefaultCollection()** that returns an instance of itself populated with a set of values.

 

This relation kind can be set up by defining a relation descriptor with its attributes carrying the relation details and adding this descriptor to the Relations collection of the main table.

 

The following steps demonstrate this process.

[] 

1.   Create a collection named **Countries** in which each entry stores a **Country** object.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                             |
|                                                                                                                                                                                                                            |
| []                                                                                                                                                                       |
|                                                                                                                                                                                                                            |
| [// Countries Collection.]                                                                                                                                               |
|                                                                                                                                                                                                                            |
| [\[[Serializable]\]]                                                                                                                                           |
|                                                                                                                                                                                                                            |
| [public][ [class] [CountriesCollection] : [ArrayList]]           |
|                                                                                                                                                                                                                            |
| [{]                                                                                                                                                                                    |
|                                                                                                                                                                                                                            |
| [    [public] [new] [Country] [this]\[[int] index\]]                       |
|                                                                                                                                                                                                                            |
| [    {]                                                                                                                                                                                |
|                                                                                                                                                                                                                            |
| [        [get]]                                                                                                                                                   |
|                                                                                                                                                                                                                            |
| [        {]                                                                                                                                                                            |
|                                                                                                                                                                                                                            |
| [            [return] ([Country]) [base]\[index\];]                                                                  |
|                                                                                                                                                                                                                            |
| [        }]                                                                                                                                                                            |
|                                                                                                                                                                                                                            |
| [        [set]]                                                                                                                                                   |
|                                                                                                                                                                                                                            |
| [        {]                                                                                                                                                                            |
|                                                                                                                                                                                                                            |
| [            [base]\[index\] = [value];]                                                                                                     |
|                                                                                                                                                                                                                            |
| [        }]                                                                                                                                                                            |
|                                                                                                                                                                                                                            |
| [    }]                                                                                                                                                                                |
|                                                                                                                                                                                                                            |
| []                                                                                                                                                                                     |
|                                                                                                                                                                                                                            |
| [    [public] [static] [CountriesCollection] CreateDefaultCollection()]                                              |
|                                                                                                                                                                                                                            |
| [    {]                                                                                                                                                                                |
|                                                                                                                                                                                                                            |
| [        [CountriesCollection] countries = [new] [CountriesCollection]();]                                        |
|                                                                                                                                                                                                                            |
| [        countries.Add([new] [Country]([\"US\"], [\"United States\"]));]                  |
|                                                                                                                                                                                                                            |
| [        countries.Add([new] [Country]([\"CA\"], [\"Canada\"]));]                         |
|                                                                                                                                                                                                                            |
| [        countries.Add([new] [Country]([\"AU\"], [\"Australia\"]));]                      |
|                                                                                                                                                                                                                            |
| [        countries.Add([new] [Country]([\"BR\"], [\"Brazil\"]));]                         |
|                                                                                                                                                                                                                            |
| [        countries.Add([new] [Country]([\"IO\"], [\"British Indian Ocean Territory\"]));] |
|                                                                                                                                                                                                                            |
| [        countries.Add([new] [Country]([\"CN\"], [\"China\"]));]                          |
|                                                                                                                                                                                                                            |
| [        countries.Add([new] [Country]([\"FI\"], [\"Finland\"]));]                        |
|                                                                                                                                                                                                                            |
| [        countries.Add([new] [Country]([\"FR\"], [\"France\"]));]                         |
|                                                                                                                                                                                                                            |
| [        countries.Add([new] [Country]([\"DE\"], [\"Germany\"]));]                        |
|                                                                                                                                                                                                                            |
| [        countries.Add([new] [Country]([\"HK\"], [\"Hong Kong\"]));]                      |
|                                                                                                                                                                                                                            |
| [        countries.Add([new] [Country]([\"HU\"], [\"Hungary\"]));]                        |
|                                                                                                                                                                                                                            |
| [        countries.Add([new] [Country]([\"IS\"], [\"Iceland\"]));]                        |
|                                                                                                                                                                                                                            |
| [        countries.Add([new] [Country]([\"IN\"], [\"India\"]));]                          |
|                                                                                                                                                                                                                            |
| [        countries.Add([new] [Country]([\"JP\"], [\"Japan\"]));]                          |
|                                                                                                                                                                                                                            |
| [        countries.Add([new] [Country]([\"MY\"], [\"Malaysia\"]));]                       |
|                                                                                                                                                                                                                            |
| [        countries.Add([new] [Country]([\"SG\"], [\"Singapore\"]));]                      |
|                                                                                                                                                                                                                            |
| [        countries.Add([new] [Country]([\"CH\"], [\"Switzerland\"]));]                    |
|                                                                                                                                                                                                                            |
| [        [return] countries;]                                                                                                                                     |
|                                                                                                                                                                                                                            |
| [    }]                                                                                                                                                                                |
|                                                                                                                                                                                                                            |
| []                                                                                                                                                                                     |
|                                                                                                                                                                                                                            |
| [    [public] [override] [bool] IsReadOnly]                                                                             |
|                                                                                                                                                                                                                            |
| [    {]                                                                                                                                                                                |
|                                                                                                                                                                                                                            |
| [        [get]]                                                                                                                                                   |
|                                                                                                                                                                                                                            |
| [        {]                                                                                                                                                                            |
|                                                                                                                                                                                                                            |
| [            [return] [true];]                                                                                                               |
|                                                                                                                                                                                                                            |
| [        }]                                                                                                                                                                            |
|                                                                                                                                                                                                                            |
| [    }]                                                                                                                                                                                |
|                                                                                                                                                                                                                            |
| []                                                                                                                                                                                     |
|                                                                                                                                                                                                                            |
| [    [public] [override] [bool] IsFixedSize]                                                                            |
|                                                                                                                                                                                                                            |
| [    {]                                                                                                                                                                                |
|                                                                                                                                                                                                                            |
| [        [get]]                                                                                                                                                   |
|                                                                                                                                                                                                                            |
| [        {]                                                                                                                                                                            |
|                                                                                                                                                                                                                            |
| [            [return] [true];]                                                                                                               |
|                                                                                                                                                                                                                            |
| [        }]                                                                                                                                                                            |
|                                                                                                                                                                                                                            |
| [    }]                                                                                                                                                                                |
|                                                                                                                                                                                                                            |
| []                                                                                                                                                                                     |
|                                                                                                                                                                                                                            |
| [}]                                                                                                                                                                                    |
|                                                                                                                                                                                                                            |
| []                                                                                                                                                                                     |
|                                                                                                                                                                                                                            |
| [// Country Class.]                                                                                                                                                      |
|                                                                                                                                                                                                                            |
| [\[[Serializable]\]]                                                                                                                                           |
|                                                                                                                                                                                                                            |
| [public][ [class] [Country]]                                                             |
|                                                                                                                                                                                                                            |
| [{]                                                                                                                                                                                    |
|                                                                                                                                                                                                                            |
| [    [private] [string] \_code;]                                                                                                             |
|                                                                                                                                                                                                                            |
| [    [private] [string] \_name;]                                                                                                             |
|                                                                                                                                                                                                                            |
| []                                                                                                                                                                                     |
|                                                                                                                                                                                                                            |
| [    [public]  Country()]                                                                                                                                         |
|                                                                                                                                                                                                                            |
| [    {]                                                                                                                                                                                |
|                                                                                                                                                                                                                            |
| [    }]                                                                                                                                                                                |
|                                                                                                                                                                                                                            |
| []                                                                                                                                                                                     |
|                                                                                                                                                                                                                            |
| [    [public]  Country([string] strCode, [string] strName)]                                                             |
|                                                                                                                                                                                                                            |
| [    {]                                                                                                                                                                                |
|                                                                                                                                                                                                                            |
| [        [this].\_code = strCode;]                                                                                                                                |
|                                                                                                                                                                                                                            |
| [        [this].\_name = strName;]                                                                                                                                |
|                                                                                                                                                                                                                            |
| [    }]                                                                                                                                                                                |
|                                                                                                                                                                                                                            |
| []                                                                                                                                                                                     |
|                                                                                                                                                                                                                            |
| [    \[[Browsable]([true])\]]                                                                                                             |
|                                                                                                                                                                                                                            |
| [    [public] [string] CountryCode]                                                                                                          |
|                                                                                                                                                                                                                            |
| [    {]                                                                                                                                                                                |
|                                                                                                                                                                                                                            |
| [        [get]]                                                                                                                                                   |
|                                                                                                                                                                                                                            |
| [        {]                                                                                                                                                                            |
|                                                                                                                                                                                                                            |
| [            [return] \_code;]                                                                                                                                    |
|                                                                                                                                                                                                                            |
| [        }]                                                                                                                                                                            |
|                                                                                                                                                                                                                            |
| [        [set]]                                                                                                                                                   |
|                                                                                                                                                                                                                            |
| [        {]                                                                                                                                                                            |
|                                                                                                                                                                                                                            |
| [            \_code = [value];]                                                                                                                                   |
|                                                                                                                                                                                                                            |
| [        }]                                                                                                                                                                            |
|                                                                                                                                                                                                                            |
| [    }]                                                                                                                                                                                |
|                                                                                                                                                                                                                            |
| []                                                                                                                                                                                     |
|                                                                                                                                                                                                                            |
| [    \[[Browsable]([true])\]]                                                                                                             |
|                                                                                                                                                                                                                            |
| [    [public] [string] Name]                                                                                                                 |
|                                                                                                                                                                                                                            |
| [    {]                                                                                                                                                                                |
|                                                                                                                                                                                                                            |
| [        [get]]                                                                                                                                                   |
|                                                                                                                                                                                                                            |
| [        {]                                                                                                                                                                            |
|                                                                                                                                                                                                                            |
| [            [return] \_name ;]                                                                                                                                   |
|                                                                                                                                                                                                                            |
| [        }]                                                                                                                                                                            |
|                                                                                                                                                                                                                            |
| [        [set]]                                                                                                                                                   |
|                                                                                                                                                                                                                            |
| [        {]                                                                                                                                                                            |
|                                                                                                                                                                                                                            |
| [            \_name = [value];]                                                                                                                                   |
|                                                                                                                                                                                                                            |
| [        }]                                                                                                                                                                            |
|                                                                                                                                                                                                                            |
| [    }]                                                                                                                                                                                |
|                                                                                                                                                                                                                            |
| []                                                                                                                                                                                     |
|                                                                                                                                                                                                                            |
| [    [public] [override] [string] ToString()]                                                                           |
|                                                                                                                                                                                                                            |
| [    {]                                                                                                                                                                                |
|                                                                                                                                                                                                                            |
| [        [return] [this].\_name + [\"(\"] + [this].\_code + [\")\"];]   |
|                                                                                                                                                                                                                            |
| [    }]                                                                                                                                                                                |
|                                                                                                                                                                                                                            |
| [}]                                                                                                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                      |
| [\'Countries Collection]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                      |
| [\<Serializable()\>  \_]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                      |
| [Public][ [Class] CountriesCollection]                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                      |
| [Inherits][ ArrayList]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                      |
| [        ]                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                      |
| [Default][ [Public] [Shadows] [Property] Item(index [As] [Integer]) [As] Country] |
|                                                                                                                                                                                                                                                                                                      |
| [Get]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                      |
| [Return][ [CType]([MyBase].Item(index), Country)]                                                                                                                     |
|                                                                                                                                                                                                                                                                                                      |
| [End][ [Get]]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                      |
| [Set]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                      |
| [MyBase][.Item(index) = Value]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                      |
| [End][ [Set]]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                      |
| [End][ [Property]        ]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                      |
| [        ]                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                      |
| [Public][ [Shared] [Function] CreateDefaultCollection() [As] CountriesCollection]                                                                |
|                                                                                                                                                                                                                                                                                                      |
| [      [Dim] countries [As] [New] CountriesCollection()]                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                      |
| [      countries.Add([New] Country([\"US\"], [\"United States\"]))]                                                                                                                         |
|                                                                                                                                                                                                                                                                                                      |
| [      countries.Add([New] Country([\"CA\"], [\"Canada\"]))]                                                                                                                                |
|                                                                                                                                                                                                                                                                                                      |
| [      countries.Add([New] Country([\"AU\"], [\"Australia\"]))]                                                                                                                             |
|                                                                                                                                                                                                                                                                                                      |
| [      countries.Add([New] Country([\"BR\"], [\"Brazil\"]))]                                                                                                                                |
|                                                                                                                                                                                                                                                                                                      |
| [      countries.Add([New] Country([\"IO\"], [\"British Indian Ocean Territory\"]))]                                                                                                        |
|                                                                                                                                                                                                                                                                                                      |
| [      countries.Add([New] Country([\"CN\"], [\"China\"]))]                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                      |
| [      countries.Add([New] Country([\"FI\"], [\"Finland\"]))]                                                                                                                               |
|                                                                                                                                                                                                                                                                                                      |
| [      countries.Add([New] Country([\"FR\"], [\"France\"]))]                                                                                                                                |
|                                                                                                                                                                                                                                                                                                      |
| [      countries.Add([New] Country([\"DE\"], [\"Germany\"]))]                                                                                                                               |
|                                                                                                                                                                                                                                                                                                      |
| [      countries.Add([New] Country([\"HK\"], [\"Hong Kong\"]))]                                                                                                                             |
|                                                                                                                                                                                                                                                                                                      |
| [      countries.Add([New] Country([\"HU\"], [\"Hungary\"]))]                                                                                                                               |
|                                                                                                                                                                                                                                                                                                      |
| [      countries.Add([New] Country([\"IS\"], [\"Iceland\"]))]                                                                                                                               |
|                                                                                                                                                                                                                                                                                                      |
| [      countries.Add([New] Country([\"IN\"], [\"India\"]))]                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                      |
| [      countries.Add([New] Country([\"JP\"], [\"Japan\"]))]                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                      |
| [      countries.Add([New] Country([\"MY\"], [\"Malaysia\"]))]                                                                                                                              |
|                                                                                                                                                                                                                                                                                                      |
| [      countries.Add([New] Country([\"SG\"], [\"Singapore\"]))]                                                                                                                             |
|                                                                                                                                                                                                                                                                                                      |
| [      countries.Add([New] Country([\"CH\"], [\"Switzerland\"]))]                                                                                                                           |
|                                                                                                                                                                                                                                                                                                      |
| [      [Return] countries]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                      |
| [End][ [Function]]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                      |
| [Public][ [Overrides] [ReadOnly] [Property] IsReadOnly() [As] [Boolean]]                               |
|                                                                                                                                                                                                                                                                                                      |
| [Get]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                      |
| [Return][ [True]]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                      |
| [End][ [Get]]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                      |
| [End][ [Property]]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                      |
| [        ]                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                      |
| [        ]                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                      |
| [Public][ [Overrides] [ReadOnly] [Property] IsFixedSize() [As] [Boolean]]                              |
|                                                                                                                                                                                                                                                                                                      |
| [Get]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                      |
| [Return][ [True]]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                      |
| [End][ [Get]]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                      |
| [End][ [Property]]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                      |
| [End][ [Class]]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                      |
| [\' Country Class.]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                      |
| [\<Serializable()\>  \_]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                      |
| [Public][ [Class] Country]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                      |
| [Private][ \_code [As] [String]]                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                      |
| [Private][ \_name [As] [String]]                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                      |
| [        ]                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                      |
| [Public][ [Sub] [New]()]                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                      |
| [End][ [Sub]]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                      |
| [        ]                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                      |
| [Public][ [Sub] [New](strCode [As] [String], strName [As] [String])]              |
|                                                                                                                                                                                                                                                                                                      |
| [Me][.\_code = strCode]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                      |
| [Me][.\_name = strName]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                      |
| [End][ [Sub]]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                      |
| [        ]                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                      |
| [\<Browsable([True])\>  \_]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                      |
| [Public][ [Property] CountryCode() [As] [String]]                                                                                                |
|                                                                                                                                                                                                                                                                                                      |
| [Get]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                      |
| [Return][ \_code]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                      |
| [End][ [Get]]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                      |
| [Set]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                      |
| [\_code = value]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                      |
| [End][ [Set]]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                      |
| [End][ [Property]]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                      |
| [        ]                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                      |
| [\<Browsable([True])\>  \_]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                      |
| [Public][ [Property] Name() [As] [String]]                                                                                                       |
|                                                                                                                                                                                                                                                                                                      |
| [Get]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                      |
| [Return][ \_name]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                      |
| [End][ [Get]]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                      |
| [Set]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                      |
| [\_name = value]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                      |
| [End][ [Set]]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                      |
| [End][ [Property]]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                      |
| [        ]                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                      |
| [Public][ [Overrides] [Function] ToString() [As] [String]]                                                                  |
|                                                                                                                                                                                                                                                                                                      |
| [Return][ [Me].\_name + [\"(\"] + [Me].\_code + [\")\"]]                                                              |
|                                                                                                                                                                                                                                                                                                      |
| [End][ [Function]]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                      |
| [End][ [Class]]                                                                                                                                                                            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Create an object of USStates and add this object into the SourceListSet with a lookup name.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                   |
|                                                                                                                                                                                                  |
| []                                                                                                                                              |
|                                                                                                                                                                                                  |
| [CountriesCollection countries = CountriesCollection.CreateDefaultCollection();]                                                                             |
|                                                                                                                                                                                                  |
| [this][.gridGroupingControl1.Engine.SourceListSet.Add([\"Countries\"], countries);] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                   |
|                                                                                                                                                                                                      |
| []                                                                                                                                                 |
|                                                                                                                                                                                                      |
| [Dim][ countries [As] CountriesCollection = CountriesCollection.CreateDefaultCollection()] |
|                                                                                                                                                                                                      |
| [Me][.gridGroupingControl1.Engine.SourceListSet.Add([\"Countries\"], countries)]        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Create a datatable with one of the columns is of type **Country**.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                  |
|                                                                                                                                                                                 |
| []                                                                                                                            |
|                                                                                                                                                                                 |
| [DataTable][ table = [new] [DataTable]();] |
|                                                                                                                                                                                 |
| [table.Columns.Add([\"Id\"], [typeof]([string]));]                        |
|                                                                                                                                                                                 |
| [table.Columns.Add([\"Country\"], [typeof](Country));]                                         |
|                                                                                                                                                                                 |
| []                                                                                                                                          |
|                                                                                                                                                                                 |
| [// Adding Rows.]                                                                                                             |
|                                                                                                                                                                                 |
| [for][ ([int] i = 0; i \< 25; i++)]                                   |
|                                                                                                                                                                                 |
| [{]                                                                                                                                         |
|                                                                                                                                                                                 |
| [    table.Rows.Add(table.NewRow());]                                                                                                       |
|                                                                                                                                                                                 |
| [    table.Rows\[i\]\[0\] = i;]                                                                                                             |
|                                                                                                                                                                                 |
| [    table.Rows\[i\]\[1\] = countries\[i % 8\];]                                                                                            |
|                                                                                                                                                                                 |
| [}]                                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                  |
|                                                                                                                                                                     |
| []                                                                                                                |
|                                                                                                                                                                     |
| [Dim][ table [As] [New] DataTable()] |
|                                                                                                                                                                     |
| [table.Columns.Add([\"Id\"], [GetType]([String]))]            |
|                                                                                                                                                                     |
| [table.Columns.Add([\"Country\"], [GetType](Country))]                             |
|                                                                                                                                                                     |
| []                                                                                                                              |
|                                                                                                                                                                     |
| [\' Adding Rows.]                                                                                                 |
|                                                                                                                                                                     |
| [Dim][ i [As] [Integer]]             |
|                                                                                                                                                                     |
| [For][ i = 0 [To] 24]                                     |
|                                                                                                                                                                     |
| [table.Rows.Add(table.NewRow())]                                                                                                |
|                                                                                                                                                                     |
| [table.Rows(i)(0) = i]                                                                                                          |
|                                                                                                                                                                     |
| [table.Rows(i)(1) = countries((i [Mod] 8))]                                                                |
|                                                                                                                                                                     |
| [Next][ i]                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Establish the ForeignKeyReference relationship.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                  |
|                                                                                                                                                                                                                 |
| []                                                                                                                                                            |
|                                                                                                                                                                                                                 |
| [GridTableDescriptor][ mainTd = [this].gridGroupingControl1.TableDescriptor;]                      |
|                                                                                                                                                                                                                 |
| []                                                                                                                                                                          |
|                                                                                                                                                                                                                 |
| [GridRelationDescriptor][ countriesRd = [new] [GridRelationDescriptor]();] |
|                                                                                                                                                                                                                 |
| [countriesRd.Name = [\"Country\"];]                                                                                                                 |
|                                                                                                                                                                                                                 |
| [countriesRd.MappingName = [\"Country\"];]                                                                                                          |
|                                                                                                                                                                                                                 |
| [countriesRd.RelationKind = [RelationKind].ListItemReference;]                                                                                      |
|                                                                                                                                                                                                                 |
| []                                                                                                                                                                          |
|                                                                                                                                                                                                                 |
| [// SourceListSet name for look up.]                                                                                                                          |
|                                                                                                                                                                                                                 |
| [countriesRd.ChildTableName = [\"Countries\"];  ]                                                                                                   |
|                                                                                                                                                                                                                 |
| []                                                                                                                                                            |
|                                                                                                                                                                                                                 |
| [// Format ChildList.]                                                                                                                                        |
|                                                                                                                                                                                                                 |
| [countriesRd.ChildTableDescriptor.Appearance.AlternateRecordFieldCell.BackColor = [Color].FromArgb(255, 245, 227);]                                 |
|                                                                                                                                                                                                                 |
| []                                                                                                                                                                          |
|                                                                                                                                                                                                                 |
| [// To hide the Key column.]                                                                                                                                  |
|                                                                                                                                                                                                                 |
| [countriesRd.ChildTableDescriptor.VisibleColumns.Add([\"Name\"]);]                                                                                  |
|                                                                                                                                                                                                                 |
| [countriesRd.ChildTableDescriptor.SortedColumns.Add([\"Name\"]);]                                                                                   |
|                                                                                                                                                                                                                 |
| [countriesRd.ChildTableDescriptor.AllowEdit = [true];]                                                                                                 |
|                                                                                                                                                                                                                 |
| []                                                                                                                                                                          |
|                                                                                                                                                                                                                 |
| [// Disallow users to modify states.]                                                                                                                         |
|                                                                                                                                                                                                                 |
| [countriesRd.ChildTableDescriptor.AllowNew = [true];]                                                                                                  |
|                                                                                                                                                                                                                 |
| []                                                                                                                                                                          |
|                                                                                                                                                                                                                 |
| [mainTd.Relations.Add(countriesRd);]                                                                                                                                        |
|                                                                                                                                                                                                                 |
| []                                                                                                                                                                          |
|                                                                                                                                                                                                                 |
| [// Assign data source.]                                                                                                                                      |
|                                                                                                                                                                                                                 |
| [this][.gridGroupingControl1.DataSource = table;]                                                                          |
|                                                                                                                                                                                                                 |
| [mainTd.Name = [\"ListItemReference\"];]                                                                                                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                 |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                               |
|                                                                                                                                                                                                                    |
| [Dim][ mainTd [As] GridTableDescriptor = [Me].gridGroupingControl1.TableDescriptor] |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                                             |
|                                                                                                                                                                                                                    |
| [Dim][ countriesRd [As] [New] GridRelationDescriptor()]                             |
|                                                                                                                                                                                                                    |
| [countriesRd.Name = [\"Country\"]]                                                                                                                     |
|                                                                                                                                                                                                                    |
| [countriesRd.MappingName = [\"Country\"]]                                                                                                              |
|                                                                                                                                                                                                                    |
| [countriesRd.RelationKind = RelationKind.ListItemReference]                                                                                                                    |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                                             |
|                                                                                                                                                                                                                    |
| [\' SourceListSet name for look up.]                                                                                                                             |
|                                                                                                                                                                                                                    |
| [countriesRd.ChildTableName = [\"Countries\"] ]                                                                                                        |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                               |
|                                                                                                                                                                                                                    |
| [\' Format ChildList.]                                                                                                                                           |
|                                                                                                                                                                                                                    |
| [countriesRd.ChildTableDescriptor.Appearance.AlternateRecordFieldCell.BackColor = Color.FromArgb(255, 245, 227)]                                                               |
|                                                                                                                                                                                                                    |
| [        ]                                                                                                                                                                     |
|                                                                                                                                                                                                                    |
| [\' To hide the Key Column.]                                                                                                                                     |
|                                                                                                                                                                                                                    |
| [countriesRd.ChildTableDescriptor.VisibleColumns.Add([\"Name\"])]                                                                                      |
|                                                                                                                                                                                                                    |
| [countriesRd.ChildTableDescriptor.SortedColumns.Add([\"Name\"])]                                                                                       |
|                                                                                                                                                                                                                    |
| [countriesRd.ChildTableDescriptor.AllowEdit = [True]]                                                                                                     |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                                |
|                                                                                                                                                                                                                    |
| [\' Disallow users to modify states.]                                                                                                                            |
|                                                                                                                                                                                                                    |
| [countriesRd.ChildTableDescriptor.AllowNew = [True]]                                                                                                      |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                               |
|                                                                                                                                                                                                                    |
| [mainTd.Relations.Add(countriesRd)]                                                                                                                                            |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                                             |
|                                                                                                                                                                                                                    |
| [\' Assign data source.]                                                                                                                                         |
|                                                                                                                                                                                                                    |
| [Me][.gridGroupingControl1.DataSource = Table]                                                                                |
|                                                                                                                                                                                                                    |
| [mainTd.Name = [\"ListItemReference\"]]                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   Here is a sample output that displays a look up child list for the data column **Country** with value **Brazil**.

**[]** 

{border="0"}

[] 

*[Figure ][314][: ListItemReference Relation]*

[] 


{border="0"}Note: For more details, refer the following browser sample:

 

\<Install Location\>\\Syncfusion\\EssentialStudio\\\[Version Number\]\\Windows\\Grid.Grouping.Windows\\Samples\\2.0\\Relations And Hierarchy\\List Item Reference Demo


 

[]{#p444} 

 

###### []{#_Uniform_Child_List}4.3.4.3.5.5 Uniform Child List Relation {#uniform-child-list-relation style="tab-stops: 0pt"}

[] 

**UniformChildList** relation can be used to map nested strong typed collection inside a parent collection. If a public property is an object, then it will be displayed in a Nested Table. The collection in the below example consists of two kinds of objects, **ParentObj** and **ChildObj**, where every ParentObj is associated with a collection of ChildObjs and it is represented by the public property named **\'Child\'**. Hence a nested table is always created to display the associated children for a given parent.

[] 

Example

[] 

1.   Create a class(ChildObj) whose instances form the child table records.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                     |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                             |
|                                                                                                                                                                                                                    |
| [public][ [class] [ChildObj] : [INotifyPropertyChanged]] |
|                                                                                                                                                                                                                    |
| [{]                                                                                                                                                                            |
|                                                                                                                                                                                                                    |
| [    [private] [string] f1, f2;]                                                                                                     |
|                                                                                                                                                                                                                    |
| [    [private] [int] f3;]                                                                                                            |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                                             |
|                                                                                                                                                                                                                    |
| [    [public] ChildObj([string] f1, [string] f2, [int] f3) {]                              |
|                                                                                                                                                                                                                    |
| [        [this].f1 = f1;]                                                                                                                                 |
|                                                                                                                                                                                                                    |
| [        [this].f2 = f2;]                                                                                                                                 |
|                                                                                                                                                                                                                    |
| [        [this].f3 = f3;]                                                                                                                                 |
|                                                                                                                                                                                                                    |
| [    }]                                                                                                                                                                        |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                                             |
|                                                                                                                                                                                                                    |
| [    [public] [string] Field1]                                                                                                       |
|                                                                                                                                                                                                                    |
| [    {]                                                                                                                                                                        |
|                                                                                                                                                                                                                    |
| [        [get] { [return] f1; }]                                                                                                     |
|                                                                                                                                                                                                                    |
| [        [set]]                                                                                                                                           |
|                                                                                                                                                                                                                    |
| [        {]                                                                                                                                                                    |
|                                                                                                                                                                                                                    |
| [            [if] (f1 != [value])]                                                                                                   |
|                                                                                                                                                                                                                    |
| [            {]                                                                                                                                                                |
|                                                                                                                                                                                                                    |
| [                f1 = [value];]                                                                                                                           |
|                                                                                                                                                                                                                    |
| [                RaisePropertyChanged([\"Field1\"]);]                                                                                                  |
|                                                                                                                                                                                                                    |
| [            }]                                                                                                                                                                |
|                                                                                                                                                                                                                    |
| [        }]                                                                                                                                                                    |
|                                                                                                                                                                                                                    |
| [    }]                                                                                                                                                                        |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                                             |
|                                                                                                                                                                                                                    |
| [    [public] [string] Field2]                                                                                                       |
|                                                                                                                                                                                                                    |
| [    {]                                                                                                                                                                        |
|                                                                                                                                                                                                                    |
| [        [get] { [return] f2; }]                                                                                                     |
|                                                                                                                                                                                                                    |
| [        [set]]                                                                                                                                           |
|                                                                                                                                                                                                                    |
| [        {]                                                                                                                                                                    |
|                                                                                                                                                                                                                    |
| [            [if] (f2 != [value])]                                                                                                   |
|                                                                                                                                                                                                                    |
| [            {]                                                                                                                                                                |
|                                                                                                                                                                                                                    |
| [                f2 = [value];]                                                                                                                           |
|                                                                                                                                                                                                                    |
| [                RaisePropertyChanged([\"Field2\"]);]                                                                                                  |
|                                                                                                                                                                                                                    |
| [            }]                                                                                                                                                                |
|                                                                                                                                                                                                                    |
| [        }]                                                                                                                                                                    |
|                                                                                                                                                                                                                    |
| [    }]                                                                                                                                                                        |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                                             |
|                                                                                                                                                                                                                    |
| [    [public] [int] Field3]                                                                                                          |
|                                                                                                                                                                                                                    |
| [    {]                                                                                                                                                                        |
|                                                                                                                                                                                                                    |
| [        [get] { [return] f3; }]                                                                                                     |
|                                                                                                                                                                                                                    |
| [        [set]]                                                                                                                                           |
|                                                                                                                                                                                                                    |
| [        {]                                                                                                                                                                    |
|                                                                                                                                                                                                                    |
| [            [if] (f3 != [value])]                                                                                                   |
|                                                                                                                                                                                                                    |
| [            {]                                                                                                                                                                |
|                                                                                                                                                                                                                    |
| [                f3 = [value];]                                                                                                                           |
|                                                                                                                                                                                                                    |
| [                RaisePropertyChanged([\"Field3\"]);]                                                                                                  |
|                                                                                                                                                                                                                    |
| [            }]                                                                                                                                                                |
|                                                                                                                                                                                                                    |
| [        }]                                                                                                                                                                    |
|                                                                                                                                                                                                                    |
| [    }]                                                                                                                                                                        |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                                             |
|                                                                                                                                                                                                                    |
| [    [void] RaisePropertyChanged([string] name)]                                                                                     |
|                                                                                                                                                                                                                    |
| [    {]                                                                                                                                                                        |
|                                                                                                                                                                                                                    |
| [        [if] (PropertyChanged != [null])]                                                                                           |
|                                                                                                                                                                                                                    |
| [            PropertyChanged([this], [new] [PropertyChangedEventArgs](name));]                               |
|                                                                                                                                                                                                                    |
| [    }]                                                                                                                                                                        |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                                             |
|                                                                                                                                                                                                                    |
| [    [public] [event] [PropertyChangedEventHandler] PropertyChanged;]                                        |
|                                                                                                                                                                                                                    |
| [}]                                                                                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [Public][ [Class] ChildObj : [Implements] INotifyPropertyChanged]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [    [Private] f1, f2 [As] [String]]                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [    [Private] f3 [As] [Integer]]                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [    [Public] [Sub] [New]([ByVal] f1 [As] [String], [ByVal] f2 [As] [String], [ByVal] f3 [As] [Integer])] |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [        [Me].f1 = f1]                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [        [Me].f2 = f2]                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [        [Me].f3 = f3]                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [    [End] [Sub]]                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [    [Public] [Property] Field1() [As] [String]]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [        [Get]]                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [            [Return] f1]                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [        [End] [Get]]                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [        [Set]([ByVal] value [As] [String])]                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [            [If] f1 \<\> value [Then]]                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [                f1 = value]                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [                RaisePropertyChanged([\"Field1\"])]                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [            [End] [If]]                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [        [End] [Set]]                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [    [End] [Property]]                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [    [Public] [Property] Field2() [As] [String]]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [        [Get]]                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [            [Return] f2]                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [        [End] [Get]]                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [        [Set]([ByVal] value [As] [String])]                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [            [If] f2 \<\> value [Then]]                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [                f2 = value]                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [                RaisePropertyChanged([\"Field2\"])]                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [            [End] [If]]                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [        [End] [Set]]                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [    [End] [Property]]                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [    [Public] [Property] Field3() [As] [Integer]]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [        [Get]]                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [            [Return] f3]                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [        [End] [Get]]                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [        [Set]([ByVal] value [As] [Integer])]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [            [If] f3 \<\> value [Then]]                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [                f3 = value]                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [                RaisePropertyChanged([\"Field3\"])]                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [            [End] [If]]                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [        [End] [Set]]                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [    [End] [Property]]                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [    [Sub] RaisePropertyChanged([ByVal] name [As] [String])]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [        [RaiseEvent] PropertyChanged([Me], [New] PropertyChangedEventArgs(name))]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [    [End] [Sub]]                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [    [Public] [Event] PropertyChanged [As] PropertyChangedEventHandler [Implements] INotifyPropertyChanged.PropertyChanged]                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [End][ [Class]]                                                                                                                                                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Create another class(ParentObj) that contains a reference to the above class (ChildObj). The instances of this class make the parent records. Both the classes implement the INotifyPropertyChanged interface in order to get notified of any property changes.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                     |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                             |
|                                                                                                                                                                                                                                    |
| [public][ [class] [ParentObj] : [INotifyPropertyChanged]]                |
|                                                                                                                                                                                                                                    |
| [{]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                    |
| [    [private] [string] f1, f2;]                                                                                                                     |
|                                                                                                                                                                                                                                    |
| [    [private] [int] f3;]                                                                                                                            |
|                                                                                                                                                                                                                                    |
| [    [private] [BindingList]\<ChildObj\> childObj = [new] [BindingList]\<ChildObj\>();]              |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                    |
| [    [public] ParentObj([string] f1, [string] f2, [int] f3, [params] ChildObj\[\] c)] |
|                                                                                                                                                                                                                                    |
| [    {]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                    |
| [        [this].f1 = f1;]                                                                                                                                                 |
|                                                                                                                                                                                                                                    |
| [        [this].f2 = f2;]                                                                                                                                                 |
|                                                                                                                                                                                                                                    |
| [        [this].f3 = f3;]                                                                                                                                                 |
|                                                                                                                                                                                                                                    |
| [        [foreach](ChildObj i [in] c)]                                                                                                               |
|                                                                                                                                                                                                                                    |
| [            childObj.Add(i);]                                                                                                                                                                 |
|                                                                                                                                                                                                                                    |
| [    }]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                    |
| [    [public] [string] Field1]                                                                                                                       |
|                                                                                                                                                                                                                                    |
| [    {]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                    |
| [        [get] { [return] f1; }]                                                                                                                     |
|                                                                                                                                                                                                                                    |
| [        [set]]                                                                                                                                                           |
|                                                                                                                                                                                                                                    |
| [        {]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                    |
| [            [if] (f1 != [value]) ]                                                                                                                  |
|                                                                                                                                                                                                                                    |
| [            { ]                                                                                                                                                                               |
|                                                                                                                                                                                                                                    |
| [                f1 = [value]; ]                                                                                                                                          |
|                                                                                                                                                                                                                                    |
| [                RaisePropertyChanged([\"Field1\"]); ]                                                                                                                 |
|                                                                                                                                                                                                                                    |
| [            }]                                                                                                                                                                                |
|                                                                                                                                                                                                                                    |
| [        }]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                    |
| [    }]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                    |
| [    [public] [string] Field2]                                                                                                                       |
|                                                                                                                                                                                                                                    |
| [    {]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                    |
| [        [get] { [return] f2; }]                                                                                                                     |
|                                                                                                                                                                                                                                    |
| [        [set]]                                                                                                                                                           |
|                                                                                                                                                                                                                                    |
| [        {]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                    |
| [            [if] (f2 != [value])]                                                                                                                   |
|                                                                                                                                                                                                                                    |
| [            {]                                                                                                                                                                                |
|                                                                                                                                                                                                                                    |
| [                f2 = [value];]                                                                                                                                           |
|                                                                                                                                                                                                                                    |
| [                RaisePropertyChanged([\"Field2\"]);]                                                                                                                  |
|                                                                                                                                                                                                                                    |
| [            }]                                                                                                                                                                                |
|                                                                                                                                                                                                                                    |
| [        }]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                    |
| [    }]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                    |
| [    [public] [int] Field3 {]                                                                                                                        |
|                                                                                                                                                                                                                                    |
| [        [get] { [return] f3; }]                                                                                                                     |
|                                                                                                                                                                                                                                    |
| [        [set]]                                                                                                                                                           |
|                                                                                                                                                                                                                                    |
| [        {]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                    |
| [            [if] (f3 != [value])]                                                                                                                   |
|                                                                                                                                                                                                                                    |
| [            {]                                                                                                                                                                                |
|                                                                                                                                                                                                                                    |
| [                f3 = [value];]                                                                                                                                           |
|                                                                                                                                                                                                                                    |
| [                RaisePropertyChanged([\"Field3\"]);]                                                                                                                  |
|                                                                                                                                                                                                                                    |
| [            }]                                                                                                                                                                                |
|                                                                                                                                                                                                                                    |
| [        }]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                    |
| [    }]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                    |
| [    [public] [BindingList]\<ChildObj\> Child {]                                                                                                  |
|                                                                                                                                                                                                                                    |
| [        [get] { [return] childObj;  }]                                                                                                              |
|                                                                                                                                                                                                                                    |
| [    }]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                    |
| [    [void] RaisePropertyChanged([string] name)]                                                                                                     |
|                                                                                                                                                                                                                                    |
| [    {]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                    |
| [        [if] (PropertyChanged != [null])]                                                                                                           |
|                                                                                                                                                                                                                                    |
| [            PropertyChanged([this], [new] [PropertyChangedEventArgs](name));]                                               |
|                                                                                                                                                                                                                                    |
| [    }]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                    |
| [    [public] [event] [PropertyChangedEventHandler] PropertyChanged;]                                                        |
|                                                                                                                                                                                                                                    |
| [}]                                                                                                                                                                                            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Public][ [Class] ParentObj : [Implements] INotifyPropertyChanged]                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [    [Private] f1, f2 [As] [String]]                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [    [Private] f3 [As] [Integer]]                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [    [Private] childObj [As] BindingList([Of] ChildObj) = [New] BindingList([Of] ChildObj)()]                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [    [Public] [Sub] [New]([ByVal] f1 [As] [String], [ByVal] f2 [As] [String], [ByVal] f3 [As] [Integer], [ByVal] [ParamArray] c [As] ChildObj())] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [        [Me].f1 = f1]                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [        [Me].f2 = f2]                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [        [Me].f3 = f3]                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [        [For] [Each] i [As] ChildObj [In] c]                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [            childObj.Add(i)]                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [        [Next] i]                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [    [End] [Sub]]                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [    [Public] [Property] Field1() [As] [String]]                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [        [Get]]                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [            [Return] f1]                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [        [End] [Get]]                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [        [Set]([ByVal] value [As] [String])]                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [            [If] f1 \<\> value [Then]]                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [                f1 = value]                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [                RaisePropertyChanged([\"Field1\"])]                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [            [End] [If]]                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [        [End] [Set]]                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [    [End] [Property]]                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [    [Public] [Property] Field2() [As] [String]]                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [        [Get]]                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [            [Return] f2]                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [        [End] [Get]]                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [        [Set]([ByVal] value [As] [String])]                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [            [If] f2 \<\> value [Then]]                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [                f2 = value]                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [                RaisePropertyChanged([\"Field2\"])]                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [            [End] [If]]                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [        [End] [Set]]                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [    [End] [Property]]                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [    [Public] [Property] Field3() [As] [Integer]]                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [        [Get]]                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [            [Return] f3]                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [        [End] [Get]]                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [        [Set]([ByVal] value [As] [Integer])]                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [            [If] f3 \<\> value [Then]]                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [                f3 = value]                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [                RaisePropertyChanged([\"Field3\"])]                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [            [End] [If]]                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [        [End] [Set]]                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [    [End] [Property]]                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [    [Public] [ReadOnly] [Property] Child() [As] BindingList([Of] ChildObj)]                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [        [Get]]                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [            [Return] childObj]                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [        [End] [Get]]                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [    [End] [Property]]                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [    [Sub] RaisePropertyChanged([ByVal] name [As] [String])]                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [        [RaiseEvent] PropertyChanged([Me], [New] PropertyChangedEventArgs(name))]                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [    [End] [Sub]]                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [    [Public] [Event] PropertyChanged [As] PropertyChangedEventHandler [Implements] INotifyPropertyChanged.PropertyChanged]                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [End][ [Class]]                                                                                                                                                                                                                                                                                                                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Generate the collection using BindingList class which implements the ListChanged events in itself so that the grid can listen to those events when the list is changed. Add few items into the collection.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                         |
| [BindingList][\<ParentObj\> topList = [new] [BindingList]\<ParentObj\>();]                                                                         |
|                                                                                                                                                                                                                                                                                         |
| [BindingList][\<ChildObj\> childList = [new] [BindingList]\<ChildObj\>();]                                                                         |
|                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                         |
| [Random][ r = [new] [Random]();]                                                                                                                   |
|                                                                                                                                                                                                                                                                                         |
| [for][ ([int] i = 0; i \< 30; i++)]                                                                                                                                           |
|                                                                                                                                                                                                                                                                                         |
| [childList.Add([new] ChildObj([string].Format([\"Name{0}\"], r.Next(10)), [string].Format([\"Desc{0}\"], r.Next(20)), r.Next(30)));] |
|                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                         |
| [for][ ([int] i = 0; i \< 5; i++)]                                                                                                                                            |
|                                                                                                                                                                                                                                                                                         |
| [{]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                         |
| [topList.Add([new] ParentObj([string].Format([\"Name{0}\"], r.Next(5)), [string].Format([\"Desc{0}\"], r.Next(15)), r.Next(20)));]   |
|                                                                                                                                                                                                                                                                                         |
| [for][ ([int] j = i \* 5; j \< (i \* 5) + 5; j++)]                                                                                                                            |
|                                                                                                                                                                                                                                                                                         |
| [topList\[i\].Child.Add(childList\[j\]);]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                         |
| [}]                                                                                                                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                 |
| [Private][ topList [As] BindingList([Of] UniformChildList_2005.ParentObj) = [New] BindingList([Of] UniformChildList_2005.ParentObj)()] |
|                                                                                                                                                                                                                                                                                                                 |
| [Private][ childList [As] BindingList([Of] UniformChildList_2005.ChildObj) = [New] BindingList([Of] UniformChildList_2005.ChildObj)()] |
|                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                 |
| [Private][ r [As] Random = [New] Random()]                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                 |
| [For][ i [As] [Integer] = 0 [To] 29]                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                 |
| [childList.Add([New] UniformChildList_2005.ChildObj([String].Format([\"Name{0}\"], r.Next(10)), [String].Format([\"Desc{0}\"], r.Next(20)), r.Next(30)))]    |
|                                                                                                                                                                                                                                                                                                                 |
| [Next][ i]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                 |
| [For][ i [As] [Integer] = 0 [To] 4]                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                 |
| [topList.Add([New] UniformChildList_2005.ParentObj([String].Format([\"Name{0}\"], r.Next(5)), [String].Format([\"Desc{0}\"], r.Next(15)), r.Next(20)))]      |
|                                                                                                                                                                                                                                                                                                                 |
| [Dim][ j [As] [Integer] = i \* 5]                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                 |
| [Do][ [While] j \< (i \* 5) + 5]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                 |
| [topList(i).Child.Add(childList(j))]                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                 |
| [j += 1]                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                 |
| [Loop]                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                 |
| [Next][ i]                                                                                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Assign the above collection to the datasource of grouping grid.

[] 

+----------------------------------------------------------------------------------+
| **[\[C#\]]**                   |
|                                                                                  |
| []                           |
|                                                                                  |
| [gridGroupingControl1.DataSource = topList;] |
+----------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------+
| **[\[VB.NET\]]**              |
|                                                                                 |
| []                          |
|                                                                                 |
| [GridGroupingControl1.DataSource = topList] |
+---------------------------------------------------------------------------------+

[] 

5.   Establish UniformChildList relation kind.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                               |
|                                                                                                                                                                                                              |
| []                                                                                                                                                         |
|                                                                                                                                                                                                              |
| [GridRelationDescriptor][ relation = [new] [GridRelationDescriptor]();] |
|                                                                                                                                                                                                              |
| [relation.RelationKind = [RelationKind].UniformChildList;]                                                                                       |
|                                                                                                                                                                                                              |
| [relation.MappingName = [\"Child\"];]                                                                                                            |
|                                                                                                                                                                                                              |
| [relation.Name = [\"Child\"];]                                                                                                                   |
|                                                                                                                                                                                                              |
| [relation.ChildTableName = [\"ChildTable\"];]                                                                                                    |
|                                                                                                                                                                                                              |
| [gridGroupingControl1.TableDescriptor.Relations.Add(relation);]                                                                                                          |
|                                                                                                                                                                                                              |
| []                                                                                                                                                                       |
|                                                                                                                                                                                                              |
| [this][.gridGroupingControl1.ShowGroupDropArea = [true];]                                          |
|                                                                                                                                                                                                              |
| [GridTable][ chiltTable = gridGroupingControl1.GetTable([\"ChildTable\"]);]                  |
|                                                                                                                                                                                                              |
| [this][.gridGroupingControl1.AddGroupDropArea(chiltTable);]                                                             |
|                                                                                                                                                                                                              |
| [chiltTable.TableDescriptor.GroupedColumns.Add([\"Field1\"]);]                                                                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                    |
|                                                                                                                                                                                                                       |
| []                                                                                                                                                                  |
|                                                                                                                                                                                                                       |
| [Dim][ relation [As] GridRelationDescriptor = [New] GridRelationDescriptor()]          |
|                                                                                                                                                                                                                       |
| [relation.RelationKind = RelationKind.UniformChildList]                                                                                                                           |
|                                                                                                                                                                                                                       |
| [relation.MappingName = [\"Child\"]]                                                                                                                      |
|                                                                                                                                                                                                                       |
| [relation.Name = [\"Child\"]]                                                                                                                             |
|                                                                                                                                                                                                                       |
| [relation.ChildTableName = [\"ChildTable\"]]                                                                                                              |
|                                                                                                                                                                                                                       |
| [gridGroupingControl1.TableDescriptor.Relations.Add(relation)]                                                                                                                    |
|                                                                                                                                                                                                                       |
| []                                                                                                                                                                                |
|                                                                                                                                                                                                                       |
| [Me][.gridGroupingControl1.ShowGroupDropArea = [True]]                                                      |
|                                                                                                                                                                                                                       |
| [Dim][ chiltTable [As] GridTable = gridGroupingControl1.GetTable([\"ChildTable\"])] |
|                                                                                                                                                                                                                       |
| [Me][.gridGroupingControl1.AddGroupDropArea(chiltTable)]                                                                         |
|                                                                                                                                                                                                                       |
| [chiltTable.TableDescriptor.GroupedColumns.Add([\"Field1\"])]                                                                                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

6.   Here is a sample output.

[] 

{border="0"}

[] 

*[Figure ][315][: UniformChildList Relation]*

[] 


{border="0"}Note: For more details, refer the following browser sample:

 

\<Install Location\>\\Syncfusion\\EssentialStudio\\\[Version Number\]\\Windows\\Grid.Grouping.Windows\\Samples\\2.0\\Relations And Hierarchy\\Uniform Child List Demo


 

[]{#p445} 

 

###### 4.3.4.3.5.6 Working with Relations {#working-with-relations style="tab-stops: 0pt"}

[] 

This section discusses how to handle the related tables in certain scenarios. It also describes the properties and events used for this purpose.

 

**AutoPopulateRelations Property**

 

It specifies if the relations should be automatically generated when you assign DataSource, with a DataTable with constraints or a DataSet with relations defined. It is true by default.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                           |
|                                                                                                                                                                          |
| []                                                                                                                     |
|                                                                                                                                                                          |
| [this][.gridGroupingControl1.AutoPopulateRelations = [false];] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                    |
|                                                                                                                                                                       |
| []                                                                                                                  |
|                                                                                                                                                                       |
| [Me][.gridGroupingControl1.AutoPopulateRelations = [False]] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

ShowRelationFields Property

[] 

[When a foreign key relation (or related collection) is used, this property controls the display of the dependent fields from a related table in the main table.]

[] 

Possible Options

**[]** 


+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| Property                          | Description                                                                                                                  |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| ShowRelationFields                | Displays the dependent fields from a related table in the main table. It includes the following options.                     |
|                                   |                                                                                                                              |
|                                   |                                                                                                                              |
|                                   |                                                                                                                              |
|                                   | [·      ]**Hide**-Hides all the fields.                                                         |
|                                   |                                                                                                                              |
|                                   | [·      ]**ShowAllRelatedFields**-Shows all related fields including Primary and Foreign Keys.  |
|                                   |                                                                                                                              |
|                                   | [·      ]**ShowDisplayFieldsOnly**-Shows only dependent fields; Hides Primary and Foreign Keys. |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------+


[] 

Default value is ShowDisplayFieldsOnly.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                             |
|                                                                                                                                                                                                            |
| []                                                                                                                                                       |
|                                                                                                                                                                                                            |
| [this][.gridGroupingControl1.ShowRelationFields = [ShowRelationFields].ShowAllRelatedFields;] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                             |
|                                                                                                                                                                                |
| []                                                                                                                           |
|                                                                                                                                                                                |
| [Me][.gridGroupingControl1.ShowRelationFields = ShowRelationFields.ShowAllRelatedFields;] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

MaxNestedCollectionRecursionLevel Property

[] 

When nested collection is used, this property specifies the number of levels of recursion allowed when self-relations are detected. Below settings lets the grid to loop through up to four recursion levels.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                 |
|                                                                                                                                                                |
| []                                                                                                           |
|                                                                                                                                                                |
| [this][.gridGroupingControl1.Engine.MaxNestedCollectionRecurseLevel = 4;] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                          |
|                                                                                                                                                             |
| []                                                                                                        |
|                                                                                                                                                             |
| [Me][.gridGroupingControl1.Engine.MaxNestedCollectionRecurseLevel = 4] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

QueryShowRelationDisplayFields Event

[] 

It is raised for every foreign-key relation. It allows you to control at run-time related fields of the child table should be added to the FieldDescriptorCollection. Inside this event, you can check for specific fields and set e.Cancel to true to avoid adding those fields.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                              |
| [this][.gridGroupingControl1.Engine.QueryShowRelationDisplayFields += [new] [QueryShowRelationFieldsEventHandler](Engine_QueryShowRelationDisplayFields);] |
|                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                              |
| [void][ Engine_QueryShowRelationDisplayFields([object] sender, [QueryShowRelationFieldsEventArgs] e)]                                                      |
|                                                                                                                                                                                                                                                                                              |
| [{]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                              |
| [if][ (e.Relation.ChildTableName == [\"Countries\"])]                                                                                                                           |
|                                                                                                                                                                                                                                                                                              |
| [{]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                              |
| [e.ShowRelationFields = [ShowRelationFields].Hide;]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                              |
| [}]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                              |
| [}]                                                                                                                                                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                           |
| [AddHandler][ gridGroupingControl1.Engine.QueryShowRelationDisplayFields, [AddressOf] Engine_QueryShowRelationDisplayFields]                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                           |
| [Private][ [Sub] Engine_QueryShowRelationDisplayFields([ByVal] sender [As] [Object], [ByVal] e [As] QueryShowRelationFieldsEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                           |
| [If][ e.Relation.ChildTableName = [\"Countries\"] [Then]]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                           |
| [e.ShowRelationFields = ShowRelationFields.Hide]                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                           |
| [End][ [If]]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                           |
| [End][ [Sub]]                                                                                                                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

QueryShowField Event

[] 

It gets fired for every field in the Field Descriptor Collection of the individual tables in the dataset. It lets you control over the population of field descriptors. Using this event, you can check for specific fields and cancel the population of desired fields at runtime.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                     |
| [this][.gridGroupingControl1.Engine.QueryShowField += [new] [QueryShowFieldEventHandler](Engine_QueryShowField);] |
|                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                     |
| [void][ Engine_QueryShowField([object] sender, [QueryShowFieldEventArgs] e)]                                      |
|                                                                                                                                                                                                                                                     |
| [{]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                     |
| [    [if] (e.Field.Name == [\"GrandChildID\"])]                                                                                                                    |
|                                                                                                                                                                                                                                                     |
| [    e.Cancel = [true];]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                     |
| [}]                                                                                                                                                                                                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                    |
| [AddHandler][ ][gridGroupingControl1.Engine.QueryShowField, [AddressOf] Engine_QueryShowField]                         |
|                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                    |
| [Private Sub ][Engine_QueryShowField([ByVal ]sender[ As ]Object,[ ByVal ]e[ As] QueryShowFieldEventArgs)] |
|                                                                                                                                                                                                                                                                                    |
| [If ][e.Field.Name =[ ][\"GrandChildID\"][ Then]]                                                                           |
|                                                                                                                                                                                                                                                                                    |
| [e.Cancel =[ True]]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                    |
| [End If]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                    |
| [End Sub]                                                                                                                                                                                                                         |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

**QueryAddRelation Event**

 

It is invoked for every relation that is being added to the RelationDescriptorCollection. By setting e.Cancel to true, you can avoid specific relations being added.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                           |
| [this][.gridGroupingControl1.Engine.QueryAddRelation += [new] [QueryAddRelationEventHandler](Engine_QueryAddRelation);] |
|                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                           |
| [void][ Engine_QueryAddRelation([object] sender, [QueryAddRelationEventArgs] e)]                                        |
|                                                                                                                                                                                                                                                           |
| [{]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                           |
| [    [Console].WriteLine(e.Relation.Name);]                                                                                                                                                   |
|                                                                                                                                                                                                                                                           |
| [}]                                                                                                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                        |
| [AddHandler][ ][gridGroupingControl1.Engine.QueryAddRelation, [AddressOf] Engine_QueryAddRelation]                         |
|                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                        |
| [Private Sub ][Engine_QueryAddRelation([ByVal ]sender[ As ]Object,[ ByVal ]e[ As ]QueryAddRelationEventArgs)] |
|                                                                                                                                                                                                                                                                                        |
| [Console.WriteLine(e.Relation.Name)]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                        |
| [End Sub]                                                                                                                                                                                                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

QueryShowNestedPropertiesFields Event

 

It is called when there exists nested properties in the bound datasource. With the help of this event, you can determine if the individual fields in the nested property should be displayed.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                        |
| [this][.gridGroupingControl1.Engine.QueryShowNestedPropertiesFields += [new] [QueryShowNestedPropertiesFieldsEventHandler](Engine_QueryShowNestedPropertiesFields);] |
|                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                        |
| [void][ Engine_QueryShowNestedPropertiesFields([object] sender, [QueryShowNestedPropertiesFieldsEventArgs] e)]                                                       |
|                                                                                                                                                                                                                                                                                                        |
| [{]                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                        |
| [    [if] (e.PropertyDescriptor.PropertyType == [typeof](BaseClass))]                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                        |
| [    e.Cancel = [true];]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                        |
| [}]                                                                                                                                                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                      |
| [AddHandler][ ][gridGroupingControl1.Engine.QueryShowNestedPropertiesFields, [AddressOf] Engine_QueryShowNestedPropertiesFields]                         |
|                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                      |
| [Private Sub ][Engine_QueryShowNestedPropertiesFields([ByVal ]sender[ As ]Object,[ ByVal ]e[ As ]QueryShowNestedPropertiesFieldsEventArgs)] |
|                                                                                                                                                                                                                                                                                                                      |
| [If ][e.PropertyDescriptor.PropertyType[ Is GetType](BaseClass)[ Then]]                                                                                                               |
|                                                                                                                                                                                                                                                                                                                      |
| [e.Cancel =[ True]]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                      |
| [End If]                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                      |
| [End Sub]                                                                                                                                                                                                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p446} 

 

[]{#related-topics}

