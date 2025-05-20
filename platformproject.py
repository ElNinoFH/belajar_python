import platform

system_info = {
    "OS Details" : platform.system_alias(platform.system(), platform.release(), platform.version()),
    "Processor" : platform.processor(),
    "Architecture" : platform.architecture()
}

for key, value in system_info.items():
    print(f"{key}: {value}")