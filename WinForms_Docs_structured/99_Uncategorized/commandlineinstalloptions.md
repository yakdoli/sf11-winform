---
title: commandlineinstalloptions.md
original_path: WinForms_Docs/99_Uncategorized/commandlineinstalloptions.md
created_at: 2025-08-05
---








  









### Command Line Install Options {#command-line-install-options style="tab-stops: 0pt"}

[] 

Syncfusion Essential Studio supports installing the setup through command line. The following steps illustrate this:

[] 

1.   Double-click the **Syncfusion Essential Studio Setup** file. The **Syncfusion Essential Studio Unified Installer wizard** opens.

2.   Click **Next**, MSI files will be extracted into the **Temp** folder.

3.   Cancel the wizard.

4.   Run **%temp%.** The **Temp** folder will open. The **EssentialStudio.msi** files will be available in one of the folders.

5.   Copy all the files in the specific folder to a desired location.  Example: D:\\temp

6.   Open the command prompt in administrator mode and pass the following arguments:

 

***msiexec /i \"MSI file path\\EssentialStudio.msi\" TEMPPATH=\"folder path of MSI and cab files\" ADDLOCAL=\"ALL\" PIDKEY=\"product unlock key\" SAMPLEPATH=\"C:\\Syncfusion\\ x.x.x.x \" /qb***

 

Example***: msiexec /i \"D:\\Temp\\EssentialStudio.msi\" TEMPPATH=\"D:\\Temp\" ADDLOCAL=\"ALL\" PIDKEY=\"product unlock key\" SAMPLEPATH=\"C:\\Syncfusion\\x.x.x.x\" /qb***

7.   Setup will be installed.


{border="0"}Note: x.x.x.x need to be replaced with the Essential studio version installed in your machine and Product unlock key need to be replaced with the unlock key for that version.


 

[]{#related-topics}

