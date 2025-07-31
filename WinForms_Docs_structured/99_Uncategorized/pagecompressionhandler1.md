---
title: pagecompressionhandler1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\pagecompressionhandler1.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}





  






    


### Page Compression Handler {#page-compression-handler style="tab-stops: 0pt"}

[] 

The Page Compression Handler shipped with **Syncfusion.Shared.Web** can be used for compression of the HTML source file to enhance the performance.

 

In order to achieve this, we need to add the following XML tag in the project\'s web.config file under \<httpModules\>, as given below.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\<] [httpModules] [\>]                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\<] [add] [ [name] [=\"HttpCompressModule\"] [type] [=\"Syncfusion.Web.UI.WebControls.Handler.PageCompressHandler, Syncfusion.Shared.Web, Version=X.X.X.X, Culture=neutral, PublicKeyToken=3D67ED1F87D44C89\"/\>] ] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\</] [httpModules] [\>]                                                                                                                                                                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Advantages

[] 

[·      ]It compresses the page and reduces the time taken to render the page

[·      ]It loads the Script files very fast

[·      ]It makes it difficult to read the compressed code, and hence provides protection against theft

 

[]{#related-topics}

