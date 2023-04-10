import os 
import subprocess

def rule_1_1_1_check(test_config):
    audit_cmd = test_config['audit']
    flag_name = '--allow-privileged'
    expected_value = 'false'

    try:
        result = subprocess.check_output(audit_cmd, shell=True, text=True)
    except subprocess.CalledProcessError as e:
        return f"Error executing command: {e}"

    if f"{flag_name}={expected_value}" in result:
        return "PASS"
    else:
        return "FAIL"

def rule_1_1_2_check(test_config):
    audit_cmd = test_config['audit']
    flag_name = 'permissions'
    expected_value = '644'

    try:
        result = subprocess.check_output(audit_cmd, shell=True, text=True)
    except subprocess.CalledProcessError as e:
        return f"Error executing command :{e}"
    if f"{flag_name}={expected_value}" in result:
        return "PASS"
    else:
        return "FAIL"
    
def get_rules():
    return [
        {
        'id': '1.1.1',
        'name': 'Ensure that the --allow-privileged argument is set to false (Scored)', 
        'check': rule_1_1_1_check,
        'remediation': 'Edit the API server pod specification file `/etc/kubernetes/manifests/kube-apiserver.yaml'
        },
        {
        'id': '1.1.2',
        'check': rule_1_1_2_check,
        'name': 'Ensure that the API server pod specification file permissions are set to 644 or more restrictive (Scored)',
        'remediation': ' Run the below command (based on the file location on your system) on themaster node. For example, chmod 644 $apiserverconf'
        }
    ]