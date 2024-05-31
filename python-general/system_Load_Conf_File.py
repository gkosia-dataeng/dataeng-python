import yaml

config = yaml.safe_load(open('./resources/conf.yaml'))
print(config['env'], config['server']['addr'])