from ssh_client import create_client
from modules.configure import install_requirements, remove_requirements
from config_deploy.json_parser import read_php_deploy

BASE_PACKAGES = ["httpd", "php"]


def deploy_php(file):
    targets, path_to_application, add_packages, delete_packages = read_php_deploy(file)

    add_packages += BASE_PACKAGES
    for target in targets:
        client = create_client(target)
        install_requirements(add_packages, client)
        if delete_packages:
            remove_requirements(delete_packages, client)

        sftp = client.open_sftp()
        client.exec_command("sudo chmod -R a+rwx /var/www/html/")
        sftp.put(path_to_application, "/var/www/html/index.php")
        client.exec_command("sudo service httpd restart")






