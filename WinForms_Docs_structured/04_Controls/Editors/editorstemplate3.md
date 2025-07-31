---
title: editorstemplate3.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Editors\editorstemplate3.md
created_at: 2025-07-03
---






#### Editors Template {#editors-template style="tab-stops: 0pt"}

To create an Editor Template using custom Syncfusion T4 Templates, follow the below steps:

 

1.   Open a new Tools MVC Project template which is fully configured for Tools MVC Controls. Refer to the [MVC Project Template]{.UGHyperlink}

2.   Now, in VisualStudio Project right click the **Home** folder and click **Add,** followed by **View**. The below image illustrates this:

 

{border="0"}

 

Figure 27: Adding View

3.   To use Editors Template in AddView dialog, select **Editors Template** from **View Content** dropdownlist as shown below:

 

{border="0"}

Figure 28: Selecting Editors Template

*[]* 

4.   In the Index.aspx file, controls are decided according to the column types. The column types are:

 

[·      ]Integer -- Numeric Textbox

[·      ]DateTime -- DatePicker

[·      ]String -- TextBox

{border="0"}

Figure 29: Controls are bounded to Database

*[]* 

5.   Refer to the [[Tools MVC UG]{.UGHyperlink}](http://help.syncfusion.com/ug_83/User%20Interface/ASP.NET%20MVC/Tools/index.htm), for further customization.

[] 

{border="0"}

Figure 30: Editor Controls are rendered in Index page

[] 

[] 

[]{#related-topics}

