---
title: bookmarksandhyperlin1.md
original_path: WinForms_Docs/99_Uncategorized/bookmarksandhyperlin1.md
created_at: 2025-08-05
---








  





### Bookmarks and Hyperlinks {#bookmarks-and-hyperlinks style="tab-stops: 0pt"}

A hyperlink is a convenient way to navigate from one workbook to another workbook. Links created in the native Excel will be imported to the Spreadsheet Control. You can also add new links.

 

Adding hyperlink to Cell

[]{#_Using_Excel_Editor_1}You can add the hyperlink to the spreadsheet cell using the Insert Hyperlink dialog box. You can open the Insert Hyperlink dialog using the *HyperlinkCommand.*

 

{border="0"}

Figure 41: Insert Hyperlink dialog box[]

 

The following code illustrates how to bind the *HyperlinkCommand* a button:

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\<][Button][ Command][=\"{][Binding][ Path][=] [HyperlinkCommand}\"\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\</][Button][\>]                                                                                                                                                                                                                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

