# i3 workflow
An application to group different application together in i3wm and start them together to fasten your workflow.
You can select for each application on which workspace it should be started
- WARNING This will edit your i3 existing config file


https://user-images.githubusercontent.com/38686669/124397406-e9b2f700-dd0f-11eb-821a-3f23087dee14.mp4


Demo starting 3 application on seperate workspaces
### Installation package
TODO will come to pypi probably

### Installation and setup (dev)
This project uses python3.9 with pipenv. Simply clone the repository and do the following steps.

Install the dependencies
```bash
pipenv install
```

Activate the environment with 
```bash
pipenv shell
```
Customize your settings with the provided config/example.config.json file (you also configure your workspace groups here).

Run the app
```bash
python main.py "path/to-your/json-config-file.json"
```
