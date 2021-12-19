import docker
from NWindow import NWindow
from DockerClient import DockerClient

if __name__ == "__main__":
    nwin = NWindow()
    cols = []
    cols.append({'name': 'ID', 'index': 0})
    cols.append({'name': 'Name', 'index': 1})
    cols.append({'name': 'Status', 'index': 2})
    nwin.create_table(cols)

    dclient = DockerClient()
    rows = dclient.get_container_rows()
    for i in rows:
        nwin.insert_row(i)

    nwin.wait_for_char()
