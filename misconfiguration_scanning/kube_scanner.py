import yaml 
import os
import cis_kubernetes_checks

def load_test_config(file_path):
    base_path = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(base_path, file_path)
    with open(full_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

def check_cis_benchmark_rules():
    cis_rules = cis_kubernetes_checks.get_rules()

    master_config = load_test_config('cis_k8s_configs/cis-1.24/master.yaml')
    # node_config = load_test_config('misconfiguration_scanning/cis_k8s_configs/cis-1.24/node.yaml')
    # etcd_config = load_test_config('misconfiguration_scanning/cis_k8s_configs/cis-1.24/etcd.yaml')

    test_configs = master_config

    results = {}
    for rule in cis_rules:
        rule_id = rule['id']
        rule_check = rule['check']
        matching_configs = [config for config in test_configs if config['id'] == rule_id]

        if matching_configs:
            rule_config = matching_configs[0]
            results[rule_id] = rule_check(rule_config)
        else:
            results[rule_id] = "Test configuration not found"
    
    return results

def main():
    benchmark_results = check_cis_benchmark_rules()

    print(benchmark_results)

if __name__ == '__main__':
    main()