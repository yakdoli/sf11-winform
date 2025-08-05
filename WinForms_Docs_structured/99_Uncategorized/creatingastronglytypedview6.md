---
title: creatingastronglytypedview6.md
original_path: WinForms_Docs/99_Uncategorized/creatingastronglytypedview6.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



#### Creating a Strongly Typed View {#creating-a-strongly-typed-view style="TEXT-INDENT: -43.2pt; MARGIN-LEFT: 43.2pt; tab-stops: 43.2pt"}

The following steps describe how to create a strongly typed view.

1.  Right-click on the **View/Home** folder

[·      ]Delete the existing **Index.aspx**  (to make it remain as a default action)

[·      ]Click **Add**, then select **View**

[·      ]Name the view "**Index.**"

[·      ]Select **Create a strongly-typed view**

[·      ]On the drop-down menu, select your model (in this case it is "MvcSampleApplication.Models.Order")

{border="0"}

Figure 59: Adding a Strongly Typed View


 

{border="0"}Note: The View Data class drop-down list will be empty until you successfully build your application. It is a good idea to select from the menu option build, build solution before opening the Add New dialog.

 


[·      ]In **View data class**, make the model an IEnumerable collection.

[] 

{border="0"}

Figure 60: View Data Classes as an IEumerable Collection

 

[]{#related-topics}

