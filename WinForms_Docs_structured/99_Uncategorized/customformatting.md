---
title: customformatting.md
original_path: WinForms_Docs/99_Uncategorized/customformatting.md
created_at: 2025-08-05
---






#### Custom Formatting {#custom-formatting style="tab-stops: 0pt"}

 

The tag cloud control supports custom formatting so that each tag item can be formatted with custom styles to distinguish one tag from another tag.

 

Properties

 

  --------------- --------------------------------------------------------------- ------------------ ------------------ ------------
  Name            Description                                                     Type of property   Value it accepts   Dependency
  QueryItemInfo   Defines the action to be called when rendering each tag item.   Action             Action method      NA
  --------------- --------------------------------------------------------------- ------------------ ------------------ ------------

 

The following steps explain how to perform custom formatting.

1.   In the controller, pass the model to the view.

 

+------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                       |
|                                                                                                                                                |
| [public][ [ActionResult] Index()] |
|                                                                                                                                                |
| [        {]                                                                                                |
|                                                                                                                                                |
| [            [Northwind] data = SqlCE;]                                            |
|                                                                                                                                                |
| [            [//passing the Model to the view]]                                      |
|                                                                                                                                                |
| [            [return] View(data.Blogs);]                                              |
|                                                                                                                                                |
| [  }  ]                                                                                                    |
|                                                                                                                                                |
| []                                                                                                         |
+------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   [Create a strongly typed view]{.UGHyperlink}[. ]

3.   In **View**, create a list of tag items and invoke the tag cloud helper with the control ID as the first argument followed by the **DataSource** and **BindTo** methods with the data source and column names for the respective tag item properties as arguments.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                    |
| [\<%][=][Html.Syncfusion().TagCloud([\"myTagCloud\"])]        |
|                                                                                                                                                                                                                                    |
| [.Title([\"Favourite Sites\"])]                                                                                                                                        |
|                                                                                                                                                                                                                                    |
| [.TitleImageUrl(Url.Content([\"\~/Content/Blog.png\"]))        .DataSource(Model)]                                                                                     |
|                                                                                                                                                                                                                                    |
| [.BindTo(bind=\>]                                                                                                                                                                              |
|                                                                                                                                                                                                                                    |
| [bind.TagName([\"Title\"])]                                                                                                                                            |
|                                                                                                                                                                                                                                    |
| [    .Frequency([\"Rank\"])]                                                                                                                                           |
|                                                                                                                                                                                                                                    |
| [                      .NavigateUrl([\"Website\"]))]                                                                                                                   |
|                                                                                                                                                                                                                                    |
| [.QueryItemInfo(args =\>{]                                                                                                                                                                     |
|                                                                                                                                                                                                                                    |
| [     [if] (args.Item.Frequency \>= 805 && args.Item.Frequency \<= 828)]                                                                                                  |
|                                                                                                                                                                                                                                    |
| [         args.HtmlAttributes.Add([\"style\"], [\"color: #14428D;\"]);]                                                                        |
|                                                                                                                                                                                                                                    |
| [     [else] [if] (args.Item.Frequency \> 829 && args.Item.Frequency \<= 855)]                                                                       |
|                                                                                                                                                                                                                                    |
| [         args.HtmlAttributes.Add([\"style\"], [\"color: Red;\"]);]                                                                            |
|                                                                                                                                                                                                                                    |
| [     [else] [if] (args.Item.Frequency \> 856 && args.Item.Frequency \<= 887)                                        ]                               |
|                                                                                                                                                                                                                                    |
| [args.HtmlAttributes.Add([\"style\"], [\"color: Green;font-style: italic;\"]);})][%\>] |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                         |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                            |
| [\@{][ Html.Syncfusion().TagCloud([\"myTagCloud\"])]                                                                   |
|                                                                                                                                                                                                                                            |
| [.Title([\"Favourite Sites\"])]                                                                                                                                                |
|                                                                                                                                                                                                                                            |
| [.TitleImageUrl(Url.Content([\"\~/Content/Blog.png\"]))        .DataSource(Model)]                                                                                             |
|                                                                                                                                                                                                                                            |
| [.BindTo(bind=\>]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                            |
| [bind.TagName([\"Title\"])]                                                                                                                                                    |
|                                                                                                                                                                                                                                            |
| [    .Frequency([\"Rank\"])]                                                                                                                                                   |
|                                                                                                                                                                                                                                            |
| [                      .NavigateUrl([\"Website\"]))]                                                                                                                           |
|                                                                                                                                                                                                                                            |
| [.QueryItemInfo(args =\>{]                                                                                                                                                                             |
|                                                                                                                                                                                                                                            |
| [     [if] (args.Item.Frequency \>= 805 && args.Item.Frequency \<= 828)]                                                                                                          |
|                                                                                                                                                                                                                                            |
| [         args.HtmlAttributes.Add([\"style\"], [\"color: #14428D;\"]);]                                                                                |
|                                                                                                                                                                                                                                            |
| [     [else] [if] (args.Item.Frequency \> 829 && args.Item.Frequency \<= 855)]                                                                               |
|                                                                                                                                                                                                                                            |
| [         args.HtmlAttributes.Add([\"style\"], [\"color: Red;\"]);]                                                                                    |
|                                                                                                                                                                                                                                            |
| [     [else] [if] (args.Item.Frequency \> 856 && args.Item.Frequency \<= 887)                                        ]                                       |
|                                                                                                                                                                                                                                            |
| [args.HtmlAttributes.Add([\"style\"], [\"color: Green;font-style: italic;\"]);}).Render();][}] |
|                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                 |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Build and run the application.

The following figure shows the output of the tag cloud control with custom formatting.

 

{border="0"}

Figure 276: Tag Cloud with Custom Formatting

 

[]{#related-topics}

