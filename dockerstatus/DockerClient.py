import docker

class DockerClient():
    def __init__(self) -> None:
        self.client = docker.from_env()
    
    def get_container_rows(self):
        containers = self.client.containers.list()
        rows = []
        for i in containers:
                rows.append([
                i.short_id,
                i.attrs['Name'],
                'test'
            ])
            
        return rows
