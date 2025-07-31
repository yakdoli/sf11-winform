---
title: projectreference4.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\projectreference4.md
created_at: 2025-07-03
---






#### Project Reference {#project-reference style="tab-stops: 0pt"}

 To place T4 templates by per-project basis, follow the below steps

 

7.   Create a folder named 'CodeTemplates' and then create a folder named  'AddView' under this. Paste the Custom Syncfusion T4 Templates to this folder and include the files into the root of your project which helps to create the templates in the above location. Then customize the templates on a per-project basis. The below image illustrates this.

 

{border="0"}

Figure 17: Including CodeTemplates


{border="0"}Note: when you copy the above folder (any time you add a T4 template(.tt)  file) into the project, you will see warnings as follows:


{border="0"}

Figure 18: Template Execution Warning

8.   Click Cancel so that you don't run the T4 template (if you are adding multiple .tt files, you have to click Cancel every time you get the Template Execution Warning window.). 

 

As soon as the project sees a .tt file, a property on the file called **CustomTool** it will get set to TextTemplatingFileGenerator.  This tells Visual Studio to use the default T4 host to execute the template and create a new file (nested underneath the template) based on the template. The below image illustrates this.

 

{border="0"}

Figure 19: Custom Tool Property

[] 

9.   Empty the text for **Custom Tool** Property and build the project as shown in the below image.

[] 

[] 

[] 

{border="0"}

Figure 20: Setting empty text in Custom Tool property

**[]** 

[]{#related-topics}

