from ncclient import manager
from ncclient.operations import RPCError

def netconf_connect(host, port, username, password):
    conn = manager.connect(
        host=host,
        port=port,
        username=username,
        password=password,
        hostkey_verify=False,
        device_params={'name': 'default'},
        allow_agent=False,
        look_for_keys=False
    )
    return conn
## DEF DE CAMBIO DE NAMEHOSTS
def change_hostname(conn, new_hostname):
    hostname_config = '''
        <config>
            <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                <hostname>{}</hostname>
            </native>
        </config>
    '''.format(new_hostname)

    conn.edit_config(target='running', config=hostname_config)
## DEF DE CREACION DE LOOPBACK

def create_loopback_interface(conn, interface_number, ip_address, netmask):
    loopback_config = f"""
    <config>
        <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
            <interface>
                <Loopback>
                    <name>{interface_number}</name>
                    <ip>
                        <address>
                            <primary>
                                <address>{ip_address}</address>
                                <mask>{netmask}</mask>
                            </primary>
                        </address>
                    </ip>
                </Loopback>
            </interface>
        </native>
    </config>
    """


    try:
        response = conn.edit_config(target='running', config=loopback_config)
        print(response)
    except RPCError as e:
        print(e)
## CIERRE DE CONEXION SSH
def close_connection(conn):
    conn.close_session()

def main():
## VARIABLE DE LOGIN
    host = '10.0.2.5'
    port = 830
    username = 'cisco'
    password = 'cisco123!'
## VARIABLE DE NAMEHOST
    new_hostname = 'SERGIOGOMEZM'
## VARIABLE CREACION DE INTERCES
    interface_number = 2
    ip_address = '2.2.2.2'
    netmask = '255.255.255.255'


## def    
    conn = netconf_connect(host, port, username, password)
    change_hostname(conn, new_hostname)
    create_loopback_interface(conn, interface_number, ip_address, netmask)
    close_connection(conn)


if __name__ == '__main__':
    main()
