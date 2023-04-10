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
    
def get_rules():
    return [
        {
        'id': '1.1.1',
        'check': rule_1_1_1_check,
        }
    ]