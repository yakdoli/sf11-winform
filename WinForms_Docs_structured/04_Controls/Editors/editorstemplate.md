---
title: editorstemplate.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Editors\editorstemplate.md
created_at: 2025-07-03
---






#### Editors Template {#editors-template style="tab-stops: 0pt"}

To create an Editor Template using custom Syncfusion T4 Templates:

 

1.   Open a new **Tools MVC Project** template, which is fully configured for Tools MVC Controls. Refer to the **[MVC Project Template]**.

2.   Now, in **VisualStudio** **Project,** right click the **Home** folder and click **Add** followed by **View**. The following image illustrates this:

[] 

{border="0"}

Figure 26: Adding View

3.   To use the **Editors** Template in **AddView dialog**, select the **Editors Template** from the **View Content** dropdownlist as shown below:

[] 

{border="0"}

Figure 27: Selecting Editors Template

*[]* 

4.   In Index.aspx file, controls are decided according to the column types. They are:

**[]** 

[·      ]Integer -- Numeric Textbox

[·      ]DateTime -- DatePicker

[·      ]String -- TextBox

{border="0"}

Figure 28: Controls are bounded to Database

*[]* 

5.   Refer to Tools MVC UG, for further customization.

[] 

{border="0"}

Figure 29: Editor Controls are rendered in the Index page

 

[]{#related-topics}

