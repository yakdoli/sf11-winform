---
title: manuallycreatingastronglytypedview3.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\manuallycreatingastronglytypedview3.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



#### Manually Creating a Strongly Typed View {#manually-creating-a-strongly-typed-view style="TEXT-INDENT: -43.2pt; MARGIN-LEFT: 43.2pt; tab-stops: 43.2pt"}

If you create a view and later need to convert it to a strongly typed view, the process is quite simple. Change the \"Inherits\" statement in the view declaration from:

*** *** ***System.Web.Mvc.ViewPage to*** ***System.Web.Mvc.ViewPage\<YourNamespace.YourClass*** ***\>***

Here our model is "MvcSampleApplication.Models.Order,"so update the index page like this:

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ***[\[]*** ***[View]*** ***[\]]*** **[]**                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\<%] [@] [ [Page] [Language] [=\"C#\"] [MasterPageFile] [=\"\~/Views/Shared/Site.Master\"] [Inherits] [=\"System.Web.Mvc.ViewPage[\<IEnumerable\<MvcSampleApplication.Models.Order\>\>]\"] [%\>] ] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[ {border="0"} ] []

Figure 61: Default Index View

 

{border="0"}

Figure 62: Default Index View

 

[]{#related-topics}

