---
title: manuallycreatingastronglytypedview4.md
original_path: WinForms_Docs/99_Uncategorized/manuallycreatingastronglytypedview4.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



#### Manually Creating a Strongly Typed View {#manually-creating-a-strongly-typed-view style="tab-stops: 0pt"}

If you create a view and later need to convert it to a strongly typed view, the process is quite simple. Change the \"Inherits\" statement in the view declaration from:

*** *** ***System.Web.Mvc.ViewPage to*** ***System.Web.Mvc.ViewPage\<YourNamespace.YourClass*** ***\>***

Here our model is "MvcSampleApplication.Models.Order,"so update the index page like this:

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ***[\[View\]]*** **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\<%] [@] [ [Page] [Language] [=\"C#\"] [MasterPageFile] [=\"\~/Views/Shared/Site.Master\"] [Inherits] [=\"System.Web.Mvc.ViewPage[\<IEnumerable\<MvcSampleApplication.Models.Order\>\>]\"] [%\>] ] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[ {border="0"} ] []

Figure 254: Default Index View

 

{border="0"}

Figure 255: Default Index View

 

[]{#related-topics}

