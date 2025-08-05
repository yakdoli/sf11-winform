---
title: dynamicconnection.md
original_path: WinForms_Docs/99_Uncategorized/dynamicconnection.md
created_at: 2025-08-05
---








  









## Dynamic Connection {#dynamic-connection style="tab-stops: 0pt"}

Dynamic Connection enables an OlapClient to connect different servers at run time. Therefore, report manipulation for different servers can be done consequently rather than closing and re-initializing the process.

The Dynamic Connection Option facilitates the following:

[·      ]Connecting different SSAS (SQL Server Analysis Service) or XMLA (XML for Analysis Service) (for example, Mondrian server) through well-formed connection strings.

[·      ]Passes the encrypted string for tightly coupled connection strings by providing an option to encrypt the string using a private key.

[·      ]It is not necessary to close the existing client connection to connect a new server.

 

Use Case Scenarios

The user can manipulate an OlapReport for different servers dynamically by a client control at run time.

 

Tables for Properties, Methods, and Events

Properties

Table 9: Property Table


  Property                                             Description                                                                       Type                                    Data Type                            Reference links
  ---------------------------------------------------- --------------------------------------------------------------------------------- --------------------------------------- ------------------------------------ -------------------------------
  ConnectionString                                     Gets or sets the connection string for an OlapClient[]   Dependency[]   String[]    \-[]
  EnabledConnectionOption[]   To show or hide the connection option button[]           Dependency[]   Boolean[]   \-[]


[] 

Methods

Table 10: Method Table


+----------------------------------------+-------------------------------------------------------------------------------------------------------------+------------------------------------------------------+----------------------------------+---------------------------------+-------------------------------+
| Method                                 | Description                                                                                                 | Parameters                                           | Type                             | Return Type                     | Reference links               |
+----------------------------------------+-------------------------------------------------------------------------------------------------------------+------------------------------------------------------+----------------------------------+---------------------------------+-------------------------------+
| UpdateConnection                       | Updates the Client's connection with the specified connection string[]             | (string connectionString)[] | **-**[] | Void[] | \-[] |
|                                        |                                                                                                             |                                                      |                                  |                                 |                               |
|                                        |                                                                                                             |                                                      |                                  |                                 |                               |
+----------------------------------------+-------------------------------------------------------------------------------------------------------------+------------------------------------------------------+----------------------------------+---------------------------------+-------------------------------+
| ResetClient[] | Resets the client( i.e., clears the Client's current server related information)[] | \-[]                        | **-[]** | Void[] | \-[] |
+========================================+=============================================================================================================+======================================================+==================================+=================================+===============================+


[] 

Sample Link

 

Windows 7/Vista:

 

SystemDrive:\\Users\\\<user_name\>\\AppData\\Local\\Syncfusion\\EssentialStudio\\\<version_number\>\\BI\\Silverlight\\OlapClient.SL\\DynamicConnection

[[]]{.UGHyperlink} 

Windows XP:

 

SystemDrive:\\Syncfusion\\EssentialStudio\\\<version_number\>\\BI\\Silverlight\\OlapClient.SL\\DynamicConnection

More:







