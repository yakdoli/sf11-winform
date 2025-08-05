---
title: hierarchicaldatabinding.md
original_path: WinForms_Docs/03_Data_Binding/hierarchicaldatabinding.md
created_at: 2025-08-05
---








  









### Hierarchical Data Binding {#hierarchical-data-binding style="tab-stops: 0pt"}

[] 

The Hierarchical data binding in GridGroupingControl is a very useful concept that is mainly used for building Nested Relationships. This type of binding will have two or more Tables connected by using the Relationship of the parent and child.

 

The Grid relations are given in code, by using the GridRelationDescriptor.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\<][sfwg][:][GridGroupingControl][ [DataSourceCachingMode][=\"ViewState\"] [ID][=\"GridGroupingControl1\"] [runat][=\"server\"] [EnableCallbacks][=\"False\"\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\</][sfwg][:][GridGroupingControl][\>]                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\<][asp][:][AccessDataSource][ [ID][=\"AccessDataSource1\"] [runat][=\"server\"] [DataFile][=\"\~/App_Data/NWIND.MDB\"]]                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [SelectCommand][=\"SELECT \[EmployeeID\], \[LastName\], \[FirstName\], \[Title\], \[City\], \[Region\] FROM \[Employees\]\"\>]                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\</][asp][:][AccessDataSource][\>]                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\<][asp][:][AccessDataSource][ [ID][=\"AccessDataSource2\"] [runat][=\"server\"] [DataFile][=\"\~/App_Data/NWIND.MDB\"]]                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [SelectCommand][=\"SELECT \[OrderID\], \[CustomerID\], \[EmployeeID\], \[OrderDate\], \[RequiredDate\], \[ShipVia\], \[Freight\], \[ShipName\], \[ShipCity\], \[ShipRegion\] FROM \[Orders\]\"\>]                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\</][asp][:][AccessDataSource][\>]                                                                                                                                                                                                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                  |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                                                 |
| [protected][ [void] Page_Load([object] sender, [EventArgs] e)]           |
|                                                                                                                                                                                                                                 |
| [{]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                 |
| [if][ (!IsPostBack)]                                                                                                                       |
|                                                                                                                                                                                                                                 |
| [{]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                 |
| [GridRelationDescriptor][ gridRelationDescriptor = [new] [GridRelationDescriptor]();]      |
|                                                                                                                                                                                                                                 |
| [gridRelationDescriptor.ChildTableName = [\"Orders\"];]                                                                                                             |
|                                                                                                                                                                                                                                 |
| [gridRelationDescriptor.RelationKind = [RelationKind].RelatedMasterDetails;]                                                                                        |
|                                                                                                                                                                                                                                 |
| [gridRelationDescriptor.RelationKeys.Add([\"EmployeeID\"], [\"EmployeeID\"]);]                                                              |
|                                                                                                                                                                                                                                 |
| [GridGroupingControl1.TableDescriptor.Relations.Add(gridRelationDescriptor);]                                                                                                               |
|                                                                                                                                                                                                                                 |
| [this][.GridGroupingControl1.SourceListSet.Add([\"Employees\"], [\"AccessDataSource1\"]);] |
|                                                                                                                                                                                                                                 |
| [this][.GridGroupingControl1.SourceListSet.Add([\"Orders\"], [\"AccessDataSource2\"]);]    |
|                                                                                                                                                                                                                                 |
| [this][.GridGroupingControl1.TableDescriptor.Name = [\"Employees\"];]                                              |
|                                                                                                                                                                                                                                 |
| [this][.GridGroupingControl1.DataSourceID = [\"AccessDataSource1\"];]                                              |
|                                                                                                                                                                                                                                 |
| [}]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                 |
| [}]                                                                                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                          |
| [Protected][ [Sub] Page_Load([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                          |
| [If][ [Not] IsPostBack [Then]]                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                          |
| [Dim][ gridRelationDescriptor [As] [New] Syncfusion.Web.UI.WebControls.Grid.Grouping.GridRelationDescriptor()]                                                            |
|                                                                                                                                                                                                                                                                                                          |
| [gridRelationDescriptor.ChildTableName = [\"Orders\"]]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                          |
| [gridRelationDescriptor.RelationKind = RelationKind.RelatedMasterDetails]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                          |
| [gridRelationDescriptor.RelationKeys.Add([\"EmployeeID\"], [\"EmployeeID\"])]                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                          |
| [GridGroupingControl1.TableDescriptor.Relations.Add(gridRelationDescriptor)]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                          |
| [Me][.GridGroupingControl1.SourceListSet.Add([\"Employees\"], [\"AccessDataSource1\"])]                                                                               |
|                                                                                                                                                                                                                                                                                                          |
| [Me][.GridGroupingControl1.SourceListSet.Add([\"Orders\"], [\"AccessDataSource2\"])]                                                                                  |
|                                                                                                                                                                                                                                                                                                          |
| [Me][.GridGroupingControl1.TableDescriptor.Name = [\"Employees\"]]                                                                                                                           |
|                                                                                                                                                                                                                                                                                                          |
| [Me][.GridGroupingControl1.DataSourceID = [\"AccessDataSource1\"]]                                                                                                                           |
|                                                                                                                                                                                                                                                                                                          |
| [End][ [If]]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                          |
| [End][ [Sub]]                                                                                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p27} 

[]{#related-topics}

