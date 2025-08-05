---
title: olapdataprovider.md
original_path: WinForms_Docs/03_Data_Binding/olapdataprovider.md
created_at: 2025-08-05
---








  









## OlapDataProvider {#olapdataprovider style="tab-stops: 0pt"}

The database connectivity related works are all taken care of by this part of the base. Here we are using **Microsoft.AnalysisService.AdomdClient** data provider. Establishing the connection, checking the state of the connection and closing the connection are basic operations provided by the general data provider, but we need some information beyond this in order to provide the input for our controls. 

This part of the base will get the connection information and establish a connection with the specified data source and retrieve the information from the data base and store it in its classes. This part of the base will have the required logic to retrieve the information from the data base and store it in the **object of class** in **Data** namespace.

 All the information about the connected cube will intersect and be stored in **object of classes** in **Data** namespace, which are equivalent to the classes in the **AdomdClient**. This information is required to provide the input for OLAP controls.

Important class in DataProvider namespace:

[·      ]AdomdDataProvider

More:





