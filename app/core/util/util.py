import platform, socket, re, uuid, json, psutil, hashlib


def get_system_info():
    try:
        info={}
        info['platform']=platform.system()
        info['platform-release']=platform.release()
        info['platform-version']=platform.version()
        info['architecture']=platform.machine()
        info['hostname']=socket.gethostname()
        info['ip-address']=socket.gethostbyname(socket.gethostname())
        info['mac-address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
        info['processor']=platform.processor()
        info['ram']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
        return info
    except Exception as e:
        print(e)
        raise Exception("Não foi possível obter as informações do sistema. " + str(e))


def generate_hash(string):
    hash_object = hashlib.sha256()
    encoded_string = string.encode('utf-8')
    hash_object.update(encoded_string)
    hex_digest = hash_object.hexdigest()
    return hex_digest


def get_machine_id():
    info = get_system_info()
    hash = generate_hash(info['architecture'] + info['processor'] + info['mac-address'])
    return hash
