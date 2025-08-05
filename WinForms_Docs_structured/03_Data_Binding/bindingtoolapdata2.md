---
title: bindingtoolapdata2.md
original_path: WinForms_Docs/03_Data_Binding/bindingtoolapdata2.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}





  






    


### Binding to OLAP Data {#binding-to-olap-data style="tab-stops: 0pt"}

**OlapData** can be bound to **OlapGrid** with the help of **OlapDataManager**. **OlapDataManager** requires **OlapReport** which contains Dimension and Measure elements.

[Refer here for OLAP Data binding]{.UGHyperlink} [\
\
]{.UGHyperlink}XAML Configuration

XAML configuration is one of the important features of OlapGrid. It helps you to configure the control entirely using XAML by eliminating the required code in code behind.

\
Use Case Scenarios

This feature will help you to set the Data source, Report and UI properties in a simple and elegant manner, when you want to perform the entire configuration in XAML.

Tables for Properties, Methods, and Events

 

  ----------------------------- ---------------------------------------------------------------------------------------- --------------------- ------------------- ----------------
  Property                      Description                                                                              Type                  Data  Type          Reference Link
  DataSource.ConnectionString   Specifies the connection string of the DataManager                                       Attached Property     String              \-
  DataSource.ConnectionName     Specifies the connection name which is available in App.Config file of the application   Attached Property     String              \-
  DataSource.DataManagerName    Specifies the DataManager name                                                           Attached Property     String              \-
  SharedDataManagerName         Specifies the DataManager name which is available in shared data manager collection      Attached Property     String              \-
  ReportName                    Species the OLAP report name                                                             CLR                   String              \-
  CurrentCubeName               Specifies the current cube name of a OLAP report                                         CLR                   String              \-
  CategoricalAxis               Specifies the Categorical axis of the OLAP report                                        Dependency Property   CategoricalAxis     \-
  SeriesAxis                    Specifies the Series axis of the OLAP report                                             Dependency Property   SeriesAxis          \-
  SlicerAxis                    Specifies the Slicer axis of the OLAP report                                             Dependency Property   SlicerAxis          \-
  CalculatedMembers             Specifies the Calculated Members of the OLAP report                                      Dependency Property   CalculatedMembers   \-
  ----------------------------- ---------------------------------------------------------------------------------------- --------------------- ------------------- ----------------

 

[]{#related-topics}

