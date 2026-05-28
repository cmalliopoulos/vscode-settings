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


## Comments
Profile exports are json files where nested payloads are strings. Use `entrypoints/show.sh` to display the contents
of a profile export (`.code-profile` file).