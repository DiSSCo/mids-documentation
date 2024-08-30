# StaDocGen - *Development*
**Development Version** of the Web-based Documentation Generator for TDWG Data Standards  
Built using Python Flask, the application transforms a set of CSV files into data standards documentation pages. 
This application is currently under active development. 
The main application is located under StaDocGen.

## Application Specifications

### Naming Conventions for Files
| Extension | Convention                              | Example              |
| --------- | --------------------------------------- | -------------------- |
| html      | Concepts are separated with hyphens     | quick-reference.html |
| py        | Concepts are separated with underscores | quick_reference.py   |
| md        | Concepts are separated with underscores | quick_reference.md   |
| (folder)  | Concepts are separated with underscores | app/quick_reference/ |
| csv       | Concepts are separated with hyphens     | quick-reference.csv  |

```
├───app
│   ├───build       | Static html files generated using Frozen Flask (https://pythonhosted.org/Frozen-Flask/)
│   ├───config      | Working standard-specific configuration files to populate standards level metadata (currently in development)
│   ├───data        | Source data files in csv format
│   │   ├───global
│   │   ├───ltc
│   │   │   ├───ltc-docs    | Source data post-transformation scripts
│   │   │   └───ltc-source  | Original source data files
│   │   │   └───ltc-source  | Tabular data schemas generated from the source CSV files (not part of the core stadocgen app)
│   ├───md          | Specific content blocks in markdown format 
│   │   └───mids     | Markdown associated with MIDS Documentation
│   │   └───tdwg    | Latest versions of official TDWG documentation markdown content, these files are then customized for each standard
│   ├───static      | Static assets (css, js, icons)
│   │   └───assets  | Standard static assets (do not change)
│   │   └───images  | Stanard-specific custom imagery 
│   │   └───custom  | Customized CSS overrides and javascript files that extend and alter the standardized template files under assets.
│   ├───templates   | Jinja templates
│   ├───utils       | Data transformation utilities 
_init__.py
freeze.py   Frozen flask script to generate build files
routes.py   Dynamic flask script
```
 
### Commands
Creating the Environment
* Stadocgen was created using Windows 11, PyCharm Professional, Python 3.11 and the Package Manager PIP
* For information on how to install Python 3.11 and the package manager, PIP, please refer to the respective documentation pages

The $ signifies the start of a new command in the command line window (also colled the console). For Windows users, 
I highly recommend using ConEmu https://conemu.github.io/ or Git Bash. You can also use the default console window by:
1. Press the Windows Key
2. Type cmd
3. Press enter

### Install Packages 
* Open command line window
* Navigate to the root directory of this repository
* Run the following commands
  * $python -m venv .stadocgen-venv
  * $.\.stadocgen-venv\Scripts\activate (Using Windows, If you are running a Mac or Linux, see python docs for activating virtual environments)
  * $pip install -r requirements.txt
* To test pages, go to **Testing**
* To build webpages for publication, go to **Build Documentation Pages**

### Testing
* Open the command line window and navigate to the project root directory
* Make sure the virtual environment is activated (conda activate stadcogen-venv)
* At the commend line, enter $flask run
* Open a browser to localhost:5000
* To end testing and stop the development server, press CTRL+C in the command line window

### Build Documentation Pages
* Open a command prompt in the app subdirectory (/app) 
* Enter *python freeze.py build*
* Copy the entire contents of the build directory (/app/build) to the docs folder in the target repository
* Publish changes using the appropriate GitHub workflow


Once the new build is pushed to the target repo, continue the standard protocol for updating a repository (create new branch with updated docs > pull request > approve > merge).  

## Notes

### Important Changes between routes.py and freeze.py
1. In freeze.py, all route names must be bound with both leading and trailing forward slashes.
2. When refreshing freeze.py with changes to routes.py, the leading 'app/' must be removed from every reference to an external files (e.g., markdown content files) 

### Conda and PIP
1. If you primarily use conda for virtual environments and package management, you may encounter issue with frozen flask. The only solution at the moment requires editing the package source
files, which is ill-advised. Fortunately, the same problems have not been encountered when using the package manager, PIP, and a native python virtual environment. 

## App Documentation
StaDocGen documentation is written and built with Writerside (https://www.jetbrains.com/writerside/). The documentation remains a work in progress. When ready, it will be published to the 
docs build directory for presentation/publication.

#### Contact
Ben Norton
michaenorton.ben@gmail.com
