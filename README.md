# ConfigDeploy - Rudimentary Configuration Management Tool

ConfigDeploy is simple CLI tool written in python that allows users to deploy apache/php based applications. Users can also add and remove Debian packages as well as
specify file metadata (file mode, group, and user owner).

ConfigDeploy is maintained and published by Micah Egiefameh.

## Getting Started

The latest version of the project will be accessible via GitHub. Download down the repo via 
`git pull https://github.com/MicahEgiefameh/ConfigManagement.git` on your master host (this can be your local or another server).

Navigate to the project files and run `./bootstrap.sh`. This will setup the project to be used like a CLI.

Users must be able to authenticate via SSH to target servers.

## How It Works

ConfigDeploy works by establish an SSH connection to your target servers from your host. It then performs actions to deploy or configure your target host. Deployments and configurations
are specified by your configuration file written in JSON.

### Deploy Workflow
1. Establish SSH connection with target specified in target JSON field.
2. Install specified packages in addition to BASE_PACKAGES needed for the deployment using SSH connection.
3. If specified, delete packages using SSH connection.
4. Move application file from master host to target host.
5. If specified, apply metadata.
6. Restart apache service


### Configure Workflow
1. Establish SSH connection with target specified in target JSON field.
2. If specified, add packages using SSH connection.
3. If specified, delete packages using SSH connection.
5. If specified, apply metadata.
6. Restart all services.


### CLI examples

The anatomy of the CLI command is as follows:
`configdeploy [operation] --file [file]`

For deployments:  
`configdeploy deploy [module] --file [json file]`

For configurations:  
`configdeploy configure  --file [json file]`

### Writing Configurations

The fields that are required in every json file are:
* **targets: list of string**
* **metadata: list of dictionary**
  * Each dictionary should contain:
    * file: str
    * owner: str
    * group: str
    * mode: int
* **add_packages: list of string**
* **delete_packages: list of string**

The only difference between the schemas of deploy operation vs configure operation is that an application deploy will require the **path_to_application** field
* **path_to_application: str**

### Configure Schema

 ```{
  "targets": list,
  "metadata" : [
    {
      "file": str,
      "owner": str,
      "group": str,
      "mode": int
    },
    {
      "file": str
      "owner": str,
      "group": str,
      "mode": int
    }
  ],
  "add_packages": list,
  "delete_packages": list
}
```

### Deploy Schema

 ```{
  "targets": list,
  "path_to_application": str,
  "metadata" : [
    {
      "file": str,
      "owner": str,
      "group": str,
      "mode": int
    },
    {
      "file": str
      "owner": str,
      "group": str,
      "mode": int
    }
  ],
  "add_packages": list,
  "delete_packages": list
}
```

Examples of the schema can be found in examples/schema/schema_examples.

## Notes

* When using ConfigDeploy please note, this tool will overwrite previous configurations. Failures will be outputted to terminal.