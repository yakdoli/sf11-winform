---
title: linq.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\linq.md
created_at: 2025-07-03
---








  









### LINQ {#linq style="tab-stops: 0pt"}

[] 

Essential Grid now provides support for Language Integrated Queries in its database operations. Linq is an essential feature of .NET 3.5 framework whose benefits are significant. Most importantly, it is a standardized way to query not just tables in a relational database but also text files, XML files, and other data sources using identical syntax. You can use this standardized method from any .NET compliant language such as C#, VB.NET and others.

The areas where LINQ comes into play are Grouping, Filtering, Caching session data, Paging and Record Search. It has proven results in improving the performance of grid. You can handle large datasets very easily and quickly.

[] 

Anonymous Type Caching

[] 

In LINQ Serializing the anonymous type data is not possible. So these kinds of data can be cached with \"Session\" caching mode.

[] 

Dynamic Filtering

[] 

One of the nice things with LINQ is that we\'ve setup LINQ data classes to perform richer and more natural queries against the database. The filtering process just queries against a database and filters the results by a particular value by using the Where clause.

The Where clause enables us to filter query data by selecting only elements that meet certain criteria. Elements whose values cause the Where clause to evaluate to True are included in the query result; other elements are excluded. The expression that is used in a Where clause must evaluate to a Boolean or the equivalent of a Boolean, such as an Integer that evaluates to False when its value is zero. You can combine multiple expressions in a Where clause by using logical operators such as And, Or, AndAlso, OrElse, Is, and IsNot.

[] 

{border="0"}

Figure 41

[] 

The following code example illustrates binding GridGroupingControl by using LINQ.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                               |
|                                                                                                                                                                                                                              |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                              |
| [NorthwindDataContext dc = [new] NorthwindDataContext();]                                                                                                           |
|                                                                                                                                                                                                                              |
| [var][ emp = [from] p [in] dc.Employees]                                                      |
|                                                                                                                                                                                                                              |
| [          [select] [new]]                                                                                                                     |
|                                                                                                                                                                                                                              |
| [          {]                                                                                                                                                                            |
|                                                                                                                                                                                                                              |
| [              p.EmployeeID,]                                                                                                                                                            |
|                                                                                                                                                                                                                              |
| [              p.FirstName,]                                                                                                                                                             |
|                                                                                                                                                                                                                              |
| [              p.LastName,]                                                                                                                                                              |
|                                                                                                                                                                                                                              |
| [              p.City,]                                                                                                                                                                  |
|                                                                                                                                                                                                                              |
| [              p.Country,]                                                                                                                                                               |
|                                                                                                                                                                                                                              |
| [              p.Address]                                                                                                                                                                |
|                                                                                                                                                                                                                              |
| [          };]                                                                                                                                                                           |
|                                                                                                                                                                                                                              |
| [this][.GridGroupingControl1.DataSource = emp;]                                                                                         |
|                                                                                                                                                                                                                              |
| []                                                                                                                                                                                       |
|                                                                                                                                                                                                                              |
| [this][.GridGroupingControl1.DataSourceCachingMode = Syncfusion.Web.UI.WebControls.Grid.Grouping.Common.DataSourceCachingMode.Session;] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                            |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                                           |
| [Dim][ dc [As] NorthwindDataContext = [New] NorthwindDataContext()]                        |
|                                                                                                                                                                                                                           |
| [Dim][ emp = From p [In] dc.Employees\_]                                                                        |
|                                                                                                                                                                                                                           |
| [  [Select] [New]]                                                                                                                          |
|                                                                                                                                                                                                                           |
| [  p.EmployeeID, p.FirstName, p.LastName, p.City, p.Country, p.Address]                                                                                                               |
|                                                                                                                                                                                                                           |
| [Me][.GridGroupingControl1.DataSource = emp]                                                                                         |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                           |
| [Me][.GridGroupingControl1.DataSourceCachingMode = Syncfusion.Web.UI.WebControls.Grid.Grouping.Common.DataSourceCachingMode.Session] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 42

[] 

[]{#related-topics}

