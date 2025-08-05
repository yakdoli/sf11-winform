---
title: revertingapatch.md
original_path: WinForms_Docs/99_Uncategorized/revertingapatch.md
created_at: 2025-08-05
---








  









### Reverting a Patch {#reverting-a-patch style="tab-stops: 0pt"}

The patch install will take a backup of the release assemblies and store them in the *Backup Assemblies* folder. The patch assemblies will also be stored in the *Patch* folder.  You can revert back if needed.

[] 

Revert back to Release assemblies

[] 

The following are the steps to revert to the release assemblies:

[] 

1.   Copy the release assemblies from the **Backup Assemblies** folder.

2.   Paste them in the **precompiledassemblies** folder.

3.   Open **Dashboard \> Utility \> Assembly Management \> Assembly Manager**.

 

{border="0"}

Figure 42: Assembly Manager

 

4.   Select **Remove all** **versions** radio button.

5.   Click **Perform Action**. All versions will be removed.

6.   Select **Install version x.x.x.x.**


{border="0"}Note: x.x.x.x has to be replaced with the corresponding Essential Studio Version.


7.   Click **Perform Action**. The assemblies of specific version will be configured in your machine.

 


{border="0"}Note: You can also revert to a specific patch assemblies by copying the patch assemblies from the Patch folder and add them in the precompiledassemblies folder.

 


[]{#related-topics}

