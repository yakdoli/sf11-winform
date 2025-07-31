---
title: connectionoption.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\connectionoption.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}





  






   


## Connection Option {#connection-option style="tab-stops: 0pt"}

[] 

{border="0"}

Figure 9: Connection Option Dialog Widow

[] 

Offline Cube:

[] 

To connect the offline cube, check the offline cube check box and select the offline cube by browsing.

[] 

Server:

 

1.   To connect an Analysis service server, check the server check box and  provide the server name and data base Name to connect the sever.

2.   If the server needs a Credential, then click the Credential menu and give the Credential information (User name and Pass word).

[] 

Connection String:

1.   You can also connect the server or Offline cube by providing the Connection string to connect.

2.   Check the Connection String check box and enter the connection in the following text box. Ex Connection string " DataSource= localhost; Initial Catalog= Adventure Works DW"

[] 

**[]**  

+-----------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                  |
|                                                                                                                                               |
| []                                                                                                        |
|                                                                                                                                               |
| [this] [.olapClient1.ShowConnectOption();] |
|                                                                                                                                               |
| []                                                                                                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------+

**[]**  

+--------------------------------------------------------------------------------------------------------------------------------------------+
| [\[VB\]]                                                                                               |
|                                                                                                                                            |
| []                                                                                                     |
|                                                                                                                                            |
| [Me] [.OlapClient1.ShowConnectOption()] |
|                                                                                                                                            |
| []                                                                                                     |
+--------------------------------------------------------------------------------------------------------------------------------------------+

More:





