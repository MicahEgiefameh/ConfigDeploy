from src.helpers.ssh_client import create_client, get_user_pass
from src.modules.configure import install_requirements, remove_requirements, metadata
from src.helpers.json_parser import read_deploy
import time

BASE_PACKAGES = ["apache2"]


def apache_server(file):
    targets, path_to_application, add_packages, delete_packages, data = read_deploy(file)
    add_packages += BASE_PACKAGES
    user, pswd = get_user_pass()
    for target in targets:
        client = create_client(target, user, pswd)
        print(f"Deploying apache application on {target}")
        install_requirements(add_packages, client)
        if delete_packages:
            remove_requirements(delete_packages, client)

        sftp = client.open_sftp()
        client.exec_command("sudo chmod -R a+rwx /var/www/html/")
        client.exec_command("rm /var/www/html/*")
        sftp.put(path_to_application, "/var/www/html/index.html")

        if data:
            metadata(data, client)
        print("Restarting apache2")
        client.exec_command("sudo service httpd restart")
        time.sleep(5.0)

        client.close()

