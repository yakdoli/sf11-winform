---
title: programmatically.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\programmatically.md
created_at: 2025-07-03
---






##### Programmatically {#programmatically style="tab-stops: 0pt"}

Apply Theme for Ribbon

The following code illustrates how to apply the Office2010 theme to the ribbon:

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| \[C#\]                                                                                                                                                                                         |
|                                                                                                                                                                                                |
| [            [this].ribbonControlAdv1.RibbonStyle = Syncfusion.Windows.Forms.Tools.[RibbonStyle].Office2010;] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| \[VB\]                                                                                                                                                                            |
|                                                                                                                                                                                   |
| [Me][.ribbonControlAdv1.RibbonStyle = Syncfusion.Windows.Forms.Tools.RibbonStyle.Office2010] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

Creating BackStageView

[] 

The following code illustrates how to create a backstage with a *BackStageButtom* and a *BackStageTab*:

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                    |
| [                using][ Syncfusion.Windows.Forms;]                                                                                                           |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                    |
| [                [BackStageView] backStageView1 = [new] [BackStageView]([this].components);]                         |
|                                                                                                                                                                                                                                                    |
| [                [BackStage] backStage1 = [new] [BackStage]();]                                                                           |
|                                                                                                                                                                                                                                                    |
| [                [BackStageTab] backStageTab1 = [new] [BackStageTab]();]                                                                  |
|                                                                                                                                                                                                                                                    |
| [                [BackStageButton] backStageButton1 = [new] [BackStageButton]();]                                                         |
|                                                                                                                                                                                                                                                    |
| [      ]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                    |
| [                  [// backStageView1]]                                                                                                                                                  |
|                                                                                                                                                                                                                                                    |
| [                backStageView1.BackStage = backStage1;]                                                                                                                                                       |
|                                                                                                                                                                                                                                                    |
| [                backStageView1.HostControl = [null];]                                                                                                                                    |
|                                                                                                                                                                                                                                                    |
| [                backStageView1.HostForm = [this];]                                                                                                                                       |
|                                                                                                                                                                                                                                                    |
| [                 ]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                    |
| [                  [// backStage1]]                                                                                                                                                      |
|                                                                                                                                                                                                                                                    |
| [                backStage1.Controls.Add(backStageTab1);]                                                                                                                                                      |
|                                                                                                                                                                                                                                                    |
| [                backStage1.Controls.Add(backStageButton1);]                                                                                                                                                   |
|                                                                                                                                                                                                                                                    |
| [                backStage1.Dock = System.Windows.Forms.[DockStyle].Fill;]                                                                                                             |
|                                                                                                                                                                                                                                                    |
| [      ]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                    |
| [                  [// backStageTab1]]                                                                                                                                                   |
|                                                                                                                                                                                                                                                    |
| [                backStageTab1.Text = [\"backStageTab1\"];]                                                                                                                            |
|                                                                                                                                                                                                                                                    |
| [               ]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                    |
| [                  [// backStageButton1]]                                                                                                                                                |
|                                                                                                                                                                                                                                                    |
| [                backStageButton1.Text = [\"backStageButton1\"];]                                                                                                                      |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                    |
| [                [// ribbonControlAdv1]]                                                                                                                                                 |
|                                                                                                                                                                                                                                                    |
| [                  ribbonControlAdv1.BackStageView = backStageView1;]                                                                                                                                          |
|                                                                                                                                                                                                                                                    |
| [                 ]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                    |
| [                  [//Add BackStage to RibbonControlAdv ]]                                                                                                                               |
|                                                                                                                                                                                                                                                    |
| [                  ribbonControlAdv1.BackStageView =backStageView1;]                                                                                                                                           |
|                                                                                                                                                                                                                                                    |
| [      ]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                    |
| [                 [//Add BackStage and RibbonControlAdv to form]]                                                                                                                        |
|                                                                                                                                                                                                                                                    |
| [                  [this].Controls.Add(backStage1);]                                                                                                                                      |
|                                                                                                                                                                                                                                                    |
| [                  [this].Controls.Add([this].ribbonControlAdv1);][        ][] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[VB\]]                                                                                                                                                                     |
|                                                                                                                                                                                                                  |
| [                    Imports][ Syncfusion.Windows.Forms]                                                                    |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                  |
| [                        [Dim] backStageView1 [As] [New] BackStageView([Me].components)] |
|                                                                                                                                                                                                                  |
| [                        [Dim] backStage1 [As] [New] BackStage()]                                             |
|                                                                                                                                                                                                                  |
| [                        [Dim] backStageTab1 [As] [New] BackStageTab()]                                       |
|                                                                                                                                                                                                                  |
| [                        [Dim] backStageButton1 [As] [New] BackStageButton()]                                 |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                  |
| [                        \' backStageView1][]                                                                              |
|                                                                                                                                                                                                                  |
| [                        backStageView1.BackStage = backStage1]                                                                                                              |
|                                                                                                                                                                                                                  |
| [                        backStageView1.HostControl = [Nothing]]                                                                                        |
|                                                                                                                                                                                                                  |
| [                        backStageView1.HostForm = [Me]]                                                                                                |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                  |
| [                        \' backStage1][]                                                                                  |
|                                                                                                                                                                                                                  |
| [                        backStage1.Controls.Add(backStageTab1)]                                                                                                             |
|                                                                                                                                                                                                                  |
| [                        backStage1.Controls.Add(backStageButton1)]                                                                                                          |
|                                                                                                                                                                                                                  |
| [                        backStage1.Dock = System.Windows.Forms.DockStyle.Fill]                                                                                              |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                  |
| [                        \' backStageTab1][]                                                                               |
|                                                                                                                                                                                                                  |
| [                        backStageTab1.Text = [\"backStageTab1\"]]                                                                                   |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                  |
| [                        \' backStageButton1][]                                                                            |
|                                                                                                                                                                                                                  |
| [                        backStageButton1.Text = [\"backStageButton1\"]]                                                                             |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                  |
| [                        \' ribbonControlAdv1][]                                                                           |
|                                                                                                                                                                                                                  |
| [                        ribbonControlAdv1.BackStageView = backStageView1]                                                                                                   |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                  |
| [                        \'Add BackStage to RibbonControlAdv ][]                                                           |
|                                                                                                                                                                                                                  |
| [                        ribbonControlAdv1.BackStageView =backStageView1]                                                                                                    |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                  |
| [                     \'Add BackStage and RibbonControlAdv to form][]                                                      |
|                                                                                                                                                                                                                  |
| [                        [Me].Controls.Add(backStage1)]                                                                                                 |
|                                                                                                                                                                                                                  |
| [                              [Me].Controls.Add([Me].ribbonControlAdv1)]                                                          |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

**[Refer to:]**

[] 

Appearance Setting[]

[] 

 

 

[]{#related-topics}

