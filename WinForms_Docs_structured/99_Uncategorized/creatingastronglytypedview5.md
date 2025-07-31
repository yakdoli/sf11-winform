---
title: creatingastronglytypedview5.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\creatingastronglytypedview5.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



#### Creating a Strongly Typed View {#creating-a-strongly-typed-view style="TEXT-INDENT: -43.2pt; MARGIN-LEFT: 43.2pt; tab-stops: 43.2pt"}

The following steps describe how to create a strongly typed view.

1.   Right-click on the **View/Home** folder

2.   Delete the existing **Index.aspx**  (to make it remain as a default action)

3.   Click **Add**, then select **View**

4.   Name the view "**Index.**"

5.   Select **Create a strongly-typed view**

6.   On the drop-down menu, select your model (in this case it is "MvcSampleApplication.Models.Order")

{border="0"}

Figure 68: Adding a Strongly Typed View


 

{border="0"}Note: The View Data class drop-down list will be empty until you successfully build your application. It is a good idea to select from the menu option build, build solution before opening the Add New dialog.

 


7.   In **View data class**, make the model an IEnumerable collection.

[] 

{border="0"}

Figure 69: View Data Classes as an IEumerable Collection

 

[]{#related-topics}

