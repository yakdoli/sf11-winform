---
title: adonetentitymodeldatasource.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\03_Data_Binding\adonetentitymodeldatasource.md
created_at: 2025-07-03
---








  









### ADO.NET Entity Model Data Source {#ado.net-entity-model-data-source style="tab-stops: 0pt"}

 

The Entity Framework supports an Entity Data Model (EDM) for defining data at both the storage and conceptual level and also mapping between the two. It also enables you to program directly against the data types defined at the conceptual level as common language runtime (CLR) objects. The Entity Framework provides tools to generate an EDM and the related CLR objects based on an existing database. This reduces much of the data access code that is required to create object-based data application and services. This makes it faster to create object-oriented data applications and services from an existing database.

 

The Entity Framework enables you to avoid the tedious work of building your data access classes by hand. Entity Framework applications can run on any computer on which the .NET Framework 3.5 Service Pack 1 (SP1) is installed.

 

For details, see: [[http://msdn.microsoft.com/en-in/library/bb399567(v=VS.90).aspx]{.UGHyperlink}](http://msdn.microsoft.com/en-in/library/bb399567(v=VS.90).aspx)

[[http://msdn.microsoft.com/en-in/library/bb896338%28v=VS.90%29.aspx]{.UGHyperlink}](http://msdn.microsoft.com/en-in/library/bb896338%28v=VS.90%29.aspx)[]{.UGHyperlink}

 

Most applications are currently written on top of relational databases. At some point, these applications will have to interact with the data represented in a relational form.Database schemas are not always ideal for building applications and the conceptual models of applications differ from the logical models of databases. The Entity Data Model (EDM) is a conceptual data model that can be used to model the data of a particular domain so that applications can interact with data as entities or objects.

 

Properties

 


  ------------ ---------------------------------------------------- ------------------ ----------------------- --------------------------------------------------
  Property     Description                                          Type of property   Value it accepts        Any other dependencies/sub-properties associated
  DataSource   Gets or sets the data source for the Grid control.   IEnumerable        Any IEnumerable data.   None
  ------------ ---------------------------------------------------- ------------------ ----------------------- --------------------------------------------------


[] 

Methods

 


  ------------------------------- ------------------------------------------------ ------------------------- -------------------
  Method                          Description                                      Parameters                Return type
  Datasource (IEnumerable\<T\>)   Used to set a data source to the Grid control.   IEnumerable data source   IGridBuilder\<T\>
  ------------------------------- ------------------------------------------------ ------------------------- -------------------


More:







