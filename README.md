# BetterClipboard
A "multiclipboards" script for an efficient way to improve the original clipboards which are only able to save one string at a time. Works on both Windows and Linux.

## Getting Started

### Installation

Clone the repository:
```powershell
git clone https://github.com/imeirewes/betterclipboard
```

Install the dependencies:

```powershell
cd betterclipboard
pip install -r requirements.txt
```

### Usage

BetterClipboard is very straightforward. Start by running:
```powershell
> python bcb.py
```

Here, a window will show up. When running for the first time, by default, a `save.json` file will be created. To change the file named you can edit the line 10.
From now on, everytime you run BetterClipboard, it will ask you if you with to reset your saved clipboards or not. They are stored inside this file.

When using the actual program, it will repeatedly ask for an ID (which is provided on the prompt) to load anything you saved into your clipboard. To save the current contents on your clipbaord, all you have to do is type `SAVE`, as insctucted on screen.

## Errors, Bugs and feature requests

If you find an error or a bug, please report it as an issue.
If you wish to suggest a feature or an improvement please report it in the issue pages.
Feel free to fix bugs or add features on your own and submit as pull requests.

## License
<a href="https://github.com/imeirewes/betterclipboard/blob/master/LICENSE"> AGPL-3.0 </a>
