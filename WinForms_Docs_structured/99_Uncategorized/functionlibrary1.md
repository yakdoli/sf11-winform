---
title: functionlibrary1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\functionlibrary1.md
created_at: 2025-07-03
---








  









### Function Library {#function-library style="tab-stops: 0pt"}

 

Excel supports various built-in functions that make large calculations in large sheets easier.

 

{border="0"}

Figure 117: Insert Function Dialog Box in Excel**[]**

 

 

XlsIO provides support for reading and writing around 520+ predefined Excel functions.

[] 

[] 

Formula Writing

 

You can enter formulas in a spreadsheet by using the **Formula** property. Following code example illustrates the built-in function of Excel by using XlsIO APIs.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                              |
|                                                                                                                                                                                               |
| **[]**                                                                                                                                                    |
|                                                                                                                                                                                               |
| [// Excel Functions]                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A22\"]\].Text = [\"ABS(ABS(-A3))\"];]                                                    |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B22\"]\].Formula = [\"ABS(ABS(-A3))\"];]                                                 |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A23\"]\].Text = [\"ABS(ABS(-100))\"];]                                                   |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B23\"]\].Formula = [\"ABS(ABS(-100))\"];]                                                |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A24\"]\].Text = [\"-A3\"];]                                                              |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B24\"]\].Formula = [\"-A3\"];]                                                           |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A25\"]\].Text = [\"ACOS(A8)\"];]                                                         |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B25\"]\].Formula = [\"ACOS(A8)\"];]                                                      |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A26\"]\].Text = [\"ADDRESS(1,1)\"];]                                                     |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B26\"]\].Formula = [\"ADDRESS(1,1)\"];]                                                  |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A27\"]\].Text = [\"ADDRESS(1,1,2)\"];]                                                   |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B27\"]\].Formula = [\"ADDRESS(1,1,2)\"];]                                                |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A28\"]\].Text = [\"ADDRESS(1,1,3)\"];]                                                   |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B28\"]\].Formula = [\"ADDRESS(1,1,3)\"];]                                                |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A29\"]\].Text = [\"ADDRESS(1,1,4)\"];]                                                   |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B29\"]\].Formula = [\"ADDRESS(1,1,4)\"];]                                                |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A30\"]\].Text = [\"ASIN(A8)\"];]                                                         |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B30\"]\].Formula = [\"ASIN(A8)\"];]                                                      |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A31\"]\].Text = [\"ATAN(A8)\"];]                                                         |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B31\"]\].Formula = [\"ATAN(A8)\"];]                                                      |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A32\"]\].Text = [\"ATANH(A8)\"];]                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B32\"]\].Formula = [\"ATANH(A8)\"];]                                                     |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A33\"]\].Text = [\"BETADIST(A8,A8,A8)\"];]                                               |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B33\"]\].Formula = [\"BETADIST(A8,A8,A8)\"];]                                            |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A34\"]\].Text = [\"BETAINV(A8,A8,A8)\"];]                                                |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B34\"]\].Formula = [\"BETAINV(A8,A8,A8)\"];]                                             |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A35\"]\].Text = [\"BINOMDIST(A4,A3,A8,A6)\"];]                                           |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B35\"]\].Formula = [\"BINOMDIST(A4,A3,A8,A6)\"];]                                        |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A36\"]\].Text = [\"CEILING(A3,A4)\"];]                                                   |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B36\"]\].Formula = [\"CEILING(A3,A4)\"];]                                                |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A37\"]\].Text = [\"CELL(B3,A4)\"];]                                                      |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B37\"]\].Formula = [\"CELL(B3,A4)\"];]                                                   |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A38\"]\].Text = [\"CHAR(65)\"];]                                                         |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B38\"]\].Formula = [\"CHAR(65)\"];]                                                      |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A39\"]\].Text = [\"CHIDIST(A3,A4)\"];]                                                   |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B39\"]\].Formula = [\"CHIDIST(A3,A4)\"];]                                                |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A40\"]\].Text = [\"CHIINV(A8,A4)\"];]                                                    |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B40\"]\].Formula = [\"CHIINV(A8,A4)\"];]                                                 |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A41\"]\].Text = [\"CHITEST(A3:A8,A13:F18)\"];]                                           |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B41\"]\].Formula = [\"CHITEST(A3:A8,A13:F18)\"];]                                        |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A42\"]\].Text = [\"CHITEST({150,100,200,300,500,0.3},{95,155,195,305,495,0.7})\"];]      |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B42\"]\].Formula = [\"CHITEST({150,100,200,300,500,0.3},{95,155,195,305,495,0.7})\"];]   |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A43\"]\].Text = [\"CONFIDENCE(A8,A4,A5)\"];]                                             |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B43\"]\].Formula = [\"CONFIDENCE(A8,A4,A5)\"];]                                          |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A44\"]\].Text = [\"CORREL(A3:A8,A13:A18)\"];]                                            |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B44\"]\].Formula = [\"CORREL(A3:A8,A13:A18)\"];]                                         |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A45\"]\].Text = [\"CORREL({150,100,200,300,500,0.3},{95,155,195,305,495,0.7})\"];]       |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B45\"]\].Formula = [\"CORREL({150,100,200,300,500,0.3},{95,155,195,305,495,0.7})\"];]    |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A46\"]\].Text = [\"CRITBINOM(A3,A8,A8)\"];]                                              |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B46\"]\].Formula = [\"CRITBINOM(A3,A8,A8)\"];]                                           |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A47\"]\].Text = [\"DATEVALUE(B8)\"];]                                                    |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B47\"]\].Formula = [\"DATEVALUE(B8)\"];]                                                 |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A48\"]\].Text = [\"DAYS360(A3,A4)\"];]                                                   |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B48\"]\].Formula = [\"DAYS360(A3,A4)\"];]                                                |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A49\"]\].Text = [\"DOLLAR(A3)\"];]                                                       |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B49\"]\].Formula = [\"DOLLAR(A3)\"];]                                                    |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A50\"]\].Text = [\"FIND(B4,B7)\"];]                                                      |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B50\"]\].Formula = [\"FIND(B4,B7)\"];]                                                   |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A51\"]\].Text = [\"FINDB(B4,B7)\"];]                                                     |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B51\"]\].Formula = [\"FINDB(B4,B7)\"];]                                                  |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A52\"]\].Text = [\"FINV(A8,A4,A5)\"];]                                                   |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B52\"]\].Formula = [\"FINV(A8,A4,A5)\"];]                                                |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A53\"]\].Text = [\"FISHER(A8)\"];]                                                       |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B53\"]\].Formula = [\"FISHER(A8)\"];]                                                    |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A54\"]\].Text = [\"FTEST(A3:A8,A13:A18)\"];]                                             |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B54\"]\].Formula = [\"FTEST(A3:A8,A13:A18)\"];]                                          |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A55\"]\].Text = [\"FTEST({150,100,200,300,500,0.3},{95,155,195,305,495,0.7})\"];]        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B55\"]\].Formula = [\"FTEST({150,100,200,300,500,0.3},{95,155,195,305,495,0.7})\"];]     |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A56\"]\].Text = [\"FV(A8,A4,A5)\"];]                                                     |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B56\"]\].Formula = [\"FV(A8,A4,A5)\"];]                                                  |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A57\"]\].Text = [\"GAMMAINV(A8,A4,A5)\"];]                                               |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B57\"]\].Formula = [\"GAMMAINV(A8,A4,A5)\"];]                                            |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A58\"]\].Text = [\"HYPGEOMDIST(A4,A3,A5,A6)\"];]                                         |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B58\"]\].Formula = [\"HYPGEOMDIST(A4,A3,A5,A6)\"];]                                      |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A59\"]\].Text = [\"INDEX(A3,1)\"];]                                                      |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B59\"]\].Formula = [\"INDEX(A3,1)\"];]                                                   |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A60\"]\].Text = [\"INDEX({150,100,200,300,500,0.3},3)\"];]                               |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B60\"]\].Formula = [\"INDEX({150,100,200,300,500,0.3},3)\"];]                            |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A61\"]\].Text = [\"INDIRECT(B5)\"];]                                                     |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B61\"]\].Formula = [\"INDIRECT(B5)\"];]                                                  |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A62\"]\].Text = [\"INFO(B6)\"];]                                                         |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B62\"]\].Formula = [\"INFO(B6)\"];]                                                      |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A63\"]\].Text = [\"INTERCEPT(A3:A8,A13:A18)\"];]                                         |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B63\"]\].Formula = [\"INTERCEPT(A3:A8,A13:A18)\"];]                                      |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A64\"]\].Text = [\"INTERCEPT({150,100,200,300,500,0.3},{95,155,195,305,495,0.7})\"];]    |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B64\"]\].Formula = [\"INTERCEPT({150,100,200,300,500,0.3},{95,155,195,305,495,0.7})\"];] |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A65\"]\].Text = [\"IPMT(A18,3,A5,A6)\"];]                                                |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B65\"]\].Formula = [\"IPMT(A18,3,A5,A6)\"];]                                             |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A66\"]\].Text = [\"IRR(A9:A12)\"];]                                                      |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B66\"]\].Formula = [\"IRR(A9:A12)\"];]                                                   |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A67\"]\].Text = [\"IRR({-100,100,200,150})\"];]                                          |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B67\"]\].Formula = [\"IRR({-100,100,200,150})\"];]                                       |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A68\"]\].Text = [\"KURT(A3:A8)\"];]                                                      |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B68\"]\].Formula = [\"KURT(A3:A8)\"];]                                                   |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A69\"]\].Text = [\"KURT({150,100,200,300,500,0.3})\"];]                                  |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B69\"]\].Formula = [\"KURT({150,100,200,300,500,0.3})\"];]                               |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A70\"]\].Text = [\"LARGE(A13:A18,3)\"];]                                                 |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B70\"]\].Formula = [\"LARGE(A13:A18,3)\"];]                                              |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A71\"]\].Text = [\"LARGE({95,155,195,305,495,0.7},3)\"];]                                |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B71\"]\].Formula = [\"LARGE({95,155,195,305,495,0.7},3)\"];]                             |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A72\"]\].Text = [\"LOGEST({10,20,30},{10,20,30})\"];]                                    |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B72\"]\].Formula = [\"LOGEST({10,20,30},{10,20,30})\"];]                                 |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A73\"]\].Text = [\"LOGNORMDIST({10,20,30},A4,A5)\"];]                                    |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B73\"]\].Formula = [\"LOGNORMDIST({10,20,30},A4,A5)\"];]                                 |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A74\"]\].Text = [\"MAX({10,20,30;5,15,35;6,16,36})\"];]                                  |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B74\"]\].Formula = [\"MAX({10,20,30;5,15,35;6,16,36})\"];]                               |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A75\"]\].Text = [\"MAXA({10,20,30;5,15,35;6,16,36})\"];]                                 |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B75\"]\].Formula = [\"MAXA({10,20,30;5,15,35;6,16,36})\"];]                              |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A76\"]\].Text = [\"MID(B6,A19,A19)\"];]                                                  |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B76\"]\].Formula = [\"MID(B6,A19,A19)\"];]                                               |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A77\"]\].Text = [\"MID(\\\"Test string\\\",A19,A19\*A19)\"];]                            |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B77\"]\].Formula = [\"MID(\\\"Test string\\\",A19,A19\*A19)\"];]                         |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A78\"]\].Text = [\"MIDB(\\\"Test string\\\",A19,A19\*A19)\"];]                           |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B78\"]\].Formula = [\"MIDB(\\\"Test string\\\",A19,A19\*A19)\"];]                        |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A79\"]\].Text = [\"LOGINV(A8,A8,A8)\"];]                                                 |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B79\"]\].Formula = [\"LOGINV(A8,A8,A8)\"];]                                              |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A80\"]\].Text = [\"LOOKUP(A3,{1,2,3,100})\"];]                                           |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B80\"]\].Formula = [\"LOOKUP(A3,{1,2,3,100})\"];]                                        |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A81\"]\].Text = [\"LOOKUP(A3,A3:A8)\"];]                                                 |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B81\"]\].Formula = [\"LOOKUP(A3,A3:A8)\"];]                                              |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A82\"]\].Text = [\"LOOKUP(A3,A3:A8,A13:A18)\"];]                                         |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B82\"]\].Formula = [\"LOOKUP(A3,A3:A8,A13:A18)\"];]                                      |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A83\"]\].Text = [\"MATCH(A1,{1,2,3,4,5,100,200,300})\"];]                                |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B83\"]\].Formula = [\"MATCH(A1,{1,2,3,4,5,100,200,300})\"];]                             |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A84\"]\].Text = [\"MIRR(A9:A12,1,3)\"];]                                                 |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B84\"]\].Formula = [\"MIRR(A9:A12,1,3)\"];]                                              |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A85\"]\].Text = [\"MIRR({-100,100,200,150},1,3)\"];]                                     |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B85\"]\].Formula = [\"MIRR({-100,100,200,150},1,3)\"];]                                  |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A86\"]\].Text = [\"MATCH(A3,A3:A8)\"];]                                                  |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B86\"]\].Formula = [\"MATCH(A3,A3:A8)\"];]                                               |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A87\"]\].Text = [\"MDETERM({3,6,1;1,1,0;3,10,1})\"];]                                    |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B87\"]\].Formula = [\"MDETERM({3,6,1;1,1,0;3,10,1})\"];]                                 |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A88\"]\].Text = [\"MEDIAN({10,20,40,10,21})\"];]                                         |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B88\"]\].Formula = [\"MEDIAN({10,20,40,10,21})\"];]                                      |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A89\"]\].Text = [\"MIN({10,20,30;5,15,35;6,16,36})\"];]                                  |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B89\"]\].Formula = [\"MIN({10,20,30;5,15,35;6,16,36})\"];]                               |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A90\"]\].Text = [\"MINA({10,20,30;5,15,35;6,16,36})\"];]                                 |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B90\"]\].Formula = [\"MINA({10,20,30;5,15,35;6,16,36})\"];]                              |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A91\"]\].Text = [\"MODE(A3:A4)\"];]                                                      |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B91\"]\].Formula = [\"MODE(A3:A4)\"];]                                                   |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A92\"]\].Text = [\"NEGBINOMDIST(A3,A4,A8)\"];]                                           |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B92\"]\].Formula = [\"NEGBINOMDIST(A3,A4,A8)\"];]                                        |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A93\"]\].Text = [\"NORMINV(A8,A4,A5)\"];]                                                |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B93\"]\].Formula = [\"NORMINV(A8,A4,A5)\"];]                                             |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A94\"]\].Text = [\"NORMSINV(A8)\"];]                                                     |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B94\"]\].Formula = [\"NORMSINV(A8)\"];]                                                  |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A95\"]\].Text = [\"NPER(A3,A4,A5)\"];]                                                   |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B95\"]\].Formula = [\"NPER(A3,A4,A5)\"];]                                                |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A96\"]\].Text = [\"NPV(A3,A4)\"];]                                                       |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B96\"]\].Formula = [\"NPV(A3,A4)\"];]                                                    |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A97\"]\].Text = [\"PEARSON(A3:A8,A13:A18)\"];]                                           |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B97\"]\].Formula = [\"PEARSON(A3:A8,A13:A18)\"];]                                        |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A98\"]\].Text = [\"PERCENTILE(A3:A8,A18)\"];]                                            |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B98\"]\].Formula = [\"PERCENTILE(A3:A8,A18)\"];]                                         |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A99\"]\].Text = [\"PERCENTRANK(A3:A8,A3)\"];]                                            |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B99\"]\].Formula = [\"PERCENTRANK(A3:A8,A3)\"];]                                         |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A100\"]\].Text = [\"PERMUT(A3,2)\"];]                                                    |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B100\"]\].Formula = [\"PERMUT(A3,2)\"];]                                                 |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A101\"]\].Text = [\"PMT(A3,A4,A5)\"];]                                                   |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B101\"]\].Formula = [\"PMT(A3,A4,A5)\"];]                                                |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A102\"]\].Text = [\"PPMT(A8,A4,A5,A6)\"];]                                               |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B102\"]\].Formula = [\"PPMT(A8,A4,A5,A6)\"];]                                            |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A103\"]\].Text = [\"PROB(A3:A4,A8:A18,A3)\"];]                                           |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B103\"]\].Formula = [\"PROB(A3:A4,A8:A18,A3)\"];]                                        |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A104\"]\].Text = [\"PRODUCT({150,2,3,4,5,20})\"];]                                       |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B104\"]\].Formula = [\"PRODUCT({150,2,3,4,5,20})\"];]                                    |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A105\"]\].Text = [\"PV(A3,A4,A5)\"];]                                                    |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B105\"]\].Formula = [\"PV(A3,A4,A5)\"];]                                                 |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A106\"]\].Text = [\"QUARTILE(A3:A7,A8)\"];]                                              |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B106\"]\].Formula = [\"QUARTILE(A3:A7,A8)\"];]                                           |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A107\"]\].Text = [\"RATE(A19,-A3,A4)\"];]                                                |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B107\"]\].Formula = [\"RATE(A19,-A3,A4)\"];]                                             |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A108\"]\].Text = [\"RANK(A3,A3:A8)\"];]                                                  |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B108\"]\].Formula = [\"RANK(A3,A3:A8)\"];]                                               |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A109\"]\].Text = [\"RSQ(A3:A8,A18:A18)\"];]                                              |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B109\"]\].Formula = [\"RSQ(A3:A8,A18:A18)\"];]                                           |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A110\"]\].Text = [\"SEARCH(B4,B7)\"];]                                                   |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B110\"]\].Formula = [\"SEARCH(B4,B7)\"];]                                                |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A111\"]\].Text = [\"SEARCHB(B4,B7)\"];]                                                  |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B111\"]\].Formula = [\"SEARCHB(B4,B7)\"];]                                               |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A112\"]\].Text = [\"SKEW(A3:A8)\"];]                                                     |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B112\"]\].Formula = [\"SKEW(A3:A8)\"];]                                                  |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A113\"]\].Text = [\"SLOPE(A3:A8,A13:A18)\"];]                                            |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B113\"]\].Formula = [\"SLOPE(A3:A8,A13:A18)\"];]                                         |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A114\"]\].Text = [\"SMALL(A3:A8,3)\"];]                                                  |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B114\"]\].Formula = [\"SMALL(A3:A8,3)\"];]                                               |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A115\"]\].Text = [\"STDEV(A3:A8)\"];]                                                    |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B115\"]\].Formula = [\"STDEV(A3:A8)\"];]                                                 |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A116\"]\].Text = [\"STDEVA(A3:A8)\"];]                                                   |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B116\"]\].Formula = [\"STDEVA(A3:A8)\"];]                                                |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A117\"]\].Text = [\"STDEVP(A3:A8)\"];]                                                   |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B117\"]\].Formula = [\"STDEVP(A3:A8)\"];]                                                |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A118\"]\].Text = [\"STDEVPA(A3:A8)\"];]                                                  |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B118\"]\].Formula = [\"STDEVPA(A3:A8)\"];]                                               |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A119\"]\].Text = [\"STEYX(A3:A8,A13:A18)\"];]                                            |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B119\"]\].Formula = [\"STEYX(A3:A8,A13:A18)\"];]                                         |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A120\"]\].Text = [\"SUBSTITUTE(B3,B4,\\\"Test\\\")\"];]                                  |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B120\"]\].Formula = [\"SUBSTITUTE(B3,B4,\\\"Test\\\")\"];]                               |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A121\"]\].Text = [\"SUBTOTAL(A19,A3:A8)\"];]                                             |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B121\"]\].Formula = [\"SUBTOTAL(A19,A3:A8)\"];]                                          |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A122\"]\].Text = [\"SUM(A3:A8,A13:A18)\"];]                                              |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B122\"]\].Formula = [\"SUM(A3:A8,A13:A18)\"];]                                           |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A123\"]\].Text = [\"SUMIF(A3:A8,\\\"\>300\\\",A13:A18)\"];]                              |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B123\"]\].Formula = [\"SUMIF(A3:A8,\\\"\>300\\\",A13:A18)\"];]                           |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A124\"]\].Text = [\"SUMPRODUCT(A3:A8,A13:A18)\"];]                                       |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B124\"]\].Formula = [\"SUMPRODUCT(A3:A8,A13:A18)\"];]                                    |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A125\"]\].Text = [\"SUMSQ(A3:A8)\"];]                                                    |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B125\"]\].Formula = [\"SUMSQ(A3:A8)\"];]                                                 |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A126\"]\].Text = [\"SUMX2MY2(A3:A8,A13:A18)\"];]                                         |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B126\"]\].Formula = [\"SUMX2MY2(A3:A8,A13:A18)\"];]                                      |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A127\"]\].Text = [\"SUMX2PY2(A3:A8,A13:A18)\"];]                                         |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B127\"]\].Formula = [\"SUMX2PY2(A3:A8,A13:A18)\"];]                                      |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A128\"]\].Text = [\"SUMXMY2(A3:A8,A13:A18)\"];]                                          |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B128\"]\].Formula = [\"SUMXMY2(A3:A8,A13:A18)\"];]                                       |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A129\"]\].Text = [\"SYD(A3,A4,A5,A19)\"];]                                               |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B129\"]\].Formula = [\"SYD(A3,A4,A5,A19)\"];]                                            |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A130\"]\].Text = [\"TDIST(A3,1,A19)\"];]                                                 |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B130\"]\].Formula = [\"TDIST(A3,1,A19)\"];]                                              |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A131\"]\].Text = [\"TIMEVALUE(B10)\"];]                                                  |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B131\"]\].Formula = [\"TIMEVALUE(B10)\"];]                                               |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A132\"]\].Text = [\"TINV(A8,A4)\"];]                                                     |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B132\"]\].Formula = [\"TINV(A8,A4)\"];]                                                  |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A133\"]\].Text = [\"TRANSPOSE({150,2,3,4,5,20})\"];]                                     |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B133\"]\].Formula = [\"TRANSPOSE({150,2,3,4,5,20})\"];]                                  |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A134\"]\].Text = [\"TREND({150,2,3,4,5,20},{110,21,6,1,3,50})\"];]                       |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B134\"]\].Formula = [\"TREND({150,2,3,4,5,20},{110,21,6,1,3,50})\"];]                    |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A135\"]\].Text = [\"TRIMMEAN(A3:A8,A18)\"];]                                             |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B135\"]\].Formula = [\"TRIMMEAN(A3:A8,A18)\"];]                                          |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A136\"]\].Text = [\"TTEST(A3:A8,A13:A18,1,1)\"];]                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B136\"]\].Formula = [\"TTEST(A3:A8,A13:A18,1,1)\"];]                                     |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A137\"]\].Text = [\"TYPE({150,2,3,4,5,20})\"];]                                          |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B137\"]\].Formula = [\"TYPE({150,2,3,4,5,20})\"];]                                       |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A138\"]\].Text = [\"UPPER(B7)\"];]                                                       |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B138\"]\].Formula = [\"UPPER(B7)\"];]                                                    |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A139\"]\].Text = [\"VAR(A3:A8)\"];]                                                      |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B139\"]\].Formula = [\"VAR(A3:A8)\"];]                                                   |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A140\"]\].Text = [\"VARA(A3:A8)\"];]                                                     |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B140\"]\].Formula = [\"VARA(A3:A8)\"];]                                                  |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A141\"]\].Text = [\"VARPA(A3:A8)\"];]                                                    |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B141\"]\].Formula = [\"VARPA(A3:A8)\"];]                                                 |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A142\"]\].Text = [\"VDB(A3,A4,A5,0,1)\"];]                                               |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B142\"]\].Formula = [\"VDB(A3,A4,A5,0,1)\"];]                                            |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A143\"]\].Text = [\"ZTEST(A3:A8,4)\"];]                                                  |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B143\"]\].Formula = [\"ZTEST(A3:A8,4)\"];]                                               |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"A144\"]\].Text = [\"ZTEST({150,100,200,300,500,0.3},4)\"];]                              |
|                                                                                                                                                                                               |
| [sheet.Range\[[\"B144\"]\].Formula = [\"ZTEST({150,100,200,300,500,0.3},4)\"];]                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[{border="0"}]

Figure 118: Formula Settings[]

[] 

Note that formula separators vary for each culture/regional settings, and there will be exceptions in such cases. This can be overcome by setting the separators by using the **SetSeparators** method of IWorkbook. Following code example illustrates how to change the formula separators through XlsIO.

[] 

+-------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\] ]**                                                               |
|                                                                                                                               |
| **[]**                                                                      |
|                                                                                                                               |
| [workbook.SetSeparators([\";\"], [\",\"]);] |
+-------------------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]Sheet1 and Sheet2 are the default names of the worksheets.

[] 

+------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                           |
|                                                                                                                              |
| **[]**                                                                     |
|                                                                                                                              |
| [workbook.SetSeparators([\";\"], [\",\"])] |
+------------------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]In addition to being able to access values in the same worksheet, you can also access values across worksheets. Assume that the \"B\" is present on the second worksheet, then use the following code for calculation.

[] 

+------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\] ]**                                                              |
|                                                                                                                              |
| **[]**                                                                     |
|                                                                                                                              |
| [sheet.Range\[\"C2:C4\"\]. Formula = \"=SUM(Sheet2!B2:B4,Sheet1!A2:A4)\";] |
+------------------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]Sheet1 and Sheet2 are the default names of the worksheets.

[] 

+--------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                       |
|                                                                                                                          |
| **[]**                                                                 |
|                                                                                                                          |
| [sheet.Range(\"C2:C4\").Formula = \"=SUM(sheet2!B2:B4,sheet1!A2:A4)\"] |
+--------------------------------------------------------------------------------------------------------------------------+

 

You can also read the Formula Text and the Computed Value of the formula in the cell.

 

Following code example illustrates how to read the formulas and computed values.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                    |
|                                                                                                                                                                                                     |
| **[]**                                                                                                                                                          |
|                                                                                                                                                                                                     |
| [// Read computed Formula Value. ]                                                                                                                |
|                                                                                                                                                                                                     |
| [this][.txtFomulaNumber.Text = sheet.Range\[[\"C1\"]\].FormulaNumberValue.ToString();] |
|                                                                                                                                                                                                     |
| []                                                                                                                                                              |
|                                                                                                                                                                                                     |
| [// Read Formula.]                                                                                                                                |
|                                                                                                                                                                                                     |
| [this][.txtFormula.Text = sheet.Range\[[\"C1\"]\].Formula;]                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                          |
|                                                                                                                                                                                               |
| **[]**                                                                                                                                                    |
|                                                                                                                                                                                               |
| [\' Read computed Formula Value. ]                                                                                                          |
|                                                                                                                                                                                               |
| [Me][.txtFomulaNumber.Text = sheet.Range([\"C1\"]).FormulaNumberValue.ToString()] |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [\' Read Formula.]                                                                                                                          |
|                                                                                                                                                                                               |
| [Me][.txtFormula.Text = sheet.Range([\"C1\"]).Formula ]                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

You can also get the Formula values as bool, date, and number type. Note that XlsIO can only read already computed formulas, and cannot compute. Please refer to the  for more information on dynamic formula computation.

[] 

Following properties of the **IRange** interface are used to fetch formulas, computed values, and to check if there exists a formula in the cell.

[] 


  ---------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Property               Description
  Formula                Returns or sets the object\'s formula in A1-style notation and in the language of the macro. Read/write Variant.
  FormulaArray           Represents array-entered formula. Visit[[http://www.cpearson.com/excel/array.htm]{.UGHyperlink}](http://www.cpearson.com/excel/ArrayFormulas.aspx) for more information.
  FormulaArrayR1C1       Returns or sets the formula array for the range by using R1C1-style notation.
  FormulaBoolValue       Returns the calculated value of the formula as a boolean.
  FormulaDateTime        Gets/sets formula DateTime value contained by this cell. DateTime.MinValue if not all cells of the range have same DateTime value.
  FormulaErrorValue      Returns the calculated value of the formula as a string.
  FormulaHidden          True if the formula will be hidden when the worksheet is protected; False if at least part of formula in the range is not hidden.
  FormulaNumberValue     Gets/sets number value evaluated by formula.
  FormulaR1C1            Returns or sets the formula for the range by using R1C1-style notation.
  FormulaStringValue     Gets/sets string value evaluated by formula.
  HasDataValidation      Indicates whether specified range object has data validation. If Range is not single cell, then returns True only if all cells have data validation. This is a Read-Only property.
  HasDateTime            Indicates whether the range contains DateTime value. This is a Read-Only property.
  HasExternalFormula     Indicates if current range has external formula. This is a Read-Only property.
  HasFormula             True if all cells in the range contain formulas; False if at least one of the cells in the range doesn\'t contain a formula. This is a Read-Only property.
  HasFormulaArray        Indicates whether range contains array-entered formula. This is a Read-Only property.
  HasFormulaBoolValue    Indicates if current range has formula bool value. This is a Read-Only property.
  HasFormulaDateTime     Indicates if current range has formula value formatted as DateTime. This is a Read-Only property.
  HasFormulaErrorValue   Indicates if current range has formula error value. This is a Read-Only property.
  HasNumber              Indicates whether the range contains number. This is a Read-Only property.
  HasRichText            Indicates whether cell contains formatted rich text string.
  HasString              Indicates whether the range contains String. This is a Read-Only property.
  HasStyle               Indicates whether range has default style. False means default style. This is a Read-Only property.
  IgnoreErrorOptions     Represents various  in Excel.
  ---------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


[] 

 

More:







