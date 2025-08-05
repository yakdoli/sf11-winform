---
title: multiplekindrelation.md
original_path: WinForms_Docs/99_Uncategorized/multiplekindrelation.md
created_at: 2025-08-05
---








  









### Multiple Kind Relation {#multiple-kind-relation style="tab-stops: 0pt"}

[] 

Illustrates how to specify hierarchy relations with multiple relation kinds.

For our example scenario, let us consider a Car Maker and the Models made.

[] 

[·      ]Populate the data in the two lists, Maker and Model.

[·      ]Generate the Association between the two lists and store it in another list.

[·      ]Establish the Relation between the Maker and Association - RelationKind is RelatedMasterDetails.

[·      ]Specify Relations in the grouping engine.

[·      ]Adding Relation to Parent table.

[·      ]Land and Maker List\<T\> Item Collections share a ForeignKeyReference Relationship.

[·      ]RelatedMasterDetail relation kind is specified between the Maker and MakerModel Item Collections.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                              |
| [//Populate the List DTOs]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                              |
| [List][\<MakerDTO_CS\> \_MakerData = GenerateMakerData();]                                                                                                                              |
|                                                                                                                                                                                                                                                                              |
| [List][\<LandDTO_CS\> \_LandData = GenerateLandData();]                                                                                                                                 |
|                                                                                                                                                                                                                                                                              |
| [List][\<ModelDTO_CS\> \_ModelData = GenerateModelData();]                                                                                                                              |
|                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                              |
| [// Maker and Model DTOs are combined to form another DTO]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                              |
| [List][\<MakerModelDTO_CS\> \_Associations = GenerateAssociation(\_ModelData, \_MakerData);]                                                                                            |
|                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                              |
| [//Establish Relation between \_Maker and \_Associations - RelationKind is RelatedMasterDetails        ]                                                                                                                   |
|                                                                                                                                                                                                                                                                              |
| [this][.GridGroupingControl1.Engine.SourceListSet.Add([new] [SourceListSetEntry]([\"Makers\"], \_MakerData));]         |
|                                                                                                                                                                                                                                                                              |
| [this][.GridGroupingControl1.Engine.SourceListSet.Add([new] [SourceListSetEntry]([\"MakerModels\"], \_Associations));] |
|                                                                                                                                                                                                                                                                              |
| [this][.GridGroupingControl1.TableDescriptor.Name = [\"Makers\"];]                                                                                               |
|                                                                                                                                                                                                                                                                              |
| [this][.GridGroupingControl1.DataMember = [\"DefaultView\"];]                                                                                                    |
|                                                                                                                                                                                                                                                                              |
| [this][.GridGroupingControl1.DataSource = \_MakerData;]                                                                                                                                 |
|                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                              |
| [//Specifying relations in grouping engine. ]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                              |
| [GridRelationDescriptor][ gridRelationDescriptor = [new] [GridRelationDescriptor]();]                                                         |
|                                                                                                                                                                                                                                                                              |
| [gridRelationDescriptor.ChildTableName = [\"MakerModels\"];]                                                                                                                                                      |
|                                                                                                                                                                                                                                                                              |
| [gridRelationDescriptor.RelationKind = [RelationKind].RelatedMasterDetails;]                                                                                                                                        |
|                                                                                                                                                                                                                                                                              |
| [gridRelationDescriptor.RelationKeys.Add([\"ID\"], [\"ParentID\"]);]                                                                                                                       |
|                                                                                                                                                                                                                                                                              |
| [gridRelationDescriptor.ChildTableDescriptor.AllowNew = [false];]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                              |
| [gridRelationDescriptor.ChildTableDescriptor.AllowEdit = [false];]                                                                                                                                                  |
|                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                              |
| [//Adding relation to parent table]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                              |
| [GridGroupingControl1.TableDescriptor.Relations.Add(gridRelationDescriptor);]                                                                                                                                                            |
|                                                                                                                                                                                                                                                                              |
| [gridRelationDescriptor.ChildTableDescriptor.VisibleColumns.Remove([\"ID\"]);]                                                                                                                                    |
|                                                                                                                                                                                                                                                                              |
| [GridColumnDescriptor][ x = gridRelationDescriptor.ChildTableDescriptor.Columns\[0\];]                                                                                                  |
|                                                                                                                                                                                                                                                                              |
| [gridRelationDescriptor.ChildTableDescriptor.Columns.RemoveAt(0);]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                              |
| [gridRelationDescriptor.ChildTableDescriptor.Columns.Add(x);]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                              |
| [this][.GridGroupingControl1.Engine.SourceListSet.Add([new] [SourceListSetEntry]([\"Lands\"], \_LandData));]           |
|                                                                                                                                                                                                                                                                              |
| [GridRelationDescriptor][ ggd = [new] [GridRelationDescriptor]();]                                                                            |
|                                                                                                                                                                                                                                                                              |
| [ggd.ChildTableName = [\"Lands\"];]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                              |
| [ggd.RelationKind = [RelationKind].ForeignKeyReference;]                                                                                                                                                            |
|                                                                                                                                                                                                                                                                              |
| [ggd.RelationKeys.Add([\"Land\"], [\"ID\"]);]                                                                                                                                              |
|                                                                                                                                                                                                                                                                              |
| [ggd.ChildTableDescriptor.AllowNew = [false];]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                              |
| [GridGroupingControl1.TableDescriptor.Relations.Add(ggd);]                                                                                                                                                                               |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                        |
| [\'Populate the List DTOs]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                        |
| [Dim][ \_MakerData [As] List([Of] MakerDTO_CS) = GenerateMakerData()]                                                                   |
|                                                                                                                                                                                                                                                                        |
| [Dim][ \_LandData [As] List([Of] LandDTO_CS) = GenerateLandData()]                                                                      |
|                                                                                                                                                                                                                                                                        |
| [Dim][ \_ModelData [As] List([Of] ModelDTO_CS) = GenerateModelData()]                                                                   |
|                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                        |
| [\' Maker and Model DTOs are combined to form another DTO]                                                                                                                                                           |
|                                                                                                                                                                                                                                                                        |
| [Dim][ \_Associations [As] List([Of] MakerModelDTO_CS) = GenerateAssociation(\_ModelData, \_MakerData)]                                 |
|                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                        |
| [\'Establish Relation between \_Maker and \_Associations - RelationKind is RelatedMasterDetails        ]                                                                                                             |
|                                                                                                                                                                                                                                                                        |
| [Me][.GridGroupingControl1.Engine.SourceListSet.Add([New] SourceListSetEntry([\"Makers\"], \_MakerData))]                             |
|                                                                                                                                                                                                                                                                        |
| [Me][.GridGroupingControl1.Engine.SourceListSet.Add([New] SourceListSetEntry([\"MakerModels\"], \_Associations))]                     |
|                                                                                                                                                                                                                                                                        |
| [Me][.GridGroupingControl1.TableDescriptor.Name = [\"Makers\"]]                                                                                            |
|                                                                                                                                                                                                                                                                        |
| [Me][.GridGroupingControl1.DataMember = [\"DefaultView\"]]                                                                                                 |
|                                                                                                                                                                                                                                                                        |
| [Me][.GridGroupingControl1.DataSource = \_MakerData]                                                                                                                              |
|                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                        |
| [\'Specifying relations in grouping engine. ]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                        |
| [Dim][ gridRelationDescriptor [As] Syncfusion.Web.UI.WebControls.Grid.Grouping.GridRelationDescriptor = [New] GridRelationDescriptor()] |
|                                                                                                                                                                                                                                                                        |
| [gridRelationDescriptor.ChildTableName = [\"MakerModels\"]]                                                                                                                                                 |
|                                                                                                                                                                                                                                                                        |
| [gridRelationDescriptor.RelationKind = RelationKind.RelatedMasterDetails]                                                                                                                                                          |
|                                                                                                                                                                                                                                                                        |
| [gridRelationDescriptor.RelationKeys.Add([\"ID\"], [\"ParentID\"])]                                                                                                                  |
|                                                                                                                                                                                                                                                                        |
| [gridRelationDescriptor.ChildTableDescriptor.AllowNew = [False]]                                                                                                                                              |
|                                                                                                                                                                                                                                                                        |
| [gridRelationDescriptor.ChildTableDescriptor.AllowEdit = [False]]                                                                                                                                             |
|                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                        |
| [\'Adding relation to parent table]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                        |
| [GridGroupingControl1.TableDescriptor.Relations.Add(gridRelationDescriptor)]                                                                                                                                                       |
|                                                                                                                                                                                                                                                                        |
| [gridRelationDescriptor.ChildTableDescriptor.VisibleColumns.Remove([\"ID\"])]                                                                                                                               |
|                                                                                                                                                                                                                                                                        |
| [Dim][ x [As] Syncfusion.Web.UI.WebControls.Grid.Grouping.GridColumnDescriptor = gridRelationDescriptor.ChildTableDescriptor.Columns(0)]                     |
|                                                                                                                                                                                                                                                                        |
| [gridRelationDescriptor.ChildTableDescriptor.Columns.RemoveAt(0)]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                        |
| [gridRelationDescriptor.ChildTableDescriptor.Columns.Add(x)]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                        |
| [Me][.GridGroupingControl1.Engine.SourceListSet.Add([New] SourceListSetEntry([\"Lands\"], \_LandData))]                               |
|                                                                                                                                                                                                                                                                        |
| [Dim][ ggd [As] Syncfusion.Web.UI.WebControls.Grid.Grouping.GridRelationDescriptor = [New] GridRelationDescriptor()]                    |
|                                                                                                                                                                                                                                                                        |
| [ggd.ChildTableName = [\"Lands\"]]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                        |
| [ggd.RelationKind = RelationKind.ForeignKeyReference]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                        |
| [ggd.RelationKeys.Add([\"Land\"], [\"ID\"])]                                                                                                                                         |
|                                                                                                                                                                                                                                                                        |
| [ggd.ChildTableDescriptor.AllowNew = [False]]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                        |
| [GridGroupingControl1.TableDescriptor.Relations.Add(ggd)]                                                                                                                                                                          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 70

[]{#p59} 

[]{#related-topics}

