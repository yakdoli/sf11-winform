---
title: databindingusingadonet.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\03_Data_Binding\databindingusingadonet.md
created_at: 2025-07-03
---






##### Data Binding using ADO.NET {#data-binding-using-ado.net style="tab-stops: 0pt"}

[] 

**ADO.NET** is an object-oriented set of libraries that allows you to interact with different types of data sources and different types of databases. It comes in different sets of libraries. These libraries are called **DataProviders** and they allow a common way to interact with specific data sources or protocols. The following table lists the data providers that are widely used.

[] 


  ---------------------- --------------------------------------------------------------------
  Provider Name          Description
  Ole Db Data Provider   Data Sources that expose an OleDb interface, i.e. Access or Excel.
  SQL Data Provider      For interacting with Microsoft SQL Server.
  ---------------------- --------------------------------------------------------------------


[] 

ADO.NET Objects

 

[The ADO.NET objects are used by the ADO data model to support database interaction. These objects must be created to supply a data-aware control like the grid with database data. The data-aware controls possess the two data binding properties, the DataSource and the DataMember. Any data source can be bound to the control by assigning it to the DataSource and the DataMember properties.]

[] 

**[The Connection Object]**

[] 

[It is used for connection to database and managing transactions against the database. The database location and access method will be specified through this connection object. The connection object should be a type of OleDBConnection in case of OLE DB data sources or should be a SqlConnection object for data sources provided by MS SQL Server.]

[] 

**[The DataAdapter Object]**

[] 

[The data adapter acts like a bridge between the dataset and the data source. It is used to retrieve the data from the database and populate the tables within a dataset. It uses the connection object to connect to the database in order to fill the dataset and update the changes back to the database. There are two adapter components supplied: the OleDBDataAdapter and the SqlDataAdapter. The former accesses data sources exposed using OLE DB and the later is designed to work with data sources provided by MS SQL Server version 7.0 or later.]

[] 

**[The DataSet]**

[] 

[The dataset acts like a memory resident cache to hold the data. It represents a complete set of data including the tables that organize the data and relationships between the tables. The dataset is designed to help manage data in memory and to support disconnected operations on data. It can be populated by calling the Fill method of the DataAdapter.]

[] 

**[The Command Object]**

[] 

[Commands contains the information that is submitted to a database, and are represented by provider-specific classes such as SQLCommand. A command can be a stored procedure call, an UPDATE statement, or a statement that returns results.]

[] 

**[The DataReader Object]**

[] 

[This is a suitable object when you want, to only get the stream of data for reading. The data returned from a data reader is a fast forward-only stream of data. This means that you can only pull the data from the stream in a sequential manner. This is good for speed, but if you need to manipulate data, then a DataSet is a better object to work with.]

[] 

Data Binding Methods

 

[To bind the grid to a database, you can use any one of the following methods.]

[] 

1.   Binding At Design Time

[] 

[[• ]]{.UGHyperlink}[Binding to a database at Design time using VS2003]{.UGHyperlink}[]{.UGHyperlink}

[[• ]]{.UGHyperlink}[Binding to a database at Design time using VS2005]{.UGHyperlink}[]{.UGHyperlink}

[] 

2.   Binding At Run Time

[] 

[[• ]]{.UGHyperlink}[Binding to an MDB file at run time]{.UGHyperlink}[]{.UGHyperlink}

[[• ]]{.UGHyperlink}[Binding to a manually created datasource]{.UGHyperlink}[]{.UGHyperlink}

 

[]{#p405} 

 

[]{#related-topics}

