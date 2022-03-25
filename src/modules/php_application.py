from src.helpers.json_parser import read_deploy
from src.helpers.ssh_client import create_client, get_user_pass
from src.modules.configure import install_requirements, metadata, remove_requirements

BASE_PACKAGES = ["apache2", "php"]


def deploy_php(file) -> None:
    """Deploys simple PHP application to target"""
    targets, path_to_application, add_packages, delete_packages, data = read_deploy(
        file
    )
    user, pswd = get_user_pass()
    add_packages += BASE_PACKAGES
    for target in targets:
        client = create_client(target, user, pswd)
        print(f"Deploying PHP application on {target}")
        install_requirements(add_packages, client)
        if delete_packages:
            remove_requirements(delete_packages, client)

        sftp = client.open_sftp()
        client.exec_command("sudo chmod -R a+rwx /var/www/html/")
        client.exec_command("rm /var/www/html/*")
        sftp.put(path_to_application, "/var/www/html/index.php", confirm=False)

        if data:
            metadata(data, client)
        print(f"Restarting apache2....")
        client.exec_command(f"sudo service apache2 restart")
        print(f"{target} Complete! \n")
        client.close()
