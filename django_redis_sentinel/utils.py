from django.core.exceptions import ImproperlyConfigured


def parse_sentinel_db_connection_string(constring):
    """
    Parse connection string in format:
        master_name/sentinel_server:port,sentinel_server:port/db_id
    Returns master name, list of tuples with pair (host, port) and db_id
    """
    try:
        connection_params = constring.split('/')
        master_name = connection_params[0]
        servers = [host_port.split(':') for host_port in connection_params[1].split(',')]
        sentinel_hosts = [(host, int(port)) for host, port in servers]
        db = connection_params[2]
    except (ValueError, TypeError, IndexError):
        raise ImproperlyConfigured("Incorrect format '%s'" % (constring))

    return master_name, sentinel_hosts, db
