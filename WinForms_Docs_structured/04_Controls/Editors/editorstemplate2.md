---
title: editorstemplate2.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Editors\editorstemplate2.md
created_at: 2025-07-03
---






#### Editors Template {#editors-template style="tab-stops: 0pt"}

To create an Editor template using custom Syncfusion T4 templates, follow the steps below.

 

1.   Open a new Tools MVC Project template which is fully configured for Tools for MVC controls. Refer to [[MVC Project Template]]{.underline} for additional information[.]

2.   In your Visual Studio Project, right-click the **Home** folder and click **Add** followed by **View**. The following image illustrates this.

 

{border="0"}

Figure 27: Adding a View

 

 

3.   To use Editors templates in the **Add View** dialog, select **Editors Template** from the **View Content** drop-down list as shown below.

 

{border="0"}

Figure 28: Selecting Editors Template

*[]* 

4.   In the **Index.aspx** file, controls are decided according to the column types. They are:

 

[·      ]Integer---Numeric TextBox

[·      ]DateTime---DatePicker

[·      ]String---TextBox

{border="0"}

Figure 29: Controls Bound to a Database

*[]* 

5.   Refer to the [[[Tools MVC UG]]{.underline}](http://help.syncfusion.com/ug_83/User%20Interface/ASP.NET%20MVC/Tools/index.htm) for further customization information.

[] 

{border="0"}

Figure 30: Editor Controls Rendered in the Index Page

[] 

[]{#_Template_Location}[]{#_Configuring_CellEditType}[] 

[] 

[] 

[] 

[]{#related-topics}

