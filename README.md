# TL;DR
In this repo I keep VSCode profiles and customizations.

## `vscode-settings/profiles`
Contains the VSCode profiles that I have exported from VSCode.  
Currently there's no scripted way to export and import a profile to VSCode and the graphical way through the
"profiles" window must be used.

### profile export
Cmd+shift+P then write "export profile" to open the profile window, then right-click the dots on the right of the profile name
and select export, then local.  
Save the profile under the `profiles` folder here and push.

### profile import
Follow the same process in the graphical "profiles" window.


## Display Profile Contents
Profile exports are json files where nested payloads are strings. Use `entrypoints/show.sh` to display the contents
of a profile export (`.code-profile` file).

## Remote Profiles (`daba-ml01`)
`daba-ml01` has the `code` commandline installed (the `daba` user at least). We can use it to quarantee that an extension
is installed on the server:
```shell
code --install-extension <extension-id>
```
`<extension-id>` is the fullname of the extension displayed on the far right of the extension's main page.  

### Database Profiles
I use the `MSSQL` and the `Oracle Developer` extension on `daba-ml01`. They don't coexist well, so I created a separate 
profile for each. The profiles have: 
1. blue-ish background for the selected pane in the activity bar and the "Azure" icon
   as profile logo for the `mssql` profile and,
2. red-ish background for the selected pane in the activity bar and a database icon as profile logo for the `oracle` profile

