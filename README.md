
## STEP 1: To create a app using FastAPI.

## STEP 2: Dockerize the API using docker container.

## STEP 3: Run the docker file Locally.

## STEP 4: Upload the Docker Image to Docker Hub and Automate the builds using GITHUB ACTIONS

Created Docker Image : rahulr44/welcome_app

To pull the docker image --> use command : docker pull rahulr44/welcome_app

```
docker --version
```
To view the docker version.
![image](https://user-images.githubusercontent.com/112580014/194936259-afcb86b5-8bf5-495b-adbe-b027655cdcca.png)

```
Docker build -t rahulr44/welcome_app .
```
To build the Docker Image
![image](https://user-images.githubusercontent.com/112580014/194936294-8ead495e-ab07-43f2-a356-51c43a78241b.png)

```
Docker images
```
Command to view the list of docker images in our local
![image](https://user-images.githubusercontent.com/112580014/194936320-556e3bf4-1e03-418b-924a-aafa414633e5.png)

```
docker kill a34531b5d35b
```
Command to kill the current running images --> docker kill <**container ID**>
![image](https://user-images.githubusercontent.com/112580014/194936367-efb16c78-25fc-4544-ae4f-9f8fd86ea759.png)

```
Docker pull rahulr44/welcome_app
```
Command to pull the Image from Docker Hub --> docker pull <**Image name**>
![image](https://user-images.githubusercontent.com/112580014/194936410-86be0e64-adf1-4aaf-aeac-29667488f3a4.png)

```
docker ps
```
command to view the currnet running dockers 
![image](https://user-images.githubusercontent.com/112580014/194936454-145928b5-0880-49ae-958a-c3548c96e7bc.png)

```
Docker login
```
Command to connect the local docker to the docker hub 
![image](https://user-images.githubusercontent.com/112580014/194936469-762d2095-af2a-4d23-90ff-fea5b39a6443.png)

```
Docker push rahulr44/welcome_app
```
Command to push the Docker image from local to the docker hub --> docker push <**Image name**>
![image](https://user-images.githubusercontent.com/112580014/194936487-dbb023f9-b587-4949-8168-4ee749e9d638.png)

```
Docker run -d -p 8000:8000 rahulr44/welcome_app
```
Command to run the docker image 
![image](https://user-images.githubusercontent.com/112580014/194936335-07349ebc-b622-489a-924f-fd7ab6cc392d.png)

```
Docker Image hosted webpage
```
Web hosted page running from docker build
![image](https://user-images.githubusercontent.com/112580014/194937371-56a17d77-c652-4846-942f-1694b9cd268f.png)

```
Docker rmi rahulr44/welcome_app
```
Command to remove the docker image from the local.
![image](https://user-images.githubusercontent.com/112580014/194936507-4ac21515-60d1-41d2-ab6b-a95b3ebd4ba1.png)

