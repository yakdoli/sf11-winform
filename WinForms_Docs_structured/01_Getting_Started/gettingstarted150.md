---
title: gettingstarted150.md
original_path: WinForms_Docs/01_Getting_Started/gettingstarted150.md
created_at: 2025-08-05
---








  






[ \> ]{.d2h_breadcrumbsLinkSeparator}[Essential BI Chart]{.d2h_breadcrumbsContentsOnly}


# Getting Started {#getting-started style="tab-stops: 0pt"}

The steps to get started are as follows:

1.   Click the **Start** menu, and then click **Microsoft Visual Studio 2010**.

2.   From the File menu, select **New Project**. The New Project dialog box is displayed as shown below.

[] 

{border="0"}

 

Figure 8: New Project Dialog Box

[] 

3.   Select the **Silverlight Application** by navigating to the Silverlight node and then click **OK**.

4.   Host the Silverlight application on the Website.

{border="0"}

 

Figure 9:  Hosting Silverlight Application in Web

[] 

5.   Click **OK**, to create a web project as well as a Silverlight project, as shown below.

[] 

{border="0"}

 

Figure 10: Web and Silverlight Project

[] 

6.   Drag and drop the **OlapChart** from the toolbox to the MainPage.xaml.

[] 

 

 

 

{border="0"}

 

Figure 11: OlapChart in Designer Page

 

7.   Add the following two assemblies as references to the web project:

[·      ]Syncfusion.Olap.Base

[·      ]Syncfusion.OlapSilverlight.BaseWrapper

[o  ][]

{border="0"}

 

Figure 12: References you need to add to the web project[]

[] 

8.   Add a WCF Service to the Web project by right-clicking the **Project -\> Add New Item -\> WCF Service**.

 

[{border="0"}]

 

Figure 13: Add New Item (WCF Service)

[] 

[] 

9.   Inherit the newly added WCF service with the IOlapDataProvider and explicitly implement the IOlapDataProvider. The connection to the database is done with the help of the WCF service. The service has to be created and instantiated as described below.

[] 

The WCF Service has to implement the IOlapDataProvider interface and for implementing this interface, we require the OlapDataProvider, which can be instantiated by passing the connection string.

The code snippet is displayed below:

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                 |
| [public][ [class] [OlapManager] : [IOlapDataProvider]]                                |
|                                                                                                                                                                                                                                                 |
| [{]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                 |
| [        Syncfusion.OlapSilverlight.Manager.[OlapDataProvider] dataManager;]                                                                                                        |
|                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                 |
| [        [///][ ][\<summary\>]]                                                                                                             |
|                                                                                                                                                                                                                                                 |
| [        [///][ Initializes a new instance of the ][\<see cref=\"OlapManager\"/\>][ class.]]                          |
|                                                                                                                                                                                                                                                 |
| [        [///][ ][\</summary\>]]                                                                                                            |
|                                                                                                                                                                                                                                                 |
| [        [public] OlapManager()]                                                                                                                                                       |
|                                                                                                                                                                                                                                                 |
| [        {]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                 |
| [            [string] connectionString = [\"DataSource=localhost;Initial Catalog=Adventure Works DW\"];]                                                       |
|                                                                                                                                                                                                                                                 |
| [            [// Instantiating the OlapDataProvider with Connection String]]                                                                                                          |
|                                                                                                                                                                                                                                                 |
| [            dataManager = [new] [OlapDataProvider](connectionString);]                                                                                        |
|                                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                 |
| [        #region][ IOlapDataProvider Members]                                                                                                              |
|                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                 |
| [        [///][ ][\<summary\>]]                                                                                                             |
|                                                                                                                                                                                                                                                 |
| [        [///][ Executing the CellSet by passing OlapReport]]                                                                                                    |
|                                                                                                                                                                                                                                                 |
| [        [///][ ][\</summary\>]]                                                                                                            |
|                                                                                                                                                                                                                                                 |
| [        [///][ ][\<param name=\"report\"\>][The report.][\</param\>]]                           |
|                                                                                                                                                                                                                                                 |
| [        [///][ ][\<returns\>\</returns\>]]                                                                                                 |
|                                                                                                                                                                                                                                                 |
| [        [public] Syncfusion.OlapSilverlight.Data.[CellSet] ExecuteOlapReport(Syncfusion.OlapSilverlight.Reports.[OlapReport] report)] |
|                                                                                                                                                                                                                                                 |
| [        {]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                 |
| [            Syncfusion.OlapSilverlight.Data.[CellSet] cellSet = [this].dataManager.ExecuteOlapReport(report);]                                                |
|                                                                                                                                                                                                                                                 |
| [            [// Closing the Provider Connection]]                                                                                                                                    |
|                                                                                                                                                                                                                                                 |
| [            [this].dataManager.DataProvider.CloseConnection();]                                                                                                                       |
|                                                                                                                                                                                                                                                 |
| [            [return] cellSet;]                                                                                                                                                        |
|                                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                 |
| [        [///][ ][\<summary\>]]                                                                                                             |
|                                                                                                                                                                                                                                                 |
| [        [///][ Executing the CellSet by passing MDX Query]]                                                                                                     |
|                                                                                                                                                                                                                                                 |
| [        [///][ ][\</summary\>]]                                                                                                            |
|                                                                                                                                                                                                                                                 |
| [        [///][ ][\<param name=\"mdxQuery\"\>][The MDX query.][\</param\>]]                      |
|                                                                                                                                                                                                                                                 |
| [        [///][ ][\<returns\>\</returns\>]]                                                                                                 |
|                                                                                                                                                                                                                                                 |
| [        [public] Syncfusion.OlapSilverlight.Data.[CellSet] ExecuteMdxQuery([string] mdxQuery)]                                           |
|                                                                                                                                                                                                                                                 |
| [        {]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                 |
| [            Syncfusion.OlapSilverlight.Data.[CellSet] cellSet = [this].dataManager.ExecuteMdxQuery(mdxQuery);]                                                |
|                                                                                                                                                                                                                                                 |
| [            [// Closing the Provider Connection]]                                                                                                                                    |
|                                                                                                                                                                                                                                                 |
| [            [this].dataManager.DataProvider.CloseConnection();]                                                                                                                       |
|                                                                                                                                                                                                                                                 |
| [            [return] cellSet;]                                                                                                                                                        |
|                                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                 |
| [        [public] [MemberCollection] GetChildMembers([string] memberUniqueName, [string] cubeName)]                  |
|                                                                                                                                                                                                                                                 |
| [        {]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                 |
| [            [throw] [new] [NotImplementedException]();]                                                                                  |
|                                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                 |
| [        [public] [CubeSchema] GetCubeSchema([string] cubeName)]                                                                          |
|                                                                                                                                                                                                                                                 |
| [        {]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                 |
| [            [throw] [new] [NotImplementedException]();]                                                                                  |
|                                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                 |
| [        [public] [CubeInfoCollection] GetCubes()]                                                                                                             |
|                                                                                                                                                                                                                                                 |
| [        {]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                 |
| [            [throw] [new] [NotImplementedException]();]                                                                                  |
|                                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                 |
| [        [public] [MemberCollection] GetLevelMembers([string] levelUniqueName, [string] cubeName)]                   |
|                                                                                                                                                                                                                                                 |
| [        {]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                 |
| [            [throw] [new] [NotImplementedException]();]                                                                                  |
|                                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                 |
| [        #endregion][]                                                                                                                                     |
|                                                                                                                                                                                                                                                 |
| [}]**[]**                                                                                                                                                               |
|                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                          |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [Public][ [Class] OlapManager]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [       [Implements] IOlapDataProvider]                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [            [Private] dataManager [As] Syncfusion.OlapSilverlight.Manager.OlapDataProvider]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [            [\'\'\' \<summary\>]]                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [            [\'\'\' Initializes a new instance of the \<see cref=\"OlapManager\"/\> class.]]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [            [\'\'\' \</summary\>]]                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [            [Public] [Sub] [New]()]                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                  [Dim] connectionString [As] [String] = \"DataSource=localhost;Initial Catalog=Adventure Works DW\"]                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                  [\' Instantiating the OlapDataProvider with Connection String]]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                  dataManager = [New] OlapDataProvider(connectionString)]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [            [End] [Sub]]                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [            [#Region] \"IOlapDataProvider Members\"]                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [            [\'\'\' \<summary\>]]                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [            [\'\'\' Executing the CellSet by passing OlapReport]]                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [            [\'\'\' \</summary\>]]                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [            [\'\'\' \<param name=\"report\"\>The report.\</param\>]]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [            [\'\'\' \<returns\>\</returns\>]]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [            [Public] [Function] ExecuteOlapReport([ByVal] report [As] Syncfusion.OlapSilverlight.Reports.OlapReport) [As] Syncfusion.OlapSilverlight.Data.CellSet]                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                  [Dim] cellSet [As] Syncfusion.OlapSilverlight.Data.CellSet = [Me].dataManager.ExecuteOlapReport(report)]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                  [\' Closing the Provider Connection]]                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                  [Me].dataManager.DataProvider.CloseConnection()]                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                  [Return] cellSet]                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [            [End] [Function]]                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [            [\'\'\' \<summary\>]]                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [            [\'\'\' Executing the CellSet by passing MDX Query]]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [            [\'\'\' \</summary\>]]                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [            [\'\'\' \<param name=\"mdxQuery\"\>The MDX query.\</param\>]]                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [            [\'\'\' \<returns\>\</returns\>]]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [            [Public] [Function] ExecuteMdxQuery([ByVal] mdxQuery [As] [String]) [As] Syncfusion.OlapSilverlight.Data.CellSet]                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                  [Dim] cellSet [As] Syncfusion.OlapSilverlight.Data.CellSet = [Me].dataManager.ExecuteMdxQuery(mdxQuery)]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                  [\' Closing the Provider Connection]]                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                  [Me].dataManager.DataProvider.CloseConnection()]                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                  [Return] cellSet]                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [            [End] [Function]]                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [            [Public] [Function] GetChildMembers([ByVal] memberUniqueName [As] [String], [ByVal] cubeName [As] [String]) [As] MemberCollection] |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                  [Throw] [New] NotImplementedException()]                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [            [End] [Function]]                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [            [Public] [Function] GetCubeSchema([ByVal] cubeName [As] [String]) [As] CubeSchema]                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                  [Throw] [New] NotImplementedException()]                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [            [End] [Function]]                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [            [Public] [Function] GetCubes() [As] CubeInfoCollection]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                  [Throw] [New] NotImplementedException()]                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [            [End] [Function]]                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [            [Public] [Function] GetLevelMembers([ByVal] levelUniqueName [As] [String], [ByVal] cubeName [As] [String]) [As] MemberCollection]  |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                  [Throw] [New] NotImplementedException()]                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [            [End] [Function]]                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [            [#End Region]]                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [ [End] [Class]]                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

10.  Include the Custom Binding and the Service endpoint address in the Web.Config file.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [     \<!\--][Binding][\--\>][\                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [      \<][bindings][\>]\                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [        \<][customBinding][\>]\                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [          \<][binding][ ][name][=]\"[binaryHttpBinding]\"[\>]\                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [            \<][binaryMessageEncoding][/\>]\                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [            \<][httpTransport][ ][maxReceivedMessageSize][=]\"[2147483647]\"[/\>]\                                                                                                                                                                                                                                                                                                                                                                                              |
| [          \</][binding][\>]\                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [        \</][customBinding][\>]\                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [      \</][bindings][\>]\                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|  \                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [      \<!---][Endpoint Address][\--\>]\                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [      \<][services][\>]\                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [        \<][service][ ][name][=]\"[SilverlightApplication1.Web.OlapManager]\"[ \>]\                                                                                                                                                                                                                                                                                                                                                                                             |
| [          \<][endpoint][ ][address][=]\"[binary]\"[ ][binding][=]\"[customBinding]\"[ ][bindingConfiguration][=]\"[binaryHttpBinding]\"[ ][contract][=]\"[Syncfusion.OlapSilverlight.Manager.IOlapDataProvider]\"[\>]\ |
| [          \</][endpoint][\>]\                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [        \</][service][\>]\                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [      \</][services][\>]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

11.  Add the System.ServiceModel assembly as a reference for the Silverlight Project.

 

**[]** 

 

 

{border="0"}

 

Figure 14: Adding ServiceModel reference to Silverlight project[]

 

12.  Service instantiation in the Silverlight Project (MainPage.xaml.cs).

            a. Declare IOlapDataProvider for Service instantiation.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                     |
|                                                                                                                                      |
| [// Declaring the IOlapDataProvider for service instantiation][\                   |
|         [IOlapDataProvider] DataProvider = [null];] |
+--------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                        |
|                                                                                                                                                                  |
| [\' Declaring the IOlapDataProvider for service instantiation][]           |
|                                                                                                                                                                  |
| [      [Dim] DataProvider [As] IOlapDataProvider = [Nothing]] |
|                                                                                                                                                                  |
| []                                                                                                                           |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

  b. Specify the custom binding and Instantiate the DataProvider from the ChannelFactory.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                       |
| [private][ [void] InitializeConnection()\                                                                                                                                                                                                                                                                       |
|          {\                                                                                                                                                                                                                                                                                                                                                                           |
|             System.ServiceModel.Channels.[Binding] customBinding = [new] [CustomBinding]([new] [BinaryMessageEncodingBindingElement](), [new] [HttpTransportBindingElement] { MaxReceivedMessageSize = 2147483647 });\ |
|             [EndpointAddress] address = [new] [EndpointAddress]([new] [Uri]([App].Current.Host.Source + [\"../../../../OlapManager.svc/binary\"]));\                                                                |
|             [ChannelFactory]\<[IOlapDataProvider]\> clientChannel = [new] [ChannelFactory]\<[IOlapDataProvider]\>(customBinding, address);\                                                                                                                      |
|             DataProvider = clientChannel.CreateChannel();\                                                                                                                                                                                                                                                                                                                            |
|          }]                                                                                                                                                                                                                                                                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                         |
| [Private][ [Sub] InitializeConnection()]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                         |
| [                  [Dim] customBinding [As] System.ServiceModel.Channels.Binding = [New] CustomBinding([New] BinaryMessageEncodingBindingElement(), [New] HttpTransportBindingElement [With] {.MaxReceivedMessageSize = 2147483647})] |
|                                                                                                                                                                                                                                                                                                                                                                                                         |
| [                  [Dim] address [As] EndpointAddress = [New] EndpointAddress([New] Uri(App.Current.Host.Source & [\"../../../../OlapManager.svc/binary\"]))]                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                         |
| [                  [Dim] clientChannel [As] ChannelFactory([Of] IOlapDataProvider) = [New] ChannelFactory([Of] IOlapDataProvider)(customBinding, address)]                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                         |
| [                  DataProvider = clientChannel.CreateChannel()]                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                         |
| [         [End] [Sub]]                                                                                                                                                                                                                                                                                                    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

13.  Create the Report.

[] 

For creating reports there is a report object called OlapReport. OlapReport contains CategoricalItems, SeriesItems, SlicerItems, and FilterItems.

 

It is associated with the OlapDataManager as the currentreport property. When a report is set to the current report then an event is triggered and the control renders based on the current report that is set.

 

The report can be defined in code as follows:

[] 

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                    |
|                                                                                                                                                                                     |
| [        [///][ ][\<summary\>]\                                                                                     |
|         [///][ OlapReport with Cateogorical and Series Elements]\                                                                        |
|         [///][ ][\</summary\>]\                                                                                     |
|         [///][ ][\<returns\>\</returns\>]\                                                                          |
|         [private] [OlapReport] CreateOlapReport()\                                                                                     |
|         {\                                                                                                                                                                          |
|             [// Instantiating the OlapReport]\                                                                                                                |
|             [OlapReport] olapReport = [new] [OlapReport]();\                                                   |
|             [// Specifying the Current cube name]\                                                                                                            |
|             olapReport.CurrentCubeName = [\"Adventure Works\"];\                                                                                            |
|  \                                                                                                                                                                                  |
|             [DimensionElement] dimensionElementColumn = [new] [DimensionElement]();\                           |
|             [//Specifying the Name for the Dimension Element]\                                                                                                |
|             dimensionElementColumn.Name = [\"Customer\"];\                                                                                                  |
|             dimensionElementColumn.HierarchyName = [\"Customer Geography\"];\                                                                               |
|             [//Adding the level Elemenet along with the Hierarchy Name]\                                                                                      |
|             dimensionElementColumn.AddLevel([\"Customer Geography\"], [\"Country\"]);\                                              |
|  \                                                                                                                                                                                  |
|             [DimensionElement] dimensionElementRow = [new] [DimensionElement]();\                              |
|             [//Specifying the Name for Dimension Element]\                                                                                                    |
|             dimensionElementRow.Name = [\"Date\"];\                                                                                                         |
|             [//Adding the level Elemenet along with the Hierarchy Name]\                                                                                      |
|             dimensionElementRow.AddLevel([\"Fiscal\"], [\"Fiscal Year\"]);\                                                         |
|  \                                                                                                                                                                                  |
|             [MeasureElements] measureElementColumn = [new] [MeasureElements]();\                               |
|             [// Specifying the Measure Elements]\                                                                                                             |
|             measureElementColumn.Elements.Add([new] [MeasureElement] { Name = [\"Internet Sales Amount\"] });\ |
|  \                                                                                                                                                                                  |
|             [// Adding Column Members]\                                                                                                                       |
|             olapReport.CategoricalElements.Add([new] [Item] { ElementValue = dimensionElementColumn });\                               |
|             [///][Adding Measure Element]\                                                                                               |
|             olapReport.CategoricalElements.Add([new] [Item] { ElementValue = measureElementColumn });\                                 |
|             [///][Adding Row Members]\                                                                                                   |
|             olapReport.SeriesElements.Add([new] [Item] { ElementValue = dimensionElementRow });\                                       |
|  \                                                                                                                                                                                  |
|             [return] olapReport;\                                                                                                                              |
|         }]                                                                                                                                      |
|                                                                                                                                                                                     |
| []                                                                                                                                              |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                     |
|                                                                                                                                                                                                      |
| [\'\'\' \<summary\>][]                                                                                         |
|                                                                                                                                                                                                      |
| [            [\'\'\' OlapReport with Cateogorical and Series Elements]]                                                                    |
|                                                                                                                                                                                                      |
| [            [\'\'\' \</summary\>]]                                                                                                        |
|                                                                                                                                                                                                      |
| [            [\'\'\' \<returns\>\</returns\>]]                                                                                             |
|                                                                                                                                                                                                      |
| [            [Private] [Function] CreateOlapReport() [As] OlapReport]                             |
|                                                                                                                                                                                                      |
| [                  [\' Instantiating the OlapReport]]                                                                                      |
|                                                                                                                                                                                                      |
| [                  [Dim] olapReport [As] OlapReport = [New] OlapReport()]                         |
|                                                                                                                                                                                                      |
| [                  [\' Specifying the Current cube name]]                                                                                  |
|                                                                                                                                                                                                      |
| [                  olapReport.CurrentCubeName = \"Adventure Works\"]                                                                                             |
|                                                                                                                                                                                                      |
| []                                                                                                                                                               |
|                                                                                                                                                                                                      |
| [                  [Dim] dimensionElementColumn [As] DimensionElement = [New] DimensionElement()] |
|                                                                                                                                                                                                      |
| [                  [\'Specifying the Name for the Dimension Element]]                                                                      |
|                                                                                                                                                                                                      |
| [                  dimensionElementColumn.Name = \"Customer\"]                                                                                                   |
|                                                                                                                                                                                                      |
| [                  dimensionElementColumn.HierarchyName = \"Customer Geography\"]                                                                                |
|                                                                                                                                                                                                      |
| [                  [\'Adding the level Elemenet along with the Hierarchy Name]]                                                            |
|                                                                                                                                                                                                      |
| [                  dimensionElementColumn.AddLevel(\"Customer Geography\", \"Country\")]                                                                         |
|                                                                                                                                                                                                      |
| []                                                                                                                                                               |
|                                                                                                                                                                                                      |
| [                  [Dim] dimensionElementRow [As] DimensionElement = [New] DimensionElement()]    |
|                                                                                                                                                                                                      |
| [                  [\'Specifying the Name for Dimension Element]]                                                                          |
|                                                                                                                                                                                                      |
| [                  dimensionElementRow.Name = \"Date\"]                                                                                                          |
|                                                                                                                                                                                                      |
| [                  [\'Adding the level Elemenet along with the Hierarchy Name]]                                                            |
|                                                                                                                                                                                                      |
| [                  dimensionElementRow.AddLevel(\"Fiscal\", \"Fiscal Year\")]                                                                                    |
|                                                                                                                                                                                                      |
| []                                                                                                                                                               |
|                                                                                                                                                                                                      |
| [                  [Dim] measureElementColumn [As] MeasureElements = [New] MeasureElements()]     |
|                                                                                                                                                                                                      |
| [                  [\' Specifying the Measure Elements]]                                                                                   |
|                                                                                                                                                                                                      |
| [                  measureElementColumn.Elements.Add([New] MeasureElement [With] {.Name = \"Internet Sales Amount\"})] |
|                                                                                                                                                                                                      |
| []                                                                                                                                                               |
|                                                                                                                                                                                                      |
| [                  [\' Adding Column Members]]                                                                                             |
|                                                                                                                                                                                                      |
| [                  olapReport.CategoricalElements.Add([New] Item [With] {.ElementValue = dimensionElementColumn})]     |
|                                                                                                                                                                                                      |
| [                  [\'\'\'Adding Measure Element]]                                                                                         |
|                                                                                                                                                                                                      |
| [                  olapReport.CategoricalElements.Add([New] Item [With] {.ElementValue = measureElementColumn})]       |
|                                                                                                                                                                                                      |
| [                  [\'\'\'Adding Row Members]]                                                                                             |
|                                                                                                                                                                                                      |
| [                  olapReport.SeriesElements.Add([New] Item [With] {.ElementValue = dimensionElementRow})]             |
|                                                                                                                                                                                                      |
| []                                                                                                                                                               |
|                                                                                                                                                                                                      |
| [                  [Return] olapReport]                                                                                                     |
|                                                                                                                                                                                                      |
| [            [End] [Function]]                                                                                         |
|                                                                                                                                                                                                      |
| []                                                                                                                                                               |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

14.  Data Binding.

[] 

The following code snippet explains how you can bind the data source with the OlapChart control.

[] 

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                         |
| [      ][ [///][ ][\<summary\>]\                                                                                                                                                                    |
|         [///][ Handles the Loaded event of the MainPage control.]\                                                                                                                                                                                           |
|         [///][ ][\</summary\>]\                                                                                                                                                                                                         |
|         [///][ ][\<param name=\"sender\"\>][The source of the event.][\</param\>]\                                                                                                           |
|         [///][ ][\<param name=\"e\"\>][The ][\<see cref=\"System.Windows.RoutedEventArgs\"/\>][ instance containing the event data.][\</param\>]\ |
|         [void] MainPage_Loaded([object] sender, [RoutedEventArgs] e)\                                                                                                                                                                 |
|         {\                                                                                                                                                                                                                                                                                              |
|             [// Initailizing the connection]\                                                                                                                                                                                                                                     |
|             [this].InitializeConnection();\                                                                                                                                                                                                                                        |
|             [// Instantiating the OlapDataManager]\                                                                                                                                                                                                                               |
|             [OlapDataManager] olapDataManager = [new] [OlapDataManager]();\                                                                                                                                                        |
|             [// Specifying the DataProvider for OlapDataManager]\                                                                                                                                                                                                                 |
|             olapDataManager.DataProvider = [this].DataProvider;\                                                                                                                                                                                                                   |
|             [// Set Current report for OlapDataManager]\                                                                                                                                                                                                                          |
|             olapDataManager.SetCurrentReport(CreateOlapReport());\                                                                                                                                                                                                                                      |
|             [// Specifying the OlapDataManager for OlapChart]\                                                                                                                                                                                                                    |
|             [this].olapChart1.OlapDataManager = olapDataManager;\                                                                                                                                                                                                                  |
|             [// DataBinding]\                                                                                                                                                                                                                                                     |
|             [this].olapChart1.DataBind();\                                                                                                                                                                                                                                         |
|         }]                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                    |
| [\'\'\' \<summary\>][]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                    |
| [            [\'\'\' Handles the Loaded event of the MainPage control.]]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                    |
| [            [\'\'\' \</summary\>]]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                    |
| [            [\'\'\' \<param name=\"sender\"\>The source of the event.\</param\>]]                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                    |
| [            [\'\'\' \<param name=\"e\"\>The \<see cref=\"System.Windows.RoutedEventArgs\"/\> instance containing the event data.\</param\>]]                                                                                            |
|                                                                                                                                                                                                                                                                                                    |
| [            [Private] [Sub] MainPage_Loaded([ByVal] sender [As] [Object], [ByVal] e [As] RoutedEventArgs)] |
|                                                                                                                                                                                                                                                                                                    |
| [                  [\' Initailizing the connection]]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                    |
| [                  [Me].InitializeConnection()]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                    |
| [                  [\' Instantiating the OlapDataManager]]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                    |
| [                  [Dim] olapDataManager [As] OlapDataManager = [New] OlapDataManager()]                                                                                                        |
|                                                                                                                                                                                                                                                                                                    |
| [                  [\' Specifying the DataProvider for OlapDataManager]]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                    |
| [                  olapDataManager.DataProvider = [Me].DataProvider]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                    |
| [                  [\' Set Current report for OlapDataManager]]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                    |
| [                  olapDataManager.SetCurrentReport(CreateOlapReport())]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                    |
| [                  [\' Specifying the OlapDataManager for OlapChart]]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                    |
| [                  [Me].olapChart1.OlapDataManager = olapDataManager]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                    |
| [                  [\' DataBinding]]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                    |
| [                  [Me].olapChart1.DataBind()]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                    |
| [            [End] [Sub]]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

 

Figure 15: OlapChart Control with OLAP Data

[]{#related-topics}

