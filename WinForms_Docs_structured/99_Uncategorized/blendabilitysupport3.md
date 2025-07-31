---
title: blendabilitysupport3.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\blendabilitysupport3.md
created_at: 2025-07-03
---






#### Blendability Support {#blendability-support style="tab-stops: 0pt"}

The TileViewControl includes the Blendability support that allows you to edit the control in Microsoft Expression Blend and apply their own styles for the control in place of predefined styles.

Use Case Scenarios

The feature enables you to set own styles for the control.

[] 

Adding Blendability Support to an Application

The following are the step-by-step procedure to edit the TileViewControl in Microsoft Expression Blend.

[] 

1.   Open a new WPF Project in Microsoft Expression Blend.

2.   Include the required dll to the application.

3.   From the Toolbox and Controls sections, drag and drop the TileViewControl into the application.

4.   Once the TileViewControl is drag and dropped, the window will look as shown below.

[] 

{border="0"}

Figure 1080:View of MainPage.xaml after inserting TileViewControl in Expression Blend[]

[] 

 

1.   Once the TileViewControl is added to the application, the instance of TileViewControl will be added to the Object and the TimeLine window.

2.   Right click the instance of the TileViewControl in the Object and TimeLine window and select "Edit Template" and then "Edit a copy" as shown below.

[] 

{border="0"}

Figure 1081:Objects and TimeLine window and how to select the "Edit a Copy"[]

 

3.   After clicking the "Edit a Copy" a new window, "Create Style Resource" will appear as shown below which asks for the Name of the Style. Give the style name and press ok.

 

{border="0"}

 

Figure 1082:Create Style Resource window[]

 

 

4.   Now edit the template and apply your own styles to the control. The sample application created using Microsoft Expression Blend will appear as shown below.

 

{border="0"}

Figure 1083:Sample Application, after applying styles using Expression Blend[]

 

[]{#related-topics}

