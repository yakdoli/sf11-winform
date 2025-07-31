---
title: multipleolapclientsupport.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\multipleolapclientsupport.md
created_at: 2025-07-03
---








  









## Multiple OLAP Client support {#multiple-olap-client-support style="tab-stops: 0pt"}

The multiple OLAP Client feature provides support to place and operate more than one OLAP Client control in a web form.  Here is a sample code snippet to bind two OLAP Client controls in a web form.

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\<][div][\>]                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [    \<][asp][:][ScriptManager][ [ID][=\"ScriptManager1\"] [runat][=\"server\"\>]]                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [    [\</][asp][:][ScriptManager][\>]]                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [    [\<][cc1][:][OlapClient] [ID][=\"OlapClient1\"] [runat][=\"server\"] [Height][=\"600px\"] [Width][=\"800px\"] [/\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [    [\<][cc2][:][OlapClient] [ID][=\"OlapClient2\"] [runat][=\"server\"] [Height][=\"600px\"] [Width][=\"800px\"] [/\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\</][div][\>][]                                                                                                                                                                                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                      |
|                                                                                                                                                                                                                       |
| []                                                                                                                                                                                |
|                                                                                                                                                                                                                       |
| [OlapDataManager][ DataManager = [null];]                                                                |
|                                                                                                                                                                                                                       |
| [protected][ [void] Page_Load([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                       |
| [{]                                                                                                                                                                               |
|                                                                                                                                                                                                                       |
| [    [if] (!IsPostBack)]                                                                                                                                     |
|                                                                                                                                                                                                                       |
| [    {]                                                                                                                                                                           |
|                                                                                                                                                                                                                       |
| [        DataManager = [new] [OlapDataManager](connectionString);]                                                                   |
|                                                                                                                                                                                                                       |
| [        [this].OlapClient1.OlapDataManager = [this].DataManager;]                                                                      |
|                                                                                                                                                                                                                       |
| [        [this].OlapClient1.DataBind();]                                                                                                                     |
|                                                                                                                                                                                                                       |
| []                                                                                                                                                                                |
|                                                                                                                                                                                                                       |
| [        DataManager = [new] [OlapDataManager](connectionString);]                                                                   |
|                                                                                                                                                                                                                       |
| [        [this].OlapClient2.OlapDataManager = [this].DataManager;]                                                                      |
|                                                                                                                                                                                                                       |
| [        [this].OlapClient2.DataBind();]                                                                                                                     |
|                                                                                                                                                                                                                       |
| [    }]                                                                                                                                                                           |
|                                                                                                                                                                                                                       |
| [}][]                                                                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                          |
| [Private][ DataManager [As] OlapDataManager = [Nothing]]                                                                                                                  |
|                                                                                                                                                                                                                                                                                                          |
| [Protected][ [Sub] Page_Load([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                          |
| [      [If] ([Not] IsPostBack) [Then]]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                          |
| [            DataManager = [New] OlapDataManager(connectionString)]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                          |
| [            [Me].OlapClient1.OlapDataManager = [Me].DataManager]                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                          |
| [            [Me].OlapClient1.DataBind()]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                          |
| [            DataManager = [New] OlapDataManager(connectionString)]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                          |
| [            [Me].OlapClient2.OlapDataManager = [Me].DataManager]                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                          |
| [            [Me].OlapClient2.DataBind()]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                          |
| [      [End] [If]]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                          |
| [End][ [Sub]]                                                                                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

